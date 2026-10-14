/* Interactive components for the lecture deck. Plain JS, inline SVG, no dependencies.
   Entry point: Deck.init() after Reveal is ready. */
(function () {
  "use strict";
  var D = window.DECK_DATA;
  var SVG = "http://www.w3.org/2000/svg";

  function el(tag, attrs, parent) {
    var e = document.createElementNS(SVG, tag);
    for (var k in attrs) if (attrs.hasOwnProperty(k)) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }
  function text(parent, x, y, str, cls, attrs) {
    var t = el("text", Object.assign({ x: x, y: y, "class": cls || "" }, attrs || {}), parent);
    t.textContent = str;
    return t;
  }
  function css(name) { return getComputedStyle(document.documentElement).getPropertyValue(name).trim(); }
  function trackColor(key) { return "var(--t-" + key + ")"; }

  /* ------------------------------------------------------------ tooltip */
  var tip = null;
  function showTip(evt, html) {
    if (!tip) { tip = document.createElement("div"); tip.className = "tl-tip"; document.body.appendChild(tip); }
    tip.innerHTML = html;
    tip.style.display = "block";
    var x = evt.clientX + 14, y = evt.clientY + 14;
    var w = tip.offsetWidth, h = tip.offsetHeight;
    if (x + w > window.innerWidth - 8) x = evt.clientX - w - 14;
    if (y + h > window.innerHeight - 8) y = evt.clientY - h - 14;
    tip.style.left = x + "px"; tip.style.top = y + "px";
  }
  function hideTip() { if (tip) tip.style.display = "none"; }

  /* ------------------------------------------------------------ timeline */
  var X0 = 2000, X1 = 2027;
  function timeline(container) {
    var mode = container.getAttribute("data-mode") || "strip";
    var focus = container.getAttribute("data-focus") || null;
    var full = mode === "full", breaksOnly = mode === "breaks", zoom = mode === "zoom";
    var showBreaks = breaksOnly || (full && container.getAttribute("data-breaks") !== "0");
    var P = zoom ? D.periods.filter(function (p) { return p.id === focus; })[0] : null;
    var W = 1200, right = 20;
    var left = showBreaks ? 232 : (zoom ? 128 : (full ? 130 : 150));
    var laneH = full ? 46 : (zoom ? 48 : 22);
    var top = full ? 36 : 26;
    var lanes = breaksOnly ? 0 : D.tracks.length;
    var breaksH = showBreaks ? 20 + D.breaks.length * 26 : 0;
    var H = top + lanes * laneH + 18 + breaksH;
    var svg = el("svg", { viewBox: "0 0 " + W + " " + H, role: "img", "aria-label": container.getAttribute("aria-label") || "Timeline 2000 to 2026" });
    container.innerHTML = "";
    container.appendChild(svg);
    var ax0 = zoom ? P.from - 0.15 : X0, ax1 = zoom ? P.to : X1;
    var xs = function (y) { return left + (y - ax0) / (ax1 - ax0) * (W - left - right); };
    var xf = function (y) { return left + (y - X0) / (X1 - X0) * (W - left - right); };
    var mid = { "text-anchor": "middle" };

    if (zoom) {
      for (var yy = P.from; yy <= P.to; yy++) el("line", { x1: xs(yy), x2: xs(yy), y1: top - 6, y2: top + lanes * laneH + 2, "class": "tick" }, svg);
    } else {
      D.periods.forEach(function (p) {
        var active = focus ? p.id === focus : false;
        el("rect", { x: xs(p.from), y: top - 4, width: xs(p.to) - xs(p.from), height: lanes * laneH + 8, "class": "period-band" + (active ? "" : " dim") }, svg);
        el("line", { x1: xs(p.from), x2: xs(p.from), y1: top - 10, y2: top + lanes * laneH + 4, "class": "tick" }, svg);
        var isLast = p === D.periods[D.periods.length - 1];
        var lx = isLast ? xs(X1) - 4 : xs(p.from) + 6, anchor = isLast ? { "text-anchor": "end" } : {};
        var lab;
        if (full) {
          var bits = p.label.split(" · ");
          text(svg, lx, 11, bits[0], "period-years", anchor);
          lab = text(svg, lx, 25, bits[1] || "", "period-label" + (active ? " active" : ""), anchor);
        } else {
          // the narrow breaks header wraps a long last label at its final comma so it clears the label before it
          var s1 = p.short, s2 = null, ci = s1.lastIndexOf(", ");
          if (breaksOnly && isLast && s1.length > 22 && ci > 0) { s2 = s1.slice(ci + 2); s1 = s1.slice(0, ci + 1); }
          lab = text(svg, lx, 14, s1, "period-label" + (active ? " active" : ""), anchor);
          if (s2) { var lab2 = text(svg, lx, 27, s2, "period-label" + (active ? " active" : ""), anchor); lab2.addEventListener("click", function () { gotoPeriod(p); }); }
        }
        lab.addEventListener("click", function () { gotoPeriod(p); });
      });
      el("line", { x1: xs(X1), x2: xs(X1), y1: top - 10, y2: top + lanes * laneH + 4, "class": "tick" }, svg);
    }

    // lanes
    if (!breaksOnly) D.tracks.forEach(function (t, i) {
      var y = top + i * laneH + laneH / 2;
      el("line", { x1: left, x2: W - right, y1: y, y2: y, "class": "lane-line" }, svg);
      text(svg, left - 10, y + 4, t.label, "lane-label", { "text-anchor": "end" });
    });
    // years
    var yl = top + lanes * laneH + 14;
    if (zoom) { for (var yr = P.from; yr < P.to; yr++) text(svg, xs(yr + 0.5), yl, String(yr), "year", mid); }
    else { for (var y2 = 2000; y2 <= 2026; y2 += 2) text(svg, xs(y2 + 0.5), yl, String(y2), "year", mid); }

    // events; labels on the key events (zoom) or the anchor events (overview), placed above or below the lane so they never overlap
    var placed = [];
    if (!breaksOnly) D.events.forEach(function (ev) {
      var li = D.tracks.findIndex(function (t) { return t.key === ev.t; });
      if (li < 0) return;
      if (zoom && (ev.y < P.from || ev.y >= P.to)) return;
      var cx = xs(ev.y), cy = top + li * laneH + laneH / 2;
      var inFocus = !focus || zoom || D.periods.some(function (p) { return p.id === focus && ev.y >= p.from && ev.y < p.to; });
      var labelled = (full && ev.h) || (zoom && ev.k);
      var r = labelled ? 6.5 : (full || zoom ? 4 : 4);
      var c = el("circle", { cx: cx, cy: cy, r: r, fill: trackColor(ev.t), "class": "ev" + (inFocus ? " in" : "") + (labelled ? " key" : ((full || zoom) ? " minor" : "")) }, svg);
      c.addEventListener("mousemove", function (e) { showTip(e, "<b>" + yearLabel(ev.y) + " · " + esc(ev.s) + "</b>" + esc(ev.d || "")); });
      c.addEventListener("mouseleave", hideTip);
      if (labelled) {
        var w = ev.s.length * 6.6 + 8, flip = cx + 9 + w > W - right;
        var x0 = flip ? cx - 9 - w : cx + 9;
        var tiers = [cy - 9, cy + 17], ly = tiers[0], free = false;
        for (var ti = 0; ti < tiers.length && !free; ti++) {
          ly = tiers[ti];
          free = !placed.some(function (pl) { return pl.lane === li && Math.abs(pl.y - ly) < 12 && x0 < pl.x + pl.w && x0 + w > pl.x; });
        }
        if (!free) { ly = tiers[0]; placed.filter(function (pl) { return pl.lane === li && Math.abs(pl.y - ly) < 12 && x0 < pl.x + pl.w; }).forEach(function (pl) { x0 = Math.max(x0, pl.x + pl.w + 6); }); }
        placed.push({ lane: li, x: x0, y: ly, w: w });
        text(svg, flip ? x0 + w : x0, ly, ev.s, "ev-label" + (zoom ? " zoom" : ""), flip ? { "text-anchor": "end" } : {});
      }
    });

    // breaks band
    if (showBreaks) {
      var by = top + lanes * laneH + 28;
      D.breaks.forEach(function (b, i) {
        var y = by + i * 26;
        var spans = b.spans || [[b.from, b.to]];
        var tipText = "<b>" + esc(b.s) + "</b>" + esc(b.note || (b.dom ? "First seen " + b.from + ", dominant from " + b.dom : "Dominant from " + b.from));
        spans.forEach(function (sp) {
          var bar = el("rect", { x: xs(sp[0]), y: y, width: Math.max(4, xs(sp[1]) - xs(sp[0])), height: 16, fill: "var(--" + b.c + ")", "class": "break-bar" }, svg);
          bar.addEventListener("mousemove", function (e) { showTip(e, tipText); });
          bar.addEventListener("mouseleave", hideTip);
        });
        if (b.dom) el("line", { x1: xs(b.dom), x2: xs(b.dom), y1: y - 2, y2: y + 18, stroke: "var(--ink)", "stroke-width": 2 }, svg);
        text(svg, left - 10, y + 12, b.short || b.s, "break-label", { "text-anchor": "end" });
      });
    }
  }
  function gotoPeriod(p) {
    if (!window.Reveal) return;
    var node = document.querySelector('.period[data-period="' + p.id + '"]');
    var sec = node && node.closest("section");
    if (sec) Reveal.slide(Reveal.getIndices(sec).h);
  }
  function yearLabel(y) { var yr = Math.floor(y); var m = Math.round((y - yr) * 12); var names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]; return (m >= 1 && m <= 12 ? names[Math.min(m, 12) - 1] + " " : "") + yr; }
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;"); }

  /* ------------------------------------------------------------ period chips */
  function chips(root) {
    var btn = root.querySelector(".details-toggle");
    if (btn) btn.addEventListener("click", function () {
      var on = root.classList.toggle("detailed");
      btn.textContent = on ? "headlines" : "details";
      btn.setAttribute("aria-pressed", on ? "true" : "false");
    });
    root.querySelectorAll(".track").forEach(function (tr) {
      var more = tr.querySelector("li.more");
      if (!more) return;
      var n = more.getAttribute("data-more");
      var toggle = function () { tr.classList.toggle("expanded"); more.textContent = (tr.classList.contains("expanded") ? "" : "+") + n + " more"; };
      more.addEventListener("click", toggle);
      more.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggle(); } });
    });
  }

  /* ------------------------------------------------------------ pipeline */
  function pipeline(container) {
    var cap = container.hasAttribute("data-caption") ? container.getAttribute("data-caption") : "activity on the left, action on the right. Click a stage.";
    var W = 1180, H = cap ? 96 : 58, n = D.pipeline.length, gap = 14, bw = (W - gap * (n - 1)) / n, bh = cap ? 50 : 40, y = cap ? 14 : 8;
    var svg = el("svg", { viewBox: "0 0 " + W + " " + H, role: "img", "aria-label": "Detection pipeline: sensor, acquisition, extraction, representation, detection, investigation, decision, response" });
    container.innerHTML = "";
    container.appendChild(svg);
    var defs = el("defs", {}, svg);
    var mk = el("marker", { id: "pipe-arrow-" + Math.random().toString(36).slice(2, 7), viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: 7, markerHeight: 7, orient: "auto-start-reverse" }, defs);
    el("path", { d: "M0,0 L10,5 L0,10 z", "class": "arrowhead" }, mk);
    var stages = {};
    D.pipeline.forEach(function (st, i) {
      var x = i * (bw + gap);
      var g = el("g", { "class": "stage", "data-stage": st.id }, svg);
      el("rect", { x: x, y: y, width: bw, height: bh }, g);
      text(g, x + bw / 2, y + bh / 2 + 5, st.label);
      if (i < n - 1) el("line", { x1: x + bw + 1, x2: x + bw + gap - 1, y1: y + bh / 2, y2: y + bh / 2, "class": "arrow", "marker-end": "url(#" + mk.id + ")" }, svg);
      stages[st.id] = g;
      g.addEventListener("click", function () {
      setHighlight(container, [st.id]); showPanel(container, st.id);
      var panel = panelFor(container); if (panel) panel.innerHTML = '<span class="k">' + st.label + "</span> — " + esc(st.q);
      if (window.Reveal && container.closest("[data-stage-options]")) { try { Reveal.navigateFragment(i - 1); } catch (e) {} }
    });
    });
    if (cap) text(svg, W / 2, H - 6, cap, "caption");
    container._stages = stages;
    var initial = container.getAttribute("data-highlight");
    if (initial) { setHighlight(container, initial.split(",")); showPanel(container, initial.split(",")[0]); }
  }
  /* stage options: the fragment markers step the panels with Next and Previous */
  function stageFromFragments(root) {
    var steps = root.querySelectorAll(".stage-step.visible");
    return steps.length ? steps[steps.length - 1].getAttribute("data-stage") : D.pipeline[0].id;
  }
  function syncStageOptions(root) {
    var pipe = root.querySelector("[data-component=pipeline]");
    var id = stageFromFragments(root);
    if (pipe) { setHighlight(pipe, [id]); showPanel(pipe, id); }
  }
  function syncSteps(root) { if (root.hasAttribute("data-cases")) { if (root._syncCases) root._syncCases(); } else if (root.hasAttribute("data-attack")) syncAttack(root); else if (root.hasAttribute("data-stage-options")) syncStageOptions(root); else syncMatrix(root); }
  function onFragment(e) {
    var list = e.fragments || [e.fragment];
    var roots = [];
    list.forEach(function (f) { if (f && (f.classList.contains("stage-step") || f.classList.contains("attack-step") || f.classList.contains("answer"))) { var r = f.closest("[data-stage-options],[data-stage-matrix],[data-attack],[data-cases]"); if (r && roots.indexOf(r) < 0) roots.push(r); } });
    roots.forEach(syncSteps);
  }
  function panelFor(container) { var id = container.getAttribute("data-panel"); return id ? document.getElementById(id) : null; }
  function showPanel(container, id) {
    var root = container.closest("[data-stage-options]");
    if (!root) return;
    root.querySelectorAll(".stage-panel").forEach(function (p) { p.classList.toggle("active", p.getAttribute("data-stage") === id); });
  }
  function setHighlight(container, ids) {
    var any = ids && ids.length && ids[0] !== "none";
    Object.keys(container._stages || {}).forEach(function (k) {
      var g = container._stages[k];
      g.classList.toggle("on", any && ids.indexOf(k) >= 0);
      g.classList.toggle("off", any && ids.indexOf(k) < 0);
    });
  }
  function reasons(root) {
    var pipe = root.querySelector("[data-component=pipeline]");
    root.querySelectorAll(".reasons li").forEach(function (li) {
      li.addEventListener("click", function () {
        root.querySelectorAll(".reasons li").forEach(function (o) { o.classList.remove("on"); });
        li.classList.add("on");
        var st = li.getAttribute("data-stage") || "none";
        if (pipe) setHighlight(pipe, st.split(","));
        var panel = panelFor(pipe);
        if (panel) panel.innerHTML = li.getAttribute("data-note") || "";
      });
    });
  }
  /* stage matrix: a table whose rows carry data-stage, linked to the pipeline strip above it */
  function matrix(root) {
    var pipe = root.querySelector("[data-component=pipeline]");
    var panels = root.getAttribute("data-view") === "panels";
    var rows = Array.prototype.slice.call(root.querySelectorAll(panels ? ".row-panel" : "tr[data-stage]"));
    var off = panels ? 1 : 0;  // in panel view the first row is shown before any fragment
    function ids(r) { return (r.getAttribute("data-stage") || "").split(","); }
    function valid(list) { return list.filter(function (s) { return pipe && pipe._stages && pipe._stages[s]; }); }
    function light(sel, stages) {
      rows.forEach(function (r) { r.classList.toggle(panels ? "active" : "on", sel.indexOf(r) >= 0); });
      root.querySelectorAll("table.matrix.full tr[data-stage]").forEach(function (tr) { tr.classList.toggle("on", sel.some(function (r) { return r.getAttribute("data-stage") === tr.getAttribute("data-stage"); })); });
      if (pipe) setHighlight(pipe, stages.length ? stages : ["none"]);
    }
    root._pickRow = function (k) {
      if (panels && k < 0) k = 0;
      if (k < 0 || k >= rows.length) light([], []); else light([rows[k]], valid(ids(rows[k])));
    };
    rows.forEach(function (r, k) { r.addEventListener("click", function () { if (!panels) { gotoFragment(root, k - off); root._pickRow(k); } }); });
    root.querySelectorAll("table.matrix.full tr[data-stage]").forEach(function (tr, k) { tr.addEventListener("click", function () { gotoFragment(root, k - off); root._pickRow(k); }); });
    if (pipe) Object.keys(pipe._stages || {}).forEach(function (id) {
      pipe._stages[id].addEventListener("click", function () {
        var hits = rows.filter(function (r) { return ids(r).indexOf(id) >= 0; });
        gotoFragment(root, hits.length ? rows.indexOf(hits[0]) - off : -1);
        light(panels ? hits.slice(0, 1) : hits, [id]);
      });
    });
    var btn = root.querySelector(".table-toggle");
    if (btn) btn.addEventListener("click", function () {
      var on = root.classList.toggle("show-table");
      btn.textContent = on ? "stages" : "full table";
      btn.setAttribute("aria-pressed", on ? "true" : "false");
    });
    if (panels) root._pickRow(0);
  }
  function gotoFragment(root, k) {
    if (!window.Reveal || root.closest("section") !== Reveal.getCurrentSlide()) return;
    try { Reveal.navigateFragment(k); } catch (e) {}
  }
  function syncMatrix(root) {
    var steps = root.querySelectorAll(".stage-step.visible");
    var k = steps.length ? parseInt(steps[steps.length - 1].getAttribute("data-row"), 10) : -1;
    if (root._pickRow) root._pickRow(k);
  }
  function cases(root) {
    var pipe = root.querySelector("[data-component=pipeline]");
    var list = Array.prototype.slice.call(root.querySelectorAll(".case"));
    function isOpen(c) { var an = c.querySelector(".answer"); return c.classList.contains("open") || (an && an.classList.contains("visible")); }
    root._syncCases = function () {
      var open = list.filter(isOpen), last = open.length ? open[open.length - 1] : null;
      if (pipe) setHighlight(pipe, last ? (last.getAttribute("data-stage") || "none").split(",") : ["none"]);
    };
    list.forEach(function (c, k) {
      var b = c.querySelector("button");
      if (!b) return;
      b.addEventListener("click", function () {
        c.classList.add("open");
        if (window.Reveal && root.closest("section") === Reveal.getCurrentSlide()) { try { Reveal.navigateFragment(k); } catch (e) {} }
        root._syncCases();
      });
    });
  }

  /* ------------------------------------------------------------ ATT&CK matrix (schematic, offline) */
  function splitIds(s) { return (s || "").split(",").map(function (x) { return x.trim(); }).filter(Boolean); }
  function attackMatrix(root) {
    var A = window.ATTACK; if (!A) return;
    var mini = root.getAttribute("data-mode") === "mini";
    var expand = splitIds(root.getAttribute("data-expand"));
    var host = root.querySelector(".am-host");
    if (!host) { host = document.createElement("div"); host.className = "am-host"; root.insertBefore(host, root.firstChild); }
    host.innerHTML = "";
    var grid = document.createElement("div"); grid.className = "am-grid"; host.appendChild(grid);
    var cells = [], names = {}, shownTotal = 0, countTotal = 0;
    function cell(tq, sub) {
      var c = document.createElement("div");
      c.className = "am-cell" + (sub ? " sub" : "");
      c.setAttribute("data-id", tq.id);
      c.textContent = tq.name;
      names[tq.id] = tq.name;
      c.addEventListener("mousemove", function (e) { showTip(e, "<b>" + esc(tq.id) + " · " + esc(tq.name) + "</b>" + esc(tq.d || "")); });
      c.addEventListener("mouseleave", hideTip);
      return c;
    }
    A.tactics.forEach(function (t) {
      var col = document.createElement("div"); col.className = "am-col";
      var h = document.createElement("div"); h.className = "am-h";
      h.innerHTML = "<b>" + esc(t.short || t.name) + "</b>" + (mini ? "" : '<span class="n">' + t.count + "</span>");
      h.title = t.name + " (" + t.id + "): " + t.count + " techniques";
      col.appendChild(h);
      var shown = 0;
      t.techniques.forEach(function (tq) {
        var c = cell(tq, false); col.appendChild(c); cells.push(c); shown++;
        (tq.subs || []).forEach(function (s) { names[s.id] = s.name; if (expand.indexOf(tq.id) >= 0) { var sc = cell(s, true); col.appendChild(sc); cells.push(sc); } });
      });
      shownTotal += shown; countTotal += t.count;
      if (!mini && t.count > shown) { var m = document.createElement("div"); m.className = "am-more"; m.textContent = "+" + (t.count - shown) + " more"; col.appendChild(m); }
      grid.appendChild(col);
    });
    if (!mini) {
      var v = document.createElement("div"); v.className = "am-version";
      v.textContent = "MITRE ATT&CK " + A.version + ", schematic: " + shownTotal + " of " + countTotal + " techniques shown, counts per tactic are the real ones. Hover a cell for its ID.";
      host.appendChild(v);
    }
    var path = root.querySelector(".am-path");
    if (!path) { path = document.createElement("div"); path.className = "am-path"; host.appendChild(path); }
    root._cells = cells; root._names = names; root._path = path;
    syncAttack(root);
  }
  function syncAttack(root) {
    if (!root._cells) return;
    var order = {}, seq = 0;
    function add(id, g) { if (!(id in order)) order[id] = { g: g, s: ++seq }; }
    splitIds(root.getAttribute("data-light")).forEach(function (id) { add(id, 0); });
    var steps = root.querySelectorAll(".attack-step.visible"), groups = steps.length;
    Array.prototype.forEach.call(steps, function (s, k) { splitIds(s.getAttribute("data-light")).forEach(function (id) { add(id, k + 1); }); });
    function label(o) { return o.g === 0 ? 0 : (groups > 1 ? o.g : o.s); }
    var rendered = {}; root._cells.forEach(function (c) { rendered[c.getAttribute("data-id")] = true; });
    var cellLabel = {};
    Object.keys(order).forEach(function (id) {
      // a sub-technique whose column is not expanded lights its parent technique's cell
      var target = rendered[id] ? id : (id.indexOf(".") > 0 && rendered[id.split(".")[0]] ? id.split(".")[0] : null);
      if (!target) return;
      var n = label(order[id]);
      if (!(target in cellLabel) || (n && (!cellLabel[target] || n < cellLabel[target]))) cellLabel[target] = n;
    });
    var any = Object.keys(order).length > 0, mini = root.getAttribute("data-mode") === "mini";
    root._cells.forEach(function (c) {
      var id = c.getAttribute("data-id"), on = id in cellLabel;
      c.classList.toggle("on", on); c.classList.toggle("dim", any && !on);
      if (mini) c.style.display = on ? "" : "none";
      var b = c.querySelector(".badge"); if (b) b.remove();
      if (on && cellLabel[id] > 0) { b = document.createElement("span"); b.className = "badge"; b.textContent = cellLabel[id]; c.appendChild(b); }
    });
    var items = Object.keys(order).sort(function (x, y) { return order[x].s - order[y].s; }).map(function (id) {
      var n = label(order[id]);
      return (n ? "<b>" + n + "</b> " : "") + esc(root._names[id] || id) + ' <span class="id">' + esc(id) + "</span>";
    });
    root._path.innerHTML = items.join('<span class="sep">→</span>');
  }

  /* ------------------------------------------------------------ vote tally */
  function vote(root) {
    var cells = root.querySelectorAll(".cell");
    function refresh() {
      root.querySelectorAll("tbody tr").forEach(function (tr) {
        var ns = Array.prototype.map.call(tr.querySelectorAll(".n"), function (x) { return +x.textContent; });
        var max = Math.max.apply(null, ns.concat([1]));
        tr.querySelectorAll(".cell").forEach(function (cell, i) { cell.querySelector(".bar").style.transform = "scaleX(" + (ns[i] / max) + ")"; });
      });
    }
    cells.forEach(function (cell) {
      var n = cell.querySelector(".n");
      cell.querySelector(".plus").addEventListener("click", function () { n.textContent = +n.textContent + 1; refresh(); });
      cell.querySelector(".minus").addEventListener("click", function () { n.textContent = Math.max(0, +n.textContent - 1); refresh(); });
    });
    var reset = root.querySelector(".reset");
    if (reset) reset.addEventListener("click", function () { root.querySelectorAll(".n").forEach(function (x) { x.textContent = "0"; }); refresh(); });
  }

  /* ------------------------------------------------------------ HTTPS chart */
  function httpsChart(container) {
    var data = D.https;
    var W = 1180, H = parseInt(container.getAttribute("data-height"), 10) || 330, L = 54, R = 160, T = 34, B = 36;
    var x0 = 2015.5, x1 = 2027, y0 = 30, y1 = 100;
    var xs = function (v) { return L + (v - x0) / (x1 - x0) * (W - L - R); };
    var ys = function (v) { return T + (y1 - v) / (y1 - y0) * (H - T - B); };
    container.classList.add("viz");
    container.innerHTML = "";
    // legend + table toggle
    var legend = document.createElement("div"); legend.className = "legend";
    data.series.forEach(function (s) { var sp = document.createElement("span"); sp.innerHTML = '<i style="background:var(--' + s.color + ')"></i>' + esc(s.label); legend.appendChild(sp); });
    var btn = document.createElement("button"); btn.type = "button"; btn.textContent = "Table"; legend.appendChild(btn);
    container.appendChild(legend);
    var svg = el("svg", { viewBox: "0 0 " + W + " " + H, role: "img", "aria-label": "Share of page loads over HTTPS, 2015 to 2026, by browser and region" });
    container.appendChild(svg);
    // grid and axes
    for (var v = 40; v <= 100; v += 10) {
      el("line", { x1: L, x2: W - R, y1: ys(v), y2: ys(v), "class": v === 90 ? "axis" : "grid" }, svg);
      text(svg, L - 8, ys(v) + 4, v + "%", "tick-label", { "text-anchor": "end" });
    }
    for (var yr = 2016; yr <= 2026; yr += 1) text(svg, xs(yr), H - 12, String(yr), "tick-label", { "text-anchor": "middle" });
    el("line", { x1: L, x2: W - R, y1: ys(y0), y2: ys(y0), "class": "axis" }, svg);
    // milestones
    data.milestones.forEach(function (m, i) {
      el("line", { x1: xs(m.y), x2: xs(m.y), y1: T - 4, y2: ys(y0), "class": "ms" }, svg);
      text(svg, xs(m.y) + 4, T + 6 + (i % 2) * 14, m.s, "ms-label");
    });
    // series
    var dots = [], ends = [];
    data.series.forEach(function (s) {
      var d = s.points.map(function (p, i) { return (i ? "L" : "M") + xs(p[0]).toFixed(1) + "," + ys(p[1]).toFixed(1); }).join(" ");
      el("path", { d: d, "class": "series", stroke: "var(--" + s.color + ")" }, svg);
      s.points.forEach(function (p) { dots.push({ s: s, x: xs(p[0]), y: ys(p[1]), yr: p[0], v: p[1], c: el("circle", { cx: xs(p[0]), cy: ys(p[1]), r: 3.5, fill: "var(--" + s.color + ")", "class": "dot" }, svg) }); });
      var last = s.points[s.points.length - 1];
      ends.push({ s: s, x: xs(last[0]), y: ys(last[1]), t: (s.short || s.label) + " " + last[1] + "%" });
    });
    // end labels sit in the right margin, pushed apart so they never overlap, with a leader to the last point
    ends.sort(function (a, b) { return a.y - b.y; });
    var minGap = 13;
    ends.forEach(function (e2, i) { e2.ly = e2.y; if (i && e2.ly - ends[i - 1].ly < minGap) e2.ly = ends[i - 1].ly + minGap; });
    var over = ends.length ? ends[ends.length - 1].ly - (ys(y0) - 4) : 0;
    if (over > 0) ends.forEach(function (e2) { e2.ly -= over; });
    ends.forEach(function (e2) {
      var lx = W - R + 8;
      if (lx - e2.x > 12 || Math.abs(e2.ly - e2.y) > 2) el("line", { x1: e2.x + 5, y1: e2.y, x2: lx - 3, y2: e2.ly, "class": "leader", stroke: "var(--" + e2.s.color + ")" }, svg);
      text(svg, lx, e2.ly + 4, e2.t, "dlabel");
    });
    // crosshair + tooltip
    var cross = el("line", { x1: 0, x2: 0, y1: T, y2: ys(y0), "class": "cross", visibility: "hidden" }, svg);
    svg.addEventListener("mousemove", function (e) {
      var pt = svg.createSVGPoint(); pt.x = e.clientX; pt.y = e.clientY;
      var loc = pt.matrixTransform(svg.getScreenCTM().inverse());
      if (loc.x < L || loc.x > W - R) { hideTip(); cross.setAttribute("visibility", "hidden"); return; }
      var yr = x0 + (loc.x - L) / (W - L - R) * (x1 - x0);
      cross.setAttribute("x1", loc.x); cross.setAttribute("x2", loc.x); cross.setAttribute("visibility", "visible");
      var rows = data.series.map(function (s) {
        var best = null; s.points.forEach(function (p) { if (!best || Math.abs(p[0] - yr) < Math.abs(best[0] - yr)) best = p; });
        return Math.abs(best[0] - yr) < 1.2 ? '<div><i style="display:inline-block;width:10px;height:10px;border-radius:5px;background:var(--' + s.color + ');margin-right:6px"></i>' + esc(s.label) + ": " + best[1] + "% (" + yearLabel(best[0]) + ")</div>" : "";
      }).join("");
      showTip(e, "<b>" + yearLabel(yr) + "</b>" + rows);
      dots.forEach(function (d) { d.c.setAttribute("r", Math.abs(d.yr - yr) < 0.3 ? 6 : 3.5); });
    });
    svg.addEventListener("mouseleave", function () { hideTip(); cross.setAttribute("visibility", "hidden"); dots.forEach(function (d) { d.c.setAttribute("r", 3.5); }); });
    // table view
    var tbl = document.createElement("table"); tbl.className = "data";
    var years = [2015.92, 2016.8, 2018.08, 2020.04, 2021.0, 2022.0, 2023.0, 2026.7];
    var thead = "<thead><tr><th>Series</th>" + years.map(function (y) { return "<th>" + yearLabel(y) + "</th>"; }).join("") + "</tr></thead>";
    var tbody = "<tbody>" + data.series.map(function (s) {
      return "<tr><td>" + esc(s.label) + "</td>" + years.map(function (y) { var best = null; s.points.forEach(function (p) { if (Math.abs(p[0] - y) < 0.3 && (!best || Math.abs(p[0] - y) < Math.abs(best[0] - y))) best = p; }); return "<td>" + (best ? best[1] + "%" : "–") + "</td>"; }).join("") + "</tr>";
    }).join("") + "</tbody>";
    tbl.innerHTML = thead + tbody;
    container.appendChild(tbl);
    var sub = document.createElement("div"); sub.className = "sub"; sub.textContent = "Sources: Mozilla ssl_ratios telemetry (Firefox, 14-day mean); Google Transparency Report page-load data (Chrome). Dashed lines mark protocol milestones.";
    container.appendChild(sub);
    btn.addEventListener("click", function () { container.classList.toggle("table-mode"); btn.textContent = container.classList.contains("table-mode") ? "Chart" : "Table"; });
  }

  /* ------------------------------------------------------------ theme + help */
  function toggleTheme() {
    var root = document.documentElement;
    var cur = root.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    var next = cur === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("deck-theme", next); } catch (e) {}
  }
  function toggleHelp() { var h = document.getElementById("help"); if (h) h.hidden = !h.hidden; }

  /* ------------------------------------------------------------ init */
  function init() {
    document.querySelectorAll("[data-component=timeline]").forEach(timeline);
    document.querySelectorAll(".period").forEach(chips);
    document.querySelectorAll("[data-component=pipeline]").forEach(pipeline);
    document.querySelectorAll("[data-reasons]").forEach(reasons);
    document.querySelectorAll("[data-cases]").forEach(cases);
    document.querySelectorAll("[data-stage-matrix]").forEach(matrix);
    document.querySelectorAll("[data-attack]").forEach(attackMatrix);
    document.querySelectorAll("[data-component=vote]").forEach(vote);
    document.querySelectorAll("[data-component=https-chart]").forEach(httpsChart);
    if (window.Reveal) {
      Reveal.addKeyBinding({ keyCode: 84, key: "T", description: "Toggle light/dark theme" }, toggleTheme);
      Reveal.addKeyBinding({ keyCode: 191, key: "?", description: "Keyboard help" }, toggleHelp);
      Reveal.on("slidechanged", hideTip);
      Reveal.on("fragmentshown", onFragment);
      Reveal.on("fragmenthidden", onFragment);
      Reveal.on("slidechanged", function (e) { if (e.currentSlide) e.currentSlide.querySelectorAll("[data-stage-options],[data-stage-matrix],[data-attack],[data-cases]").forEach(syncSteps); });
    }
  }
  window.Deck = { init: init, toggleTheme: toggleTheme };
})();
