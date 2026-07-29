#!/usr/bin/env python3
import argparse
import html
import json
import re
import shutil
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
ASSET_ROOT = SKILL_ROOT / "assets"
DEFAULT_VENDOR_ROOT = SKILL_ROOT / "vendor"
VENDOR_FILES = ("react.production.min.js", "react-dom.production.min.js", "dagre.min.js", "THIRD_PARTY_LICENSES.txt")
ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]+$")
REMOTE_PATTERN = re.compile(r"https?://", re.IGNORECASE)
INVALID_DIRECTORY_PATTERN = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
THEME_DEFAULTS = {
    "primary": "#2563eb",
    "background": "#eef2f7",
    "surface": "#ffffff",
    "text": "#172033",
    "muted": "#64748b",
}


def parse_args():
    parser = argparse.ArgumentParser(description="Generate an offline React visual prototype.")
    parser.add_argument("input", type=Path, help="UTF-8 JSON prototype specification.")
    parser.add_argument("--output", type=Path, default=Path("prototype-output"))
    parser.add_argument("--vendor-dir", type=Path, default=DEFAULT_VENDOR_ROOT)
    parser.add_argument("--check", action="store_true", help="Validate the input and dependencies only.")
    parser.add_argument("--force", action="store_true", help="Replace an existing output directory.")
    return parser.parse_args()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def require_string(value, path, allow_empty=False):
    require(isinstance(value, str), f"{path} must be a string")
    if not allow_empty:
        require(bool(value.strip()), f"{path} must not be empty")
    return value


def default_directory(name):
    directory = INVALID_DIRECTORY_PATTERN.sub("-", name).strip(" .")
    require(bool(directory), "business name cannot produce an empty directory")
    return directory


def normalize_viewport(page, path):
    platform = page["platform"]
    defaults = {"mobile": {"width": 390, "height": 844}, "desktop": {"width": 1440, "height": 900}}
    viewport = page.get("viewport", defaults[platform])
    require(isinstance(viewport, dict), f"{path}.viewport must be an object")
    width = viewport.get("width")
    height = viewport.get("height")
    require(isinstance(width, int) and 240 <= width <= 3840, f"{path}.viewport.width must be an integer from 240 to 3840")
    require(isinstance(height, int) and 320 <= height <= 3840, f"{path}.viewport.height must be an integer from 320 to 3840")
    return {"width": width, "height": height}


def validate_page(page, path, allow_remote_assets):
    require(isinstance(page, dict), f"{path} must be an object")
    page_id = require_string(page.get("id"), f"{path}.id")
    require(ID_PATTERN.fullmatch(page_id) is not None, f"{path}.id may contain only letters, digits, underscores, and hyphens")
    title = require_string(page.get("title"), f"{path}.title")
    platform = page.get("platform")
    require(platform in {"mobile", "desktop"}, f"{path}.platform must be mobile or desktop")
    markup = require_string(page.get("markup"), f"{path}.markup")
    styles = require_string(page.get("styles", ""), f"{path}.styles", allow_empty=True)
    require("</style" not in styles.lower(), f"{path}.styles must not contain a closing style tag")
    if not allow_remote_assets:
        require(REMOTE_PATTERN.search(markup) is None and REMOTE_PATTERN.search(styles) is None, f"{path} contains a remote URL but allow_remote_assets is false")
    callouts = page.get("callouts", [])
    require(isinstance(callouts, list), f"{path}.callouts must be an array")
    normalized_callouts = []
    for index, callout in enumerate(callouts):
        callout_path = f"{path}.callouts[{index}]"
        require(isinstance(callout, dict), f"{callout_path} must be an object")
        tone = callout.get("tone", "state")
        require(tone in {"trigger", "state", "action", "risk", "element"}, f"{callout_path}.tone is invalid")
        normalized_callouts.append({"tone": tone, "text": require_string(callout.get("text"), f"{callout_path}.text")})
    return {
        "id": page_id,
        "title": title,
        "platform": platform,
        "viewport": normalize_viewport(page, path),
        "markup": markup,
        "styles": styles,
        "callouts": normalized_callouts,
    }


def validate_business(business, path, allow_remote_assets):
    require(isinstance(business, dict), f"{path} must be an object")
    name = require_string(business.get("name"), f"{path}.name")
    directory = require_string(business.get("directory", default_directory(name)), f"{path}.directory")
    require(directory not in {".", ".."}, f"{path}.directory is invalid")
    require(INVALID_DIRECTORY_PATTERN.search(directory) is None, f"{path}.directory contains a filesystem-invalid character")
    require(directory == directory.strip(" ."), f"{path}.directory must not start or end with a space or period")
    direction = business.get("direction", "LR")
    require(direction in {"LR", "RL", "TB", "BT"}, f"{path}.direction is invalid")
    theme_input = business.get("theme", {})
    require(isinstance(theme_input, dict), f"{path}.theme must be an object")
    theme = dict(THEME_DEFAULTS)
    for key, value in theme_input.items():
        require(key in THEME_DEFAULTS, f"{path}.theme.{key} is not supported")
        theme[key] = require_string(value, f"{path}.theme.{key}")
        require(not any(character in theme[key] for character in "<>;{}"), f"{path}.theme.{key} contains an unsafe CSS character")
    shared_styles = require_string(business.get("shared_styles", ""), f"{path}.shared_styles", allow_empty=True)
    require("</style" not in shared_styles.lower(), f"{path}.shared_styles must not contain a closing style tag")
    if not allow_remote_assets:
        require(REMOTE_PATTERN.search(shared_styles) is None, f"{path}.shared_styles contains a remote URL but allow_remote_assets is false")
    pages_input = business.get("pages")
    require(isinstance(pages_input, list) and pages_input, f"{path}.pages must be a non-empty array")
    pages = [validate_page(page, f"{path}.pages[{index}]", allow_remote_assets) for index, page in enumerate(pages_input)]
    page_ids = [page["id"] for page in pages]
    require(len(page_ids) == len(set(page_ids)), f"{path}.pages contains duplicate IDs")
    edges_input = business.get("edges", [])
    require(isinstance(edges_input, list), f"{path}.edges must be an array")
    edges = []
    for index, edge in enumerate(edges_input):
        edge_path = f"{path}.edges[{index}]"
        require(isinstance(edge, dict), f"{edge_path} must be an object")
        source = require_string(edge.get("from"), f"{edge_path}.from")
        target = require_string(edge.get("to"), f"{edge_path}.to")
        require(source in page_ids, f"{edge_path}.from references missing page {source}")
        require(target in page_ids, f"{edge_path}.to references missing page {target}")
        label = require_string(edge.get("label", ""), f"{edge_path}.label", allow_empty=True)
        tone = edge.get("tone", "default")
        require(tone in {"default", "success", "warning", "danger"}, f"{edge_path}.tone is invalid")
        edges.append({"from": source, "to": target, "label": label, "tone": tone})
    return {
        "name": name,
        "directory": directory,
        "direction": direction,
        "theme": theme,
        "shared_styles": shared_styles,
        "pages": pages,
        "edges": edges,
    }


def load_and_validate(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValueError(f"Input file not found: {path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON at line {error.lineno}, column {error.colno}: {error.msg}") from error
    require(isinstance(data, dict), "Root must be an object")
    project = require_string(data.get("project"), "project")
    allow_remote_assets = data.get("allow_remote_assets", False)
    require(isinstance(allow_remote_assets, bool), "allow_remote_assets must be a boolean")
    businesses_input = data.get("businesses")
    require(isinstance(businesses_input, list) and businesses_input, "businesses must be a non-empty array")
    businesses = [validate_business(item, f"businesses[{index}]", allow_remote_assets) for index, item in enumerate(businesses_input)]
    directories = [business["directory"] for business in businesses]
    require(len(directories) == len(set(directories)), "businesses contains duplicate directories")
    return {"project": project, "businesses": businesses}


def validate_vendor(vendor_dir):
    missing = [str(vendor_dir / name) for name in VENDOR_FILES if not (vendor_dir / name).is_file()]
    require(not missing, "Missing offline dependencies: " + ", ".join(missing) + ". Run scripts/prepare_vendor.py first.")


def script_json(data):
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def theme_css(theme):
    return ":root{" + "".join(f"--prototype-{key}:{value};" for key, value in theme.items()) + "}"


def html_document(title, config, css_href, script_prefix, custom_styles="", include_dagre=False, snapshot=True):
    scripts = [
        f'<script src="{script_prefix}react.production.min.js"></script>',
        f'<script src="{script_prefix}react-dom.production.min.js"></script>',
    ]
    if include_dagre:
        scripts.append(f'<script src="{script_prefix}dagre.min.js"></script>')
    scripts.append(f'<script src="{script_prefix}prototype-runtime.js"></script>')
    snapshot_tag = '<script id="prototype-snapshot" type="application/json">{"edits":{},"notes":[]}</script>' if snapshot else ""
    return "\n".join([
        "<!DOCTYPE html>",
        '<html lang="zh-CN">',
        "<head>",
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f"<title>{html.escape(title)}</title>",
        f'<link rel="stylesheet" href="{css_href}">',
        f"<style>{custom_styles}</style>" if custom_styles else "",
        "</head>",
        "<body>",
        '<div id="root"></div>',
        f'<script id="prototype-config" type="application/json">{script_json(config)}</script>',
        snapshot_tag,
        *scripts,
        "</body>",
        "</html>",
        "",
    ])


def copy_assets(destination, vendor_dir):
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ASSET_ROOT / "prototype.css", destination / "prototype.css")
    shutil.copy2(ASSET_ROOT / "prototype-runtime.js", destination / "prototype-runtime.js")
    for filename in VENDOR_FILES:
        shutil.copy2(vendor_dir / filename, destination / filename)


def write_business(output, business, has_index, vendor_dir):
    business_root = output / business["directory"]
    pages_root = business_root / "pages"
    assets_root = business_root / "assets"
    pages_root.mkdir(parents=True, exist_ok=True)
    copy_assets(assets_root, vendor_dir)
    overview_config = {
        "kind": "overview",
        "businessName": business["name"],
        "direction": business["direction"],
        "indexHref": "../index.html" if has_index else None,
        "pages": [{"id": page["id"], "title": page["title"]} for page in business["pages"]],
        "edges": business["edges"],
    }
    overview = html_document(
        business["name"],
        overview_config,
        "assets/prototype.css",
        "assets/",
        theme_css(business["theme"]),
        include_dagre=True,
        snapshot=False,
    )
    (business_root / "overview.html").write_text(overview, encoding="utf-8")
    for page in business["pages"]:
        page_config = {"kind": "page", "businessDirectory": business["directory"], "page": page}
        custom_styles = theme_css(business["theme"]) + business["shared_styles"] + page["styles"]
        page_html = html_document(
            f'{page["id"]} {page["title"]}',
            page_config,
            "../assets/prototype.css",
            "../assets/",
            custom_styles,
            snapshot=True,
        )
        (pages_root / f'{page["id"]}.html').write_text(page_html, encoding="utf-8")


def write_index(output, project, businesses, vendor_dir):
    copy_assets(output / "assets", vendor_dir)
    config = {"kind": "index", "project": project, "businesses": [{"name": business["name"], "directory": business["directory"]} for business in businesses]}
    index_html = html_document(project, config, "assets/prototype.css", "assets/", snapshot=False)
    (output / "index.html").write_text(index_html, encoding="utf-8")


def generate(specification, output, vendor_dir, force):
    if output.exists():
        require(force, f"Output already exists: {output}. Use --force to replace it.")
        shutil.rmtree(output)
    output.mkdir(parents=True)
    has_index = len(specification["businesses"]) > 1
    if has_index:
        write_index(output, specification["project"], specification["businesses"], vendor_dir)
    for business in specification["businesses"]:
        write_business(output, business, has_index, vendor_dir)


def main():
    args = parse_args()
    try:
        specification = load_and_validate(args.input)
        validate_vendor(args.vendor_dir)
        if args.check:
            print(f'Valid: {len(specification["businesses"])} business(es), {sum(len(item["pages"]) for item in specification["businesses"])} page(s)')
            return
        generate(specification, args.output, args.vendor_dir, args.force)
    except ValueError as error:
        raise SystemExit(f"Validation failed: {error}") from error
    print(f"Generated prototype in {args.output}")


if __name__ == "__main__":
    main()
