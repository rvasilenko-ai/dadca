/* Lecture 2 deck runtime: scales the stage, steps builds, routes #/s12/3, and shows presenter notes.
   No dependencies. Sections are read from the DOM in order; each carries data-id, data-steps and data-part. */
(function () {
  'use strict';
  var stage = document.getElementById('stage');
  var slides = Array.prototype.slice.call(stage.querySelectorAll('section.slide'));
  var progress = document.getElementById('progress');
  var notes = document.getElementById('notes');
  var notesBody = document.getElementById('notes-body');
  var help = document.getElementById('help');
  var i = 0, step = 0;

  function stepsOf(s) { return parseInt(s.dataset.steps || '0', 10) || 0; }
  // an appearing build's self-drawing edges keep their arrowheads hidden until the line has drawn (760ms, see deck.css)
  function holdArrowheads(group) {
    var edges = group.querySelectorAll('.draw[marker-end]');
    for (var k = 0; k < edges.length; k++) (function (d) { d.classList.add('marker-wait'); setTimeout(function () { d.classList.remove('marker-wait'); }, 760); })(edges[k]);
  }

  function fit() {
    var w = window.innerWidth - (notes.hidden ? 0 : notes.offsetWidth), h = window.innerHeight;
    var s = Math.min(w / 1920, h / 1080);
    stage.style.setProperty('--scale', s);
    stage.style.left = Math.max(0, (w - 1920 * s) / 2) + 'px';
    stage.style.top = Math.max(0, (h - 1080 * s) / 2) + 'px';
  }

  function apply(pushHash) {
    var s = slides[i];
    slides.forEach(function (el, k) { el.classList.toggle('is-current', k === i); });
    var builds = s.querySelectorAll('[data-build]');
    var still = document.documentElement.classList.contains('is-still');
    for (var b = 0; b < builds.length; b++) {
      var n = parseInt(builds[b].dataset.build, 10);
      var shown = n <= step, appearing = shown && !builds[b].classList.contains('is-shown');
      builds[b].classList.toggle('is-shown', shown);
      builds[b].classList.toggle('is-current', n === step && step > 0);
      if (appearing && !still && pushHash !== false) holdArrowheads(builds[b]);
    }
    var caps = s.querySelectorAll('.step-captions > p');
    if (caps.length) {
      var idx = Math.min(step, caps.length - 1);
      for (var c = 0; c < caps.length; c++) caps[c].classList.toggle('is-shown', c === idx);
    }
    // progress across stage sections, with a share for the step
    var frac = (i + (stepsOf(s) ? step / (stepsOf(s) + 1) : 0)) / Math.max(1, slides.length - 1);
    progress.style.width = (Math.min(1, frac) * 100) + '%';
    progress.style.background = getComputedStyle(s).getPropertyValue('--part') || '';
    // presenter notes
    var aside = s.querySelector('aside.notes');
    notesBody.innerHTML = aside ? aside.innerHTML : '<p class="meta">no notes</p>';
    // close any open sources panel on other slides
    slides.forEach(function (el, k) { if (k !== i) { var d = el.querySelector('details.srcs'); if (d) d.open = false; } });
    if (pushHash !== false) {
      var id = s.dataset.id + (step ? '/' + step : '');
      if (location.hash !== '#/' + id) history.replaceState(null, '', '#/' + id);
    }
    document.title = (s.dataset.number ? s.dataset.number + ' · ' : '') + (s.querySelector('.slide-title, .display, .divider-title') || {}).textContent || 'When the Attacker Is an Agent';
  }

  function next() {
    if (step < stepsOf(slides[i])) { step++; }
    else if (i < slides.length - 1) { i++; step = 0; }
    apply();
  }
  function prev() {
    if (step > 0) { step--; }
    else if (i > 0) { i--; step = stepsOf(slides[i]); }
    apply();
  }
  function go(idx, st) { i = Math.max(0, Math.min(slides.length - 1, idx)); step = Math.max(0, Math.min(stepsOf(slides[i]), st || 0)); apply(); }

  function fromHash() {
    var m = /^#\/([a-z0-9]+)(?:\/(\d+))?$/i.exec(location.hash || '');
    if (!m) { apply(false); return; }
    var id = m[1], st = parseInt(m[2] || '0', 10);
    var idx = -1;
    slides.forEach(function (el, k) { if (el.dataset.id === id) idx = k; });
    if (idx < 0 && /^\d+$/.test(id)) slides.forEach(function (el, k) { if (el.dataset.number === id) idx = k; });
    if (idx < 0) idx = 0;
    i = idx; step = Math.min(stepsOf(slides[i]), st); apply(false);
  }

  function toggleNotes() { notes.hidden = !notes.hidden; try { localStorage.setItem('deck2-notes', notes.hidden ? '0' : '1'); } catch (e) {} fit(); }
  function toggleTheme() {
    var cur = document.documentElement.getAttribute('data-theme');
    var dark = cur ? cur === 'dark' : window.matchMedia('(prefers-color-scheme: dark)').matches;
    var nextTheme = dark ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', nextTheme);
    try { localStorage.setItem('deck2-theme', nextTheme); } catch (e) {}
    apply(false);
  }
  function toggleSources() { var d = slides[i].querySelector('details.srcs'); if (d) d.open = !d.open; }
  function fullscreen() { var el = document.documentElement; if (document.fullscreenElement) document.exitFullscreen(); else if (el.requestFullscreen) el.requestFullscreen(); }

  document.addEventListener('keydown', function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var k = e.key;
    if (!help.hidden && k !== '?' && k !== 'Escape') return;
    switch (k) {
      case 'ArrowRight': case 'ArrowDown': case 'PageDown': case ' ': case 'Enter': e.preventDefault(); next(); break;
      case 'ArrowLeft': case 'ArrowUp': case 'PageUp': case 'Backspace': e.preventDefault(); prev(); break;
      case 'Home': e.preventDefault(); go(0, 0); break;
      case 'End': e.preventDefault(); go(slides.length - 1, 0); break;
      case 'n': case 'N': toggleNotes(); break;
      case 's': case 'S': toggleSources(); break;
      case 't': case 'T': toggleTheme(); break;
      case 'f': case 'F': fullscreen(); break;
      case '?': help.hidden = !help.hidden; break;
      case 'Escape': help.hidden = true; var d = slides[i].querySelector('details.srcs'); if (d) d.open = false; break;
    }
  });
  stage.addEventListener('click', function (e) {
    if (e.target.closest('a, details, summary, button, input')) return;
    var x = e.clientX;
    if (x < window.innerWidth * 0.18) prev(); else next();
  });
  var tx = null;
  stage.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; }, { passive: true });
  stage.addEventListener('touchend', function (e) { if (tx === null) return; var dx = e.changedTouches[0].clientX - tx; tx = null; if (dx < -40) next(); else if (dx > 40) prev(); }, { passive: true });
  help.addEventListener('click', function () { help.hidden = true; });
  window.addEventListener('resize', fit);
  window.addEventListener('hashchange', fromHash);

  try { if (localStorage.getItem('deck2-notes') === '1') notes.hidden = false; } catch (e) {}
  // ?still turns motion off (screenshots); ?theme=light|dark forces a theme without storing it
  var q = new URLSearchParams(location.search);
  if (q.has('still')) document.documentElement.classList.add('is-still');
  if (q.get('theme') === 'light' || q.get('theme') === 'dark') document.documentElement.setAttribute('data-theme', q.get('theme'));
  fit();
  fromHash();
  window.deck = { go: go, next: next, prev: prev, slides: slides };
})();
