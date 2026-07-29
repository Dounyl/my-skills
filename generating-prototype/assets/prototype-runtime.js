(function () {
  const element = React.createElement;
  const { useEffect, useMemo, useRef, useState } = React;
  const SCRIPT_BLOCK_PATTERN = /<script\b[^>]*\bid=["']prototype-snapshot["'][^>]*>[\s\S]*?<\/script>/i;

  function readConfig() {
    const node = document.getElementById("prototype-config");
    return node ? JSON.parse(node.textContent) : {};
  }

  function readSnapshot() {
    const node = document.getElementById("prototype-snapshot");
    if (!node) return { edits: {}, notes: [] };
    try {
      const parsed = JSON.parse(node.textContent);
      return { edits: parsed.edits || {}, notes: parsed.notes || [] };
    } catch (_error) {
      return { edits: {}, notes: [] };
    }
  }

  function safeStorageGet(key, fallback) {
    try {
      const value = localStorage.getItem(key);
      return value ? JSON.parse(value) : fallback;
    } catch (_error) {
      return fallback;
    }
  }

  function safeStorageSet(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (_error) {
      return false;
    }
    return true;
  }

  function safeStorageRemove(key) {
    try {
      localStorage.removeItem(key);
    } catch (_error) {
      return false;
    }
    return true;
  }

  function sanitizeSnapshot(snapshot) {
    return JSON.stringify(snapshot).replace(/</g, "\\u003c");
  }

  function assignEditableNodes(root, edits) {
    if (!root) return;
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (walker.nextNode()) {
      const textNode = walker.currentNode;
      const parent = textNode.parentElement;
      if (!parent || !textNode.nodeValue.trim()) continue;
      if (parent.closest("script, style, textarea, input, select, option, svg")) continue;
      if (parent.children.length || parent.dataset.editId) continue;
      nodes.push(parent);
    }
    nodes.forEach(function (node, index) {
      const editId = "text-" + String(index + 1).padStart(3, "0");
      node.dataset.editId = editId;
      if (Object.prototype.hasOwnProperty.call(edits, editId)) node.textContent = edits[editId];
    });
  }

  function useDraft(config, embedded) {
    const storageKey = "prototype-draft:" + encodeURIComponent(location.pathname) + ":" + config.businessDirectory + ":" + config.page.id;
    const initialDraft = safeStorageGet(storageKey, embedded);
    const [edits, setEdits] = useState(initialDraft.edits || {});
    const [notes, setNotes] = useState(initialDraft.notes || []);
    useEffect(function () {
      safeStorageSet(storageKey, { edits: edits, notes: notes });
    }, [edits, notes, storageKey]);
    return { edits: edits, setEdits: setEdits, notes: notes, setNotes: setNotes, storageKey: storageKey };
  }

  function ToolButton(props) {
    const className = ["prototype-tool", props.active ? "prototype-tool-active" : "", props.primary ? "prototype-tool-primary" : "", props.danger ? "prototype-tool-danger" : ""].filter(Boolean).join(" ");
    return element("button", { className: className, type: "button", onClick: props.onClick }, props.children);
  }

  function HelpDialog(props) {
    if (!props.dialog) return null;
    return element("div", { className: "prototype-dialog-backdrop", onMouseDown: props.onClose },
      element("section", { className: "prototype-dialog", onMouseDown: function (event) { event.stopPropagation(); } },
        element("h2", null, props.dialog.title),
        element("p", null, props.dialog.body),
        element("div", { className: "prototype-dialog-actions" },
          props.dialog.confirm ? element(ToolButton, { danger: true, onClick: props.dialog.confirm }, props.dialog.confirmLabel || "确认") : null,
          element(ToolButton, { primary: true, onClick: props.onClose }, props.dialog.confirm ? "取消" : "知道了")
        )
      )
    );
  }

  function Note(props) {
    const note = props.note;
    const drag = useRef(null);
    function beginDrag(event) {
      drag.current = { pointerId: event.pointerId, offsetX: event.clientX - note.x, offsetY: event.clientY - note.y };
      event.currentTarget.setPointerCapture(event.pointerId);
    }
    function moveDrag(event) {
      if (!drag.current || drag.current.pointerId !== event.pointerId) return;
      props.update({
        x: Math.max(0, Math.min(window.innerWidth - 220, event.clientX - drag.current.offsetX)),
        y: Math.max(0, Math.min(window.innerHeight - 132, event.clientY - drag.current.offsetY))
      });
    }
    function endDrag(event) {
      if (drag.current && drag.current.pointerId === event.pointerId) drag.current = null;
    }
    return element("aside", { className: "prototype-note" + (note.completed ? " prototype-note-completed" : ""), style: { left: note.x, top: note.y } },
      element("div", { className: "prototype-note-handle", onPointerDown: beginDrag, onPointerMove: moveDrag, onPointerUp: endDrag, onPointerCancel: endDrag },
        element("span", null, note.completed ? "已完成" : "修改标记"),
        element("div", { className: "prototype-note-actions" },
          element("button", { type: "button", title: note.completed ? "重新打开" : "完成", onPointerDown: function (event) { event.stopPropagation(); }, onClick: function () { props.update({ completed: !note.completed }); } }, note.completed ? "↺" : "✓"),
          element("button", { type: "button", title: "删除", onPointerDown: function (event) { event.stopPropagation(); }, onClick: props.remove }, "×")
        )
      ),
      element("textarea", { value: note.text, placeholder: "输入修改内容…", onChange: function (event) { props.update({ text: event.target.value }); } })
    );
  }

  function Callouts(props) {
    if (!props.items || !props.items.length) return null;
    return element("aside", { className: "prototype-callouts" }, props.items.map(function (item, index) {
      return element("div", { className: "prototype-callout prototype-callout-" + (item.tone || "state"), key: index }, item.text);
    }));
  }

  function Device(props) {
    const page = props.page;
    const isMobile = page.platform === "mobile";
    const width = "min(" + page.viewport.width + "px, calc(100vw - " + (isMobile ? 48 : 80) + "px))";
    return element("div", { className: "device " + (isMobile ? "device-mobile" : "device-desktop"), style: { width: width } },
      isMobile ? null : element("div", { className: "device-chrome" }, element("span"), element("span"), element("span")),
      element("div", { className: "device-viewport", style: { minHeight: page.viewport.height + "px" } },
        element("div", { className: "prototype-content", ref: props.contentRef, dangerouslySetInnerHTML: { __html: page.markup } })
      )
    );
  }

  function PageApp(props) {
    const config = props.config;
    const embedded = props.snapshot;
    const draft = useDraft(config, embedded);
    const contentRef = useRef(null);
    const [editing, setEditing] = useState(false);
    const [dialog, setDialog] = useState(null);
    const [saving, setSaving] = useState(false);
    const fileHandle = useRef(null);

    useEffect(function () {
      assignEditableNodes(contentRef.current, draft.edits);
    }, []);

    useEffect(function () {
      if (!contentRef.current) return;
      contentRef.current.querySelectorAll("[data-edit-id]").forEach(function (node) {
        node.contentEditable = editing ? "true" : "false";
      });
    }, [editing]);

    function captureEdit(event) {
      const target = event.target.closest("[data-edit-id]");
      if (!target || !contentRef.current.contains(target)) return;
      draft.setEdits(function (current) {
        return Object.assign({}, current, { [target.dataset.editId]: target.textContent });
      });
    }

    function protectNavigation(event) {
      if (editing && event.target.closest("a")) event.preventDefault();
    }

    function addNote() {
      const offset = draft.notes.length * 18;
      draft.setNotes(draft.notes.concat({ id: "note-" + Date.now(), x: Math.max(12, window.innerWidth - 260 - offset % 160), y: 72 + offset % 220, text: "", completed: false }));
    }

    function updateNote(id, patch) {
      draft.setNotes(draft.notes.map(function (note) { return note.id === id ? Object.assign({}, note, patch) : note; }));
    }

    function snapshotHtml() {
      const snapshot = { edits: draft.edits, notes: draft.notes };
      const replacement = '<script id="prototype-snapshot" type="application/json">' + sanitizeSnapshot(snapshot) + "</script>";
      return "<!DOCTYPE html>\n" + document.documentElement.outerHTML.replace(SCRIPT_BLOCK_PATTERN, replacement);
    }

    async function saveFile() {
      setSaving(true);
      const html = snapshotHtml();
      try {
        if (window.showSaveFilePicker) {
          if (!fileHandle.current) fileHandle.current = await window.showSaveFilePicker({ suggestedName: config.page.id + ".html", types: [{ description: "HTML", accept: { "text/html": [".html"] } }] });
          const writable = await fileHandle.current.createWritable();
          await writable.write(html);
          await writable.close();
        } else {
          const blob = new Blob([html], { type: "text/html;charset=utf-8" });
          const anchor = document.createElement("a");
          anchor.href = URL.createObjectURL(blob);
          anchor.download = config.page.id + ".html";
          anchor.click();
          setTimeout(function () { URL.revokeObjectURL(anchor.href); }, 1000);
        }
      } catch (error) {
        if (error && error.name !== "AbortError") setDialog({ title: "保存失败", body: String(error.message || error) });
      } finally {
        setSaving(false);
      }
    }

    function confirmReset() {
      setDialog({
        title: "确认重置",
        body: "重置会恢复生成时的页面文字，并删除当前页面的全部便签。此操作无法撤销。",
        confirmLabel: "确认重置",
        confirm: function () {
          draft.setEdits({});
          draft.setNotes([]);
          safeStorageSet(draft.storageKey, { edits: {}, notes: [] });
          setEditing(false);
          if (contentRef.current) {
            contentRef.current.innerHTML = config.page.markup;
            assignEditableNodes(contentRef.current, {});
          }
          setDialog(null);
        }
      });
    }

    return element(React.Fragment, null,
      element("main", { className: "prototype-shell", onInput: captureEdit, onClickCapture: protectNavigation },
        element("header", { className: "prototype-header" },
          element("div", { className: "prototype-heading" }, element("div", { className: "prototype-kicker" }, config.page.id), element("h1", { className: "prototype-title" }, config.page.title)),
          element("a", { className: "prototype-back", href: "../overview.html" }, "流程总览")
        ),
        element("div", { className: "prototype-workspace" },
          element("section", { className: "prototype-stage" }, element(Device, { page: config.page, contentRef: contentRef })),
          element(Callouts, { items: config.page.callouts })
        )
      ),
      draft.notes.map(function (note) {
        return element(Note, { key: note.id, note: note, update: function (patch) { updateNote(note.id, patch); }, remove: function () { draft.setNotes(draft.notes.filter(function (item) { return item.id !== note.id; })); } });
      }),
      element("nav", { className: "prototype-toolbar", "aria-label": "原型编辑工具" },
        element(ToolButton, { active: editing, onClick: function () { setEditing(!editing); } }, editing ? "完成编辑" : "编辑文字"),
        element(ToolButton, { onClick: addNote }, "添加便签"),
        element("span", { className: "prototype-tool-group" },
          element(ToolButton, { primary: true, onClick: saveFile }, saving ? "保存中…" : "保存"),
          element("button", { className: "prototype-help", type: "button", "aria-label": "保存说明", onClick: function () { setDialog({ title: "保存说明", body: "Chrome 或 Edge 支持选择 HTML 文件并写入更新内容；首次需要手动确认文件。其他浏览器会下载一份包含当前文字修改和便签的新 HTML。页面草稿也会自动保存在当前浏览器中。" }); } }, "!")
        ),
        element("span", { className: "prototype-tool-group" },
          element(ToolButton, { danger: true, onClick: confirmReset }, "重置"),
          element("button", { className: "prototype-help", type: "button", "aria-label": "重置说明", onClick: function () { setDialog({ title: "重置说明", body: "重置会恢复生成时的页面文字并删除全部便签。点击重置按钮后仍需二次确认，不会直接执行。" }); } }, "!")
        )
      ),
      element(HelpDialog, { dialog: dialog, onClose: function () { setDialog(null); } })
    );
  }

  function edgePath(points) {
    if (!points || !points.length) return "";
    return points.reduce(function (path, point, index) { return path + (index ? " L " : "M ") + point.x + " " + point.y; }, "");
  }

  function FlowApp(props) {
    const config = props.config;
    const layout = useMemo(function () {
      const graph = new dagre.graphlib.Graph({ multigraph: true }).setGraph({ rankdir: config.direction || "LR", nodesep: 48, ranksep: 92, marginx: 50, marginy: 50 }).setDefaultEdgeLabel(function () { return {}; });
      config.pages.forEach(function (page) { graph.setNode(page.id, { width: 190, height: 82 }); });
      config.edges.forEach(function (edge, index) { graph.setEdge(edge.from, edge.to, { index: index, label: edge.label || "", tone: edge.tone || "default", width: edge.label ? 110 : 0, height: edge.label ? 28 : 0, labelpos: "c" }, "edge-" + index); });
      dagre.layout(graph);
      return { graph: graph, width: Math.max(graph.graph().width, window.innerWidth - 54), height: Math.max(graph.graph().height, window.innerHeight - 105) };
    }, [config]);
    const colors = { default: "#94a3b8", success: "#22c55e", warning: "#f59e0b", danger: "#ef4444" };
    const edges = layout.graph.edges().map(function (edgeRef) { return Object.assign({}, layout.graph.edge(edgeRef), { ref: edgeRef }); });
    return element("main", { className: "flow-shell" },
      element("header", { className: "flow-header" }, element("h1", { className: "flow-title" }, config.businessName), config.indexHref ? element("a", { className: "prototype-back", href: config.indexHref }, "全部业务") : null),
      element("section", { className: "flow-canvas", style: { width: layout.width, height: layout.height } },
        element("svg", { className: "flow-svg", width: layout.width, height: layout.height },
          element("defs", null, Object.keys(colors).map(function (tone) { return element("marker", { key: tone, id: "arrow-" + tone, markerWidth: 9, markerHeight: 9, refX: 7, refY: 4.5, orient: "auto" }, element("path", { d: "M0,0 L9,4.5 L0,9 Z", fill: colors[tone] })); })),
          edges.map(function (edge, index) { const tone = colors[edge.tone] ? edge.tone : "default"; return element("path", { key: index, d: edgePath(edge.points), fill: "none", stroke: colors[tone], strokeWidth: 2, markerEnd: "url(#arrow-" + tone + ")" }); })
        ),
        edges.filter(function (edge) { return edge.label; }).map(function (edge, index) { return element("div", { className: "flow-edge-label", key: index, style: { left: edge.x, top: edge.y } }, edge.label); }),
        config.pages.map(function (page) { const node = layout.graph.node(page.id); return element("a", { className: "flow-node", href: "pages/" + encodeURIComponent(page.id) + ".html", key: page.id, style: { left: node.x - 95, top: node.y - 41 } }, element("span", { className: "flow-node-id" }, page.id), element("span", { className: "flow-node-title" }, page.title)); })
      )
    );
  }

  function BusinessIndex(props) {
    return element("main", { className: "business-index" }, element("section", { className: "business-panel" }, element("h1", { className: "business-title" }, props.config.project), element("div", { className: "business-grid" }, props.config.businesses.map(function (business) { return element("a", { className: "business-card", href: encodeURIComponent(business.directory) + "/overview.html", key: business.directory }, element("strong", null, business.name), element("span", null, "打开业务流程 →")); }))));
  }

  const config = readConfig();
  const snapshot = readSnapshot();
  const root = ReactDOM.createRoot(document.getElementById("root"));
  if (config.kind === "page") root.render(element(PageApp, { config: config, snapshot: snapshot }));
  else if (config.kind === "overview") root.render(element(FlowApp, { config: config }));
  else root.render(element(BusinessIndex, { config: config }));
}());
