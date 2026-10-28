"""Motor de Normalización de Prototipos (Fase 10).

Inyecta el contrato de altura 100%, la tipografía fluida de diapositiva real,
la distribución anti-vacíos, el runtime responsivo (is-embedded + ResizeObserver
universal de <canvas>) y la Entrada Cinemática de Video (#cinematicVideoGate)
en los prototipos HTML embebidos por back/build_deck.py.
"""

from __future__ import annotations

import base64
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

SECTION_GATE_BG = {
    1: "#040714",
    2: "#040714",
    3: "#040812",
    4: "#040714",
    5: "#03050F",
}

VIDEO_SLIDE_CANDIDATES = (
    (1, 5),
    (1, 7),
    (1, 9),
    (1, 10),
    (3, 19),
    (3, 21),
    (4, 26),
    (4, 27),
    (5, 29),
)

ENGINE_OVERRIDE_CSS = """<style id="deck-engine-override-css">
/* === MOTOR DE NORMALIZACIÓN VISUAL Y TIPOGRÁFICA DE DIAPOSITIVAS (F10) === */
html, body {
  width: 100% !important;
  height: 100% !important;
  min-height: 100% !important;
  max-height: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
  overflow: hidden !important;
}
body.is-embedded {
  display: flex !important;
  flex-direction: column !important;
  width: 100% !important;
  height: 100% !important;
}
body.is-embedded #slideFrame {
  width: 100% !important;
  height: 100% !important;
  min-height: 100% !important;
  max-height: 100% !important;
  aspect-ratio: auto !important;
  flex: 1 1 100% !important;
  display: grid !important;
  grid-template-rows: auto auto minmax(0, 1fr) auto !important;
  gap: clamp(8px, 1.1vh, 14px) !important;
  padding: clamp(10px, 1.4vh, 18px) clamp(14px, 1.6vw, 24px) clamp(8px, 1vh, 12px) !important;
  border: none !important;
  border-radius: 0 !important;
  box-shadow: none !important;
}

/* CABECERA Y BARRA DE PROCESO UNIFICADAS */
.eyebrow {
  font-size: clamp(10.5px, 0.8vw, 12.5px) !important;
  letter-spacing: 0.12em !important;
}
h1 {
  font-size: clamp(20px, 1.75vw, 28px) !important;
  line-height: 1.12 !important;
}
.proc-year, .step-title {
  font-size: clamp(12px, 0.92vw, 14.5px) !important;
  line-height: 1.18 !important;
}
.proc-sub, .step-sub {
  font-size: clamp(10px, 0.75vw, 12px) !important;
}

/* PROPORCIÓN ARMÓNICA 40/60 Y ALTURA COMPLETA DEL WORKSPACE */
.workspace, .main-stage {
  display: grid !important;
  grid-template-columns: minmax(340px, 0.40fr) minmax(0, 0.60fr) !important;
  gap: clamp(12px, 1.2vw, 18px) !important;
  height: 100% !important;
  min-height: 0 !important;
  align-items: stretch !important;
}

/* COLUMNA EXPLICATIVA: ESCALA DE DIAPOSITIVA REAL Y CERO HUECOS NEGROS */
.left-column, .narrative-card {
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  height: 100% !important;
  min-height: 0 !important;
  padding: clamp(12px, 1.5vh, 20px) clamp(14px, 1.3vw, 20px) !important;
  gap: clamp(8px, 1.1vh, 14px) !important;
  overflow: hidden !important;
}
.narr-top, .narr-header {
  display: flex !important;
  flex-direction: column !important;
  gap: clamp(4px, 0.6vh, 8px) !important;
  flex-shrink: 0 !important;
}
.stage-tag, .narr-tag, .act-badge {
  font-size: clamp(10.5px, 0.78vw, 12px) !important;
  padding: 4px 10px !important;
}
.narr-title, .narrative-card h2, .left-column h2 {
  font-size: clamp(17.5px, 1.42vw, 22.5px) !important;
  line-height: 1.2 !important;
  font-weight: 700 !important;
  color: #f8fbff !important;
  margin: 0 !important;
}
.narr-lead, .narrative-card .lead {
  font-size: clamp(13px, 1.02vw, 15.8px) !important;
  line-height: 1.42 !important;
  color: #d8e6f8 !important;
  margin: 0 !important;
}
.narr-blocks, .layers-strip {
  flex: 1 1 auto !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-evenly !important;
  gap: clamp(7px, 1vh, 12px) !important;
  min-height: 0 !important;
}
.narr-block, .info-block {
  flex: 1 1 auto !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
  padding: clamp(9px, 1.2vh, 14px) clamp(11px, 1vw, 15px) !important;
  border-radius: 10px !important;
}
.narr-block-title, .info-block-label {
  font-size: clamp(10.5px, 0.8vw, 12.5px) !important;
  margin-bottom: 4px !important;
  letter-spacing: 0.08em !important;
}
.narr-block p, .narr-block-body, .info-block-text {
  font-size: clamp(12.5px, 0.96vw, 15px) !important;
  line-height: 1.38 !important;
  color: #e2edf8 !important;
  margin: 0 !important;
}
.layer-list {
  flex: 1 1 auto !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  gap: clamp(5px, 0.7vh, 9px) !important;
}
.layer-row {
  flex: 1 1 auto !important;
  padding: clamp(6px, 0.85vh, 10px) 10px !important;
}
.layer-name {
  font-size: clamp(12.5px, 0.94vw, 14.5px) !important;
}
.layer-desc {
  font-size: clamp(11px, 0.84vw, 13px) !important;
  color: #cbd5e1 !important;
}
.formula-bar {
  padding: clamp(8px, 1vh, 12px) 13px !important;
  flex-shrink: 0 !important;
}
.formula-lhs {
  font-size: clamp(12.5px, 0.95vw, 14.8px) !important;
}
.executive-takeaway, .speaker-box {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  padding: clamp(8px, 1vh, 12px) 13px !important;
  border-radius: 9px !important;
  font-size: clamp(12px, 0.92vw, 14.2px) !important;
  line-height: 1.32 !important;
  margin-top: 0 !important;
  flex-shrink: 0 !important;
}

/* COLUMNA DERECHA: LIENZOS AUTO-AJUSTABLES AL 100% DE LA ALTURA */
.sim-card, .visual-column {
  height: 100% !important;
  min-height: 0 !important;
}
.canvas-wrap, .chart-wrap {
  flex: 1 1 0% !important;
  min-height: 0 !important;
  height: 100% !important;
}

/* BOTÓN DE ENTRADA CINEMÁTICA EN LA BARRA DE ETAPAS (F10 ↔ F11) */
.flowbar:has(> .cinematic-intro-btn) {
  grid-template-columns: auto minmax(0, 1fr) auto !important;
}
.stage-nav:has(> .cinematic-intro-btn) {
  display: flex !important;
  align-items: center !important;
}
.cinematic-intro-btn {
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  flex: 0 0 auto !important;
  padding: clamp(6px, 0.8vh, 9px) clamp(9px, 0.8vw, 13px) !important;
  border: 1px solid rgba(56, 239, 255, 0.42) !important;
  border-radius: 10px !important;
  background: linear-gradient(120deg, rgba(8, 47, 73, 0.9), rgba(8, 15, 32, 0.92)) !important;
  color: #7dd3fc !important;
  font: 700 clamp(10.5px, 0.8vw, 12.5px)/1 var(--mono, "IBM Plex Mono", monospace) !important;
  letter-spacing: 0.06em !important;
  cursor: pointer !important;
  white-space: nowrap !important;
  transition: transform 0.18s ease, border-color 0.18s ease !important;
}
.cinematic-intro-btn:hover {
  border-color: #38efff !important;
  transform: translateY(-1px) !important;
}
</style>"""

ENGINE_RUNTIME_JS = """<script id="deck-engine-runtime-js">
/* === RUNTIME UNIVERSAL DEL MOTOR DE DIAPOSITIVAS (F10) === */
(function () {
  "use strict";
  var DECK_SLIDE_NUM = __DECK_SLIDE_NUM__;
  var DECK_HAS_VIDEO = __DECK_HAS_VIDEO__;

  function ensureEmbedded() {
    try {
      if (window.self !== window.top || document.documentElement.hasAttribute("data-embedded")) {
        document.body.classList.add("is-embedded");
      }
    } catch (err) {
      document.body.classList.add("is-embedded");
    }
  }

  function normalizeLegacySpeakerBoxes() {
    var boxes = document.querySelectorAll(".speaker-box");
    Array.prototype.forEach.call(boxes, function (box) {
      var text = box.textContent || "";
      if (text.indexOf("GUÍA DE EXPOSICIÓN") !== -1 || text.indexOf("GUIA DE EXPOSICION") !== -1) {
        var header = box.querySelector(".speaker-header, .speaker-box-title, span");
        if (header) header.innerHTML = "💡 Idea Clave:";
        box.classList.remove("speaker-box");
        box.classList.add("executive-takeaway");
      }
    });
  }

  function normalizeTakeawayFragments() {
    var boxes = document.querySelectorAll(".executive-takeaway, .takeaway-card");
    Array.prototype.forEach.call(boxes, function (box) {
      var label = box.firstElementChild;
      while (label && label.tagName !== "STRONG" && label.tagName !== "B") {
        label = label.nextElementSibling;
      }
      if (!label) return;
      var nodes = [];
      var node = label.nextSibling;
      while (node) {
        nodes.push(node);
        node = node.nextSibling;
      }
      if (!nodes.length) return;
      var hasUnwrappedElement = nodes.some(function (n) {
        return n.nodeType === 1 && n.tagName !== "SPAN";
      });
      if (!hasUnwrappedElement) return;
      var wrapper = document.createElement("span");
      nodes.forEach(function (n) { wrapper.appendChild(n); });
      box.appendChild(wrapper);
    });
  }

  var resizeTimer = null;
  function requestResize() {
    if (resizeTimer) clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
      try {
        window.dispatchEvent(new Event("resize"));
      } catch (err) {
        var ev = document.createEvent("Event");
        ev.initEvent("resize", true, true);
        window.dispatchEvent(ev);
      }
    }, 80);
  }

  var canvasObserver = null;
  if (typeof ResizeObserver !== "undefined") {
    canvasObserver = new ResizeObserver(function () { requestResize(); });
    try { canvasObserver.observe(document.documentElement); } catch (err) {}
  }

  function observeCanvases() {
    if (!canvasObserver) return;
    var canvases = document.querySelectorAll("canvas");
    Array.prototype.forEach.call(canvases, function (canvas) {
      if (canvas.__deckEngineObserved) return;
      canvas.__deckEngineObserved = true;
      try { canvasObserver.observe(canvas); } catch (err) {}
    });
  }

  function bootstrapCanvasSizes() {
    var dpr = window.devicePixelRatio || 1;
    var canvases = document.querySelectorAll("canvas");
    Array.prototype.forEach.call(canvases, function (canvas) {
      if (canvas.width > 1 && canvas.height > 1) return;
      var rect = canvas.getBoundingClientRect();
      if (rect.width < 2 || rect.height < 2) return;
      canvas.width = Math.round(rect.width * dpr);
      canvas.height = Math.round(rect.height * dpr);
    });
  }

  function wireCinematicIntroButton() {
    if (!DECK_HAS_VIDEO) return;
    var flowbar = document.querySelector(".flowbar, .stage-nav");
    if (!flowbar) return;
    if (document.getElementById("btnCinematicIntro")) return;
    var btn = document.createElement("button");
    btn.type = "button";
    btn.id = "btnCinematicIntro";
    btn.className = "cinematic-intro-btn";
    btn.innerHTML = "🎬 Intro";
    btn.title = "Reproyectar la introducción cinemática (tecla V)";
    btn.addEventListener("click", function (event) {
      event.preventDefault();
      event.stopPropagation();
      window.parent.postMessage({ type: "deck_replay_video", slide: DECK_SLIDE_NUM }, "*");
    });
    flowbar.insertBefore(btn, flowbar.firstChild);
    window.addEventListener("keydown", function (event) {
      if (event.ctrlKey || event.metaKey || event.altKey) return;
      if (event.key === "v" || event.key === "V" || event.key === "0") {
        window.parent.postMessage({ type: "deck_replay_video", slide: DECK_SLIDE_NUM }, "*");
      }
    });
  }

  function boot() {
    ensureEmbedded();
    normalizeLegacySpeakerBoxes();
    normalizeTakeawayFragments();
    observeCanvases();
    bootstrapCanvasSizes();
    wireCinematicIntroButton();
    requestResize();
    setTimeout(requestResize, 160);
    setTimeout(function () {
      observeCanvases();
      bootstrapCanvasSizes();
      requestResize();
    }, 640);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
  window.addEventListener("load", function () {
    observeCanvases();
    requestResize();
  });
})();
</script>"""

ENGINE_DECK_GATE_CSS = """<style id="deck-cinematic-gate-css">
/* === COMPUERTA DE ENTRADA CINEMÁTICA (F10 ↔ F11) === */
.cinematic-video-gate {
  position: absolute;
  inset: 0;
  z-index: 90;
  display: none;
  align-items: center;
  justify-content: center;
  border-radius: 14px;
  overflow: hidden;
  background: var(--gate-bg, #040714);
  opacity: 0;
  transition: opacity 0.45s cubic-bezier(0.22, 1, 0.36, 1);
  cursor: pointer;
}
.cinematic-video-gate.is-active {
  display: flex;
  opacity: 1;
}
.cinematic-video-gate.is-fading {
  opacity: 0;
  pointer-events: none;
}
.cinematic-video-gate video {
  width: 100%;
  height: 100%;
  object-fit: contain;
  background: var(--gate-bg, #040714);
}
.cinematic-hud {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  padding: 16px 24px;
  background: linear-gradient(to top, rgba(2, 6, 16, 0.92), rgba(2, 6, 16, 0));
}
.cinematic-badge {
  font: 700 12px/1.3 "IBM Plex Mono", monospace;
  letter-spacing: 0.16em;
  color: #7dd3fc;
  text-transform: uppercase;
}
.cinematic-skip-btn {
  flex: 0 0 auto;
  padding: 10px 18px;
  border: 1px solid rgba(125, 211, 252, 0.5);
  border-radius: 10px;
  background: rgba(8, 47, 73, 0.85);
  color: #e0f2fe;
  font: 700 13px/1 "IBM Plex Sans", sans-serif;
  cursor: pointer;
  transition: border-color 0.2s ease, transform 0.2s ease;
}
.cinematic-skip-btn:hover {
  border-color: #38efff;
  transform: translateY(-1px);
}
</style>"""

ENGINE_DECK_GATE_JS = """<script id="deck-cinematic-gate-js">
/* === HANDOFF SIN COSTURA DE LA ENTRADA CINEMÁTICA (F10 ↔ F11) === */
(function () {
  "use strict";
  var gates = Array.prototype.slice.call(document.querySelectorAll(".cinematic-video-gate"));
  if (!gates.length) return;
  var activeGate = null;
  var deckBooted = false;
  var GATE_FADE_MS = 450;

  function gateFor(index) {
    for (var i = 0; i < gates.length; i++) {
      if (String(gates[i].getAttribute("data-slide-index")) === String(index)) return gates[i];
    }
    return null;
  }

  function openGate(gate) {
    if (!gate) return;
    if (activeGate && activeGate !== gate) closeGate(activeGate, true);
    var video = gate.querySelector("video");
    activeGate = gate;
    gate.hidden = false;
    gate.classList.remove("is-fading");
    gate.classList.add("is-active");
    if (video) {
      try { video.currentTime = 0; } catch (err) {}
      var promise = video.play();
      if (promise && promise.catch) promise.catch(function () {});
    }
  }

  function closeGate(gate, instant) {
    gate = gate || activeGate;
    if (!gate) return;
    var video = gate.querySelector("video");
    if (video) { try { video.pause(); } catch (err) {} }
    if (activeGate === gate) activeGate = null;
    if (instant) {
      gate.classList.remove("is-active", "is-fading");
      gate.hidden = true;
      return;
    }
    gate.classList.add("is-fading");
    setTimeout(function () {
      gate.classList.remove("is-active", "is-fading");
      gate.hidden = true;
    }, GATE_FADE_MS);
  }

  gates.forEach(function (gate) {
    var video = gate.querySelector("video");
    if (video) {
      video.addEventListener("ended", function () {
        gate.dataset.seen = "true";
        closeGate(gate);
      });
    }
    var skip = gate.querySelector(".cinematic-skip-btn");
    if (skip) {
      skip.addEventListener("click", function (event) {
        event.stopPropagation();
        gate.dataset.seen = "true";
        closeGate(gate);
      });
    }
    gate.addEventListener("click", function (event) {
      if (event.target === gate) {
        gate.dataset.seen = "true";
        closeGate(gate);
      }
    });
  });

  window.__deckCinematicEnterSlide = function (index) {
    var gate = gateFor(index);
    if (activeGate && activeGate !== gate) closeGate(activeGate, true);
    if (gate && deckBooted && gate.dataset.seen !== "true") openGate(gate);
  };

  window.addEventListener("message", function (event) {
    var data = event.data || {};
    if (data.type === "deck_replay_video") {
      var gate = gateFor(data.slide);
      if (gate) {
        gate.dataset.seen = "true";
        openGate(gate);
      }
    }
  });

  window.addEventListener("keydown", function (event) {
    if (!activeGate) return;
    var key = event.key;
    if (key === "ArrowRight" || key === " " || key === "Spacebar" || key === "Enter" || key === "Escape") {
      event.preventDefault();
      event.stopImmediatePropagation();
      activeGate.dataset.seen = "true";
      closeGate(activeGate);
    }
  }, true);

  var params = new URLSearchParams(window.location.search);
  var forcedIntro = params.get("intro");
  window.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () { deckBooted = true; }, 350);
    if (forcedIntro) {
      var gate = gateFor(forcedIntro);
      if (gate) {
        gate.dataset.seen = "true";
        openGate(gate);
      }
    }
  });
})();
</script>"""


def discover_slide_video(root_dir: Path | str, section_num: int, slide_num: int) -> Path | None:
    """Busca el MP4 canónico en video/seccion_{N}/diapo_{M}/video_*/<nombre>.mp4.

    Prioriza el render principal e ignora respaldos versionados (_v1, _v2, _v3).
    """
    root = Path(root_dir)
    diapo_dir = root / "video" / f"seccion_{section_num}" / f"diapo_{slide_num}"
    if not diapo_dir.exists():
        return None
    candidates = sorted(
        p for p in diapo_dir.glob("video_*/*.mp4")
        if not re.search(r"_v\d+", p.stem)
    )
    return candidates[0] if candidates else None


def render_slide_video_gate(
    section_num: int,
    slide_num: int,
    video_rel_path: str,
    badge_label: str | None = None,
    gate_id: str = "cinematicVideoGate",
) -> str:
    """Genera la compuerta #cinematicVideoGate (Etapa 0 dentro de la diapositiva)."""
    bg = SECTION_GATE_BG.get(section_num, "#040714")
    label = badge_label or f"🎬 INTRO VISUAL · DIAPO {slide_num:02d}"
    return f"""<div id="{gate_id}" class="cinematic-video-gate" data-slide-video="true" data-slide-index="{slide_num}" style="--gate-bg: {bg};" hidden>
  <video id="{gate_id}Player" src="{video_rel_path}" preload="auto" muted playsinline></video>
  <div class="cinematic-hud">
    <span class="cinematic-badge">{label}</span>
    <button type="button" class="cinematic-skip-btn">Pasar al Simulador Interactivo →</button>
  </div>
</div>"""


def _inject_before(html_str: str, closing_tag: str, payload: str) -> str:
    if closing_tag in html_str:
        return html_str.replace(closing_tag, payload + "\n" + closing_tag, 1)
    return html_str + "\n" + payload


def _normalize_dom(html_str: str) -> str:
    def _hide_split_hint(match: re.Match) -> str:
        tag = match.group(0)
        if re.search(r"\shidden(\s|=|>)", tag):
            return tag
        return tag[:-1] + " hidden>"

    html_str = re.sub(
        r'<div[^>]*class="[^"]*\bcanvas-split-hint\b[^"]*"[^>]*>',
        _hide_split_hint,
        html_str,
    )
    return html_str


def normalize_prototype_html(
    html_str: str,
    slide_num: int,
    section_num: int,
    video_rel_path: str | None = None,
) -> str:
    """Aplica al prototipo el CSS maestro, el runtime responsivo y la Entrada Cinemática."""
    normalized = _normalize_dom(html_str)
    normalized = _inject_before(normalized, "</head>", ENGINE_OVERRIDE_CSS)
    runtime = (
        ENGINE_RUNTIME_JS
        .replace("__DECK_SLIDE_NUM__", str(int(slide_num)))
        .replace("__DECK_HAS_VIDEO__", "true" if video_rel_path else "false")
    )
    normalized = _inject_before(normalized, "</body>", runtime)
    return normalized


def load_prototype_b64(
    path: Path | str,
    slide_num: int,
    section_num: int,
    root_dir: Path | str | None = None,
) -> str:
    """Lee un prototipo, lo homologa con el motor y lo codifica en Base64."""
    path = Path(path)
    root = Path(root_dir) if root_dir is not None else ROOT_DIR
    html_str = path.read_text(encoding="utf-8")
    video_rel_path = None
    video = discover_slide_video(root, section_num, slide_num)
    if video is not None:
        try:
            video_rel_path = video.relative_to(root).as_posix()
        except ValueError:
            video_rel_path = video.as_posix()
    normalized = normalize_prototype_html(html_str, slide_num, section_num, video_rel_path)
    return base64.b64encode(normalized.encode("utf-8")).decode("ascii")
