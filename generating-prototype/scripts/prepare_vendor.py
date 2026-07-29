#!/usr/bin/env python3
import argparse
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path


PACKAGES = {
    "react-18.2.0.tgz": ("react@18.2.0", "package/umd/react.production.min.js", "react.production.min.js"),
    "react-dom-18.2.0.tgz": ("react-dom@18.2.0", "package/umd/react-dom.production.min.js", "react-dom.production.min.js"),
    "dagrejs-dagre-1.1.5.tgz": ("@dagrejs/dagre@1.1.5", "package/dist/dagre.min.js", "dagre.min.js"),
}
NOTICE_SOURCE = Path(__file__).resolve().parent.parent / "assets" / "THIRD_PARTY_LICENSES.txt"


def parse_args():
    parser = argparse.ArgumentParser(description="Prepare fixed offline browser dependencies.")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent.parent / "vendor")
    parser.add_argument("--package-dir", type=Path, help="Use existing npm tarballs instead of npm pack.")
    return parser.parse_args()


def extract_member(archive_path, member_name, destination):
    with tarfile.open(archive_path, "r:gz") as archive:
        member = archive.getmember(member_name)
        source = archive.extractfile(member)
        if source is None:
            raise RuntimeError(f"Missing {member_name} in {archive_path}")
        with destination.open("wb") as target:
            shutil.copyfileobj(source, target)


def main():
    args = parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="prototype-vendor-") as temporary:
        package_dir = args.package_dir or Path(temporary)
        if args.package_dir is None:
            subprocess.run(
                ["npm", "pack", *[item[0] for item in PACKAGES.values()], "--pack-destination", str(package_dir)],
                check=True,
            )
        for archive_name, (_package, member_name, output_name) in PACKAGES.items():
            archive_path = package_dir / archive_name
            if not archive_path.is_file():
                raise SystemExit(f"Package archive not found: {archive_path}")
            extract_member(archive_path, member_name, args.output / output_name)
        shutil.copy2(NOTICE_SOURCE, args.output / NOTICE_SOURCE.name)
    print(f"Prepared offline assets in {args.output}")


if __name__ == "__main__":
    main()
