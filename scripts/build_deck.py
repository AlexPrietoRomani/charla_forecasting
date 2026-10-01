"""
Generador del deck interactivo avanzado presentacion.html (22 slides)
Usa reemplazo de placeholders sin f-string para evitar colisiones de llaves CSS/JS.
"""

from pathlib import Path
import pandas as pd

def build_advanced_deck():
    senamhi_7d_csv = Path("data/senamhi_forecast_7d.csv").read_text(encoding="utf-8").strip()
    cafe_csv = Path("data/cafe_ndvi_rendimiento.csv").read_text(encoding="utf-8").strip()
    df_senamhi = pd.read_csv("data/senamhi_diario.csv")
    senamhi_diario_sub = df_senamhi.tail(180).to_csv(index=False).strip()

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
    --bg-light-panel: #F7F7F8;
    --text-light-main: #0B0F19;
    --text-light-mute: #4B5563;
    --text-light-faint: #9CA3AF;
    --line-light: #111827;
    --line-light-faint: #E5E7EB;

    --bg-dark: #080B10;
    --bg-dark-panel: #0E131F;
    --text-dark-main: #F9FAFB;
    --text-dark-mute: #9CA3AF;
    --text-dark-faint: #4B5563;
    --line-dark: #374151;
    --line-dark-faint: #1F2937;

    --accent-blue: #2563EB;
    --accent-amber: #D97706;
    --accent-red: #DC2626;
    --accent-green: #059669;
    --accent-purple: #7C3AED;
    --accent-cyan: #0891B2;

    --stage-pad: clamp(24px, 4.5vw, 72px);
  }

  * { box-sizing: border-box; margin: 0; padding: 0; border-radius: 0 !important; }
  html, body { height: 100%; }

  body {
    background: var(--bg-light);
    color: var(--text-light-main);
    font-family: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, sans-serif;
    overflow: hidden;
    -webkit-font-smoothing: antialiased;
    transition: background 0.3s ease, color 0.3s ease;
  }

  body::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    background-size: 36px 36px;
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
      linear-gradient(to right, rgba(255,255,255,0.03) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255,255,255,0.03) 1px, transparent 1px);
  }

  .mono { font-family: "IBM Plex Mono", monospace; font-variant-numeric: tabular-nums; }
  .display { font-family: "Space Grotesk", sans-serif; font-weight: 700; }

  /* Layout */
  .deck { position: fixed; inset: 0; left: 60px; z-index: 1; transition: left 0.3s ease; }
  
  .slide {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: var(--stage-pad);
    opacity: 0;
    visibility: hidden;
    transform: translateY(8px);
    transition: opacity .35s ease, transform .35s ease, visibility .35s;
    max-width: 1400px;
    margin: 0 auto;
    overflow-y: auto;
  }
  .slide.active { opacity: 1; visibility: visible; transform: none; }

  /* Sidebar */
  .sidebar {
    position: fixed;
    top: 0; bottom: 0; left: 0;
    width: 60px;
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
    width: 40px; height: 40px;
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
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--accent-blue);
    margin-bottom: 0.45rem;
    display: inline-block;
  }
  h1 { font-size: clamp(2rem, 4.2vw, 3.6rem); line-height: 1.08; letter-spacing: -0.02em; margin-bottom: 1rem; }
  h2 { font-size: clamp(1.4rem, 2.7vw, 2.2rem); line-height: 1.15; letter-spacing: -0.01em; margin-bottom: 0.8rem; }
  h3 { font-size: 1.15rem; font-weight: 600; margin-bottom: 0.4rem; }
  .lead { font-size: clamp(0.95rem, 1.5vw, 1.2rem); line-height: 1.5; color: var(--text-light-mute); max-width: 1000px; margin-bottom: 1.2rem; }
  body.dark-active .lead { color: var(--text-dark-mute); }

  /* Cards & Grids */
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 0.8rem; }
  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-top: 0.8rem; }
  .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-top: 0.8rem; }

  .card {
    background: var(--bg-light-panel);
    border: 1px solid var(--line-light-faint);
    padding: 18px;
    transition: border-color 0.2s, transform 0.15s;
  }
  body.dark-active .card {
    background: var(--bg-dark-panel);
    border-color: var(--line-dark-faint);
  }
  .card:hover { border-color: var(--accent-blue); }

  .stat-val { font-family: "Space Grotesk", sans-serif; font-size: 2rem; font-weight: 700; margin-bottom: 4px; }
  .stat-label { font-size: 0.8rem; color: var(--text-light-mute); text-transform: uppercase; letter-spacing: 0.06em; }
  body.dark-active .stat-label { color: var(--text-dark-mute); }

  /* Interactive Elements */
  .chart-container {
    position: relative;
    width: 100%;
    height: 380px;
    background: var(--bg-light-panel);
    border: 1px solid var(--line-light-faint);
    padding: 14px;
    margin-top: 0.8rem;
  }
  body.dark-active .chart-container {
    background: var(--bg-dark-panel);
    border-color: var(--line-dark-faint);
  }

  .map-container {
    width: 100%;
    height: 380px;
    border: 1px solid var(--line-light-faint);
    margin-top: 0.8rem;
    position: relative;
    background: #111;
  }

  /* Table styling */
  table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 0.8rem;
    font-size: 0.85rem;
  }
  table.data-table th, table.data-table td {
    padding: 8px 12px;
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
    bottom: 18px; right: 26px;
    display: flex; align-items: center; gap: 12px;
    z-index: 100;
  }
  .slide-counter { font-family: "IBM Plex Mono", monospace; font-size: 0.88rem; font-weight: 600; }
  .nav-btn {
    padding: 7px 14px;
    background: var(--text-light-main);
    color: var(--bg-light);
    border: 1px solid var(--text-light-main);
    cursor: pointer;
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.82rem;
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
    padding: 2px 7px;
    font-size: 0.72rem;
    font-family: "IBM Plex Mono", monospace;
    font-weight: 600;
    margin-right: 6px;
  }
  .badge-blue { background: rgba(37, 99, 235, 0.15); color: var(--accent-blue); }
  .badge-green { background: rgba(5, 150, 105, 0.15); color: var(--accent-green); }
  .badge-amber { background: rgba(217, 119, 6, 0.15); color: var(--accent-amber); }
  .badge-red { background: rgba(220, 38, 38, 0.15); color: var(--accent-red); }
  .badge-purple { background: rgba(124, 58, 237, 0.15); color: var(--accent-purple); }

  /* HyperFrames Motion Graphics & Diagram Styles */
  .diagram-box {
    background: var(--bg-light-panel);
    border: 1px solid var(--line-light-faint);
    padding: 16px;
    position: relative;
    overflow: hidden;
  }
  body.dark-active .diagram-box {
    background: var(--bg-dark-panel);
    border-color: var(--line-dark-faint);
  }

  @keyframes flowDash {
    to { stroke-dashoffset: -20; }
  }
  .flow-line {
    stroke-dasharray: 4, 4;
    animation: flowDash 1s linear infinite;
  }

  /* Layer Switcher Pill Buttons */
  .pill-group {
    display: flex;
    gap: 8px;
    margin-bottom: 8px;
  }
  .pill-btn {
    padding: 5px 12px;
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.75rem;
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
    <button class="theme-btn" id="themeToggle" title="Cambiar Tema (Claro/Oscuro)">🌓</button>
    <button class="theme-btn mono" id="fsBtn" title="Pantalla Completa (F)">⛶</button>
  </div>
</div>

<!-- FOOTER CONTROLS -->
<div class="slide-footer">
  <span class="slide-counter mono" id="slideNum">01 / 22</span>
  <button class="nav-btn" id="prevBtn">← PREV</button>
  <button class="nav-btn" id="nextBtn">NEXT →</button>
</div>

<!-- DECK -->
<div class="deck">

  <!-- SLIDE 1: PORTADA -->
  <section class="slide active" data-title="Portada">
    <span class="tag">Charla Técnica · Forecasting, Teledetección & IA</span>
    <h1 class="display">¿Puede la IA predecir el futuro?</h1>
    <p class="lead">Lecciones de forecasting, biofísica satelital y cuantificación de incertidumbre desde el mundo real.</p>
    <div class="grid-3" style="max-width: 950px; margin-top: 1.5rem;">
      <div class="card">
        <div class="stat-label">Caso A · Meteorología</div>
        <div style="font-weight: 600; margin-top: 4px;">SENAMHI Iquitos</div>
        <div style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 4px;">7 años diarios (2019–2025). 5 familias en benchmark.</div>
      </div>
      <div class="card">
        <div class="stat-label">Caso B · Agricultura</div>
        <div style="font-weight: 600; margin-top: 4px;">Café & Sentinel-2</div>
        <div style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 4px;">Fusión EVI + microclima vs la saturación del NDVI.</div>
      </div>
      <div class="card">
        <div class="stat-label">Tesis Central</div>
        <div style="font-weight: 600; margin-top: 4px;">Incertidumbre vs Certeza</div>
        <div style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 4px;">Predecir es estimar probabilidades honestas para decidir.</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MAPA 4 FAMILIAS -->
  <section class="slide" data-title="El Mapa de Modelos">
    <span class="tag">Taxonomía de Métodos</span>
    <h2>El mapa de las 4 familias de modelos</h2>
    <p class="lead">No existe un "mejor algoritmo universal". La elección depende de tres ejes: volumen de historia previa, número de series interconectadas e interpretabilidad.</p>
    <div class="grid-4">
      <div class="card">
        <span class="badge badge-blue">Familia 1</span>
        <h3 style="margin-top: 8px;">ML Tabular</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); line-height: 1.45;">
          Random Forest, ExtraTrees, XGBoost.<br>
          <b>Especialidad:</b> Datos estructurados (<100K filas) con lags y exógenas.<br>
          <b>Limitación:</b> Incapaz de extrapolar tendencias fuera de rango.
        </p>
      </div>
      <div class="card">
        <span class="badge badge-amber">Familia 2</span>
        <h3 style="margin-top: 8px;">Series Clásicas</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); line-height: 1.45;">
          ARIMA, SARIMA, ETS, Prophet.<br>
          <b>Especialidad:</b> 1 sola serie, horizontes cortos (1-3 días), base matemática sólida.<br>
          <b>Limitación:</b> Difícil cruzar decenas de señales externas.
        </p>
      </div>
      <div class="card">
        <span class="badge badge-purple">Familia 3</span>
        <h3 style="margin-top: 8px;">DL Secuencial</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); line-height: 1.45;">
          LSTM, TFT, N-BEATS, PatchTST.<br>
          <b>Especialidad:</b> Millones de series compartidas (retail, inventarios).<br>
          <b>Limitación:</b> Sobreajuste severo en una sola serie chica.
        </p>
      </div>
      <div class="card">
        <span class="badge badge-green">Familia 4</span>
        <h3 style="margin-top: 8px;">Visión + Fusión</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); line-height: 1.45;">
          Sentinel-2, YOLOv12, SAM 2.1.<br>
          <b>Especialidad:</b> Información biofísica espacial (dosel vegetal, agua).<br>
          <b>Limitación:</b> Nubosidad y latencia de adquisición.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: ML TABULAR - MECANISMO -->
  <section class="slide" data-title="ML Tabular: Mecanismo">
    <span class="tag">Familia 1 · Machine Learning Tabular</span>
    <h2>Mecanismo: ¿Cómo convierte un árbol el tiempo en tabla?</h2>
    <p class="lead">Los árboles de decisión no entienden el tiempo de forma intrínseca. Para usarlos, transformamos la serie en una matriz de características autorregresivas respetando la causalidad temporal.</p>
    <div class="grid-2">
      <div class="diagram-box">
        <h3 style="font-size: 1rem; color: var(--accent-blue);">Ventana Deslizante (Lags de Tiempo)</h3>
        <svg viewBox="0 0 500 180" style="width: 100%; height: auto; margin-top: 10px;">
          <line x1="20" y1="80" x2="480" y2="80" stroke="var(--line-light-faint)" stroke-width="2"/>
          <circle cx="60" cy="80" r="8" fill="var(--text-light-faint)"/>
          <text x="60" y="110" font-size="11" font-family="IBM Plex Mono" text-anchor="middle" fill="currentColor">y(t-3)</text>
          
          <circle cx="150" cy="80" r="8" fill="var(--text-light-faint)"/>
          <text x="150" y="110" font-size="11" font-family="IBM Plex Mono" text-anchor="middle" fill="currentColor">y(t-2)</text>
          
          <circle cx="240" cy="80" r="8" fill="var(--accent-blue)"/>
          <text x="240" y="110" font-size="11" font-family="IBM Plex Mono" text-anchor="middle" fill="var(--accent-blue)">y(t-1)</text>

          <path d="M 260 70 Q 330 30 380 70" fill="none" stroke="var(--accent-green)" stroke-width="2" class="flow-line"/>
          
          <circle cx="390" cy="80" r="10" fill="var(--accent-green)"/>
          <text x="390" y="110" font-size="12" font-family="IBM Plex Mono" font-weight="700" text-anchor="middle" fill="var(--accent-green)">y(t) [Target]</text>

          <text x="20" y="30" font-size="12" font-family="IBM Plex Sans" fill="currentColor">Matriz de Entrada: X = [lag_1, lag_2, roll_mean_7, mes] ➔ y</text>
        </svg>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); margin-top: 8px;">
          Cada observación futura se predice dividiendo el espacio en hiperrectángulos ortogonales condicionados por los valores previos.
        </p>
      </div>

      <div class="card">
        <h3>Evolución de los Modelos de Árboles</h3>
        <ul style="font-size: 0.85rem; line-height: 1.6; margin-left: 1.2rem; color: var(--text-light-mute); margin-top: 8px;">
          <li><b>Decision Tree (1984):</b> Particiones binarias con criterio de varianza mínima. Propenso a sobreajuste.</li>
          <li><b>Random Forest (Breiman 2001):</b> Bagging de N árboles con muestreo aleatorio de features. Varianza reducida dramáticamente.</li>
          <li><b>ExtraTrees (Geurts 2006):</b> Splits con umbrales totalmente aleatorios. Mayor velocidad y aún menor varianza en series ruidosas.</li>
          <li><b>Gradient Boosting / XGBoost (Chen 2016):</b> Cada árbol nuevo entrena sobre los residuos de los anteriores, minimizando funciones de pérdida complejas.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: ML TABULAR - PROS Y CONTRAS -->
  <section class="slide" data-title="ML Tabular: Análisis">
    <span class="tag">Familia 1 · Diagnóstico Práctico</span>
    <h2>Fortalezas y Patologías Críticas de los Árboles</h2>
    <p class="lead">Grinsztajn et al. (NeurIPS 2022) confirmaron que los árboles dominan en tablas. Pero tienen un punto ciego que causa desastres si no se detecta.</p>
    <div class="grid-2">
      <div class="card" style="border-left: 3px solid var(--accent-green);">
        <h3 style="color: var(--accent-green);">Fortalezas Clave</h3>
        <ul style="font-size: 0.85rem; line-height: 1.6; margin-left: 1.2rem; color: var(--text-light-mute); margin-top: 8px;">
          <li><b>Invarianza a escalas:</b> No requieren normalización ni escalado min-max.</li>
          <li><b>Captura automática de no-linealidades:</b> Interacciones complejas (ej. calor extremo + lluvia) se resuelven sin crear términos polinomiales a mano.</li>
          <li><b>Robustez ante outliers:</b> Un pico aislado de lluvia no descalibra los pesos globales como en una red neuronal.</li>
          <li><b>Bajo costo de cómputo:</b> Entrenamiento en segundos sobre CPU sin necesidad de clústeres GPU.</li>
        </ul>
      </div>

      <div class="card" style="border-left: 3px solid var(--accent-red);">
        <h3 style="color: var(--accent-red);">Patología Fatal: Incapacidad de Extrapolar</h3>
        <p style="font-size: 0.85rem; line-height: 1.5; color: var(--text-light-mute); margin-top: 8px;">
          Un árbol de regresión predice el promedio de las muestras que cayeron en la hoja terminal. <b>Si una serie temporal tiene tendencia creciente y el valor futuro supera el máximo histórico visto en entrenamiento, el árbol predecirá una línea plana horizontal fija.</b>
        </p>
        <div style="background: rgba(220, 38, 38, 0.08); padding: 8px 12px; margin-top: 8px; font-size: 0.78rem; font-family: IBM Plex Mono;">
          Regla de oro: Antes de aplicar árboles a series no estacionarias, se DEBE diferenciar la serie (predecir el cambio Delta y_t o desestacionalizar) en lugar de predecir el nivel crudo.
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: SERIES CLASICAS - MECANISMO -->
  <section class="slide" data-title="Series Clásicas: Mecanismo">
    <span class="tag">Familia 2 · Series Temporales Clásicas</span>
    <h2>Mecanismo: Descomposición y Procesos Estocásticos</h2>
    <p class="lead">Las series clásicas parten de una hipótesis matemática elegante: cualquier señal temporal puede descomponerse en fuerzas subyacentes independientes.</p>
    <div class="grid-3">
      <div class="card">
        <span class="badge badge-amber">ARIMA(p, d, q)</span>
        <h3 style="margin-top: 6px;">Box-Jenkins (1970)</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); line-height: 1.5;">
          • <b>AR(p):</b> Regresión sobre p observaciones previas.<br>
          • <b>I(d):</b> Grado de diferenciación para alcanzar estacionariedad.<br>
          • <b>MA(q):</b> Promedio móvil ponderado de los choques aleatorios previos (epsilon_t).
        </p>
      </div>

      <div class="card">
        <span class="badge badge-blue">ETS / Holt-Winters</span>
        <h3 style="margin-top: 6px;">Suavizado Exponencial</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); line-height: 1.5;">
          Asigna pesos decrecientes geométricamente: lo ocurrido ayer importa más que lo de hace un mes. Modela nivel, tendencia lineal o amortiguada y multiplicadores estacionales exactos.
        </p>
      </div>

      <div class="card">
        <span class="badge badge-green">Prophet (Meta)</span>
        <h3 style="margin-top: 6px;">Modelo Aditivo Generalizado</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); line-height: 1.5;">
          y(t) = g(t) + s(t) + h(t) + epsilon_t<br>
          Curva logística o lineal con selección bayesiana de changepoints, series de Fourier para periodicidades anuales/semanales y efectos de días festivos.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: SERIES CLASICAS - EVALUACION -->
  <section class="slide" data-title="Series Clásicas: Evaluación">
    <span class="tag">Familia 2 · Análisis Crítico</span>
    <h2>Fortalezas y Límites de las Series Clásicas</h2>
    <p class="lead">Makridakis et al. (M4 Competition, 2018) demostraron que los métodos estadísticos simples superan frecuentemente al ML complejo en horizontes cortos de una sola serie.</p>
    <div class="grid-2">
      <div class="card" style="border-left: 3px solid var(--accent-green);">
        <h3 style="color: var(--accent-green);">¿Dónde son insuperables?</h3>
        <ul style="font-size: 0.85rem; line-height: 1.6; margin-left: 1.2rem; color: var(--text-light-mute); margin-top: 8px;">
          <li><b>Pocos datos históricos:</b> Funcionan con 50 o 100 puntos; no necesitan miles de ejemplos para converger.</li>
          <li><b>Horizontes ultra-cortos (h = 1 a 3):</b> La persistencia estacional y el término autorregresivo capturan la inercia física de inmediato.</li>
          <li><b>Incertidumbre analítica:</b> Intervalos de confianza matemáticamente derivados del proceso generativo de ruido blanco.</li>
        </ul>
      </div>

      <div class="card" style="border-left: 3px solid var(--accent-red);">
        <h3 style="color: var(--accent-red);">¿Dónde colapsan?</h3>
        <ul style="font-size: 0.85rem; line-height: 1.6; margin-left: 1.2rem; color: var(--text-light-mute); margin-top: 8px;">
          <li><b>No-linealidades complejas:</b> No pueden capturar umbrales bruscos (ej. si la helada ocurre sólo cuando viento < 2 km/h Y cielo despejado).</li>
          <li><b>Muchas variables exógenas (SARIMAX):</b> Se vuelve inestable y costoso de estimar con más de 3 o 4 covariables.</li>
          <li><b>Series intermitentes:</b> Fallan ante series con muchos ceros seguidos (ej. lluvia diaria en estaciones secas).</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: DEEP LEARNING - MECANISMO -->
  <section class="slide" data-title="DL: Mecanismo">
    <span class="tag">Familia 3 · Deep Learning Secuencial</span>
    <h2>Mecanismo: De Celdas Recurrentes a Parches de Atención</h2>
    <p class="lead">Las redes neuronales modernas para series temporales abordan la memoria a largo plazo mediante dos paradigmas: propagación de estado oculto o auto-atención en parches.</p>
    <div class="grid-2">
      <div class="diagram-box">
        <h3 style="font-size: 1rem; color: var(--accent-purple);">Celda LSTM (Hochreiter & Schmidhuber, 1997)</h3>
        <svg viewBox="0 0 450 160" style="width: 100%; height: auto; margin-top: 10px;">
          <rect x="50" y="30" width="350" height="100" fill="none" stroke="var(--accent-purple)" stroke-width="2"/>
          <text x="60" y="50" font-size="11" font-family="Space Grotesk" fill="var(--accent-purple)">Celda Recurrente (Memoria C_t)</text>
          
          <rect x="80" y="70" width="60" height="35" fill="rgba(124, 58, 237, 0.15)" stroke="var(--accent-purple)"/>
          <text x="110" y="92" font-size="10" text-anchor="middle" fill="currentColor">Forget sigma</text>

          <rect x="180" y="70" width="60" height="35" fill="rgba(124, 58, 237, 0.15)" stroke="var(--accent-purple)"/>
          <text x="210" y="92" font-size="10" text-anchor="middle" fill="currentColor">Input sigma</text>

          <rect x="290" y="70" width="60" height="35" fill="rgba(124, 58, 237, 0.15)" stroke="var(--accent-purple)"/>
          <text x="320" y="92" font-size="10" text-anchor="middle" fill="currentColor">Output sigma</text>
        </svg>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); margin-top: 6px;">
          La compuerta de olvido (forget gate) decide qué información anterior descartar, resolviendo el desvanecimiento de gradiente de las RNN simples.
        </p>
      </div>

      <div class="diagram-box">
        <h3 style="font-size: 1rem; color: var(--accent-cyan);">PatchTST (Nie et al., ICLR 2023)</h3>
        <svg viewBox="0 0 450 160" style="width: 100%; height: auto; margin-top: 10px;">
          <path d="M 20 80 Q 70 20 120 80 T 220 80 T 320 80 T 420 80" fill="none" stroke="var(--accent-cyan)" stroke-width="2"/>
          <rect x="40" y="40" width="50" height="80" fill="none" stroke="var(--text-light-main)" stroke-dasharray="3,3"/>
          <text x="65" y="135" font-size="9" text-anchor="middle" fill="currentColor">Patch 1</text>
          
          <rect x="120" y="40" width="50" height="80" fill="none" stroke="var(--text-light-main)" stroke-dasharray="3,3"/>
          <text x="145" y="135" font-size="9" text-anchor="middle" fill="currentColor">Patch 2</text>
          
          <rect x="200" y="40" width="50" height="80" fill="none" stroke="var(--text-light-main)" stroke-dasharray="3,3"/>
          <text x="225" y="135" font-size="9" text-anchor="middle" fill="currentColor">Patch 3</text>
        </svg>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); margin-top: 6px;">
          Segmenta la serie continua en ventanas discretas de 16-64 puntos. Permite a los Transformers capturar semántica de horizonte largo con memoria reducida.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: DEEP LEARNING - CUANDO USARLO -->
  <section class="slide" data-title="DL: Pros y Contras">
    <span class="tag">Familia 3 · Análisis Crítico</span>
    <h2>La trampa del Deep Learning en Series Únicas</h2>
    <p class="lead">Entrenar un Transformer o una LSTM profunda en una sola estación meteorológica o un solo producto es la receta clásica para el sobreajuste.</p>
    <div class="grid-2">
      <div class="card" style="border-left: 3px solid var(--accent-green);">
        <h3 style="color: var(--accent-green);">El Nicho Ganador de DL</h3>
        <p style="font-size: 0.85rem; line-height: 1.5; color: var(--text-light-mute); margin-top: 6px;">
          DL brilla en <b>modelado global multi-serie</b>: cuando una empresa tiene 50,000 tiendas y cada producto tiene poca historia, una arquitectura como <b>TFT (Temporal Fusion Transformer)</b> o <b>DeepAR</b> aprende representaciones conjuntas que ningún ARIMA o RF individual puede capturar.
        </p>
      </div>

      <div class="card" style="border-left: 3px solid var(--accent-red);">
        <h3 style="color: var(--accent-red);">El Escenario Donde Fracasa</h3>
        <p style="font-size: 0.85rem; line-height: 1.5; color: var(--text-light-mute); margin-top: 6px;">
          En una serie univariada de 2,000 días (como nuestra estación de clima), una red de 500,000 parámetros memoriza el ruido térmico. Requiere regularización extrema, dropout, y su mejora vs Random Forest apenas ronda el 3–8% a cambio de 100x mayor complejidad operativa y nula interpretabilidad.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: ZERO SHOT FOUNDATION MODELS -->
  <section class="slide" data-title="Foundation Zero-Shot">
    <span class="tag">Nueva Frontera · Modelos Pre-entrenados</span>
    <h2>Zero-Shot: Predecir sin entrenar (Chronos y TimesFM)</h2>
    <p class="lead">¿Qué ocurre si tratamos el pronóstico del tiempo como un problema de completación de texto? La revolución de los Modelos Fundacionales de Series de Tiempo (2024).</p>
    <div class="grid-2">
      <div class="diagram-box">
        <h3 style="font-size: 1rem; color: var(--accent-blue);">Cómo Chronos Tokeniza los Números (Amazon, 2024)</h3>
        <svg viewBox="0 0 450 140" style="width: 100%; height: auto; margin-top: 8px;">
          <text x="20" y="30" font-size="11" fill="currentColor">Serie Continua: [31.4, 32.8, 30.1, 35.6]</text>
          <path d="M 20 80 L 100 50 L 180 95 L 260 20" fill="none" stroke="var(--accent-blue)" stroke-width="2"/>
          <line x1="300" y1="20" x2="300" y2="100" stroke="var(--line-light-faint)" stroke-dasharray="2,2"/>
          <text x="320" y="55" font-size="11" font-family="IBM Plex Mono" fill="var(--accent-amber)">Token_412</text>
          <text x="320" y="75" font-size="11" font-family="IBM Plex Mono" fill="var(--accent-amber)">Token_891</text>
          <text x="320" y="95" font-size="11" font-family="IBM Plex Mono" fill="var(--accent-amber)">Token_104</text>
        </svg>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); margin-top: 4px;">
          Escala la serie localmente y la divide en contenedores discretos. Un Transformer T5 predice la distribución de probabilidad del siguiente token numérico.
        </p>
      </div>

      <div class="card">
        <h3>Ventajas Disruptivas y Limitaciones</h3>
        <ul style="font-size: 0.85rem; line-height: 1.6; margin-left: 1.2rem; color: var(--text-light-mute); margin-top: 8px;">
          <li><b>Zero-Shot puro:</b> Predice una nueva serie sin necesidad de fase de entrenamiento ni tuning de hiperparámetros.</li>
          <li><b>Excelente con estacionalidades limpias:</b> Supera a Prophet en benchmarks de retail y tráfico.</li>
          <li><b>Limitación:</b> Aún tienen dificultades para incorporar múltiples variables exógenas complejas en tiempo real (viento, lluvia, presión).</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: VISION POR COMPUTADOR -->
  <section class="slide" data-title="Visión en Agricultura">
    <span class="tag">Familia 4 · Visión Computacional</span>
    <h2>Del Píxel a la Cosecha: Detección y Segmentación en Campo</h2>
    <p class="lead">Para cultivos donde no basta la señal satelital gruesa, la visión artificial sobre drones y cámaras locales extrae métricas directas de volumen y salud.</p>
    <div class="grid-3">
      <div class="card">
        <span class="badge badge-blue">YOLOv12</span>
        <h3 style="margin-top: 8px;">Conteo por Atención de Área</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); line-height: 1.5;">
          Atención por área (A2) que elimina la complejidad cuadrática. Procesa ortomosaicos a 1.6 ms por cuadro en GPU, permitiendo conteo masivo de frutos o racimos con mAP@0.5 superior al 89%.
        </p>
      </div>

      <div class="card">
        <span class="badge badge-green">SAM 2.1 & ARAMSAM</span>
        <h3 style="margin-top: 8px;">Segmentación de Copas</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); line-height: 1.5;">
          Segment Anything optimizado para geometrías agrícolas repetitivas. Delimita la cobertura del dosel vegetal (canopy area) pasando de 9.7s por planta manual a 1.6s automatizado.
        </p>
      </div>

      <div class="card">
        <span class="badge badge-purple">DINOv2 (Meta AI)</span>
        <h3 style="margin-top: 8px;">Representación Auto-supervisada</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); line-height: 1.5;">
          Modelado de imágenes enmascaradas (MIM). Extrae características inmunes a sombras y variación de luz solar, vital para clasificar severidad de roya o estrés foliar en campo.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: BIOFISICA SATELITAL Y SATURACION -->
  <section class="slide" data-title="Biofísica Satelital">
    <span class="tag">Teledetección · Biofísica de la Hoja</span>
    <h2>La Biofísica de la Reflectancia: Por qué el NDVI se satura</h2>
    <p class="lead">El NDVI no es infalible. En cultivos de dosel denso como el café o árboles frutales, la física de la reflectancia impone un límite ciego.</p>
    <div class="grid-2">
      <div class="diagram-box">
        <h3 style="font-size: 1rem; color: var(--accent-red);">Curva de Saturación: NDVI vs EVI / NDRE</h3>
        <svg viewBox="0 0 450 160" style="width: 100%; height: auto; margin-top: 8px;">
          <line x1="40" y1="130" x2="420" y2="130" stroke="var(--line-light-faint)" stroke-width="1.5"/>
          <line x1="40" y1="130" x2="40" y2="20" stroke="var(--line-light-faint)" stroke-width="1.5"/>
          <text x="240" y="152" font-size="10" text-anchor="middle" fill="currentColor">Índice de Área Foliar (LAI) / Biomasa ➔</text>
          <text x="20" y="20" font-size="10" text-anchor="middle" fill="currentColor">Índice</text>

          <path d="M 40 120 Q 120 40 400 35" fill="none" stroke="var(--accent-red)" stroke-width="3"/>
          <text x="360" y="30" font-size="11" font-weight="700" fill="var(--accent-red)">NDVI (Satura en LAI > 3)</text>

          <path d="M 40 125 L 400 45" fill="none" stroke="var(--accent-green)" stroke-width="3"/>
          <text x="360" y="60" font-size="11" font-weight="700" fill="var(--accent-green)">EVI (Lineal hasta LAI > 6)</text>
        </svg>
        <p style="font-size: 0.8rem; color: var(--text-light-mute); margin-top: 6px;">
          La clorofila absorbe casi el 99% de la luz roja (B04). En dosel cerrado, un aumento de hojas no incrementa la absorción roja; el NDVI se congela en ~0.85.
        </p>
      </div>

      <div class="card">
        <h3>Fórmulas Espectrales (Herencia AgroVisión)</h3>
        <div style="font-size: 0.82rem; font-family: 'IBM Plex Mono'; line-height: 1.8; color: var(--text-light-mute);">
          • <b>NDVI:</b> (B08 - B04) / (B08 + B04)<br>
          • <b>EVI (Huete 2002):</b> 2.5 * (B08 - B04) / (B08 + 6*B04 - 7.5*B02 + 1)<br>
          • <b>NDRE (Barnes 2000):</b> (B08 - B05) / (B08 + B05) (Red-Edge: sensible a nitrógeno)<br>
          • <b>NDWI (Gao 1996):</b> (B03 - B08) / (B03 + B08) (Contenido de agua líquida foliar)
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: FUSION MULTIMODAL -->
  <section class="slide" data-title="Fusión Multimodal">
    <span class="tag">Arquitectura Multimodal</span>
    <h2>Fusión Multimodal: Espectro + Microclima + Fenología</h2>
    <p class="lead">El rendimiento de un cultivo no depende de una foto satelital en cualquier día, sino de la coincidencia entre el vigor vegetal y el estrés climático en ventanas críticas.</p>
    <div class="grid-3">
      <div class="card">
        <div class="stat-label">Ventana 1 · Agosto a Octubre</div>
        <h3 style="margin-top: 4px;">Floración & Cuajado</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); margin-top: 4px;">
          Sensible a golpes de calor y estrés hídrico. Temperaturas >31°C abortan la flor, reduciendo el rendimiento final sin que el follaje pierda color verde.
        </p>
      </div>
      <div class="card">
        <div class="stat-label">Ventana 2 · Noviembre a Febrero</div>
        <h3 style="margin-top: 4px;">Llenado de Fruto</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); margin-top: 4px;">
          Pico de demanda fotosintética. La acumulación sum(EVI) y la lluvia en llenado determinan el peso y densidad del grano de café.
        </p>
      </div>
      <div class="card">
        <div class="stat-label">Ventana 3 · Marzo a Julio</div>
        <h3 style="margin-top: 4px;">Maduración & Cosecha</h3>
        <p style="font-size: 0.82rem; color: var(--text-light-mute); margin-top: 4px;">
          Descenso fisiológico del vigor. La senescencia controlada favorece la concentración de azúcares en la cereza.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: CASO A - MAPA IQUITOS -->
  <section class="slide" data-title="Caso A: Ubicación">
    <span class="tag">Caso Real A · SENAMHI</span>
    <h2>Ubicación Geográfica: Estación Punchana (Iquitos, Loreto)</h2>
    <p class="lead">Selva baja tropical (-3.6903°, -73.2556°, altitud 91 msnm). Clima cálido húmedo con fuerte influencia de la cuenca amazónica y episodios abruptos de frentes fríos ("friajes").</p>
    <div class="map-container" id="mapIquitos"></div>
  </section>

  <!-- SLIDE 14: CASO A - RESULTADOS BENCHMARK -->
  <section class="slide" data-title="Caso A: Benchmark">
    <span class="tag">Caso Real A · Evaluación Rigurosa</span>
    <h2>Benchmark Multi-modelo SENAMHI (Holdout 90 días)</h2>
    <p class="lead">Entrenamiento sobre 2,467 días continuos y validación estricta en los últimos 90 días de 2025 sin fuga temporal.</p>
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
          <td>Referencia mínima. Asume que mañana la T° será igual a hoy.</td>
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
          <td>Supera al naive. Filtra bien el ruido de humedad y lluvia.</td>
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
          <td>Ligeramente sensible a picos extremos de lluvia si no se poda.</td>
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

  <!-- SLIDE 15: CASO A - DEMO EN VIVO -->
  <section class="slide" data-title="Caso A: Demo en Vivo">
    <span class="tag">Demo en Vivo · SENAMHI 7 Días</span>
    <h2>Pronóstico a 7 días y Cuantificación de Incertidumbre</h2>
    <p class="lead">Datos leídos en vivo de <code>data/senamhi_forecast_7d.csv</code>. La banda azul representa el intervalo de confianza al 90% (±1.645 sigma).</p>
    <div class="chart-container">
      <canvas id="chartClima7d"></canvas>
    </div>
  </section>

  <!-- SLIDE 16: CASO B - MAPA JAEN & HEATMAP -->
  <section class="slide" data-title="Caso B: Mapa Jaén">
    <span class="tag">Caso Real B · Teledetección en Jaén</span>
    <h2>Finca Cafetalera en Jaén: Visor Multiespectral</h2>
    <p class="lead">Coordenadas cafetaleras (-5.6766°, -78.7742°, 1,100 msnm). Interactúe con los botones para simular las capas de índices espectrales calculadas según el pipeline de AgroVisión.</p>
    <div class="pill-group">
      <button class="pill-btn active" id="btnLayerSat">Satélite RGB</button>
      <button class="pill-btn" id="btnLayerNdvi">Heatmap NDVI (Saturado)</button>
      <button class="pill-btn" id="btnLayerEvi">Heatmap EVI (Biomasa Real)</button>
      <button class="pill-btn" id="btnLayerNdre">Heatmap NDRE (Nitrógeno)</button>
    </div>
    <div class="map-container" id="mapJaen"></div>
  </section>

  <!-- SLIDE 17: CASO B - LA PRUEBA DE SATURACION -->
  <section class="slide" data-title="Caso B: La Prueba">
    <span class="tag">Caso Real B · Evidencia Empírica</span>
    <h2>La prueba de campo: 6 campañas de café (2020–2025)</h2>
    <p class="lead">Demostración con datos reales: por qué un modelo basado solo en NDVI anual no puede anticipar mermas de cosecha.</p>
    <div class="grid-2">
      <div class="card">
        <h3 style="color: var(--accent-red);">Comportamiento del NDVI Anual</h3>
        <p style="font-size: 0.85rem; line-height: 1.5; color: var(--text-light-mute); margin-top: 6px;">
          En las 6 campañas analizadas, el NDVI promedio fue exactamente <b>0.788, 0.788, 0.788, 0.788, 0.787, 0.788</b>. El índice satelital no varió absolutamente nada porque la copa del cafeto permaneció cerrada. El modelo de regresión con solo NDVI predijo la misma media fija (MAPE 5.4%).
        </p>
      </div>

      <div class="card">
        <h3 style="color: var(--accent-green);">Comportamiento de la Fusión Multimodal</h3>
        <p style="font-size: 0.85rem; line-height: 1.5; color: var(--text-light-mute); margin-top: 6px;">
          En la campaña 2024, la temperatura en floración subió a <b>32.3 °C</b> provocando aborto floral, mientras que el sum(EVI) en llenado capturó menor fotosíntesis. El modelo fusionado predijo <b>30.24 qq/ha</b> frente a los <b>29.98 qq/ha</b> reales (error de solo 0.26 qq/ha).
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 18: CASO B - DEMO EN VIVO -->
  <section class="slide" data-title="Caso B: Demo en Vivo">
    <span class="tag">Demo en Vivo · Rendimiento de Café</span>
    <h2>Rendimiento Observado vs Modelo Fusión (LOYO)</h2>
    <p class="lead">Comparación de campañas leyendo <code>data/cafe_ndvi_rendimiento.csv</code> con validación Leave-One-Year-Out (RMSE 1.74 qq/ha, MAPE 4.4%).</p>
    <div class="chart-container">
      <canvas id="chartCafeRend"></canvas>
    </div>
  </section>

  <!-- SLIDE 19: LECCIONES DEL MUNDO REAL -->
  <section class="slide" data-title="Lecciones">
    <span class="tag">Síntesis Operativa</span>
    <h2>5 Lecciones desde las trincheras del forecasting</h2>
    <div class="grid-2" style="margin-top: 0.8rem;">
      <div class="card">
        <h3>1. Validación temporal estricta</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 4px;">Hacer k-fold aleatorio en series temporales es el mayor autoengaño: filtra el futuro en el pasado. Siempre usar TimeSeriesSplit o Leave-One-Year-Out.</p>
      </div>
      <div class="card">
        <h3>2. Árboles antes que Deep Learning</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 4px;">Un ensamble tabular bien construido bate a redes complejas en el 90% de los problemas tabulares con menos costo y cero dependencias de hardware.</p>
      </div>
      <div class="card">
        <h3>3. El costo del error casi nunca es simétrico</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 4px;">Predecir 2°C de más en clima no cuesta nada; errar 2°C hacia abajo en una helada destruye cosechas millonarias. Ajustar la función de pérdida al riesgo del negocio.</p>
      </div>
      <div class="card">
        <h3>4. Respetar la física del sensor</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 4px;">El NDVI satura en alta biomasa. En agricultura intensiva y doseles leñosos densos, el uso de EVI, NDRE y clima en ventanas biológicas es mandatorio.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 20: ARBOL DE DECISION -->
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

  <!-- SLIDE 21: CIERRE Y FILOSOFIA -->
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

  <!-- SLIDE 22: REFERENCIAS Y RECURSOS -->
  <section class="slide" data-title="Referencias">
    <span class="tag">Código Abierto & Bibliografía</span>
    <h2>Gracias por su atención</h2>
    <p class="lead">Todo el código, notebooks reproducibles y datasets procesados están en el repositorio:</p>
    <div class="grid-2" style="max-width: 950px; margin-top: 0.8rem;">
      <div class="card">
        <h3>Repositorio del Proyecto</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); line-height: 1.6; margin-top: 6px;">
          • Notebooks: <code>01_clima_senamhi.ipynb</code>, <code>02_cafe_ndvi.ipynb</code><br>
          • Extracción y limpieza: <code>scripts/</code><br>
          • Bibliografía BibTeX: <code>refs.bib</code>
        </p>
      </div>
      <div class="card">
        <h3>Bibliografía Esencial</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); line-height: 1.6; margin-top: 6px;">
          • Breiman (2001) - Random Forests.<br>
          • Huete et al. (2002) - Overview of MODIS Vegetation Indices (EVI).<br>
          • Grinsztajn et al. (2022) - Why Tree Models Still Outperform DL.<br>
          • Ansari et al. (2024) - Chronos: Learning the Language of Time Series.<br>
          • Barbosa et al. (2021) - Smart Coffee Yield Prediction.
        </p>
      </div>
    </div>
  </section>

</div>

<!-- FALLBACK DATA EMBEBIDA PARA DOBLE CLIC OFFLINE -->
<script type="text/csv" id="senamhi-7d-fallback">
__SENAMHI_7D__
</script>

<script type="text/csv" id="cafe-fallback">
__CAFE__
</script>

<script type="text/csv" id="senamhi-diario-fallback">
__SENAMHI_DIARIO__
</script>

<!-- CONTROLADORES Y MAPAS -->
<script>
const slides = Array.from(document.querySelectorAll('.slide'));
let cur = 0;
const slideNum = document.getElementById('slideNum');
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
  
  // Renderizado perezoso de mapas y gráficos
  if(cur === 12) {
    setTimeout(initMapIquitos, 100);
  }
  if(cur === 14 && !chartClimaInstance) {
    initClimaChart();
  }
  if(cur === 15) {
    setTimeout(initMapJaen, 100);
  }
  if(cur === 17 && !chartCafeInstance) {
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

// Toggle Tema Claro / Oscuro
const themeToggle = document.getElementById('themeToggle');
themeToggle.onclick = () => {
  document.body.classList.toggle('dark-active');
  if(chartClimaInstance) { chartClimaInstance.destroy(); chartClimaInstance = null; initClimaChart(); }
  if(chartCafeInstance) { chartCafeInstance.destroy(); chartCafeInstance = null; initCafeChart(); }
};

document.getElementById('fsBtn').onclick = () => {
  if(!document.fullscreenElement) document.documentElement.requestFullscreen();
  else document.exitFullscreen();
};

// Carga de datos con fallback
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

// Mapa Iquitos (SENAMHI)
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
    fillOpacity: 0.9
  }).addTo(mapIquitosInstance);
  marker.bindPopup('<b>Estación SENAMHI Punchana (103015)</b><br>Altitud: 91 msnm<br>Iquitos, Loreto, Perú').openPopup();

  L.circle([lat, lon], {
    radius: 3500,
    color: '#D97706',
    fillColor: '#D97706',
    fillOpacity: 0.15,
    weight: 1
  }).addTo(mapIquitosInstance);
}

// Mapa Jaén (Café) con visor de capas
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
  polygon.bindPopup('<b>Finca Cafetalera Referencial</b><br>Jaén, Cajamarca (~1,100 msnm)<br>Área: 100 ha').openPopup();

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
    jaenHeatmapLayer.bindPopup('<b>Capa NDVI: 0.85 (Saturado)</b><br>No muestra diferencias intra-parcelarias debido a la densidad del dosel.').openPopup();
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
    jaenHeatmapLayer.bindPopup('<b>Capa EVI: Dinámica (0.42 a 0.72)</b><br>Revela variabilidad fotosintética real en la fase de llenado de fruto.').openPopup();
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
    jaenHeatmapLayer.bindPopup('<b>Capa NDRE (Red-Edge)</b><br>Sensible al contenido foliar de nitrógeno activo durante floración.').openPopup();
  };
}

// Gráfico Caso A: Clima 7 días
async function initClimaChart() {
  const data = await loadData('data/senamhi_forecast_7d.csv', 'senamhi-7d-fallback');
  const validData = data.filter(d => d.fecha);
  const labels = validData.map(d => d.fecha);
  const isDark = document.body.classList.contains('dark-active');
  const textColor = isDark ? '#9CA3AF' : '#4B5563';
  const gridColor = isDark ? 'rgba(255,255,255,0.06)' : 'rgba(0,0,0,0.06)';

  const ctx = document.getElementById('chartClima7d').getContext('2d');
  chartClimaInstance = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Observado SENAMHI',
          data: validData.map(d => d.tmax_observada),
          borderColor: '#059669',
          backgroundColor: '#059669',
          borderWidth: 3,
          pointRadius: 5,
        },
        {
          label: 'ExtraTrees Regressor',
          data: validData.map(d => d.pred_random_forest),
          borderColor: '#2563EB',
          borderWidth: 2,
          pointRadius: 4,
          borderDash: [4, 4]
        },
        {
          label: 'LSTM (PyTorch)',
          data: validData.map(d => d.pred_lstm),
          borderColor: '#7C3AED',
          borderWidth: 2,
          pointRadius: 4,
        },
        {
          label: 'Naive Persistencia',
          data: validData.map(d => d.pred_naive),
          borderColor: '#D97706',
          borderWidth: 1.5,
          borderDash: [6, 4],
          pointRadius: 3
        },
        {
          label: 'Banda Superior 90%',
          data: validData.map(d => d.ci_upper_90),
          borderColor: 'transparent',
          backgroundColor: 'rgba(37, 99, 235, 0.12)',
          fill: '+1',
          pointRadius: 0
        },
        {
          label: 'Banda Inferior 90%',
          data: validData.map(d => d.ci_lower_90),
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

// Gráfico Caso B: Rendimiento Café
async function initCafeChart() {
  const data = await loadData('data/cafe_ndvi_rendimiento.csv', 'cafe-fallback');
  const validData = data.filter(d => d.campania);
  const labels = validData.map(d => 'Campaña ' + d.campania);
  const isDark = document.body.classList.contains('dark-active');
  const textColor = isDark ? '#9CA3AF' : '#4B5563';
  const gridColor = isDark ? 'rgba(255,255,255,0.06)' : 'rgba(0,0,0,0.06)';

  const ctx = document.getElementById('chartCafeRend').getContext('2d');
  chartCafeInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Rendimiento Real Observado (qq/ha)',
          data: validData.map(d => d.rendimiento_obs_qq_ha),
          backgroundColor: '#059669',
          borderWidth: 0
        },
        {
          label: 'Predicción Fusión (EVI + Clima)',
          data: validData.map(d => d.pred_modelo_fusion),
          backgroundColor: '#2563EB',
          borderWidth: 0
        },
        {
          label: 'Predicción Solo NDVI (Saturado)',
          data: validData.map(d => d.pred_solo_ndvi),
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

// Inicialización
updateSlide(0);
</script>
</body>
</html>
"""
    html = html.replace("__SENAMHI_7D__", senamhi_7d_csv)
    html = html.replace("__CAFE__", cafe_csv)
    html = html.replace("__SENAMHI_DIARIO__", senamhi_diario_sub)

    out_path = Path("presentacion.html")
    out_path.write_text(html, encoding="utf-8")
    print(f"Deck avanzado de 22 diapositivas generado en: {out_path} ({out_path.stat().st_size / 1024:.1f} KB)")

if __name__ == "__main__":
    build_advanced_deck()
