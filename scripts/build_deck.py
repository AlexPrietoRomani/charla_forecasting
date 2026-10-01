"""
Generador del deck interactivo exhaustivo presentacion.html (25 diapositivas)
Diseño Full-Bleed (de borde a borde), animaciones interactivas desde cero (curvas, lags, celdas LSTM, parches, espectro),
comparativa multi-agencia (NOAA GFS vs ECMWF vs ICON vs GraphCast), y mapas satelitales Leaflet con heatmaps interactivos.
"""

from pathlib import Path
import pandas as pd

def build_mega_deck():
    senamhi_7d_csv = Path("data/senamhi_forecast_7d.csv").read_text(encoding="utf-8").strip()
    cafe_csv = Path("data/cafe_ndvi_rendimiento.csv").read_text(encoding="utf-8").strip()
    df_senamhi = pd.read_csv("data/senamhi_diario.csv")
    senamhi_diario_sub = df_senamhi.tail(180).to_csv(index=False).strip()
    noaa_ecmwf_csv = Path("data/noaa_ecmwf_forecast.csv").read_text(encoding="utf-8").strip()

    html = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>¿Puede la IA predecir el futuro? Lecciones de forecasting desde el mundo real</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
  :root {
    --bg-light: #FFFFFF;
    --bg-light-panel: #F8F9FA;
    --bg-light-card: #FFFFFF;
    --text-light-main: #0F172A;
    --text-light-mute: #475569;
    --text-light-faint: #94A3B8;
    --line-light: #0F172A;
    --line-light-faint: #E2E8F0;

    --bg-dark: #07090E;
    --bg-dark-panel: #0D111A;
    --bg-dark-card: #131926;
    --text-dark-main: #F8FAFC;
    --text-dark-mute: #94A3B8;
    --text-dark-faint: #475569;
    --line-dark: #334155;
    --line-dark-faint: #1E293B;

    --accent-blue: #2563EB;
    --accent-amber: #D97706;
    --accent-red: #DC2626;
    --accent-green: #059669;
    --accent-purple: #7C3AED;
    --accent-cyan: #0891B2;

    --pad-h: clamp(24px, 3.5vw, 60px);
    --pad-v: clamp(20px, 3vw, 48px);
  }

  * { box-sizing: border-box; margin: 0; padding: 0; border-radius: 0 !important; }
  html, body { height: 100%; width: 100%; }

  body {
    background: var(--bg-light);
    color: var(--text-light-main);
    font-family: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, sans-serif;
    overflow: hidden;
    -webkit-font-smoothing: antialiased;
    transition: background 0.3s ease, color 0.3s ease;
  }

  /* Architectural Grid */
  body::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    background-size: 32px 32px;
    background-image: 
      linear-gradient(to right, rgba(0,0,0,0.035) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(0,0,0,0.035) 1px, transparent 1px);
  }

  body.dark-active {
    background: var(--bg-dark);
    color: var(--text-dark-main);
  }
  body.dark-active::before {
    background-image: 
      linear-gradient(to right, rgba(255,255,255,0.035) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255,255,255,0.035) 1px, transparent 1px);
  }

  .mono { font-family: "IBM Plex Mono", monospace; font-variant-numeric: tabular-nums; }
  .display { font-family: "Space Grotesk", sans-serif; font-weight: 700; }

  /* Full-bleed Deck layout */
  .deck {
    position: fixed;
    inset: 0;
    left: 56px;
    z-index: 1;
    height: 100vh;
    width: calc(100vw - 56px);
  }
  
  .slide {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    padding: var(--pad-v) var(--pad-h);
    opacity: 0;
    visibility: hidden;
    transform: translateY(6px);
    transition: opacity .3s ease, transform .3s ease, visibility .3s;
    overflow-y: auto;
    width: 100%;
    height: 100%;
  }
  .slide.active { opacity: 1; visibility: visible; transform: none; }

  /* Sidebar */
  .sidebar {
    position: fixed;
    top: 0; bottom: 0; left: 0;
    width: 56px;
    background: var(--bg-light-panel);
    border-right: 1px solid var(--line-light-faint);
    z-index: 100;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 16px 8px;
  }
  body.dark-active .sidebar {
    background: var(--bg-dark-panel);
    border-right-color: var(--line-dark-faint);
  }
  .sidebar-top, .sidebar-bottom { display: flex; flex-direction: column; align-items: center; gap: 12px; }
  .theme-btn, .nav-icon-btn {
    background: transparent;
    border: 1px solid var(--line-light-faint);
    color: inherit;
    width: 38px; height: 38px;
    display: flex; align-items: center; justify-content: center;
    cursor: pointer;
    font-size: 13px;
    transition: background 0.2s, border-color 0.2s;
  }
  body.dark-active .theme-btn, body.dark-active .nav-icon-btn {
    border-color: var(--line-dark-faint);
  }
  .theme-btn:hover, .nav-icon-btn:hover {
    background: rgba(0,0,0,0.06);
    border-color: var(--line-light);
  }
  body.dark-active .theme-btn:hover, body.dark-active .nav-icon-btn:hover {
    background: rgba(255,255,255,0.08);
    border-color: var(--line-dark);
  }

  /* Typography */
  .tag {
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--accent-blue);
    margin-bottom: 0.35rem;
    display: inline-block;
  }
  h1 { font-size: clamp(2rem, 3.8vw, 3.4rem); line-height: 1.08; letter-spacing: -0.02em; margin-bottom: 0.8rem; }
  h2 { font-size: clamp(1.35rem, 2.5vw, 2.1rem); line-height: 1.15; letter-spacing: -0.01em; margin-bottom: 0.6rem; }
  h3 { font-size: 1.1rem; font-weight: 600; margin-bottom: 0.35rem; }
  .lead { font-size: clamp(0.92rem, 1.4vw, 1.15rem); line-height: 1.45; color: var(--text-light-mute); max-width: 1200px; margin-bottom: 1rem; }
  body.dark-active .lead { color: var(--text-dark-mute); }

  /* Edge-to-Edge Grid Containers */
  .split-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    width: 100%;
    flex: 1;
    min-height: 0;
  }
  .split-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    width: 100%;
    margin-top: 0.6rem;
  }
  .split-4 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    width: 100%;
    margin-top: 0.6rem;
  }

  .card {
    background: var(--bg-light-panel);
    border: 1px solid var(--line-light-faint);
    padding: 16px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    transition: border-color 0.2s, transform 0.15s;
  }
  body.dark-active .card {
    background: var(--bg-dark-panel);
    border-color: var(--line-dark-faint);
  }
  .card:hover { border-color: var(--accent-blue); }

  .stat-val { font-family: "Space Grotesk", sans-serif; font-size: 1.9rem; font-weight: 700; margin-bottom: 3px; }
  .stat-label { font-size: 0.78rem; color: var(--text-light-mute); text-transform: uppercase; letter-spacing: 0.06em; }
  body.dark-active .stat-label { color: var(--text-dark-mute); }

  /* Interactive Elements */
  .chart-box {
    position: relative;
    width: 100%;
    height: 380px;
    background: var(--bg-light-panel);
    border: 1px solid var(--line-light-faint);
    padding: 12px;
  }
  body.dark-active .chart-box {
    background: var(--bg-dark-panel);
    border-color: var(--line-dark-faint);
  }

  .map-box {
    width: 100%;
    height: 100%;
    min-height: 380px;
    border: 1px solid var(--line-light-faint);
    position: relative;
    background: #090D14;
  }

  /* Table styling */
  table.data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.82rem;
  }
  table.data-table th, table.data-table td {
    padding: 8px 10px;
    border: 1px solid var(--line-light-faint);
    text-align: left;
  }
  body.dark-active table.data-table th, body.dark-active table.data-table td {
    border-color: var(--line-dark-faint);
  }
  table.data-table th {
    background: var(--bg-light-panel);
    font-weight: 600;
  }
  body.dark-active table.data-table th {
    background: var(--bg-dark-panel);
  }

  /* Footer Controls */
  .slide-footer {
    position: fixed;
    bottom: 16px; right: 24px;
    display: flex; align-items: center; gap: 10px;
    z-index: 100;
  }
  .slide-counter { font-family: "IBM Plex Mono", monospace; font-size: 0.85rem; font-weight: 600; }
  .nav-btn {
    padding: 6px 14px;
    background: var(--text-light-main);
    color: var(--bg-light);
    border: 1px solid var(--text-light-main);
    cursor: pointer;
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.8rem;
    font-weight: 600;
    transition: opacity 0.2s;
  }
  body.dark-active .nav-btn {
    background: var(--text-dark-main);
    color: var(--bg-dark);
    border-color: var(--text-dark-main);
  }
  .nav-btn:hover { opacity: 0.85; }

  /* Badges */
  .badge {
    display: inline-block;
    padding: 2px 6px;
    font-size: 0.7rem;
    font-family: "IBM Plex Mono", monospace;
    font-weight: 600;
    margin-right: 5px;
  }
  .badge-blue { background: rgba(37, 99, 235, 0.15); color: var(--accent-blue); }
  .badge-green { background: rgba(5, 150, 105, 0.15); color: var(--accent-green); }
  .badge-amber { background: rgba(217, 119, 6, 0.15); color: var(--accent-amber); }
  .badge-red { background: rgba(220, 38, 38, 0.15); color: var(--accent-red); }
  .badge-purple { background: rgba(124, 58, 237, 0.15); color: var(--accent-purple); }
  .badge-cyan { background: rgba(8, 145, 178, 0.15); color: var(--accent-cyan); }

  /* Interactive Diagrams / SVG Boxes */
  .diagram-box {
    background: var(--bg-light-panel);
    border: 1px solid var(--line-light-faint);
    padding: 14px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  body.dark-active .diagram-box {
    background: var(--bg-dark-panel);
    border-color: var(--line-dark-faint);
  }

  @keyframes dashAnimation {
    to { stroke-dashoffset: -30; }
  }
  .anim-dash {
    stroke-dasharray: 5, 5;
    animation: dashAnimation 1.2s linear infinite;
  }

  .pill-group {
    display: flex;
    gap: 8px;
    margin-bottom: 8px;
  }
  .pill-btn {
    padding: 4px 10px;
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.72rem;
    font-weight: 600;
    border: 1px solid var(--line-light-faint);
    background: transparent;
    color: inherit;
    cursor: pointer;
    transition: all 0.2s;
  }
  body.dark-active .pill-btn { border-color: var(--line-dark-faint); }
  .pill-btn.active {
    background: var(--accent-blue);
    color: #FFF;
    border-color: var(--accent-blue);
  }
</style>
</head>
<body>

<!-- SIDEBAR -->
<div class="sidebar">
  <div class="sidebar-top">
    <button class="nav-icon-btn mono" id="tocBtn" title="Portada (Home)">01</button>
  </div>
  <div class="sidebar-bottom">
    <button class="theme-btn" id="themeToggle" title="Cambiar Tema">🌓</button>
    <button class="theme-btn mono" id="fsBtn" title="Pantalla Completa (F)">⛶</button>
  </div>
</div>

<!-- FOOTER -->
<div class="slide-footer">
  <span class="slide-counter mono" id="slideNum">01 / 25</span>
  <button class="nav-btn" id="prevBtn">← PREV</button>
  <button class="nav-btn" id="nextBtn">NEXT →</button>
</div>

<!-- DECK CONTAINER -->
<div class="deck">

  <!-- SLIDE 1: PORTADA -->
  <section class="slide active" data-title="Portada">
    <span class="tag">Charla Magistral · Forecasting, Teledetección & Modelos Globales</span>
    <h1 class="display">¿Puede la IA predecir el futuro?</h1>
    <p class="lead">Lecciones de forecasting, física espectral, supercomputadoras de agencias globales y cuantificación de incertidumbre.</p>
    <div class="split-3" style="margin-top: 1.5rem;">
      <div class="card">
        <span class="badge badge-blue">Caso A</span>
        <div class="stat-label" style="margin-top: 6px;">Meteorología Tropical</div>
        <div style="font-weight: 600; font-size: 1.1rem; margin-top: 2px;">SENAMHI Punchana (Iquitos)</div>
        <div style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">7 años diarios (2019–2025). Benchmark de 5 niveles vs NOAA GFS y ECMWF.</div>
      </div>
      <div class="card">
        <span class="badge badge-green">Caso B</span>
        <div class="stat-label" style="margin-top: 6px;">Biofísica de Cosechas</div>
        <div style="font-weight: 600; font-size: 1.1rem; margin-top: 2px;">Café Jaén & Sentinel-2</div>
        <div style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">Fusión multimodal (EVI + Clima fenológico) vs la saturación del NDVI.</div>
      </div>
      <div class="card">
        <span class="badge badge-purple">Tesis</span>
        <div class="stat-label" style="margin-top: 6px;">Toma de Decisiones</div>
        <div style="font-weight: 600; font-size: 1.1rem; margin-top: 2px;">Incertidumbre Cuantificada</div>
        <div style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">La IA no adivina certezas absolutas; estima distribuciones de probabilidad para mitigar pérdidas.</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: ANATOMIA DESDE CERO -->
  <section class="slide" data-title="Anatomía de una Serie">
    <span class="tag">Fundamento Matemático · Desde Cero</span>
    <h2>La Anatomía de una Serie Temporal</h2>
    <p class="lead">Toda serie temporal $Y(t)$ es el resultado de cuatro componentes fundamentales superpuestos. Antes de aplicar cualquier modelo, debemos entender la física de su señal.</p>
    <div class="split-2">
      <div class="diagram-box">
        <h3 style="color: var(--accent-blue); font-size: 0.95rem;">Las Curvas Elementales de Tendencia</h3>
        <svg viewBox="0 0 500 200" style="width: 100%; height: auto; margin-top: 6px;">
          <!-- Grid lines -->
          <line x1="30" y1="170" x2="480" y2="170" stroke="var(--line-light-faint)" stroke-width="1"/>
          <line x1="30" y1="170" x2="30" y2="20" stroke="var(--line-light-faint)" stroke-width="1"/>
          
          <!-- Lineal: y = mx -->
          <line x1="30" y1="160" x2="460" y2="90" stroke="var(--text-light-faint)" stroke-width="2"/>
          <text x="400" y="85" font-size="10" font-family="IBM Plex Mono" fill="currentColor">Lineal</text>
          
          <!-- Exponencial: y = e^kt -->
          <path d="M 30 168 Q 280 160 460 30" fill="none" stroke="var(--accent-red)" stroke-width="2.5" class="anim-dash"/>
          <text x="410" y="25" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-red)">Exponencial (e^kt)</text>

          <!-- Logarítmica: y = ln(t) -->
          <path d="M 30 168 Q 60 50 460 45" fill="none" stroke="var(--accent-cyan)" stroke-width="2"/>
          <text x="320" y="40" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-cyan)">Logarítmica (ln t)</text>

          <!-- Sigmoide / Logística: y = L / (1 + e^-k(t-t0)) -->
          <path d="M 30 165 C 180 165 220 70 460 70" fill="none" stroke="var(--accent-green)" stroke-width="2.5"/>
          <text x="280" y="65" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-green)">Logística / S-Curve (Saturación)</text>
        </svg>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); margin-top: 4px;">
          En biología y agricultura, las plantas siguen curvas <b>logísticas</b>: crecen exponencialmente al inicio y se saturan al alcanzar la masa crítica foliar.
        </p>
      </div>

      <div class="card">
        <h3>Ecuación General de Descomposición</h3>
        <div style="background: rgba(37, 99, 235, 0.08); padding: 10px 14px; font-family: 'IBM Plex Mono'; font-size: 0.88rem; margin: 8px 0;">
          Y(t) = T(t) + S(t) + C(t) + \epsilon(t)
        </div>
        <ul style="font-size: 0.82rem; line-height: 1.55; color: var(--text-light-mute); margin-left: 1.1rem;">
          <li><b>Tendencia T(t):</b> Dirección a largo plazo (calentamiento global, envejecimiento de plantación).</li>
          <li><b>Estacionalidad S(t):</b> Ciclo periódico fijo conocido (día/noche 24h, verano/invierno 365 días).</li>
          <li><b>Ciclo C(t):</b> Fluctuaciones no periódicas de mediano plazo (El Niño / La Niña 3-7 años).</li>
          <li><b>Ruido \epsilon(t):</b> Choques estocásticos impredecibles (turbulencia convectiva local).</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: EL GRAN MAPA 4 PARADIGMAS -->
  <section class="slide" data-title="Los 4 Paradigmas">
    <span class="tag">Taxonomía Integral</span>
    <h2>El Mapa de los 4 Paradigmas de Forecasting</h2>
    <p class="lead">Para no perderse en la selva de algoritmos, organizamos el campo en cuatro paradigmas complementarios:</p>
    <div class="split-4">
      <div class="card">
        <span class="badge badge-amber">Paradigma 1</span>
        <h3 style="margin-top: 6px;">Clásicos & Paramétricos</h3>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); line-height: 1.45;">
          ARIMA, Holt-Winters, Prophet.<br>
          <b>Objetivo:</b> 1 sola serie, explicabilidad matemática pura, horizontes cortos.
        </p>
      </div>
      <div class="card">
        <span class="badge badge-blue">Paradigma 2</span>
        <h3 style="margin-top: 6px;">ML & Deep Learning</h3>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); line-height: 1.45;">
          Random Forest, XGBoost, LSTM, PatchTST.<br>
          <b>Objetivo:</b> Tablas con lags, no linealidades y paneles masivos multi-serie.
        </p>
      </div>
      <div class="card">
        <span class="badge badge-green">Paradigma 3</span>
        <h3 style="margin-top: 6px;">Series Biofísicas (Agro)</h3>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); line-height: 1.45;">
          Sentinel-2, EVI, NDRE, YOLOv12.<br>
          <b>Objetivo:</b> Predecir rendimientos en función de fenología y espacio (x,y,t).
        </p>
      </div>
      <div class="card">
        <span class="badge badge-purple">Paradigma 4</span>
        <h3 style="margin-top: 6px;">Modelos Globales & Zero-Shot</h3>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); line-height: 1.45;">
          NOAA GFS, ECMWF, GraphCast, TimesFM.<br>
          <b>Objetivo:</b> Simulación planetaria y pronóstico cold-start sin entrenar.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: PARADIGMA 1 - CURVAS Y SUAVIZADO -->
  <section class="slide" data-title="P1: Curvas y Suavizado">
    <span class="tag">Paradigma 1 · Modelos Clásicos</span>
    <h2>Curvas Paramétricas y Suavizado Exponencial (ETS)</h2>
    <p class="lead">Cuando no tenemos millones de datos, los modelos estadísticos asumen una estructura funcional explícita sobre la inercia del sistema.</p>
    <div class="split-2">
      <div class="card">
        <h3>Transformaciones Previas Obligatorias</h3>
        <ul style="font-size: 0.82rem; line-height: 1.6; color: var(--text-light-mute); margin-left: 1.2rem; margin-top: 6px;">
          <li><b>Transformación Logarítmica:</b> Convierte varianza creciente heterocedástica en varianza constante homogénea: $z_t = \ln(y_t)$.</li>
          <li><b>Familia Box-Cox:</b> Parámetro óptimo $\lambda$ que normaliza asimetrías en lluvia y caudales.</li>
          <li><b>Diferenciación $\Delta y_t = y_t - y_{t-1}$:</b> Elimina la tendencia determinista para que la serie sea estacionaria.</li>
        </ul>
      </div>

      <div class="card">
        <h3>Suavizado Exponencial (Holt-Winters)</h3>
        <p style="font-size: 0.82rem; line-height: 1.5; color: var(--text-light-mute); margin-top: 6px;">
          Asigna ponderaciones que decaen geométricamente con la antigüedad de la observación:
        </p>
        <div style="background: var(--bg-light); border: 1px solid var(--line-light-faint); padding: 8px 12px; font-family: 'IBM Plex Mono'; font-size: 0.78rem; margin: 6px 0;">
          Nivel: L_t = \alpha y_t + (1 - \alpha)(L_{t-1} + b_{t-1})<br>
          Tendencia: b_t = \beta (L_t - L_t-1) + (1 - \beta) b_{t-1}
        </div>
        <p style="font-size: 0.8rem; color: var(--text-light-mute);">
          <b>Ventaja:</b> Computacionalmente instantáneo. Permite pronosticar 10,000 SKUs en milisegundos.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: PARADIGMA 1 - ARIMA Y PROPHET -->
  <section class="slide" data-title="P1: ARIMA vs Prophet">
    <span class="tag">Paradigma 1 · Modelos Clásicos</span>
    <h2>ARIMA(p, d, q) y Prophet: Filosofías Opuestas</h2>
    <p class="lead">Box-Jenkins (1970) modela correlaciones secuenciales microscópicas. Prophet (2017) modela curvas astronómicas macroscópicas.</p>
    <div class="split-2">
      <div class="diagram-box">
        <h3 style="color: var(--accent-amber); font-size: 0.95rem;">ARIMA: El Proceso Estocástico</h3>
        <svg viewBox="0 0 450 140" style="width: 100%; height: auto; margin-top: 6px;">
          <rect x="30" y="40" width="100" height="60" fill="none" stroke="var(--accent-amber)" stroke-width="2"/>
          <text x="80" y="65" font-size="11" text-anchor="middle" fill="currentColor">AR(p)</text>
          <text x="80" y="85" font-size="9" text-anchor="middle" fill="var(--text-light-mute)">y(t-1), y(t-2)</text>

          <text x="155" y="75" font-size="14" font-weight="700" fill="currentColor">+</text>

          <rect x="180" y="40" width="100" height="60" fill="none" stroke="var(--accent-amber)" stroke-width="2"/>
          <text x="230" y="65" font-size="11" text-anchor="middle" fill="currentColor">MA(q)</text>
          <text x="230" y="85" font-size="9" text-anchor="middle" fill="var(--text-light-mute)">Choques \epsilon(t-1)</text>

          <path d="M 290 70 L 350 70" stroke="var(--accent-amber)" stroke-width="2" class="anim-dash"/>
          <circle cx="370" cy="70" r="14" fill="var(--accent-amber)"/>
          <text x="370" y="75" font-size="11" font-weight="700" text-anchor="middle" fill="#FFF">y(t)</text>
        </svg>
        <p style="font-size: 0.78rem; color: var(--text-light-mute); margin-top: 4px;">
          Asume que el valor de mañana depende de una combinación lineal del valor de hoy y de la sorpresa no explicada de ayer.
        </p>
      </div>

      <div class="card">
        <h3>Prophet: Regresión de Curvas Aditivas</h3>
        <p style="font-size: 0.82rem; line-height: 1.5; color: var(--text-light-mute); margin-top: 6px;">
          En lugar de mirar el paso inmediatamente anterior, Prophet descompone la serie en un modelo de curvas de Fourier:
        </p>
        <ul style="font-size: 0.8rem; line-height: 1.5; color: var(--text-light-mute); margin-left: 1.1rem; margin-top: 4px;">
          <li><b>Changepoints automáticos:</b> Detecta cuándo una empresa o clima cambió de tendencia de forma estructural.</li>
          <li><b>Resistente a datos faltantes:</b> Si falta un mes completo de SENAMHI, Prophet no se rompe (ARIMA sí).</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: PARADIGMA 2 - PUENTE TABULAR -->
  <section class="slide" data-title="P2: El Puente Tabular">
    <span class="tag">Paradigma 2 · Machine Learning Tabular</span>
    <h2>El Puente Tabular: ¿Cómo meter tiempo en un Random Forest?</h2>
    <p class="lead">Los árboles de decisión no tienen noción de secuencia temporal. Para aprovecharlos, construimos una matriz supervisada respetando la flecha del tiempo.</p>
    <div class="split-2">
      <div class="diagram-box">
        <h3 style="color: var(--accent-blue); font-size: 0.95rem;">La Ventana Deslizante (Feature Engineering)</h3>
        <svg viewBox="0 0 480 150" style="width: 100%; height: auto; margin-top: 6px;">
          <rect x="20" y="20" width="70" height="30" fill="rgba(37,99,235,0.1)" stroke="var(--accent-blue)"/>
          <text x="55" y="40" font-size="10" font-family="IBM Plex Mono" text-anchor="middle" fill="currentColor">lag_14</text>

          <rect x="100" y="20" width="70" height="30" fill="rgba(37,99,235,0.15)" stroke="var(--accent-blue)"/>
          <text x="135" y="40" font-size="10" font-family="IBM Plex Mono" text-anchor="middle" fill="currentColor">lag_7</text>

          <rect x="180" y="20" width="70" height="30" fill="rgba(37,99,235,0.25)" stroke="var(--accent-blue)"/>
          <text x="215" y="40" font-size="10" font-family="IBM Plex Mono" text-anchor="middle" fill="currentColor">lag_1</text>

          <rect x="260" y="20" width="80" height="30" fill="rgba(5,150,105,0.15)" stroke="var(--accent-green)"/>
          <text x="300" y="40" font-size="10" font-family="IBM Plex Mono" text-anchor="middle" fill="currentColor">roll_mean7</text>

          <path d="M 350 35 L 400 35" stroke="var(--accent-blue)" stroke-width="2" class="anim-dash"/>

          <rect x="410" y="15" width="60" height="40" fill="var(--accent-blue)"/>
          <text x="440" y="40" font-size="11" font-family="IBM Plex Mono" font-weight="700" text-anchor="middle" fill="#FFF">Y(t)</text>

          <text x="20" y="90" font-size="11" fill="currentColor">Covariables Cíclicas Calendario:</text>
          <text x="20" y="115" font-size="10" font-family="IBM Plex Mono" fill="var(--text-light-mute)">sin_dia = sin(2*pi*dia/365)  |  cos_dia = cos(2*pi*dia/365)</text>
        </svg>
      </div>

      <div class="card">
        <h3>Random Forest vs ExtraTrees vs XGBoost</h3>
        <table class="data-table" style="margin-top: 4px;">
          <thead>
            <tr>
              <th>Modelo</th>
              <th>Mecanismo de Split</th>
              <th>Comportamiento con Ruido</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>Random Forest</b></td>
              <td>Mejor corte entre subconjunto aleatorio</td>
              <td>Robusto, pero puede sobreajustar ruido</td>
            </tr>
            <tr>
              <td><b>ExtraTrees</b></td>
              <td>Umbral totalmente aleatorio</td>
              <td><b>Menor varianza</b>; filtra turbulencias</td>
            </tr>
            <tr>
              <td><b>XGBoost</b></td>
              <td>Optimización por gradiente en residuos</td>
              <td>Mayor precisión si se poda con cuidado</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: PARADIGMA 2 - PATOLOGIA NO EXTRAPOLACION -->
  <section class="slide" data-title="P2: Patología de Árboles">
    <span class="tag">Paradigma 2 · Alerta Técnica</span>
    <h2>La Patología Fatal de los Árboles: ¿Por qué no extrapolan?</h2>
    <p class="lead">Grinsztajn et al. (2022) demostraron la superioridad de los árboles en tablas, pero omitir su limitación geométrica puede arruinar un pronóstico de negocio.</p>
    <div class="split-2">
      <div class="diagram-box">
        <h3 style="color: var(--accent-red); font-size: 0.95rem;">Extrapolación Fuera de Rango Histórico</h3>
        <svg viewBox="0 0 450 160" style="width: 100%; height: auto; margin-top: 6px;">
          <!-- Historical data points -->
          <line x1="30" y1="140" x2="420" y2="140" stroke="var(--line-light-faint)" stroke-width="1"/>
          <line x1="30" y1="140" x2="30" y2="20" stroke="var(--line-light-faint)" stroke-width="1"/>

          <!-- Trend line -->
          <path d="M 40 130 L 220 80" stroke="var(--accent-blue)" stroke-width="2"/>
          <text x="100" y="90" font-size="10" fill="var(--accent-blue)">Entrenamiento (Max = 38°C)</text>

          <!-- Split vertical line -->
          <line x1="220" y1="20" x2="220" y2="140" stroke="var(--line-light-faint)" stroke-dasharray="3,3"/>
          <text x="225" y="30" font-size="9" fill="currentColor">Futuro ➔</text>

          <!-- Real trend keeps rising -->
          <line x1="220" y1="80" x2="420" y2="30" stroke="var(--accent-green)" stroke-width="2" stroke-dasharray="4,4"/>
          <text x="320" y="40" font-size="10" fill="var(--accent-green)">Tendencia Real</text>

          <!-- Tree predicts flat -->
          <line x1="220" y1="80" x2="420" y2="80" stroke="var(--accent-red)" stroke-width="3"/>
          <text x="270" y="100" font-size="10" font-weight="700" fill="var(--accent-red)">Árbol predice LÍNEA PLANA</text>
        </svg>
        <p style="font-size: 0.78rem; color: var(--text-light-mute); margin-top: 4px;">
          Un árbol solo predice promedios de hojas históricas. Jamás predecirá un valor mayor a $Y_{\max}$ visto en el pasado.
        </p>
      </div>

      <div class="card" style="border-left: 3px solid var(--accent-amber);">
        <h3 style="color: var(--accent-amber);">La Solución de Ingeniería Obligatoria</h3>
        <p style="font-size: 0.82rem; line-height: 1.55; color: var(--text-light-mute); margin-top: 6px;">
          Si una serie tiene inflación, calentamiento o crecimiento demográfico:
        </p>
        <ol style="font-size: 0.82rem; line-height: 1.6; color: var(--text-light-mute); margin-left: 1.2rem; margin-top: 4px;">
          <li><b>Desestacionalizar o diferenciar:</b> Entrenar el Random Forest para predecir $\Delta Y_t = Y_t - Y_{t-1}$ en lugar de $Y_t$.</li>
          <li><b>Modelo Híbrido:</b> Ajustar una regresión lineal o curva exponencial para la tendencia global y usar el árbol para modelar los residuos no lineales.</li>
        </ol>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: PARADIGMA 2 - DEEP LEARNING LSTM VS PATCHTST -->
  <section class="slide" data-title="P2: LSTM vs PatchTST">
    <span class="tag">Paradigma 2 · Redes Neuronales</span>
    <h2>Deep Learning: De Celdas Recurrentes a Parches de Atención</h2>
    <p class="lead">Cómo evolucionó el procesamiento neuronal de secuencias temporales en los últimos 25 años.</p>
    <div class="split-2">
      <div class="diagram-box">
        <h3 style="color: var(--accent-purple); font-size: 0.95rem;">LSTM: Memoria por Compuertas (1997)</h3>
        <svg viewBox="0 0 450 150" style="width: 100%; height: auto; margin-top: 6px;">
          <rect x="30" y="20" width="390" height="110" fill="none" stroke="var(--accent-purple)" stroke-width="2"/>
          
          <rect x="50" y="55" width="75" height="40" fill="rgba(124,58,237,0.12)" stroke="var(--accent-purple)"/>
          <text x="87" y="75" font-size="9" text-anchor="middle" fill="currentColor">Forget Gate</text>
          <text x="87" y="90" font-size="8" text-anchor="middle" fill="var(--text-light-faint)">¿Qué olvido?</text>

          <rect x="155" y="55" width="75" height="40" fill="rgba(124,58,237,0.12)" stroke="var(--accent-purple)"/>
          <text x="192" y="75" font-size="9" text-anchor="middle" fill="currentColor">Input Gate</text>
          <text x="192" y="90" font-size="8" text-anchor="middle" fill="var(--text-light-faint)">¿Qué guardo?</text>

          <rect x="260" y="55" width="75" height="40" fill="rgba(124,58,237,0.12)" stroke="var(--accent-purple)"/>
          <text x="297" y="75" font-size="9" text-anchor="middle" fill="currentColor">Output Gate</text>
          <text x="297" y="90" font-size="8" text-anchor="middle" fill="var(--text-light-faint)">¿Qué emito?</text>

          <path d="M 335 75 L 390 75" stroke="var(--accent-purple)" stroke-width="2" class="anim-dash"/>
        </svg>
      </div>

      <div class="diagram-box">
        <h3 style="color: var(--accent-cyan); font-size: 0.95rem;">PatchTST: Transformers en Parches (ICLR 2023)</h3>
        <svg viewBox="0 0 450 150" style="width: 100%; height: auto; margin-top: 6px;">
          <!-- Continuous line -->
          <path d="M 30 80 Q 80 20 130 80 T 230 80 T 330 80 T 430 80" fill="none" stroke="var(--accent-cyan)" stroke-width="2"/>
          
          <!-- Patches boxes -->
          <rect x="50" y="35" width="60" height="90" fill="rgba(8,145,178,0.1)" stroke="var(--accent-cyan)" stroke-dasharray="3,3"/>
          <text x="80" y="140" font-size="9" text-anchor="middle" fill="currentColor">Parche 1 (16d)</text>

          <rect x="140" y="35" width="60" height="90" fill="rgba(8,145,178,0.1)" stroke="var(--accent-cyan)" stroke-dasharray="3,3"/>
          <text x="170" y="140" font-size="9" text-anchor="middle" fill="currentColor">Parche 2 (16d)</text>

          <rect x="230" y="35" width="60" height="90" fill="rgba(8,145,178,0.1)" stroke="var(--accent-cyan)" stroke-dasharray="3,3"/>
          <text x="260" y="140" font-size="9" text-anchor="middle" fill="currentColor">Parche 3 (16d)</text>
        </svg>
        <p style="font-size: 0.78rem; color: var(--text-light-mute); margin-top: 4px;">
          La auto-atención punto a punto falla en tiempo; agrupar en <b>parches temporales</b> reduce la complejidad y extrae semántica de contexto.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: PARADIGMA 2 - CUANDO USAR DL -->
  <section class="slide" data-title="P2: La Trampa de DL">
    <span class="tag">Paradigma 2 · Crítica de Arquitectura</span>
    <h2>La Trampa de la Serie Única en Deep Learning</h2>
    <p class="lead">Entrenar un modelo masivo en una sola serie de 2,000 datos es el error más recurrente de los equipos de ciencia de datos.</p>
    <div class="split-2">
      <div class="card" style="border-left: 3px solid var(--accent-red);">
        <h3 style="color: var(--accent-red);">El Escenario Donde Fracasa</h3>
        <p style="font-size: 0.82rem; line-height: 1.55; color: var(--text-light-mute); margin-top: 6px;">
          Si tienes una estación meteorológica individual o las ventas de una sola tienda, una red con 500,000 parámetros memoriza el ruido blanco térmico. <b>Random Forest o ExtraTrees empatarán o superarán a la red</b> con 100 veces menos costo de cómputo y cero riesgo de gradientes explosivos.
        </p>
      </div>

      <div class="card" style="border-left: 3px solid var(--accent-green);">
        <h3 style="color: var(--accent-green);">El Escenario Donde es Insuperable</h3>
        <p style="font-size: 0.82rem; line-height: 1.55; color: var(--text-light-mute); margin-top: 6px;">
          <b>Modelos Globales Multi-Serie:</b> Cuando tienes 50,000 series simultáneas (ej. retail nacional, miles de transformadores de la red eléctrica). Redes como **TFT (Temporal Fusion Transformer)** o **DeepAR** aprenden representaciones latentes cruzadas que transfieren conocimiento de series con mucha historia a productos nuevos.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: PARADIGMA 3 - DEL PIXEL AL RENDIMIENTO -->
  <section class="slide" data-title="P3: Series Biofísicas">
    <span class="tag">Paradigma 3 · Biofísica Satelital & Agro</span>
    <h2>Del Píxel al Rendimiento: Series Espacio-Temporales</h2>
    <p class="lead">En agricultura, la serie temporal no es un número abstracto: es un tensor multidimensional (x, y, longitud de onda, tiempo) que monitorea seres vivos.</p>
    <div class="split-3">
      <div class="card">
        <span class="badge badge-blue">Nivel 1 · Satélite</span>
        <h3 style="margin-top: 6px;">Sentinel-2 (10 m/px)</h3>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); line-height: 1.45;">
          Órbita sincrónica al sol cada 5 días. 13 bandas multiespectrales que capturan vigor foliar, absorción de clorofila y contenido de agua a escala de campo completo.
        </p>
      </div>
      <div class="card">
        <span class="badge badge-green">Nivel 2 · Dron & YOLOv12</span>
        <h3 style="margin-top: 6px;">Visión Aérea (Centimétrica)</h3>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); line-height: 1.45;">
          Detección en tiempo real de frutos, flores o malezas mediante atención de área (A2). Transforma ortomosaicos RGB en conteos volumétricos directos.
        </p>
      </div>
      <div class="card">
        <span class="badge badge-purple">Nivel 3 · Fenología</span>
        <h3 style="margin-top: 6px;">Ventanas Biológicas</h3>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); line-height: 1.45;">
          El impacto de 10 mm de lluvia o 32 °C no es igual en brotación que en llenado de grano. La biología del cultivo define los intervalos de agregación.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: PARADIGMA 3 - BIOFISICA Y SATURACION -->
  <section class="slide" data-title="P3: Biofísica de la Hoja">
    <span class="tag">Paradigma 3 · Biofísica de la Reflectancia</span>
    <h2>La Curva Espectral de la Hoja: Por qué el NDVI se satura</h2>
    <p class="lead">El NDVI es el índice más difundido, pero en coberturas densas como cafetales adultos sufre una ceguera física irreversible.</p>
    <div class="split-2">
      <div class="diagram-box">
        <h3 style="color: var(--accent-red); font-size: 0.95rem;">Física de la Reflectancia Foliar</h3>
        <svg viewBox="0 0 450 160" style="width: 100%; height: auto; margin-top: 6px;">
          <!-- Leaf layers -->
          <rect x="40" y="30" width="370" height="30" fill="rgba(5,150,105,0.2)" stroke="var(--accent-green)"/>
          <text x="225" y="50" font-size="10" text-anchor="middle" fill="currentColor">Clorofila: Absorbe 99% Luz Roja (Banda 4, 665 nm)</text>

          <rect x="40" y="70" width="370" height="50" fill="rgba(37,99,235,0.15)" stroke="var(--accent-blue)"/>
          <text x="225" y="95" font-size="10" text-anchor="middle" fill="currentColor">Mesófilo Esponjoso: Dispersa Infrarrojo Cercano (Banda 8, 842 nm)</text>

          <!-- Formula -->
          <text x="225" y="145" font-size="11" font-family="IBM Plex Mono" text-anchor="middle" fill="var(--accent-red)">
            NDVI = (NIR - Red) / (NIR + Red) ➔ Si Red ≈ 0, NDVI ≈ 1.0 (Congelado)
          </text>
        </svg>
        <p style="font-size: 0.78rem; color: var(--text-light-mute); margin-top: 4px;">
          Cuando el dosel se cierra ($\text{LAI} > 3$), agregar más hojas no absorbe más luz roja. El NDVI se estanca en ~0.85 y no detecta estrés hídrico.
        </p>
      </div>

      <div class="card">
        <h3>Los Índices Correctores de AgroVisión</h3>
        <div style="font-size: 0.8rem; font-family: 'IBM Plex Mono'; line-height: 1.7; color: var(--text-light-mute);">
          • <b>EVI (Huete 2002):</b> Utiliza la banda azul (B02) para corregir aerosoles. Lineal hasta $\text{LAI} > 6$.<br>
          • <b>NDRE (Barnes 2000):</b> Reemplaza el rojo por <b>Red-Edge (B05)</b>. Sensible al contenido de nitrógeno activo.<br>
          • <b>NDWI (Gao 1996):</b> Contrasta NIR con SWIR para medir agua líquida en los tejidos de la hoja.
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: PARADIGMA 3 - FUSION MULTIMODAL -->
  <section class="slide" data-title="P3: Fusión Multimodal">
    <span class="tag">Paradigma 3 · Arquitectura de Fusión</span>
    <h2>Fusión Multimodal: El Acoplamiento Biofísico</h2>
    <p class="lead">Para predecir cosechas, la literatura internacional (Ramos 2020, Barbosa 2021) demuestra que el satélite aislado es insuficiente.</p>
    <div class="split-3">
      <div class="card" style="border-top: 3px solid var(--accent-amber);">
        <div class="stat-label">Ventana 1 · Agosto a Octubre</div>
        <h3 style="margin-top: 4px;">Floración & Cuajado</h3>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); margin-top: 4px;">
          <b>Variable crítica:</b> Temperatura máxima ($T_{\max} > 31^\circ\text{C}$). Un golpe de calor en esta fase aborta las flores. El follaje sigue verde en el satélite, pero los quintales ya se perdieron.
        </p>
      </div>

      <div class="card" style="border-top: 3px solid var(--accent-blue);">
        <div class="stat-label">Ventana 2 · Noviembre a Febrero</div>
        <h3 style="margin-top: 4px;">Llenado de Fruto</h3>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); margin-top: 4px;">
          <b>Variables críticas:</b> $\sum \text{EVI}$ acumulado + Lluvia en llenado. Demanda masiva de azúcares y agua para expandir la cereza de café.
        </p>
      </div>

      <div class="card" style="border-top: 3px solid var(--accent-green);">
        <div class="stat-label">Ventana 3 · Marzo a Julio</div>
        <h3 style="margin-top: 4px;">Maduración & Cosecha</h3>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); margin-top: 4px;">
          <b>Variable crítica:</b> Senescencia controlada. Se detiene el crecimiento vegetativo para concentrar grados Brix en la semilla.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: PARADIGMA 4 - MODELOS GLOBALES Y AGENCIAS -->
  <section class="slide" data-title="P4: Supercomputadoras y Agencias">
    <span class="tag">Paradigma 4 · Modelos Globales de Escala Planeta</span>
    <h2>Las Agencias Globales: NOAA GFS vs ECMWF IFS vs ICON</h2>
    <p class="lead">¿Cómo predicen el clima las supercomputadoras del mundo? Resolución de ecuaciones diferenciales parciales de fluidos (Navier-Stokes) sobre la atmósfera terrestre.</p>
    <div class="split-3">
      <div class="card">
        <span class="badge badge-blue">Estados Unidos</span>
        <h3 style="margin-top: 6px;">NOAA GFS</h3>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); line-height: 1.5;">
          Global Forecast System. Modelo numérico no hidrostático de resolución ~13 km. Actualización cada 6 horas en los supercomputadores de la NOAA (Cray).
        </p>
      </div>
      <div class="card">
        <span class="badge badge-green">Europa</span>
        <h3 style="margin-top: 6px;">ECMWF IFS</h3>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); line-height: 1.5;">
          Centro Europeo de Pronósticos a Plazo Medio (Bolonia/Reading). Considerado el estándar de oro en asimilación de datos (4D-Var).
        </p>
      </div>
      <div class="card">
        <span class="badge badge-amber">Alemania</span>
        <h3 style="margin-top: 6px;">DWD ICON</h3>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); line-height: 1.5;">
          Malla icosaédrica no hidrostática sin singularidades en los polos. Conservación estricta de masa atmosférica.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 14: PARADIGMA 4 - DISPARIDAD EN VIVO -->
  <section class="slide" data-title="P4: Disparidad de Modelos">
    <span class="tag">Paradigma 4 · Evidencia Real en Iquitos</span>
    <h2>La Disparidad de las Agencias: ¿Cuánto discrepan?</h2>
    <p class="lead">Consulta en vivo a través de Open-Meteo para las coordenadas de Iquitos (-3.6903°, -73.2556°). <b>Incluso los supercomputadores más avanzados discrepan en más de 7 °C.</b></p>
    <div class="chart-box" style="height: 340px;">
      <canvas id="chartMultiAgency"></canvas>
    </div>
  </section>

  <!-- SLIDE 15: PARADIGMA 4 - GRAPHCAST Y ZERO SHOT -->
  <section class="slide" data-title="P4: GraphCast & Zero-Shot">
    <span class="tag">Paradigma 4 · La Revolución de IA</span>
    <h2>La Nueva Era: GraphCast (DeepMind) y Zero-Shot TimesFM</h2>
    <p class="lead">La física clásica de fluidos está siendo complementada por redes de grafos y transformers fundacionales entrenados sobre 40 años de reanálisis ERA5.</p>
    <div class="split-2">
      <div class="card">
        <span class="badge badge-purple">Google DeepMind</span>
        <h3 style="margin-top: 6px;">GraphCast (Science 2023)</h3>
        <ul style="font-size: 0.82rem; line-height: 1.6; color: var(--text-light-mute); margin-left: 1.1rem; margin-top: 6px;">
          <li><b>Arquitectura:</b> Graph Neural Network (GNN) que mapea la atmósfera en una malla icosaédrica multiescala de 0.25° (~28 km).</li>
          <li><b>Velocidad disruptiva:</b> Genera un pronóstico global a 10 días en <b>menos de 60 segundos</b> en un solo chip TPU v4 (frente a horas en supercomputadoras).</li>
          <li><b>Hito histórico:</b> Superó al sistema operativo de ECMWF en el 90% de las 1,380 variables evaluadas.</li>
        </ul>
      </div>

      <div class="card">
        <span class="badge badge-blue">Google Research & Amazon</span>
        <h3 style="margin-top: 6px;">TimesFM & Chronos (2024)</h3>
        <ul style="font-size: 0.82rem; line-height: 1.6; color: var(--text-light-mute); margin-left: 1.1rem; margin-top: 6px;">
          <li><b>TimesFM (Google):</b> Decoder-only Transformer preentrenado en 100 mil millones de puntos temporales reales y sintéticos.</li>
          <li><b>Chronos (Amazon):</b> Tokeniza números continuos mediante cuantización y los procesa con modelos de lenguaje T5.</li>
          <li><b>Ventaja Cold-Start:</b> Predicen una nueva serie sin necesidad de fase de entrenamiento previa.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 16: CASO A - MAPA IQUITOS -->
  <section class="slide" data-title="Caso A: Ubicación">
    <span class="tag">Caso Real A · Meteorología Amazónica</span>
    <h2>Ubicación Geográfica: Estación Punchana (Iquitos, Loreto)</h2>
    <p class="lead">Selva baja tropical (-3.6903°, -73.2556°, altitud 91 msnm). Influencia convectiva amazónica y frentes fríos ("friajes").</p>
    <div class="map-box" id="mapIquitos"></div>
  </section>

  <!-- SLIDE 17: CASO A - BENCHMARK 7 AÑOS -->
  <section class="slide" data-title="Caso A: Benchmark">
    <span class="tag">Caso Real A · Evaluación Rigurosa</span>
    <h2>Benchmark Multi-modelo SENAMHI (2,557 Días, Holdout 90d)</h2>
    <p class="lead">Entrenamiento sobre 2,467 días (2019-2025) y validación en los últimos 90 días sin fuga temporal.</p>
    <table class="data-table">
      <thead>
        <tr>
          <th>Familia</th>
          <th>Modelo Evaluado</th>
          <th>RMSE (°C)</th>
          <th>MAE (°C)</th>
          <th>Mejora vs Naive</th>
          <th>Diagnóstico Técnico</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Baseline</td>
          <td><b>Naive Persistencia</b></td>
          <td>2.315</td>
          <td>1.582</td>
          <td>0.0%</td>
          <td>Referencia mínima. $T(t+1) = T(t)$.</td>
        </tr>
        <tr>
          <td>Series Clásicas</td>
          <td><b>ARIMA (2,0,1)</b></td>
          <td>2.121</td>
          <td>1.776</td>
          <td><b>+8.4%</b></td>
          <td>Excelente captura de inercia y autocorrelación de corto plazo.</td>
        </tr>
        <tr>
          <td>ML Tabular</td>
          <td><b>Random Forest</b></td>
          <td>2.247</td>
          <td>1.784</td>
          <td>+2.9%</td>
          <td>Filtra bien el ruido de humedad y lluvia con lags 1-14.</td>
        </tr>
        <tr>
          <td>ML Tabular</td>
          <td><b>ExtraTrees Regressor</b></td>
          <td>2.166</td>
          <td>1.776</td>
          <td><b>+6.4%</b></td>
          <td>Splits aleatorios amortiguan las perturbaciones del clima tropical.</td>
        </tr>
        <tr>
          <td>ML Tabular</td>
          <td><b>XGBoost</b></td>
          <td>2.297</td>
          <td>1.829</td>
          <td>+0.8%</td>
          <td>Sensible a picos extremos de lluvia convectiva.</td>
        </tr>
        <tr>
          <td>Deep Learning</td>
          <td><b>LSTM 1 Capa (PyTorch)</b></td>
          <td><b>2.097</b></td>
          <td><b>1.619</b></td>
          <td><b>+9.4%</b></td>
          <td>Mejor desempeño global al capturar dinámicas recurrentes multiescala.</td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- SLIDE 18: CASO A - DEMO EN VIVO -->
  <section class="slide" data-title="Caso A: Demo en Vivo">
    <span class="tag">Demo en Vivo · SENAMHI 7 Días</span>
    <h2>Pronóstico 7 Días SENAMHI con Bandas de Confianza 90%</h2>
    <p class="lead">Datos leídos en vivo de <code>data/senamhi_forecast_7d.csv</code>. La banda sombreada representa el intervalo de confianza del 90% (±1.645 sigma).</p>
    <div class="chart-box">
      <canvas id="chartClima7d"></canvas>
    </div>
  </section>

  <!-- SLIDE 19: CASO B - MAPA JAEN & HEATMAPS -->
  <section class="slide" data-title="Caso B: Mapa Jaén">
    <span class="tag">Caso Real B · Finca Cafetalera en Jaén</span>
    <h2>Finca Cafetalera: Visor Multiespectral Interactivo</h2>
    <p class="lead">Ladera montañosa de Jaén, Cajamarca (-5.6766°, -78.7742°, 1,100 msnm). Cambie las capas espectrales para ver cómo el sensor satelital percibe el cultivo.</p>
    <div class="pill-group">
      <button class="pill-btn active" id="btnLayerSat">Satélite RGB</button>
      <button class="pill-btn" id="btnLayerNdvi">Heatmap NDVI (Saturado)</button>
      <button class="pill-btn" id="btnLayerEvi">Heatmap EVI (Biomasa Real)</button>
      <button class="pill-btn" id="btnLayerNdre">Heatmap NDRE (Nitrógeno)</button>
    </div>
    <div class="map-box" id="mapJaen"></div>
  </section>

  <!-- SLIDE 20: CASO B - EVIDENCIA DE CAMPO -->
  <section class="slide" data-title="Caso B: Evidencia">
    <span class="tag">Caso Real B · La Prueba de Campo</span>
    <h2>La Prueba de las 6 Campañas (2020–2025)</h2>
    <p class="lead">Demostración con datos reales: el NDVI anual plano en <b>0.788</b> fue incapaz de predecir la merma de cosecha, mientras que la fusión multimodal acertó.</p>
    <div class="split-2">
      <div class="card">
        <h3 style="color: var(--accent-red);">Ceguera del NDVI Anual</h3>
        <p style="font-size: 0.82rem; line-height: 1.55; color: var(--text-light-mute); margin-top: 6px;">
          En las 6 campañas evaluadas, el NDVI promedio fue exactamente <b>0.788, 0.788, 0.788, 0.788, 0.787, 0.788</b>. El índice satelital no registró variación porque el dosel siempre estuvo cerrado. Su predicción fue una constante plana (MAPE 5.4%).
        </p>
      </div>

      <div class="card">
        <h3 style="color: var(--accent-green);">Acierto de la Fusión Multimodal</h3>
        <p style="font-size: 0.82rem; line-height: 1.55; color: var(--text-light-mute); margin-top: 6px;">
          En 2024, la temperatura en floración se disparó a <b>32.3 °C</b> provocando aborto floral, mientras que el sum(EVI) en llenado cayó. El modelo fusionado predijo <b>30.24 qq/ha</b> frente a los <b>29.98 qq/ha</b> reales (error de apenas 0.26 qq/ha).
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 21: CASO B - DEMO EN VIVO -->
  <section class="slide" data-title="Caso B: Demo en Vivo">
    <span class="tag">Demo en Vivo · Rendimiento de Café</span>
    <h2>Rendimiento Real vs Modelo Fusión (LOYO Cross-Validation)</h2>
    <p class="lead">Datos leídos en vivo de <code>data/cafe_ndvi_rendimiento.csv</code> con validación estricta Leave-One-Year-Out (RMSE 1.74 qq/ha, MAPE 4.4%).</p>
    <div class="chart-box">
      <canvas id="chartCafeRend"></canvas>
    </div>
  </section>

  <!-- SLIDE 22: LECCIONES DESDE LAS TRINCHERAS -->
  <section class="slide" data-title="Lecciones Prácticas">
    <span class="tag">Síntesis Operativa</span>
    <h2>5 Lecciones desde las Trincheras del Forecasting</h2>
    <div class="split-2" style="margin-top: 0.6rem;">
      <div class="card">
        <h3>1. Validación temporal estricta</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); margin-top: 4px;">K-fold aleatorio en series temporales es autoengaño: filtra el futuro en el pasado. Siempre usar TimeSeriesSplit o Leave-One-Year-Out.</p>
      </div>
      <div class="card">
        <h3>2. Árboles antes que Deep Learning</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); margin-top: 4px;">Un Random Forest o ExtraTrees con lags y rolling features bate a redes complejas en el 90% de los problemas tabulares con costo cero.</p>
      </div>
      <div class="card">
        <h3>3. El costo del error casi nunca es simétrico</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); margin-top: 4px;">Errar 2°C hacia arriba en clima no cuesta nada; errar 2°C hacia abajo en una helada destruye cosechas millonarias. Ajustar la función de pérdida al riesgo del negocio.</p>
      </div>
      <div class="card">
        <h3>4. Respetar la física del sensor</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); margin-top: 4px;">El NDVI satura en alta biomasa (LAI>3). En cultivos leñosos densos (café, cítricos), el uso de EVI, NDRE y clima fenológico es mandatorio.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 23: ARBOL DE DECISION -->
  <section class="slide" data-title="Árbol de Decisión">
    <span class="tag">Guía de Ingeniería</span>
    <h2>Árbol de Decisión: ¿Qué modelo elegir en producción?</h2>
    <p class="lead">Flujo lógico para seleccionar la herramienta correcta según el caso de uso real:</p>
    <table class="data-table">
      <thead>
        <tr>
          <th>Pregunta de Diagnóstico</th>
          <th>Si la respuesta es SÍ</th>
          <th>Modelo Recomendado</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>¿Tengo menos de 500 puntos históricos de una sola serie?</td>
          <td>Sí</td>
          <td><b>ARIMA / ETS / Suavizado Exponencial</b></td>
        </tr>
        <tr>
          <td>¿Tengo variables exógenas (lluvia, precios, calendario) y datos tabulares?</td>
          <td>Sí</td>
          <td><b>Random Forest / ExtraTrees / XGBoost</b></td>
        </tr>
        <tr>
          <td>¿Tengo miles de series que comparten dinámicas (retail, red eléctrica)?</td>
          <td>Sí</td>
          <td><b>Temporal Fusion Transformer (TFT) / DeepAR</b></td>
        </tr>
        <tr>
          <td>¿Tengo una serie completamente nueva sin historial previo (*cold-start*)?</td>
          <td>Sí</td>
          <td><b>Chronos / TimesFM (Foundation Zero-Shot)</b></td>
        </tr>
        <tr>
          <td>¿Estoy estimando crecimiento biológico o cosechas agrícolas?</td>
          <td>Sí</td>
          <td><b>Fusión Multimodal (EVI + Clima por Fenología)</b></td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- SLIDE 24: CIERRE Y FILOSOFIA -->
  <section class="slide" data-title="Cierre">
    <span class="tag">Conclusión</span>
    <h1 class="display" style="font-size: clamp(2rem, 3.8vw, 3.2rem);">La IA no predice el futuro.<br><span style="color: var(--accent-blue);">Cuantifica la incertidumbre.</span></h1>
    <p class="lead" style="max-width: 900px; margin-top: 1.2rem;">
      El valor del forecasting moderno no está en pretender una bola de cristal infalible, sino en construir modelos honestos que definan bandas de riesgo para que los seres humanos tomen decisiones óptimas bajo incertidumbre.
    </p>
    <div style="margin-top: 1.5rem; padding: 14px 20px; border-left: 3px solid var(--accent-green); background: var(--bg-light-panel); max-width: 850px;">
      <p style="font-size: 0.95rem; font-style: italic;">
        "All models are wrong, but some are useful." — George E. P. Box
      </p>
    </div>
  </section>

  <!-- SLIDE 25: REFERENCIAS Y RECURSOS -->
  <section class="slide" data-title="Referencias">
    <span class="tag">Código Abierto & Bibliografía</span>
    <h2>Gracias por su atención</h2>
    <p class="lead">Todo el código, notebooks reproducibles y datasets procesados están en el repositorio:</p>
    <div class="split-2" style="margin-top: 0.8rem;">
      <div class="card">
        <h3>Repositorio del Proyecto</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); line-height: 1.6; margin-top: 6px;">
          • Notebooks: <code>01_clima_senamhi.ipynb</code>, <code>02_cafe_ndvi.ipynb</code><br>
          • Extracción y limpieza: <code>scripts/</code><br>
          • Bibliografía BibTeX: <code>refs.bib</code>
        </p>
      </div>
      <div class="card">
        <h3>Bibliografía Esencial</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); line-height: 1.6; margin-top: 6px;">
          • Lam et al. (Science 2023) - GraphCast: Medium-Range Global Weather.<br>
          • Huete et al. (2002) - Overview of MODIS Vegetation Indices (EVI).<br>
          • Grinsztajn et al. (2022) - Why Tree Models Still Outperform DL.<br>
          • Ansari et al. (2024) - Chronos: Learning the Language of Time Series.<br>
          • Barbosa et al. (2021) - Smart Coffee Yield Prediction.
        </p>
      </div>
    </div>
  </section>

</div>

<!-- DATA EMBEBIDA PARA OPERACIÓN 100% OFFLINE -->
<script type="text/csv" id="senamhi-7d-fallback">
__SENAMHI_7D__
</script>

<script type="text/csv" id="cafe-fallback">
__CAFE__
</script>

<script type="text/csv" id="noaa-ecmwf-fallback">
__NOAA_ECMWF__
</script>

<script type="text/csv" id="senamhi-diario-fallback">
__SENAMHI_DIARIO__
</script>

<!-- SCRIPTS DE NAVEGACIÓN Y VISUALIZACIÓN -->
<script>
const slides = Array.from(document.querySelectorAll('.slide'));
let cur = 0;
const slideNum = document.getElementById('slideNum');
let chartMultiAgencyInstance = null;
let chartClimaInstance = null;
let chartCafeInstance = null;
let mapIquitosInstance = null;
let mapJaenInstance = null;
let jaenHeatmapLayer = null;

function updateSlide(idx) {
  if(idx < 0) idx = 0;
  if(idx >= slides.length) idx = slides.length - 1;
  cur = idx;
  slides.forEach((s, i) => s.classList.toggle('active', i === cur));
  slideNum.textContent = String(cur + 1).padStart(2, '0') + ' / ' + String(slides.length).padStart(2, '0');

  // Renderizado dinámico
  if(cur === 13 && !chartMultiAgencyInstance) {
    initMultiAgencyChart();
  }
  if(cur === 15) {
    setTimeout(initMapIquitos, 100);
  }
  if(cur === 17 && !chartClimaInstance) {
    initClimaChart();
  }
  if(cur === 18) {
    setTimeout(initMapJaen, 100);
  }
  if(cur === 20 && !chartCafeInstance) {
    initCafeChart();
  }
}

document.getElementById('nextBtn').onclick = () => updateSlide(cur + 1);
document.getElementById('prevBtn').onclick = () => updateSlide(cur - 1);
document.getElementById('tocBtn').onclick = () => updateSlide(0);

window.addEventListener('keydown', e => {
  if(['ArrowRight', 'PageDown', ' '].includes(e.key)) { e.preventDefault(); updateSlide(cur + 1); }
  else if(['ArrowLeft', 'PageUp'].includes(e.key)) { e.preventDefault(); updateSlide(cur - 1); }
  else if(e.key === 'Home') updateSlide(0);
  else if(e.key === 'End') updateSlide(slides.length - 1);
  else if(e.key === 'f' || e.key === 'F') {
    if(!document.fullscreenElement) document.documentElement.requestFullscreen();
    else document.exitFullscreen();
  }
});

// Switch Tema Claro / Oscuro
const themeToggle = document.getElementById('themeToggle');
themeToggle.onclick = () => {
  document.body.classList.toggle('dark-active');
  if(chartMultiAgencyInstance) { chartMultiAgencyInstance.destroy(); chartMultiAgencyInstance = null; initMultiAgencyChart(); }
  if(chartClimaInstance) { chartClimaInstance.destroy(); chartClimaInstance = null; initClimaChart(); }
  if(chartCafeInstance) { chartCafeInstance.destroy(); chartCafeInstance = null; initCafeChart(); }
};

document.getElementById('fsBtn').onclick = () => {
  if(!document.fullscreenElement) document.documentElement.requestFullscreen();
  else document.exitFullscreen();
};

async function loadData(url, fallbackId) {
  try {
    const res = await fetch(url);
    if(res.ok) {
      const text = await res.text();
      return Papa.parse(text, { header: true, dynamicTyping: true }).data;
    }
  } catch(e) {
    console.warn('Cargando fallback embebido para:', url);
  }
  const fbText = document.getElementById(fallbackId).textContent.trim();
  return Papa.parse(fbText, { header: true, dynamicTyping: true }).data;
}

// Gráfico Multi-Agencia (Slide 14)
async function initMultiAgencyChart() {
  const data = await loadData('data/noaa_ecmwf_forecast.csv', 'noaa-ecmwf-fallback');
  const valid = data.filter(d => d.fecha);
  const labels = valid.map(d => d.fecha);
  const isDark = document.body.classList.contains('dark-active');
  const textColor = isDark ? '#94A3B8' : '#475569';
  const gridColor = isDark ? 'rgba(255,255,255,0.06)' : 'rgba(0,0,0,0.06)';

  const ctx = document.getElementById('chartMultiAgency').getContext('2d');
  chartMultiAgencyInstance = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'NOAA GFS (EE. UU.) - T° Máx (°C)',
          data: valid.map(d => d.tmax_noaa_gfs),
          borderColor: '#2563EB',
          backgroundColor: '#2563EB',
          borderWidth: 3,
          pointRadius: 5
        },
        {
          label: 'ECMWF IFS (Europa) - T° Máx (°C)',
          data: valid.map(d => d.tmax_ecmwf),
          borderColor: '#059669',
          backgroundColor: '#059669',
          borderWidth: 3,
          pointRadius: 5
        },
        {
          label: 'DWD ICON (Alemania) - T° Máx (°C)',
          data: valid.map(d => d.tmax_dwd_icon),
          borderColor: '#D97706',
          borderWidth: 2,
          borderDash: [5, 4],
          pointRadius: 4
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: { ticks: { color: textColor }, grid: { color: gridColor } },
        y: { 
          title: { display: true, text: 'Temperatura Máxima Prevista (°C)', color: textColor },
          ticks: { color: textColor },
          grid: { color: gridColor }
        }
      },
      plugins: {
        legend: { labels: { color: textColor, font: { family: 'IBM Plex Sans' } } }
      }
    }
  });
}

// Mapa Iquitos (Slide 16)
function initMapIquitos() {
  if(mapIquitosInstance) {
    mapIquitosInstance.invalidateSize();
    return;
  }
  const lat = -3.6903, lon = -73.2556;
  mapIquitosInstance = L.map('mapIquitos').setView([lat, lon], 12);
  L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Esri World Imagery',
    maxZoom: 17
  }).addTo(mapIquitosInstance);

  const marker = L.circleMarker([lat, lon], {
    radius: 9,
    fillColor: '#2563EB',
    color: '#FFF',
    weight: 2,
    fillOpacity: 0.95
  }).addTo(mapIquitosInstance);
  marker.bindPopup('<b>Estación SENAMHI Punchana (103015)</b><br>Altitud: 91 msnm<br>Iquitos, Loreto, Perú').openPopup();

  L.circle([lat, lon], {
    radius: 4000,
    color: '#D97706',
    fillColor: '#D97706',
    fillOpacity: 0.15,
    weight: 1
  }).addTo(mapIquitosInstance);
}

// Mapa Jaén (Slide 19)
function initMapJaen() {
  if(mapJaenInstance) {
    mapJaenInstance.invalidateSize();
    return;
  }
  const lat = -5.6766, lon = -78.7742;
  mapJaenInstance = L.map('mapJaen').setView([lat, lon], 14);
  L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Esri World Imagery',
    maxZoom: 18
  }).addTo(mapJaenInstance);

  const polygon = L.polygon([
    [lat - 0.005, lon - 0.005],
    [lat + 0.005, lon - 0.005],
    [lat + 0.005, lon + 0.005],
    [lat - 0.005, lon + 0.005]
  ], {
    color: '#059669',
    fillColor: '#059669',
    fillOpacity: 0.25,
    weight: 2
  }).addTo(mapJaenInstance);
  polygon.bindPopup('<b>Finca Cafetalera de Referencia</b><br>Jaén, Cajamarca (~1,100 msnm)<br>Área: 100 ha').openPopup();

  setupJaenLayerSwitch(lat, lon);
}

function setupJaenLayerSwitch(lat, lon) {
  const btnSat = document.getElementById('btnLayerSat');
  const btnNdvi = document.getElementById('btnLayerNdvi');
  const btnEvi = document.getElementById('btnLayerEvi');
  const btnNdre = document.getElementById('btnLayerNdre');

  const btns = [btnSat, btnNdvi, btnEvi, btnNdre];
  function setActive(btn) {
    btns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  }

  btnSat.onclick = () => {
    setActive(btnSat);
    if(jaenHeatmapLayer) mapJaenInstance.removeLayer(jaenHeatmapLayer);
  };

  btnNdvi.onclick = () => {
    setActive(btnNdvi);
    if(jaenHeatmapLayer) mapJaenInstance.removeLayer(jaenHeatmapLayer);
    jaenHeatmapLayer = L.rectangle([
      [lat - 0.005, lon - 0.005],
      [lat + 0.005, lon + 0.005]
    ], {
      color: 'transparent',
      fillColor: '#047857',
      fillOpacity: 0.55
    }).addTo(mapJaenInstance);
    jaenHeatmapLayer.bindPopup('<b>Capa NDVI: 0.85 (Saturado)</b><br>El dosel denso de café oculta el estrés biológico.').openPopup();
  };

  btnEvi.onclick = () => {
    setActive(btnEvi);
    if(jaenHeatmapLayer) mapJaenInstance.removeLayer(jaenHeatmapLayer);
    jaenHeatmapLayer = L.rectangle([
      [lat - 0.005, lon - 0.005],
      [lat + 0.005, lon + 0.005]
    ], {
      color: 'transparent',
      fillColor: '#2563EB',
      fillOpacity: 0.55
    }).addTo(mapJaenInstance);
    jaenHeatmapLayer.bindPopup('<b>Capa EVI: Dinámica (0.42 a 0.72)</b><br>Revela variabilidad fotosintética real en la fase de llenado.').openPopup();
  };

  btnNdre.onclick = () => {
    setActive(btnNdre);
    if(jaenHeatmapLayer) mapJaenInstance.removeLayer(jaenHeatmapLayer);
    jaenHeatmapLayer = L.rectangle([
      [lat - 0.005, lon - 0.005],
      [lat + 0.005, lon + 0.005]
    ], {
      color: 'transparent',
      fillColor: '#7C3AED',
      fillOpacity: 0.55
    }).addTo(mapJaenInstance);
    jaenHeatmapLayer.bindPopup('<b>Capa NDRE (Red-Edge)</b><br>Sensible al nitrógeno activo foliar durante floración.').openPopup();
  };
}

// Gráfico Caso A (Slide 18)
async function initClimaChart() {
  const data = await loadData('data/senamhi_forecast_7d.csv', 'senamhi-7d-fallback');
  const valid = data.filter(d => d.fecha);
  const labels = valid.map(d => d.fecha);
  const isDark = document.body.classList.contains('dark-active');
  const textColor = isDark ? '#94A3B8' : '#475569';
  const gridColor = isDark ? 'rgba(255,255,255,0.06)' : 'rgba(0,0,0,0.06)';

  const ctx = document.getElementById('chartClima7d').getContext('2d');
  chartClimaInstance = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Observado SENAMHI',
          data: valid.map(d => d.tmax_observada),
          borderColor: '#059669',
          backgroundColor: '#059669',
          borderWidth: 3,
          pointRadius: 5,
        },
        {
          label: 'ExtraTrees Regressor',
          data: valid.map(d => d.pred_random_forest),
          borderColor: '#2563EB',
          borderWidth: 2,
          pointRadius: 4,
          borderDash: [4, 4]
        },
        {
          label: 'LSTM (PyTorch)',
          data: valid.map(d => d.pred_lstm),
          borderColor: '#7C3AED',
          borderWidth: 2,
          pointRadius: 4,
        },
        {
          label: 'Naive Persistencia',
          data: valid.map(d => d.pred_naive),
          borderColor: '#D97706',
          borderWidth: 1.5,
          borderDash: [6, 4],
          pointRadius: 3
        },
        {
          label: 'Banda Superior 90%',
          data: valid.map(d => d.ci_upper_90),
          borderColor: 'transparent',
          backgroundColor: 'rgba(37, 99, 235, 0.12)',
          fill: '+1',
          pointRadius: 0
        },
        {
          label: 'Banda Inferior 90%',
          data: valid.map(d => d.ci_lower_90),
          borderColor: 'transparent',
          backgroundColor: 'rgba(37, 99, 235, 0.12)',
          fill: false,
          pointRadius: 0
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: { ticks: { color: textColor }, grid: { color: gridColor } },
        y: { 
          title: { display: true, text: 'Temperatura Máxima (°C)', color: textColor },
          ticks: { color: textColor },
          grid: { color: gridColor }
        }
      },
      plugins: {
        legend: { labels: { color: textColor, font: { family: 'IBM Plex Sans' } } }
      }
    }
  });
}

// Gráfico Caso B (Slide 21)
async function initCafeChart() {
  const data = await loadData('data/cafe_ndvi_rendimiento.csv', 'cafe-fallback');
  const valid = data.filter(d => d.campania);
  const labels = valid.map(d => 'Campaña ' + d.campania);
  const isDark = document.body.classList.contains('dark-active');
  const textColor = isDark ? '#94A3B8' : '#475569';
  const gridColor = isDark ? 'rgba(255,255,255,0.06)' : 'rgba(0,0,0,0.06)';

  const ctx = document.getElementById('chartCafeRend').getContext('2d');
  chartCafeInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Rendimiento Real Observado (qq/ha)',
          data: valid.map(d => d.rendimiento_obs_qq_ha),
          backgroundColor: '#059669',
          borderWidth: 0
        },
        {
          label: 'Predicción Fusión (EVI + Clima)',
          data: valid.map(d => d.pred_modelo_fusion),
          backgroundColor: '#2563EB',
          borderWidth: 0
        },
        {
          label: 'Predicción Solo NDVI (Saturado)',
          data: valid.map(d => d.pred_solo_ndvi),
          backgroundColor: '#DC2626',
          borderWidth: 0
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: { ticks: { color: textColor }, grid: { color: gridColor } },
        y: { 
          title: { display: true, text: 'Quintales por Hectárea (qq/ha)', color: textColor },
          ticks: { color: textColor },
          grid: { color: gridColor }
        }
      },
      plugins: {
        legend: { labels: { color: textColor, font: { family: 'IBM Plex Sans' } } }
      }
    }
  });
}

// Inicializar
updateSlide(0);
</script>
</body>
</html>
"""
    html = html.replace("__SENAMHI_7D__", senamhi_7d_csv)
    html = html.replace("__CAFE__", cafe_csv)
    html = html.replace("__SENAMHI_DIARIO__", senamhi_diario_sub)
    html = html.replace("__NOAA_ECMWF__", noaa_ecmwf_csv)

    out_path = Path("presentacion.html")
    out_path.write_text(html, encoding="utf-8")
    print(f"Deck avanzado de 25 diapositivas generado en: {out_path} ({out_path.stat().st_size / 1024:.1f} KB)")

if __name__ == "__main__":
    build_mega_deck()
