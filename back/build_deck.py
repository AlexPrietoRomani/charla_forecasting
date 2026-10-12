import os
import sys
import json
from pathlib import Path
import pandas as pd

# Resolver directorios base y front
BASE_DIR = Path(__file__).resolve().parent.parent
FRONT_DIR = BASE_DIR / "front"
if str(FRONT_DIR) not in sys.path:
    sys.path.insert(0, str(FRONT_DIR))
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from deck_styles import get_deck_css
from deck_slides_p1 import get_slides_part1
from deck_slides_p2 import get_slides_part2
from deck_notes import get_speaker_notes
from deck_branding import get_branding

def clean_nans(obj):
    if isinstance(obj, float) and (pd.isna(obj) or obj != obj):
        return None
    elif isinstance(obj, dict):
        return {k: clean_nans(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_nans(v) for v in obj]
    return obj

def build_deck():
    # Cargar datos reales auditados
    bench_df = pd.read_csv(BASE_DIR / "data/caso_1/benchmark_punchana.csv")
    forecast_7d_df = pd.read_csv(BASE_DIR / "data/caso_1/senamhi_forecast_7d.csv")
    extrap_df = pd.read_csv(BASE_DIR / "data/caso_1/experimento_extrapolacion.csv")
    cafe_camp_df = pd.read_csv(BASE_DIR / "data/caso_2/cafe_jaen_campanias.csv")
    cafe_res_df = pd.read_csv(BASE_DIR / "data/caso_2/cafe_jaen_resultados.csv")
    noaa_ecmwf_df = pd.read_csv(BASE_DIR / "data/caso_1/noaa_ecmwf_forecast.csv")
    
    with open(BASE_DIR / "data/caso_2/cafe_jaen_hipotesis.json", "r", encoding="utf-8") as f:
        hipotesis_cafe = json.load(f)

    senamhi_diario_df = pd.read_csv(BASE_DIR / "data/caso_1/senamhi_diario.csv")
    senamhi_sub = senamhi_diario_df.tail(180).to_dict(orient="records")

    raw_payload = {
        "benchmark": bench_df.to_dict(orient="records"),
        "forecast_7d": forecast_7d_df.to_dict(orient="records"),
        "extrapolacion": extrap_df.to_dict(orient="records"),
        "cafe_campanias": cafe_camp_df.to_dict(orient="records"),
        "cafe_resultados": cafe_res_df.to_dict(orient="records"),
        "hipotesis_cafe": hipotesis_cafe,
        "noaa_ecmwf": noaa_ecmwf_df.to_dict(orient="records"),
        "senamhi_reciente": senamhi_sub
    }
    data_payload = clean_nans(raw_payload)
    data_json = json.dumps(data_payload, ensure_ascii=False)
    notes_json = json.dumps(get_speaker_notes(), ensure_ascii=False)

    branding = get_branding()
    b64_header_logo = branding["b64_header"]
    b64_dw_logo = branding["b64_dw"]
    qr_svg = branding["qr_svg"]

    css_content = get_deck_css(branding=branding)

    # Inyección de Chart.js local offline como fallback si CDN no responde
    chartjs_local_code = ""
    if os.path.exists("scripts/assets/chart.umd.min.js"):
        with open("scripts/assets/chart.umd.min.js", "r", encoding="utf-8") as f:
            chartjs_local_code = f.read()

    slides_p1 = get_slides_part1(branding=branding)
    slides_p2 = get_slides_part2(branding=branding)

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>¿Puede la IA predecir el futuro? Lecciones de forecasting desde el mundo real</title>
<link rel="icon" href="data:,">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<script>
  if (typeof Chart === 'undefined') {{
    {chartjs_local_code}
  }}
  if (typeof Chart !== 'undefined') {{
    Chart.defaults.color = '#CBD5E1';
    Chart.defaults.borderColor = 'rgba(169, 184, 218, 0.15)';
    Chart.defaults.font.family = '"IBM Plex Sans", sans-serif';
  }}
</script>
<style>
{css_content}
</style>
</head>
<body>

<!-- BARRA DE PROGRESO SUPERIOR -->
<div class="progress-container">
  <div class="progress-bar" id="progressBar"></div>
</div>

<!-- CONTENEDOR PRINCIPAL DE DIAPOSITIVAS -->
<main class="deck-container">
{slides_p1}
{slides_p2}
</main>

<!-- BARRA INFERIOR DE ESTADO Y CONTROL CON BRANDING IQUITOS DATA FEST 2026 -->
<footer class="deck-footer">
  <div style="display:flex; align-items:center; gap:16px;">
    <!-- LOGOS INSTITUCIONALES DEL EVENTO -->
    <div style="display:flex; align-items:center; gap:12px;">
      <img src="data:image/png;base64,{b64_header_logo}" alt="UNAP · Neo Kernel · Grupo de Datos & IA" style="height:26px; filter:drop-shadow(0 1px 2px rgba(0,0,0,0.6)); opacity:0.95;">
      <span style="font-size:11px; font-weight:700; color:var(--text-faint); letter-spacing:0.04em;" class="mono hidden-mobile">
        IQUITOS <span style="color:#12C8FC;">DATA FEST 2026</span> · 30 de octubre · Aula Magna UNAP
      </span>
    </div>
    <div style="width:1px; height:18px; background:rgba(18, 200, 252, 0.25); margin:0 4px;"></div>
    <div style="font-weight:700; font-size:13px; color:#12C8FC;" class="mono" id="slideIndicator">01 / 23</div>
    <div style="font-size:12px; color:var(--text-faint);" class="mono" id="actIndicator">Apertura · Portada</div>
  </div>

  <div style="display:flex; align-items:center; gap:8px;">
    <button class="nav-btn" onclick="toggleSpeakerNotes()" title="Ver notas y guion del orador (N)">[N] Notas</button>
    <button class="nav-btn" onclick="prevSlide()" title="Diapositiva anterior (&larr; / PageUp)">&larr; Prev</button>
    <button class="nav-btn" onclick="nextSlide()" title="Siguiente diapositiva (&rarr; / Espacio)">Next &rarr;</button>
  </div>
</footer>

<!-- DRAWER DE NOTAS DEL ORADOR (ACCESIBLE CON 'N') -->
<aside class="speaker-drawer" id="speakerDrawer">
  <div class="speaker-header">
    <div style="display:flex; align-items:center; gap:12px;">
      <span style="font-weight:700; font-size:12px;" class="mono">🎙️ NOTAS DEL ORADOR & GUION CONVERSACIONAL</span>
      <span id="speakerTimer" style="font-size:11.5px; color:#60A5FA;" class="mono">⏱️ 1.5 min</span>
    </div>
    <button class="nav-btn" style="padding:2px 8px;" onclick="toggleSpeakerNotes()">Cerrar [N]</button>
  </div>
  <div class="speaker-body" id="speakerNotesText">
    Notas cargando...
  </div>
</aside>

<!-- MODAL LIGHTBOX PARA AMPLIAR INFOGRAFÍAS NOTEBOOKLM -->
<div class="lightbox-modal" id="lightboxModal" onclick="closeLightbox()">
  <div class="lightbox-close" onclick="closeLightbox()">&times;</div>
  <img class="lightbox-img" id="lightboxImg" src="" alt="Infografía Ampliada" onclick="event.stopPropagation()">
</div>

<!-- INYECCIÓN DE DATOS REALES -->
<script>
  window.DECK_DATA = {data_json};
</script>

<!-- SCRIPTS DE NAVEGACIÓN Y VISUALES -->
<script>
  let currentSlide = 1;
  const totalSlides = 23;

  const notesBySlide = {notes_json};

  function updateSlide(index) {{
    if (index < 1) index = 1;
    if (index > totalSlides) index = totalSlides;

    document.querySelectorAll(".slide").forEach(s => s.classList.remove("active"));
    const target = document.querySelector(`.slide[data-index="${{index}}"]`);
    if (target) {{
      target.classList.add("active");
      currentSlide = index;
      document.getElementById("slideIndicator").textContent = `${{String(index).padStart(2, '0')}} / ${{totalSlides}}`;
      document.getElementById("actIndicator").textContent = target.getAttribute("data-act");
      document.getElementById("progressBar").style.width = `${{(index / totalSlides) * 100}}%`;
      
      document.getElementById("speakerTimer").textContent = `⏱️ ${{target.getAttribute("data-time")}}`;
      document.getElementById("speakerNotesText").innerHTML = notesBySlide[index] || "Notas en preparación.";

      try {{
        if (window.location.hash !== "#" + index) {{
          history.replaceState(null, "", "#" + index);
        }}
      }} catch (e) {{}}

      initSlideVisuals(index);
    }}
  }}

  function nextSlide() {{ updateSlide(currentSlide + 1); }}
  function prevSlide() {{ updateSlide(currentSlide - 1); }}

  function toggleSpeakerNotes() {{
    document.getElementById("speakerDrawer").classList.toggle("open");
  }}

  function toggleDarkMode() {{
    document.body.classList.toggle("dark-mode");
  }}

  function openLightbox(src) {{
    const modal = document.getElementById("lightboxModal");
    const img = document.getElementById("lightboxImg");
    if (modal && img) {{
      img.src = src;
      modal.classList.add("active");
    }}
  }}

  function closeLightbox() {{
    const modal = document.getElementById("lightboxModal");
    if (modal) {{
      modal.classList.remove("active");
    }}
  }}

  window.addEventListener("keydown", (e) => {{
    if (e.key === "Escape") {{
      closeLightbox();
      return;
    }}
    if (e.key === "ArrowRight" || e.key === " " || e.key === "PageDown") {{
      e.preventDefault();
      nextSlide();
    }} else if (e.key === "ArrowLeft" || e.key === "PageUp") {{
      e.preventDefault();
      prevSlide();
    }} else if (e.key === "Home") {{
      e.preventDefault();
      updateSlide(1);
    }} else if (e.key === "End") {{
      e.preventDefault();
      updateSlide(totalSlides);
    }} else if (e.key.toLowerCase() === "n") {{
      e.preventDefault();
      toggleSpeakerNotes();
    }} else if (e.key.toLowerCase() === "d") {{
      e.preventDefault();
      toggleDarkMode();
    }} else if (e.key.toLowerCase() === "f") {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen();
      }} else {{
        document.exitFullscreen();
      }}
    }}
  }});

  function updateAlpha(val) {{
    document.getElementById("alphaVal").textContent = parseFloat(val).toFixed(2);
    renderAlphaBars(parseFloat(val));
  }}

  function renderAlphaBars(alpha) {{
    const container = document.getElementById("alphaBars");
    if (!container) return;
    container.innerHTML = "";
    for (let k = 0; k < 5; k++) {{
      const weight = alpha * Math.pow(1 - alpha, k);
      const pct = (weight * 100).toFixed(1);
      const bar = document.createElement("div");
      bar.style.flex = "1";
      bar.style.height = `${{weight * 200}}px`;
      bar.style.background = k === 0 ? "#2563EB" : "#94A3B8";
      bar.style.borderRadius = "4px 4px 0 0";
      bar.style.display = "flex";
      bar.style.alignItems = "flex-start";
      bar.style.justifyContent = "center";
      bar.style.paddingTop = "4px";
      bar.style.color = "#FFF";
      bar.style.fontSize = "10px";
      bar.style.fontFamily = "IBM Plex Mono";
      bar.textContent = `${{pct}}%`;
      container.appendChild(bar);
    }}
  }}

  // Procedural Ontological Signal Simulator (Slide 02)
  const signalLayers = {{ T: true, S: true, C: true, E: true }};
  let waveAnimId = null;
  let wavePhase = 0;

  function toggleSignalLayer(layer) {{
    signalLayers[layer] = !signalLayers[layer];
    const btn = document.getElementById("btnToggle" + layer);
    if (btn) {{
      if (signalLayers[layer]) {{
        btn.classList.add("active");
        btn.textContent = btn.textContent.replace("✗", "✓");
      }} else {{
        btn.classList.remove("active");
        btn.textContent = btn.textContent.replace("✓", "✗");
      }}
    }}
    const count = Object.values(signalLayers).filter(Boolean).length;
    const status = document.getElementById("simLayerStatus");
    if (status) {{
      status.textContent = `${{count}} / 4 Capas Físicas`;
    }}
  }}

  function startOntologicalWaveSimulation() {{
    const canvas = document.getElementById("ontologicalWaveCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");

    function resize() {{
      const rect = canvas.getBoundingClientRect();
      if (rect.width > 0 && rect.height > 0) {{
        canvas.width = rect.width * (window.devicePixelRatio || 1);
        canvas.height = rect.height * (window.devicePixelRatio || 1);
      }}
    }}
    resize();

    function draw() {{
      if (currentSlide !== 2) {{
        if (waveAnimId) cancelAnimationFrame(waveAnimId);
        return;
      }}
      wavePhase += 0.025;
      const w = canvas.width;
      const h = canvas.height;
      if (w === 0 || h === 0) {{
        resize();
      }}
      ctx.clearRect(0, 0, w, h);

      const isDark = document.body.classList.contains("dark-mode");
      const gridColor = isDark ? "rgba(255,255,255,0.05)" : "rgba(0,0,0,0.05)";
      const axisColor = isDark ? "rgba(255,255,255,0.2)" : "rgba(0,0,0,0.15)";
      
      // Grid lines
      ctx.strokeStyle = gridColor;
      ctx.lineWidth = 1;
      for (let x = 0; x < w; x += 40) {{
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, h);
        ctx.stroke();
      }}
      for (let y = 0; y < h; y += 28) {{
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(w, y);
        ctx.stroke();
      }}

      // Zero axis
      const midY = h * 0.52;
      ctx.strokeStyle = axisColor;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(0, midY);
      ctx.lineTo(w, midY);
      ctx.stroke();
      ctx.setLineDash([]);

      const numPts = 260;
      const points = [];
      for (let i = 0; i < numPts; i++) {{
        const t = (i / numPts) * 10;
        let val = 0;
        if (signalLayers.T) val += (t - 5) * 3.8;
        if (signalLayers.S) val += Math.sin(t * 3.6 + wavePhase) * 22;
        if (signalLayers.C) val += Math.sin(t * 0.85 + wavePhase * 0.35) * 14;
        if (signalLayers.E) {{
          const pseudoNoise = Math.sin(i * 123.4 + Math.floor(wavePhase * 3)) * Math.cos(i * 56.7);
          val += pseudoNoise * 6.5;
          if (i === 160) val -= 32; // Friaje spike
          if (i === 65) val += 24;  // Heat wave spike
        }}
        const px = (i / (numPts - 1)) * w;
        const py = midY - val * (h / 120);
        points.push({{ x: px, y: py }});
      }}

      // Gradient fill
      const grad = ctx.createLinearGradient(0, 0, 0, h);
      grad.addColorStop(0, "rgba(37, 99, 235, 0.22)");
      grad.addColorStop(1, "rgba(37, 99, 235, 0.0)");
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.moveTo(points[0].x, points[0].y);
      for (let i = 1; i < points.length; i++) {{
        ctx.lineTo(points[i].x, points[i].y);
      }}
      ctx.lineTo(w, h);
      ctx.lineTo(0, h);
      ctx.closePath();
      ctx.fill();

      // Signal line
      ctx.strokeStyle = isDark ? "#60A5FA" : "#2563EB";
      ctx.lineWidth = 2.4;
      ctx.beginPath();
      ctx.moveTo(points[0].x, points[0].y);
      for (let i = 1; i < points.length; i++) {{
        ctx.lineTo(points[i].x, points[i].y);
      }}
      ctx.stroke();

      // Highlight Friaje extreme spike if noise enabled
      if (signalLayers.E && points[160]) {{
        const fp = points[160];
        ctx.fillStyle = "#DC2626";
        ctx.beginPath();
        ctx.arc(fp.x, fp.y, 4.5, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = isDark ? "#FCA5A5" : "#DC2626";
        ctx.font = "9.5px 'IBM Plex Mono'";
        ctx.fillText("Anomalía Friaje > 2.5σ (-19.2°C)", fp.x - 70, fp.y + 16);
      }}

      waveAnimId = requestAnimationFrame(draw);
    }}

    if (waveAnimId) cancelAnimationFrame(waveAnimId);
    draw();
  }}

  let charts = {{}};

  function initSlideVisuals(idx) {{
    try {{
      if (idx === 2) {{
        startOntologicalWaveSimulation();
      }}

      if (idx === 4) {{
        renderAlphaBars(0.35);
      }}

      // Slide 10: Experimento Extrapolación
      if (idx === 10 && !charts["extrap"]) {{
        const canvas = document.getElementById("chartExtrap") || document.getElementById("chartExtrapolacion");
        if (canvas) {{
          const ctx = canvas.getContext("2d");
          const d = window.DECK_DATA.extrapolacion;
          charts["extrap"] = new Chart(ctx, {{
            type: "line",
            data: {{
              labels: d.map(r => r.fecha.slice(5)),
              datasets: [
                {{
                  label: "Temperatura Real Observada (°C)",
                  data: d.map(r => r.tmax_real),
                  borderColor: "#FFFFFF",
                  borderWidth: 2.8,
                  pointRadius: 3
                }},
                {{
                  label: "Random Forest Directo (Meseta 31.5°C)",
                  data: d.map(r => r.pred_arbol_niveles),
                  borderColor: "#DC2626",
                  borderWidth: 2.5,
                  borderDash: [5, 4],
                  pointRadius: 2.5
                }},
                {{
                  label: "Modelo sobre Diferencias Δy (Sube a 35.45°C)",
                  data: d.map(r => r.pred_arbol_diferencias),
                  borderColor: "#059669",
                  borderWidth: 2.5,
                  pointRadius: 2.5
                }},
                {{
                  label: "Tope Entrenamiento (34.0°C)",
                  data: d.map(r => r.tope_entrenamiento),
                  borderColor: "#94A3B8",
                  borderWidth: 1.5,
                  borderDash: [3, 3],
                  pointRadius: 0
                }}
              ]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{
                legend: {{ position: "top", labels: {{ font: {{ family: "IBM Plex Mono", size: 10.5 }} }} }}
              }},
              scales: {{
                y: {{ min: 28, max: 39, title: {{ display: true, text: "Tmax (°C)" }} }}
              }}
            }}
          }});
        }}
      }}

      // Slide 10: Discrepancia NOAA vs ECMWF
      if (idx === 10 && !charts["noaaEcmwf"]) {{
        const canvas = document.getElementById("chartNoaaEcmwf");
        if (canvas) {{
          const ctx = canvas.getContext("2d");
          const d = window.DECK_DATA.noaa_ecmwf;
          charts["noaaEcmwf"] = new Chart(ctx, {{
            type: "bar",
            data: {{
              labels: d.map(r => r.fecha.slice(5)),
              datasets: [
                {{
                  label: "NOAA GFS Tmax (°C)",
                  data: d.map(r => r.tmax_noaa_gfs),
                  backgroundColor: "rgba(37, 99, 235, 0.75)"
                }},
                {{
                  label: "ECMWF IFS Tmax (°C)",
                  data: d.map(r => r.tmax_ecmwf),
                  backgroundColor: "rgba(217, 119, 6, 0.75)"
                }}
              ]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{
                legend: {{ position: "top", labels: {{ font: {{ family: "IBM Plex Mono", size: 11 }} }} }}
              }},
              scales: {{
                y: {{ min: 24, max: 38, title: {{ display: true, text: "Tmax (°C)" }} }}
              }}
            }}
          }});
        }}
      }}

      // Slide 12: Serie histórica reciente SENAMHI
      if (idx === 12 && !charts["senamhiReciente"]) {{
        const canvas = document.getElementById("chartSenamhiReciente");
        if (canvas) {{
          const ctx = canvas.getContext("2d");
          const d = window.DECK_DATA.senamhi_reciente;
          charts["senamhiReciente"] = new Chart(ctx, {{
            type: "line",
            data: {{
              labels: d.map(r => r.fecha.slice(5)),
              datasets: [
                {{
                  label: "Tmax Punchana (°C)",
                  data: d.map(r => r.tmax),
                  borderColor: "#2563EB",
                  borderWidth: 2,
                  pointRadius: 0
                }},
                {{
                  label: "Tmin Punchana (°C)",
                  data: d.map(r => r.tmin),
                  borderColor: "#0891B2",
                  borderDash: [2, 2],
                  borderWidth: 1.5,
                  pointRadius: 0
                }}
              ]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{
                legend: {{ position: "top", labels: {{ font: {{ family: "IBM Plex Mono", size: 10.5 }} }} }}
              }},
              scales: {{
                y: {{ min: 18, max: 38, title: {{ display: true, text: "Temperatura (°C)" }} }}
              }}
            }}
          }});
        }}
      }}

      // Slide 11: Benchmark Punchana
      if (idx === 11 && !charts["benchmark"]) {{
        const canvas = document.getElementById("chartBenchmark");
        if (canvas) {{
          const ctx = canvas.getContext("2d");
          const d = window.DECK_DATA.benchmark;
          charts["benchmark"] = new Chart(ctx, {{
            type: "bar",
            data: {{
              labels: d.map(r => r.modelo),
              datasets: [{{
                label: "RMSE (°C) en Holdout de 90 Días",
                data: d.map(r => r.rmse_1d),
                backgroundColor: d.map(r => {{
                  if (r.modelo.includes("ExtraTrees")) return "#059669";
                  if (r.p_valor_vs_mejor > 0.05) return "#2563EB";
                  return "#DC2626";
                }})
              }}]
            }},
            options: {{
              indexAxis: "y",
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{
                legend: {{ display: false }}
              }},
              scales: {{
                x: {{ min: 1.6, max: 3.0, title: {{ display: true, text: "RMSE (°C) en Holdout de 90 Días — Menor es mejor" }} }}
              }}
            }}
          }});
        }}
      }}

      // Slide 12: Demo Pronóstico 7 Días con Bandas
      if (idx === 12 && !charts["demo7d"]) {{
        const canvas = document.getElementById("chartDemo7d");
        if (canvas) {{
          const ctx = canvas.getContext("2d");
          const d = window.DECK_DATA.forecast_7d;
          charts["demo7d"] = new Chart(ctx, {{
            type: "line",
            data: {{
              labels: d.map(r => r.fecha.slice(5)),
              datasets: [
                {{
                  label: "Observado SENAMHI",
                  data: d.map(r => r.tmax_observada),
                  borderColor: "#FFFFFF",
                  borderWidth: 3,
                  pointRadius: 4,
                  fill: false
                }},
                {{
                  label: "ExtraTrees (Ganador)",
                  data: d.map(r => r.pred_extratrees),
                  borderColor: "#059669",
                  borderWidth: 2.5,
                  pointRadius: 3,
                  fill: false
                }},
                {{
                  label: "P90 Incertidumbre",
                  data: d.map(r => r.ci_upper_p90),
                  borderColor: "rgba(5, 150, 105, 0.4)",
                  borderDash: [3, 3],
                  borderWidth: 1.5,
                  pointRadius: 0,
                  fill: false
                }},
                {{
                  label: "P10 Incertidumbre",
                  data: d.map(r => r.ci_lower_p10),
                  borderColor: "rgba(5, 150, 105, 0.4)",
                  borderDash: [3, 3],
                  borderWidth: 1.5,
                  pointRadius: 0,
                  fill: "-1",
                  backgroundColor: "rgba(5, 150, 105, 0.1)"
                }},
                {{
                  label: "TimesFM 200M Zero-Shot",
                  data: d.map(r => r.pred_timesfm),
                  borderColor: "#7C3AED",
                  borderWidth: 2,
                  pointRadius: 2.5,
                  hidden: false
                }},
                {{
                  label: "Chronos T5 Zero-Shot",
                  data: d.map(r => r.pred_chronos),
                  borderColor: "#D97706",
                  borderWidth: 2,
                  borderDash: [4, 4],
                  pointRadius: 2.5,
                  hidden: true
                }},
                {{
                  label: "ARIMA (2,0,1)",
                  data: d.map(r => r.pred_arima),
                  borderColor: "#0284C7",
                  borderWidth: 1.8,
                  borderDash: [2, 2],
                  pointRadius: 2,
                  hidden: true
                }}
              ]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{
                legend: {{ position: "top", labels: {{ font: {{ family: "IBM Plex Mono", size: 10.5 }} }} }}
              }},
              scales: {{
                y: {{ min: 28, max: 37, title: {{ display: true, text: "Tmax (°C)" }} }}
              }}
            }}
          }});
        }}
      }}

      // Slide 15: Jaén Histórico
      if (idx === 15 && !charts["jaenHist"]) {{
        const canvas = document.getElementById("chartJaenHistorico");
        if (canvas) {{
          const ctx = canvas.getContext("2d");
          const d = window.DECK_DATA.cafe_campanias;
          const valid = d.filter(r => r.rendimiento_qq_ha !== null);
          charts["jaenHist"] = new Chart(ctx, {{
            type: "line",
            data: {{
              labels: valid.map(r => r.campania),
              datasets: [{{
                label: "Rendimiento Oficial SIEA (qq/ha)",
                data: valid.map(r => r.rendimiento_qq_ha),
                borderColor: "#059669",
                backgroundColor: "rgba(5, 150, 105, 0.08)",
                fill: true,
                borderWidth: 2.5,
                pointRadius: 5,
                pointBackgroundColor: valid.map(r => (r.campania === 2013 || r.campania === 2014) ? "#DC2626" : "#059669")
              }}]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{
                legend: {{ display: false }},
                tooltip: {{
                  callbacks: {{
                    afterLabel: (ctx) => ctx.label === "2014" ? "⚠️ CRISIS DE LA ROYA AMARILLA (-56%)" : ""
                  }}
                }}
              }},
              scales: {{
                y: {{ min: 8, max: 38, title: {{ display: true, text: "Rendimiento (qq/ha)" }} }}
              }}
            }}
          }});
        }}
      }}

      // Slide 19: Scatter NDVI vs Rendimiento
      if ((idx === 19 || idx === 16) && !charts["scatterNdvi"]) {{
        const canvas = document.getElementById("chartScatterNdvi");
        if (canvas) {{
          const ctx = canvas.getContext("2d");
          const d = window.DECK_DATA.cafe_campanias;
          const valid = d.filter(r => r.rendimiento_qq_ha !== null);
          charts["scatterNdvi"] = new Chart(ctx, {{
            type: "scatter",
            data: {{
              datasets: [
                {{
                  label: "Campañas Auditadas (2010-2024)",
                  data: valid.map(r => ({{ x: r.ndvi_anual, y: r.rendimiento_qq_ha, anio: r.campania }})),
                  backgroundColor: valid.map(r => r.campania === 2014 ? "#DC2626" : "#2563EB"),
                  pointRadius: valid.map(r => r.campania === 2014 ? 8 : 5)
                }},
                {{
                  type: "line",
                  label: "Tendencia Lineal (r = 0.154, p = 0.600 — Pendiente Nula)",
                  data: [{{ x: 0.69, y: 19.8 }}, {{ x: 0.78, y: 21.6 }}],
                  borderColor: "#94A3B8",
                  borderDash: [4, 4],
                  borderWidth: 1.8,
                  pointRadius: 0,
                  fill: false
                }}
              ]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{
                legend: {{ position: "top", labels: {{ font: {{ family: "IBM Plex Mono", size: 10 }} }} }},
                tooltip: {{
                  callbacks: {{
                    label: (ctx) => ctx.raw.anio ? `Campaña ${{ctx.raw.anio}}: NDVI ${{ctx.raw.x.toFixed(3)}}, Rend: ${{ctx.raw.y}} qq/ha` : "Línea de regresión plana"
                  }}
                }}
              }},
              scales: {{
                x: {{ min: 0.68, max: 0.79, title: {{ display: true, text: "NDVI MODIS Anual (r = 0.154, p = 0.600)" }} }} ,
                y: {{ min: 8, max: 38, title: {{ display: true, text: "Rendimiento (qq/ha)" }} }}
              }}
            }}
          }});
        }}
      }}

      // Slide 20: Demo 2 Validación expansiva Jaén
      if ((idx === 20 || idx === 18) && !charts["demoJaen"]) {{
        const canvas = document.getElementById("chartDemoJaen");
        if (canvas) {{
          const ctx = canvas.getContext("2d");
          const d = window.DECK_DATA.cafe_resultados;
          charts["demoJaen"] = new Chart(ctx, {{
            type: "line",
            data: {{
              labels: d.map(r => r.campania),
              datasets: [
                {{
                  label: "Rendimiento Real Observado (qq/ha)",
                  data: d.map(r => r.rendimiento_obs),
                  borderColor: "#FFFFFF",
                  borderWidth: 3,
                  pointRadius: 4
                }},
                {{
                  label: "Fusión Clima + Tendencia (MAE 4.51)",
                  data: d.map(r => r.pred_m4_fusion),
                  borderColor: "#059669",
                  borderWidth: 2.5,
                  pointRadius: 3
                }},
                {{
                  label: "Solo Satélite NDVI (MAE 5.32 — Empeora)",
                  data: d.map(r => r.pred_m2_satelite),
                  borderColor: "#DC2626",
                  borderWidth: 2,
                  borderDash: [5, 4],
                  pointRadius: 2.5
                }},
                {{
                  label: "Solo Clima Floración (MAE 4.60)",
                  data: d.map(r => r.pred_m3_clima),
                  borderColor: "#2563EB",
                  borderWidth: 1.8,
                  borderDash: [3, 3],
                  pointRadius: 2
                }},
                {{
                  label: "Tendencia Pura (MAE 4.79)",
                  data: d.map(r => r.pred_m1_tendencia),
                  borderColor: "#94A3B8",
                  borderDash: [2, 2],
                  borderWidth: 1.5,
                  pointRadius: 0
                }}
              ]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{
                legend: {{ position: "top", labels: {{ font: {{ family: "IBM Plex Mono", size: 10.5 }} }} }}
              }},
              scales: {{
                y: {{ min: 14, max: 28, title: {{ display: true, text: "Rendimiento (qq/ha)" }} }}
              }}
            }}
          }});
        }}
      }}
    }} catch (err) {{
      console.warn("Visual initialization notice on slide", idx, err);
    }}
  }}

  function toggleDataset(dsIndex) {{
    if (!charts["demo7d"]) return;
    const isHidden = charts["demo7d"].isDatasetVisible(dsIndex);
    charts["demo7d"].setDatasetVisibility(dsIndex, !isHidden);
    charts["demo7d"].update();
  }}

  function getSlideFromHash() {{
    const hash = window.location.hash.replace("#", "");
    const num = parseInt(hash, 10);
    return (!isNaN(num) && num >= 1 && num <= totalSlides) ? num : 1;
  }}

  window.addEventListener("DOMContentLoaded", () => {{
    updateSlide(getSlideFromHash());
  }});

  window.addEventListener("hashchange", () => {{
    const s = getSlideFromHash();
    if (s !== currentSlide) {{
      updateSlide(s);
    }}
  }});
</script>
</body>
</html>
"""

    output_path = str(BASE_DIR / "presentacion.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Deck interactivo de 23 diapositivas generado con éxito en: {output_path} ({len(html_content)} bytes)")

if __name__ == "__main__":
    build_deck()
