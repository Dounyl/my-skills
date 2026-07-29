# Prototype Input Specification

Pass one UTF-8 JSON file to `scripts/generate_prototype.py`.

## Root

```json
{
  "project": "会员中心改版",
  "businesses": []
}
```

- `project`: visible only on the multi-business selector.
- `businesses`: one or more independent business flows.

## Business

```json
{
  "name": "登录注册",
  "directory": "登录注册",
  "direction": "LR",
  "theme": {
    "primary": "#2563eb",
    "background": "#eef2f7",
    "surface": "#ffffff",
    "text": "#172033",
    "muted": "#64748b"
  },
  "pages": [],
  "edges": []
}
```

- `directory`: optional output directory. It defaults to the business name after removing filesystem-invalid characters. Set it only when a different directory name is required.
- `direction`: Dagre direction, one of `LR`, `RL`, `TB`, or `BT`.
- `theme`: optional CSS colors shared by this business.

## Page

```json
{
  "id": "P01",
  "title": "手机号登录",
  "platform": "mobile",
  "viewport": { "width": 390, "height": 844 },
  "markup": "<section class=\"screen login-screen\">...</section>",
  "styles": ".login-screen { ... }",
  "callouts": [
    { "tone": "action", "text": "点击登录进入首页" }
  ]
}
```

- `id`: unique within the business; use stable page IDs from the PRD where possible.
- `title`: page name shown over the frame and in the graph node.
- `platform`: `mobile` or `desktop`.
- `viewport`: optional positive integer width and height. Defaults to `390×844` or `1440×900`.
- `markup`: the visual page body. Use semantic HTML and add links for specified navigation. Escape it as a JSON string.
- `styles`: page-specific CSS. Scope selectors to a page class to avoid affecting the shell.
- `callouts`: optional concise product annotations outside the screen. Valid tones are `trigger`, `state`, `action`, `risk`, and `element`.

The runtime finds visible text leaf nodes inside `markup`, assigns stable edit IDs from DOM order, and makes them editable in editing mode. Do not put essential text in CSS pseudo-elements or canvas.

For navigation, use relative page links:

```html
<a class="primary-button" href="P02.html">继续</a>
```

Use `../overview.html` for a page-to-overview link. Do not create links for behavior absent from the PRD.

## Edge

```json
{
  "from": "P01",
  "to": "P02",
  "label": "验证码正确",
  "tone": "success"
}
```

- `from` and `to`: existing page IDs in the same business.
- `label`: optional transition or branch condition.
- `tone`: optional `default`, `success`, `warning`, or `danger`.

## Multi-business Layout

Given businesses `登录注册` and `订单售后`, generation produces:

```text
prototype-output/
  index.html
  登录注册/
    overview.html
    pages/
      P01.html
    assets/
      prototype-runtime.js
      prototype.css
      react.production.min.js
      react-dom.production.min.js
      dagre.min.js
  订单售后/
    overview.html
    pages/
    assets/
```

Each business directory is self-contained. `index.html` contains only business entry cards and is omitted when there is one business.

## Authoring Decisions

- Represent distinct UI states as separate pages when they affect flow comprehension, acceptance, or review.
- Keep transient cosmetic states in one page when splitting would add noise.
- Prefer real-looking product data over lorem ipsum.
- Keep external callouts short and tied to a visible condition or transition.
- Use the reference visual system when supplied. Otherwise choose one coherent, restrained system appropriate to the domain.
- Avoid explanatory panels inside the prototype unless they are part of the product UI.
