"""
Generador del deck interactivo exhaustivo presentacion.html (25 diapositivas)
Diseño Full-Bleed (de borde a borde), cero espacios vacíos, pedagogía desde cero,
animaciones interactivas con narrativa paso a paso, comparativa global NOAA vs ECMWF vs DWD ICON,
y mapas satelitales Leaflet con Visor de Capas y Heatmaps en tiempo real.
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
<link rel="icon" href="data:,">
<title>¿Puede la IA predecir el futuro? Lecciones de forecasting desde el mundo real</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<style>
  :root {
    --bg-light: #F8FAFC;
    --bg-light-panel: #FFFFFF;
    --bg-light-sub: #F1F5F9;
    --text-light-main: #0F172A;
    --text-light-mute: #334155;
    --text-light-faint: #64748B;
    --line-light: #CBD5E1;
    --line-light-faint: #E2E8F0;

    --bg-dark: #07090E;
    --bg-dark-panel: #0D121F;
    --bg-dark-sub: #141C2E;
    --text-dark-main: #F8FAFC;
    --text-dark-mute: #94A3B8;
    --text-dark-faint: #475569;
    --line-dark: #334155;
    --line-dark-faint: #1E293B;

    --accent-blue: #2563EB;
    --accent-emerald: #059669;
    --accent-amber: #D97706;
    --accent-red: #DC2626;
    --accent-purple: #7C3AED;
    --accent-cyan: #0891B2;

    --sidebar-w: 56px;
    --footer-h: 46px;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { height: 100%; width: 100%; }

  body {
    background: var(--bg-light);
    color: var(--text-light-main);
    font-family: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, sans-serif;
    overflow: hidden;
    -webkit-font-smoothing: antialiased;
    transition: background 0.25s ease, color 0.25s ease;
  }

  body::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    background-size: 32px 32px;
    background-image: 
      linear-gradient(to right, rgba(15,23,42,0.03) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(15,23,42,0.03) 1px, transparent 1px);
  }

  body.dark-active {
    background: var(--bg-dark);
    color: var(--text-dark-main);
  }
  body.dark-active::before {
    background-image: 
      linear-gradient(to right, rgba(255,255,255,0.025) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255,255,255,0.025) 1px, transparent 1px);
  }

  .mono { font-family: "IBM Plex Mono", monospace; font-variant-numeric: tabular-nums; }
  .display { font-family: "Space Grotesk", sans-serif; font-weight: 700; letter-spacing: -0.02em; }

  /* SIDEBAR NAVEGACION */
  .sidebar {
    position: fixed;
    top: 0; left: 0; bottom: 0;
    width: var(--sidebar-w);
    background: var(--bg-light-panel);
    border-right: 1px solid var(--line-light-faint);
    z-index: 100;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 14px 0;
  }
  body.dark-active .sidebar {
    background: var(--bg-dark-panel);
    border-color: var(--line-dark-faint);
  }

  .nav-icon-btn, .theme-btn {
    width: 38px; height: 38px;
    border: 1px solid var(--line-light);
    background: transparent;
    color: var(--text-light-mute);
    cursor: pointer;
    font-size: 13px;
    display: flex; align-items: center; justify-content: center;
    transition: all 0.2s;
  }
  body.dark-active .nav-icon-btn, body.dark-active .theme-btn {
    border-color: var(--line-dark);
    color: var(--text-dark-mute);
  }
  .nav-icon-btn:hover, .theme-btn:hover {
    background: var(--accent-blue);
    color: #FFF;
    border-color: var(--accent-blue);
  }

  /* FOOTER */
  .slide-footer {
    position: fixed;
    bottom: 0; left: var(--sidebar-w); right: 0;
    height: var(--footer-h);
    background: var(--bg-light-panel);
    border-top: 1px solid var(--line-light-faint);
    z-index: 90;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding: 0 24px;
    gap: 12px;
  }
  body.dark-active .slide-footer {
    background: var(--bg-dark-panel);
    border-color: var(--line-dark-faint);
  }

  .slide-counter {
    font-size: 13px;
    color: var(--text-light-faint);
    font-weight: 500;
    margin-right: 12px;
  }
  body.dark-active .slide-counter { color: var(--text-dark-faint); }

  .nav-btn {
    background: transparent;
    border: 1px solid var(--line-light);
    color: var(--text-light-main);
    padding: 6px 14px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.05em;
    cursor: pointer;
    transition: all 0.15s;
    font-family: "IBM Plex Mono", monospace;
  }
  body.dark-active .nav-btn {
    border-color: var(--line-dark);
    color: var(--text-dark-main);
  }
  .nav-btn:hover {
    background: var(--accent-blue);
    color: #FFF;
    border-color: var(--accent-blue);
  }

  /* FULL-BLEED DECK LAYOUT */
  .deck {
    position: fixed;
    top: 0; left: var(--sidebar-w); right: 0; bottom: var(--footer-h);
    z-index: 10;
  }

  .slide {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    padding: 24px 36px 16px 36px;
    opacity: 0;
    visibility: hidden;
    transform: translateY(4px);
    transition: opacity .25s ease, transform .25s ease, visibility .25s;
    overflow-y: auto;
  }
  .slide.active {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }

  /* HEADERS */
  .slide-header {
    margin-bottom: 16px;
    flex-shrink: 0;
  }
  .tag {
    display: inline-block;
    font-family: "IBM Plex Mono", monospace;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--accent-blue);
    margin-bottom: 4px;
  }
  .slide-title {
    font-size: clamp(24px, 2.4vw, 32px);
    line-height: 1.15;
    color: var(--text-light-main);
    margin-bottom: 4px;
  }
  body.dark-active .slide-title { color: var(--text-dark-main); }
  .slide-subtitle {
    font-size: clamp(13px, 1.05vw, 15px);
    color: var(--text-light-mute);
    line-height: 1.4;
  }
  body.dark-active .slide-subtitle { color: var(--text-dark-mute); }

  /* CONTENIDO PRINCIPAL */
  .slide-body {
    flex: 1;
    min-height: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .split-50 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    flex: 1;
    min-height: 0;
  }
  .split-55 {
    display: grid;
    grid-template-columns: 1.25fr 1fr;
    gap: 20px;
    flex: 1;
    min-height: 0;
  }
  .split-60 {
    display: grid;
    grid-template-columns: 1.45fr 1fr;
    gap: 20px;
    flex: 1;
    min-height: 0;
  }
  .split-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 18px;
    flex: 1;
    min-height: 0;
  }
  .grid-2x2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 16px;
    flex: 1;
    min-height: 0;
  }

  /* CARDS Y CONTENEDORES ANTI-VACIO */
  .panel {
    background: var(--bg-light-panel);
    border: 1px solid var(--line-light-faint);
    padding: 18px 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
    min-height: 0;
    position: relative;
    overflow: hidden;
  }
  body.dark-active .panel {
    background: var(--bg-dark-panel);
    border-color: var(--line-dark-faint);
  }

  .panel-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--line-light-faint);
    flex-shrink: 0;
  }
  body.dark-active .panel-header { border-color: var(--line-dark-faint); }
  .panel-title {
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--text-light-main);
  }
  body.dark-active .panel-title { color: var(--text-dark-main); }
  .panel-badge {
    font-family: "IBM Plex Mono", monospace;
    font-size: 11px;
    padding: 2px 6px;
    background: var(--bg-light-sub);
    color: var(--text-light-mute);
    border: 1px solid var(--line-light-faint);
  }
  body.dark-active .panel-badge {
    background: var(--bg-dark-sub);
    color: var(--text-dark-mute);
    border-color: var(--line-dark-faint);
  }

  .panel-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    gap: 12px;
    min-height: 0;
  }

  /* KPI BOXES */
  .kpi-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
    gap: 10px;
    margin: 6px 0;
  }
  .kpi-box {
    background: var(--bg-light-sub);
    border: 1px solid var(--line-light-faint);
    padding: 10px 12px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  body.dark-active .kpi-box {
    background: var(--bg-dark-sub);
    border-color: var(--line-dark-faint);
  }
  .kpi-val {
    font-size: clamp(18px, 1.8vw, 24px);
    font-weight: 700;
    line-height: 1.1;
    color: var(--text-light-main);
  }
  body.dark-active .kpi-val { color: var(--text-dark-main); }
  .kpi-lbl {
    font-size: 11px;
    color: var(--text-light-faint);
    margin-top: 3px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
  }
  body.dark-active .kpi-lbl { color: var(--text-dark-faint); }

  /* CALLOUT / INSIGHT BOXES */
  .callout {
    padding: 12px 14px;
    border-left: 3px solid var(--accent-blue);
    background: rgba(37, 99, 235, 0.04);
    font-size: 13px;
    line-height: 1.45;
    color: var(--text-light-mute);
  }
  body.dark-active .callout {
    background: rgba(37, 99, 235, 0.08);
    color: var(--text-dark-mute);
  }
  .callout.alert {
    border-color: var(--accent-red);
    background: rgba(220, 38, 38, 0.05);
  }
  body.dark-active .callout.alert {
    background: rgba(220, 38, 38, 0.1);
  }
  .callout.success {
    border-color: var(--accent-emerald);
    background: rgba(5, 150, 105, 0.05);
  }
  body.dark-active .callout.success {
    background: rgba(5, 150, 105, 0.1);
  }

  /* LISTAS Y COMPARATIVAS */
  .feature-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 8px;
    font-size: 13px;
    line-height: 1.4;
  }
  .feature-item {
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }
  .feature-bullet {
    width: 6px; height: 6px;
    background: var(--accent-blue);
    margin-top: 6px;
    flex-shrink: 0;
  }

  /* TABLAS PROFESIONALES */
  .data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
    font-family: "IBM Plex Sans", sans-serif;
  }
  .data-table th, .data-table td {
    padding: 8px 10px;
    text-align: left;
    border-bottom: 1px solid var(--line-light-faint);
  }
  body.dark-active .data-table th, body.dark-active .data-table td {
    border-color: var(--line-dark-faint);
  }
  .data-table th {
    font-family: "IBM Plex Mono", monospace;
    font-size: 11px;
    text-transform: uppercase;
    color: var(--text-light-faint);
    background: var(--bg-light-sub);
    letter-spacing: 0.05em;
  }
  body.dark-active .data-table th {
    background: var(--bg-dark-sub);
    color: var(--text-dark-faint);
  }
  .data-table tr:hover td {
    background: rgba(37, 99, 235, 0.03);
  }

  /* CANVAS Y CONTENEDORES GRAFICOS */
  .chart-container {
    position: relative;
    flex: 1;
    width: 100%;
    min-height: 0;
  }
  .map-container {
    width: 100%;
    height: 100%;
    min-height: 250px;
    border: 1px solid var(--line-light-faint);
  }
  body.dark-active .map-container { border-color: var(--line-dark-faint); }

  /* PILL SWITCHERS */
  .btn-group {
    display: flex;
    gap: 6px;
    margin-bottom: 8px;
    flex-wrap: wrap;
  }
  .pill-btn {
    border: 1px solid var(--line-light);
    background: transparent;
    padding: 5px 11px;
    font-size: 11px;
    font-weight: 600;
    cursor: pointer;
    color: var(--text-light-mute);
    font-family: "IBM Plex Mono", monospace;
    transition: all 0.15s;
  }
  body.dark-active .pill-btn {
    border-color: var(--line-dark);
    color: var(--text-dark-mute);
  }
  .pill-btn.active, .pill-btn:hover {
    background: var(--accent-blue);
    color: #FFF;
    border-color: var(--accent-blue);
  }

  /* ANIMACIONES SVG PEDAGOGICAS */
  .svg-canvas {
    width: 100%;
    height: 100%;
    min-height: 200px;
  }
  
  @keyframes radarSweep {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
  @keyframes slideLag {
    0%, 100% { transform: translateX(0); }
    50% { transform: translateX(120px); }
  }
  @keyframes pulseGate {
    0%, 100% { opacity: 0.3; }
    50% { opacity: 1; }
  }
  @keyframes photonRed {
    0% { transform: translateY(-30px); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translateY(60px); opacity: 0; }
  }
  @keyframes photonNIR {
    0% { transform: translateY(-30px); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translate(50px, -40px); opacity: 0; }
  }

  /* HYPERFRAMES presenter step controls (injected per animated slide) */
  .hf-controls {
    display: flex;
    align-items: center;
    gap: 6px;
    flex-shrink: 0;
    font-family: "IBM Plex Mono", monospace;
  }
  .hf-controls .hf-label {
    font-size: 10px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-light-faint);
    margin-right: 2px;
  }
  body.dark-active .hf-controls .hf-label { color: var(--text-dark-faint); }
</style>
</head>
<body>

<!-- SIDEBAR -->
<div class="sidebar">
  <div class="sidebar-top">
    <button class="nav-icon-btn mono" id="tocBtn" title="Portada (Home)">01</button>
  </div>
  <div class="sidebar-bottom">
    <button class="theme-btn" id="themeToggle" title="Cambiar Tema (Claro / Oscuro)">🌓</button>
    <button class="theme-btn mono" id="fsBtn" title="Pantalla Completa (F)">⛶</button>
  </div>
</div>

<!-- FOOTER -->
<div class="slide-footer">
  <span class="slide-counter mono" id="slideNum">01 / 25</span>
  <button class="nav-btn" id="prevBtn">&larr; PREV</button>
  <button class="nav-btn" id="nextBtn">NEXT &rarr;</button>
</div>

<!-- DECK CONTAINER -->
<div class="deck">

  <!-- SLIDE 1: PORTADA -->
  <section class="slide active" data-title="Portada">
    <div class="slide-header">
      <span class="tag">Charla Magistral · Forecasting, Teledetección &amp; Modelos Globales</span>
      <h1 class="display slide-title">¿Puede la IA predecir el futuro?</h1>
      <p class="slide-subtitle">Lecciones de forecasting, teledetección multiespectral y cuantificación de incertidumbre en el mundo real.</p>
    </div>
    <div class="slide-body">
      <div class="split-55">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Tesis Central de la Conferencia</span>
            <span class="panel-badge">FILOSOFÍA APLICADA</span>
          </div>
          <div class="panel-content">
            <p style="font-size: 15px; line-height: 1.5; color: var(--text-light-mute);">
              La Inteligencia Artificial <strong>no es una bola de cristal mágica</strong>. Predecir no es adivinar con certeza absoluta, sino <strong>cuantificar matemáticamente la incertidumbre</strong> para habilitar decisiones estratégicas bajo riesgo controlado.
            </p>
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono">2,557</span>
                <span class="kpi-lbl">Días SENAMHI Punchana</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">6</span>
                <span class="kpi-lbl">Campañas Café Jaén</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">&plusmn;1.65&sigma;</span>
                <span class="kpi-lbl">Cono de Confianza (90%)</span>
              </div>
            </div>
            <div class="callout">
              <strong>Dos Casos Reales en Perú:</strong> 1) Pronóstico térmico en Iquitos con 5 niveles de modelo vs agencias globales (NOAA/ECMWF), y 2) Rendimiento cafetalero con Sentinel-2 y el fenómeno de saturación del NDVI.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Dinámica Temporal: El Cono de Incertidumbre</span>
            <span class="panel-badge">MECANISMO</span>
          </div>
          <div class="panel-content">
            <div class="chart-container">
              <svg class="svg-canvas" viewBox="0 0 450 220" preserveAspectRatio="xMidYMid meet">
                <!-- Ejes -->
                <line x1="40" y1="180" x2="420" y2="180" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
                <line x1="40" y1="20" x2="40" y2="180" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
                <!-- Línea presente t=0 -->
                <line x1="200" y1="20" x2="200" y2="180" stroke="var(--accent-amber)" stroke-width="1.5" stroke-dasharray="4,4" />
                <text x="200" y="15" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-amber)" text-anchor="middle">PRESENTE (t=0)</text>
                
                <!-- Histórico observado -->
                <path d="M 40,130 Q 80,90 120,120 T 200,105" fill="none" stroke="var(--accent-blue)" stroke-width="2.5" />
                <circle cx="200" cy="105" r="4" fill="var(--accent-blue)" />
                <text x="110" y="150" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-blue)" text-anchor="middle">Datos Observados</text>

                <!-- Cono de incertidumbre futuro -->
                <polygon points="200,105 400,40 400,170" fill="rgba(37,99,235,0.12)" />
                <!-- Líneas límite cono -->
                <line x1="200" y1="105" x2="400" y2="40" stroke="var(--accent-blue)" stroke-width="1" stroke-dasharray="3,3" />
                <line x1="200" y1="105" x2="400" y2="170" stroke="var(--accent-blue)" stroke-width="1" stroke-dasharray="3,3" />
                
                <!-- Trayectorias posibles simuladas -->
                <path d="M 200,105 Q 280,75 400,95" fill="none" stroke="var(--accent-emerald)" stroke-width="2" />
                <path d="M 200,105 Q 300,125 400,145" fill="none" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" stroke-dasharray="2,2" />
                <path d="M 200,105 Q 290,60 400,65" fill="none" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" stroke-dasharray="2,2" />

                <!-- Etiquetas de cono -->
                <text x="320" y="80" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-emerald)">Valor Esperado &mu;(t)</text>
                <text x="390" y="35" font-size="9" font-family="IBM Plex Mono" fill="var(--text-light-faint)" text-anchor="end">+1.645&sigma; (P95)</text>
                <text x="390" y="180" font-size="9" font-family="IBM Plex Mono" fill="var(--text-light-faint)" text-anchor="end">-1.645&sigma; (P5)</text>
              </svg>
            </div>
            <div class="callout success">
              <strong>Principio de Oro:</strong> A mayor horizonte temporal ($t+h$), la varianza del error crece inevitablemente. Nunca entregues un punto; entrega un intervalo de decisión.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: ANATOMIA DESDE CERO -->
  <section class="slide" data-title="Anatomía de una Serie">
    <div class="slide-header">
      <span class="tag">Fundamento Físico &amp; Matemático · Deconstrucción Ontológica</span>
      <h2 class="display slide-title">La Anatomía de una Serie Temporal</h2>
      <p class="slide-subtitle">Toda serie temporal Y(t) es el resultado de 4 componentes superpuestos. Antes de aplicar IA, debemos entender la física de su señal.</p>
    </div>
    <div class="slide-body">
      <div class="split-55">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Suma Constructiva de la Señal</span>
            <span class="panel-badge">MECANISMO PASO A PASO</span>
          </div>
          <div class="panel-content">
            <div class="btn-group" id="decompBtns">
              <button class="pill-btn active" onclick="setDecompLayer('all')">Ver Señal Completa</button>
              <button class="pill-btn" onclick="setDecompLayer('trend')">1. Tendencia T(t)</button>
              <button class="pill-btn" onclick="setDecompLayer('season')">2. Estacionalidad S(t)</button>
              <button class="pill-btn" onclick="setDecompLayer('cycle')">3. Ciclo C(t)</button>
              <button class="pill-btn" onclick="setDecompLayer('noise')">4. Ruido &epsilon;(t)</button>
            </div>
            <div class="chart-container">
              <svg id="decompSvg" class="svg-canvas" viewBox="0 0 500 240" preserveAspectRatio="xMidYMid meet">
                <!-- Eje base -->
                <line x1="30" y1="210" x2="470" y2="210" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
                <line x1="30" y1="20" x2="30" y2="210" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
                
                <!-- Capa 1: Tendencia (Azul) -->
                <path id="layerTrend" d="M 30,170 Q 250,140 470,80" fill="none" stroke="var(--accent-blue)" stroke-width="2.5" />
                
                <!-- Capa 2: Estacionalidad (Esmeralda) -->
                <path id="layerSeason" d="M 30,170 C 60,120 80,220 110,165 C 140,115 160,215 190,160 C 220,110 240,210 270,150 C 300,100 320,190 350,135 C 380,85 400,175 430,120 C 450,80 460,130 470,80" fill="none" stroke="var(--accent-emerald)" stroke-width="2" stroke-dasharray="3,3" />

                <!-- Capa 3: Ciclo (Púrpura) -->
                <path id="layerCycle" d="M 30,170 Q 150,100 270,160 T 470,80" fill="none" stroke="var(--accent-purple)" stroke-width="2" stroke-opacity="0.7" />

                <!-- Capa 4: Señal con Ruido (Caos Real) -->
                <path id="layerNoise" d="M 30,175 L 50,140 L 70,160 L 90,125 L 110,180 L 130,130 L 150,170 L 170,115 L 190,165 L 210,120 L 230,150 L 250,105 L 270,160 L 290,110 L 310,145 L 330,95 L 350,130 L 370,80 L 390,120 L 410,75 L 430,110 L 450,65 L 470,75" fill="none" stroke="var(--accent-amber)" stroke-width="1.8" />
              </svg>
            </div>
            <div class="callout">
              <strong>Ecuación Aditiva:</strong> <span class="mono">Y(t) = T(t) + S(t) + C(t) + &epsilon;(t)</span>. El objetivo del modelado es extraer patrones deterministas ($T, S, C$) y jamás intentar ajustar el ruido estocástico (&epsilon;).
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Los 4 Componentes en el Mundo Real</span>
            <span class="panel-badge">CASOS DE USO</span>
          </div>
          <div class="panel-content">
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-blue);"></span>
                <div>
                  <strong>Tendencia T(t) &mdash; Inercia de Largo Plazo:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Calentamiento global (+0.2 °C/década), envejecimiento y merma biológica de un cafetal de 10 años, o expansión demográfica urbana.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-emerald);"></span>
                <div>
                  <strong>Estacionalidad S(t) &mdash; Ciclos Calendario Rígidos:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">El ciclo circadiano día/noche (24h), la oscilación verano/invierno (365d), y la floración del café en Jaén (agosto a octubre).</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-purple);"></span>
                <div>
                  <strong>Ciclo C(t) &mdash; Oscilaciones Plurianuales Aperiódicas:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">El Fenómeno El Niño / La Niña (ENSO, recurrencia cada 3 a 7 años), ciclos macroeconómicos de tasas de interés y precios de commodities.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-amber);"></span>
                <div>
                  <strong>Ruido &epsilon;(t) &mdash; Innovaciones Estocásticas:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Turbulencia convectiva amazónica local, un aguacero repentino de 20 minutos, o fallas en el sensor óptico del satélite.</p>
                </div>
              </div>
            </div>
            <div class="callout alert">
              <strong>Error Fatal Típico:</strong> Sobrecargar una red neuronal con 50 capas para que memorize el ruido &epsilon;(t). El resultado es un sobreajuste masivo que colapsa en producción.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: EL GRAN MAPA 4 PARADIGMAS -->
  <section class="slide" data-title="Mapa de 4 Paradigmas">
    <div class="slide-header">
      <span class="tag">Taxonomía Completa · Espacio de Soluciones</span>
      <h2 class="display slide-title">El Gran Mapa de los 4 Paradigmas</h2>
      <p class="slide-subtitle">No existe una única "IA para el tiempo". Hay cuatro escuelas metodológicas con supuestos, costos y límites distintos.</p>
    </div>
    <div class="slide-body">
      <div class="grid-2x2">
        <!-- P1 -->
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">1. Curvas &amp; Descomposición Clásica</span>
            <span class="panel-badge">PARSIMONIA</span>
          </div>
          <div class="panel-content">
            <p style="font-size: 12.5px; color: var(--text-light-mute);">
              Estructura analítica explícita: modelos autorregresivos, suavizado de Holt-Winters, ARIMA, SARIMAX y GAM bayesiano (Prophet).
            </p>
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono" style="font-size: 16px;">1 - 7 Días</span>
                <span class="kpi-lbl">Horizonte Óptimo</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono" style="font-size: 16px;">0.05 s</span>
                <span class="kpi-lbl">Entrenamiento</span>
              </div>
            </div>
            <div class="callout success">
              <strong>Poder:</strong> Imbatibles con pocos datos (N &lt; 500) y alta estacionalidad.
            </div>
          </div>
        </div>

        <!-- P2 -->
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">2. ML Tabular &amp; Deep Learning</span>
            <span class="panel-badge">NO-LINEALIDAD</span>
          </div>
          <div class="panel-content">
            <p style="font-size: 12.5px; color: var(--text-light-mute);">
              El puente temporal: lags 1-14 en Random Forest / ExtraTrees / LightGBM, y redes secuenciales (LSTM, TFT, PatchTST).
            </p>
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono" style="font-size: 16px;">Tabular ML</span>
                <span class="kpi-lbl">Rey Industrial</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono" style="font-size: 16px;">Patología</span>
                <span class="kpi-lbl">No Extrapola</span>
              </div>
            </div>
            <div class="callout">
              <strong>Atención:</strong> Un árbol jamás predecirá un récord que no estuvo en el set de datos.
            </div>
          </div>
        </div>

        <!-- P3 -->
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">3. Biofísica Satelital &amp; Visión Agro</span>
            <span class="panel-badge">TELEDETECCIÓN</span>
          </div>
          <div class="panel-content">
            <p style="font-size: 12.5px; color: var(--text-light-mute);">
              Fusión del espectro electromagnético (Sentinel-2 L2A: NDVI, EVI, NDRE) con ventanas fenológicas y visión local (YOLOv12, SAM 2.1).
            </p>
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono" style="font-size: 16px;">786 km</span>
                <span class="kpi-lbl">Órbita Espacial</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono" style="font-size: 16px;">Fenología</span>
                <span class="kpi-lbl">3 Fases Café</span>
              </div>
            </div>
            <div class="callout success">
              <strong>Descubrimiento:</strong> El NDVI se satura en dosel denso (LAI > 3); EVI y NDRE rescatan la señal.
            </div>
          </div>
        </div>

        <!-- P4 -->
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">4. Modelos Físicos Globales &amp; Zero-Shot</span>
            <span class="panel-badge">FRONTERA 2024-2026</span>
          </div>
          <div class="panel-content">
            <p style="font-size: 12.5px; color: var(--text-light-mute);">
              Supercómputo numérico Navier-Stokes (NOAA GFS, ECMWF IFS) junto a la disrupción de GraphCast (DeepMind) y TimesFM / Chronos.
            </p>
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono" style="font-size: 16px;">&Delta; 7.6 &deg;C</span>
                <span class="kpi-lbl">Discrepancia Iquitos</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono" style="font-size: 16px;">60 s</span>
                <span class="kpi-lbl">GraphCast GPU</span>
              </div>
            </div>
            <div class="callout alert">
              <strong>Realidad:</strong> Incluso los supercomputadores mundiales discrepan 8 °C entre sí.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: PARADIGMA 1 - CURVAS PARAMETRICAS -->
  <section class="slide" data-title="P1: Curvas Paramétricas">
    <div class="slide-header">
      <span class="tag">Paradigma 1 · Crecimiento Físico &amp; Inercia</span>
      <h2 class="display slide-title">Curvas Paramétricas y Suavizado Exponencial</h2>
      <p class="slide-subtitle">Cuando los recursos son finitos, la naturaleza impone techos. Exponencial vs saturación logística y la memoria de Holt-Winters.</p>
    </div>
    <div class="slide-body">
      <div class="split-50">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Simulación: Exponencial vs Logística</span>
            <span class="panel-badge">DINÁMICA BIOLÓGICA</span>
          </div>
          <div class="panel-content">
            <div class="chart-container">
              <svg class="svg-canvas" viewBox="0 0 460 220" preserveAspectRatio="xMidYMid meet">
                <!-- Ejes -->
                <line x1="40" y1="190" x2="430" y2="190" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
                <line x1="40" y1="20" x2="40" y2="190" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
                
                <!-- Techo Asintótico Capacidad L -->
                <line x1="40" y1="65" x2="430" y2="65" stroke="var(--accent-red)" stroke-dasharray="4,4" stroke-width="1.5" />
                <text x="420" y="55" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-red)" text-anchor="end">Capacidad de Carga L (Techo Físico)</text>

                <!-- Curva Lineal (Gris) -->
                <line x1="40" y1="180" x2="420" y2="110" stroke="var(--text-light-faint)" stroke-width="1.5" />
                <text x="420" y="125" font-size="10" font-family="IBM Plex Mono" fill="var(--text-light-faint)" text-anchor="end">Lineal (y = mx + b)</text>

                <!-- Curva Exponencial (Rojo punteado) -->
                <path d="M 40,185 Q 260,180 340,30" fill="none" stroke="var(--accent-red)" stroke-width="2.5" stroke-dasharray="4,2" />
                <text x="280" y="45" font-size="11" font-family="IBM Plex Mono" fill="var(--accent-red)" font-weight="700">Exponencial (e^rt)</text>

                <!-- Curva Logística (Esmeralda) -->
                <path d="M 40,185 C 160,185 200,70 420,68" fill="none" stroke="var(--accent-emerald)" stroke-width="3" />
                <text x="320" y="85" font-size="11" font-family="IBM Plex Mono" fill="var(--accent-emerald)" font-weight="700">Logística Sigmoide</text>
                
                <!-- Punto de Inflexión -->
                <circle cx="180" cy="125" r="4" fill="var(--accent-emerald)" />
                <text x="185" y="140" font-size="9" font-family="IBM Plex Mono" fill="var(--text-light-mute)">Inflexión (L/2)</text>
              </svg>
            </div>
            <div class="callout success">
              <strong>Fórmula Logística:</strong> <span class="mono">y(t) = L / (1 + e^(-k(t - t0)))</span>. Modela desde el crecimiento de biomasa foliar hasta la adopción de nuevas tecnologías.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Suavizado Exponencial de Holt-Winters</span>
            <span class="panel-badge">INERCIA TEMPORAL</span>
          </div>
          <div class="panel-content">
            <p style="font-size: 13px; color: var(--text-light-mute); line-height: 1.45;">
              Asigna ponderaciones que decaen geométricamente con la antigüedad: lo ocurrido ayer tiene más peso que lo de hace un mes.
            </p>
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono">50k SKUs</span>
                <span class="kpi-lbl">Escala por Segundo</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">&alpha;, &beta;, &gamma;</span>
                <span class="kpi-lbl">Ponderaciones [0, 1]</span>
              </div>
            </div>
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-blue);"></span>
                <div>
                  <strong>Nivel (&alpha;):</strong> <span class="mono">L_t = &alpha;&middot;y_t + (1 - &alpha;)&middot;(L_{t-1} + b_{t-1})</span>
                  <p style="font-size: 11px; color: var(--text-light-faint);">Filtra el choque instantáneo y estabiliza la base.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-emerald);"></span>
                <div>
                  <strong>Tendencia (&beta;):</strong> <span class="mono">b_t = &beta;&middot;(L_t - L_{t-1}) + (1 - &beta;)&middot;b_{t-1}</span>
                  <p style="font-size: 11px; color: var(--text-light-faint);">Captura si la pendiente general va al alza o a la baja.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-purple);"></span>
                <div>
                  <strong>Estacionalidad (&gamma;):</strong> <span class="mono">s_t = &gamma;&middot;(y_t - L_t) + (1 - &gamma;)&middot;s_{t-m}</span>
                  <p style="font-size: 11px; color: var(--text-light-faint);">Ajusta el ciclo estacional de periodo m (ej. 365 días).</p>
                </div>
              </div>
            </div>
            <div class="callout">
              <strong>Ventaja Operativa:</strong> Computacionalmente ultrarrápido. Permite pronosticar 50,000 SKUs o sensores en menos de 2 segundos en CPU.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: PARADIGMA 1 - ARIMA Y PROPHET -->
  <section class="slide" data-title="P1: Descomposición Estadística">
    <div class="slide-header">
      <span class="tag">Paradigma 1 · Modelos Clásicos</span>
      <h2 class="display slide-title">ARIMA, SARIMAX y Prophet</h2>
      <p class="slide-subtitle">La visión estocástica: procesos generativos autorregresivos vs piezas de lego aditivas bayesianas.</p>
    </div>
    <div class="slide-body">
      <div class="split-50">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Anatomía de ARIMA(p, d, q)</span>
            <span class="panel-badge">AUTORREGRESIÓN &amp; RUIDO</span>
          </div>
          <div class="panel-content">
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono">p</span>
                <span class="kpi-lbl">Lags Autorregresivos (AR)</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">d</span>
                <span class="kpi-lbl">Orden Diferenciación (I)</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">q</span>
                <span class="kpi-lbl">Choques Medias Móviles (MA)</span>
              </div>
            </div>
            <div style="background: var(--bg-light-sub); padding: 12px; border: 1px solid var(--line-light-faint); font-family: 'IBM Plex Mono'; font-size: 12px; line-height: 1.5;">
              (1 - &sum; &phi;_i B^i) (1 - B)^d Y_t = c + (1 + &sum; &theta;_j B^j) &epsilon;_t
            </div>
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet"></span>
                <span><strong>Estacionariedad Obligatoria:</strong> Si la media o varianza cambian en el tiempo, la prueba Dickey-Fuller falla y el modelo colapsa.</span>
              </div>
              <div class="feature-item">
                <span class="feature-bullet"></span>
                <span><strong>Horizonte Corto:</strong> A partir de $t+3$ días, la predicción converge asintóticamente a la media histórica incondicional.</span>
              </div>
            </div>
            <div class="callout success">
              <strong>Benchmark SENAMHI Iquitos:</strong> ARIMA(2,1,1) logró RMSE 2.121 °C en holdout de 90 días, superando a Random Forest.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Prophet (Meta) &mdash; Piezas de Lego</span>
            <span class="panel-badge">GAM BAYESIANO</span>
          </div>
          <div class="panel-content">
            <p style="font-size: 13px; color: var(--text-light-mute);">
              En lugar de autorregresión pura, descompone la serie en curvas independientes mediante un Modelo Aditivo Generalizado (GAM):
            </p>
            <div style="background: var(--bg-light-sub); padding: 12px; border: 1px solid var(--line-light-faint); font-family: 'IBM Plex Mono'; font-size: 12px; line-height: 1.5;">
              y(t) = g(t) [Tendencia] + s(t) [Estacionalidad] + h(t) [Feriados] + &epsilon;_t
            </div>
            <table class="data-table">
              <thead>
                <tr>
                  <th>Criterio</th>
                  <th>ARIMA / SARIMAX</th>
                  <th>Prophet (Meta)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Tolerancia a Huecos</strong></td>
                  <td>Cero (requiere imputar)</td>
                  <td>Alta (ignora NaNs)</td>
                </tr>
                <tr>
                  <td><strong>Puntos de Cambio</strong></td>
                  <td>Manual o no lineal</td>
                  <td>Automático (Changepoints)</td>
                </tr>
                <tr>
                  <td><strong>Interpretabilidad</strong></td>
                  <td>Alta (parámetros &phi;, &theta;)</td>
                  <td>Máxima para negocios</td>
                </tr>
              </tbody>
            </table>
            <div class="callout alert">
              <strong>Límite:</strong> Falla cuando existen relaciones físicas cruzadas complejas (ej. lluvia modulada por viento y presión simultánea).
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: PARADIGMA 2 - PUENTE TABULAR -->
  <section class="slide" data-title="P2: El Puente Tabular">
    <div class="slide-header">
      <span class="tag">Paradigma 2 · Machine Learning Tabular</span>
      <h2 class="display slide-title">El Puente Tabular: ¿Cómo meter tiempo en un Bosque?</h2>
      <p class="slide-subtitle">Los árboles de decisión no tienen noción de secuencia temporal. Creamos una matriz supervisada respetando la flecha del tiempo.</p>
    </div>
    <div class="slide-body">
      <div class="split-55">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Mecanismo: Ventana Deslizante (Sliding Window)</span>
            <span class="panel-badge">FEATURE ENGINEERING</span>
          </div>
          <div class="panel-content">
            <div class="chart-container">
              <svg class="svg-canvas" viewBox="0 0 480 210" preserveAspectRatio="xMidYMid meet">
                <!-- Eje temporal con onda (base) -->
                <path d="M 30,52 q 20,-18 40,0 t 40,0 t 40,0 t 40,0 t 40,0 t 40,0 t 40,0 t 40,0 t 40,0" fill="none" stroke="currentColor" stroke-opacity="0.35" stroke-width="1.5" />
                <circle cx="330" cy="52" r="6" fill="var(--accent-blue)" />
                <text x="330" y="36" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-blue)" font-weight="700" text-anchor="middle">t (hoy)</text>
                <circle cx="410" cy="52" r="6" fill="var(--accent-emerald)" />
                <text x="410" y="36" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-emerald)" font-weight="700" text-anchor="middle">t+1 ★</text>

                <!-- PASO 1: ventana que congela el pasado en una fila -->
                <g data-hf-step="1">
                  <rect x="150" y="20" width="180" height="66" fill="rgba(37,99,235,0.07)" stroke="var(--accent-blue)" stroke-width="2" stroke-dasharray="5,3" />
                  <text x="240" y="78" font-size="9" font-family="IBM Plex Mono" fill="var(--accent-blue)" text-anchor="middle">ventana W = 14 días</text>
                  <circle cx="142" cy="30" r="9" fill="var(--bg-light-panel)" stroke="var(--accent-blue)" stroke-width="2" />
                  <text x="142" y="26" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-blue)" font-weight="700" text-anchor="middle">1</text>
                  <g transform="translate(70, 108)">
                    <text x="-8" y="20" font-size="9" font-family="IBM Plex Mono" text-anchor="end">fila t</text>
                    <rect x="0" y="0" width="62" height="30" fill="var(--bg-light-sub)" stroke="var(--line-light)" />
                    <text x="31" y="19" font-size="10" font-family="IBM Plex Mono" text-anchor="middle">lag_14</text>
                    <rect x="66" y="0" width="62" height="30" fill="var(--bg-light-sub)" stroke="var(--line-light)" />
                    <text x="97" y="19" font-size="10" font-family="IBM Plex Mono" text-anchor="middle">lag_7</text>
                    <rect x="132" y="0" width="62" height="30" fill="var(--bg-light-sub)" stroke="var(--line-light)" />
                    <text x="163" y="19" font-size="10" font-family="IBM Plex Mono" text-anchor="middle">lag_1</text>
                    <rect x="198" y="0" width="72" height="30" fill="var(--bg-light-sub)" stroke="var(--line-light)" />
                    <text x="234" y="19" font-size="10" font-family="IBM Plex Mono" text-anchor="middle">media_7</text>
                    <rect x="274" y="0" width="66" height="30" fill="rgba(5,150,105,0.15)" stroke="var(--accent-emerald)" stroke-width="1.5" />
                    <text x="307" y="19" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-emerald)" font-weight="700" text-anchor="middle">Y&#8348;</text>
                  </g>
                </g>

                <!-- PASO 2: la ventana se desliza +1 y nace la fila t+1 -->
                <g data-hf-step="2">
                  <rect x="190" y="20" width="180" height="66" fill="none" stroke="var(--accent-amber)" stroke-width="1.5" stroke-dasharray="2,3" />
                  <path d="M 165,96 L 200,96" stroke="var(--accent-amber)" stroke-width="2" />
                  <polygon points="200,91 210,96 200,101" fill="var(--accent-amber)" />
                  <text x="182" y="90" font-size="8.5" font-family="IBM Plex Mono" fill="var(--accent-amber)" text-anchor="middle">+1 día</text>
                  <circle cx="378" cy="30" r="9" fill="var(--bg-light-panel)" stroke="var(--accent-emerald)" stroke-width="2" />
                  <text x="378" y="26" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-emerald)" font-weight="700" text-anchor="middle">2</text>
                  <g transform="translate(70, 148)">
                    <text x="-8" y="20" font-size="9" font-family="IBM Plex Mono" text-anchor="end">fila t+1</text>
                    <rect x="0" y="0" width="62" height="30" fill="var(--bg-light-sub)" stroke="var(--line-light)" stroke-dasharray="2,2" />
                    <text x="31" y="19" font-size="10" font-family="IBM Plex Mono" text-anchor="middle">lag_14</text>
                    <rect x="66" y="0" width="62" height="30" fill="var(--bg-light-sub)" stroke="var(--line-light)" stroke-dasharray="2,2" />
                    <text x="97" y="19" font-size="10" font-family="IBM Plex Mono" text-anchor="middle">lag_7</text>
                    <rect x="132" y="0" width="62" height="30" fill="var(--bg-light-sub)" stroke="var(--line-light)" stroke-dasharray="2,2" />
                    <text x="163" y="19" font-size="10" font-family="IBM Plex Mono" text-anchor="middle">lag_1</text>
                    <rect x="198" y="0" width="72" height="30" fill="var(--bg-light-sub)" stroke="var(--line-light)" stroke-dasharray="2,2" />
                    <text x="234" y="19" font-size="10" font-family="IBM Plex Mono" text-anchor="middle">media_7</text>
                    <rect x="274" y="0" width="66" height="30" fill="none" stroke="var(--accent-emerald)" stroke-width="1.5" stroke-dasharray="2,2" />
                    <text x="307" y="19" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-emerald)" font-weight="700" text-anchor="middle">?</text>
                  </g>
                  <text x="240" y="202" font-size="9" font-family="IBM Plex Mono" text-anchor="middle">cada día = una fila · el árbol nunca ve el calendario</text>
                </g>
              </svg>
            </div>
            <div class="callout success">
              <strong>El Truco:</strong> Cada fila de la matriz supervisada es un instante en el tiempo. El árbol entrena con relaciones estáticas entre columnas sin saber qué orden tenían en el calendario.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Ingeniería de Características Crítica</span>
            <span class="panel-badge">MATRIZ DE FEATURES</span>
          </div>
          <div class="panel-content">
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet"></span>
                <div>
                  <strong>Lags Puros (t-1, t-2, t-7, t-14):</strong> Capturan la autocorrelación inmediata y el ciclo semanal.
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet"></span>
                <div>
                  <strong>Estadísticas Rodantes (Rolling Mean/Std):</strong> Señal suavizada que reduce el ruido térmico diario.
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet"></span>
                <div>
                  <strong>Codificación Cíclica (Seno / Coseno):</strong>
                  <div class="mono" style="font-size: 11px; margin-top: 3px;">sin_d = sin(2&pi;&middot;dia/365) &nbsp;|&nbsp; cos_d = cos(2&pi;&middot;dia/365)</div>
                  <p style="font-size: 11px; color: var(--text-light-faint); margin-top: 2px;">Enseña al árbol que el 31 de diciembre está pegado al 1 de enero.</p>
                </div>
              </div>
            </div>
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono">14</span>
                <span class="kpi-lbl">Lags Históricos</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">365 d</span>
                <span class="kpi-lbl">Ciclo Anual Causal</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">0.25 s</span>
                <span class="kpi-lbl">Tiempo Entrenamiento</span>
              </div>
            </div>
            <table class="data-table">
              <thead>
                <tr>
                  <th>Algoritmo</th>
                  <th>Mecanismo Split</th>
                  <th>RMSE Holdout Iquitos</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>ExtraTrees</strong></td>
                  <td>Umbrales aleatorios</td>
                  <td><strong>2.166 &deg;C</strong> (Filtra ruido)</td>
                </tr>
                <tr>
                  <td><strong>Random Forest</strong></td>
                  <td>Mejor corte estocástico</td>
                  <td>2.247 &deg;C</td>
                </tr>
                <tr>
                  <td><strong>XGBoost</strong></td>
                  <td>Gradiente en residuos</td>
                  <td>2.215 &deg;C</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: PARADIGMA 2 - PATOLOGIA NO EXTRAPOLACION -->
  <section class="slide" data-title="P2: Patología de los Árboles">
    <div class="slide-header">
      <span class="tag">Paradigma 2 · Limitación Fatal del ML Tabular</span>
      <h2 class="display slide-title">La Patología de No-Extrapolación</h2>
      <p class="slide-subtitle">Un árbol de decisión no puede predecir un valor fuera del rango histórico con el que fue entrenado.</p>
    </div>
    <div class="slide-body">
      <div class="split-55">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Demostración Gráfica: El Colapso en Meseta</span>
            <span class="panel-badge">FALLA ESTRUCTURAL</span>
          </div>
          <div class="panel-content">
            <div class="chart-container">
              <svg class="svg-canvas" viewBox="0 0 480 220" preserveAspectRatio="xMidYMid meet">
                <!-- Ejes -->
                <line x1="40" y1="190" x2="450" y2="190" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
                <line x1="40" y1="20" x2="40" y2="190" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />

                <!-- PASO 1: lo conocido (zona train + historia + techo) -->
                <g data-hf-step="1">
                  <rect x="40" y="20" width="200" height="170" fill="rgba(37,99,235,0.06)" />
                  <text x="140" y="35" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-blue)" text-anchor="middle">① train: T ≤ 35 °C</text>
                  <path d="M 40,160 Q 100,120 160,130 T 240,92" fill="none" stroke="var(--accent-blue)" stroke-width="2.5" />
                  <line x1="40" y1="90" x2="450" y2="90" stroke="var(--accent-red)" stroke-dasharray="3,3" stroke-width="1.5" />
                  <text x="440" y="82" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-red)" text-anchor="end">techo visto: 35 °C</text>
                </g>

                <!-- PASO 2: el futuro rompe el récord + la lineal lo sigue -->
                <g data-hf-step="2">
                  <path d="M 240,92 Q 320,50 440,35" fill="none" stroke="currentColor" stroke-opacity="0.5" stroke-width="2" stroke-dasharray="3,3" />
                  <text x="440" y="25" font-size="10" font-family="IBM Plex Mono" fill="currentColor" text-anchor="end">② realidad: ola de 39 °C</text>
                  <line x1="240" y1="92" x2="440" y2="48" stroke="var(--accent-emerald)" stroke-width="2.5" />
                  <text x="440" y="62" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-emerald)" text-anchor="end">lineal: y = mx+b (extrapola)</text>
                </g>

                <!-- PASO 3: el árbol se estrella contra su techo + gap -->
                <g data-hf-step="3">
                  <line x1="240" y1="92" x2="440" y2="92" stroke="var(--accent-red)" stroke-width="3.5" />
                  <rect x="270" y="86" width="12" height="12" fill="rgba(220,38,38,0.25)" stroke="var(--accent-red)" />
                  <rect x="310" y="86" width="12" height="12" fill="rgba(220,38,38,0.25)" stroke="var(--accent-red)" />
                  <rect x="350" y="86" width="12" height="12" fill="rgba(220,38,38,0.25)" stroke="var(--accent-red)" />
                  <rect x="390" y="86" width="12" height="12" fill="rgba(220,38,38,0.25)" stroke="var(--accent-red)" />
                  <text x="340" y="114" font-size="11" font-family="IBM Plex Mono" fill="var(--accent-red)" font-weight="700" text-anchor="middle">③ árbol: MESETA 35.0 °C (hoja terminal)</text>
                  <line x1="452" y1="35" x2="452" y2="92" stroke="var(--accent-amber)" stroke-width="2" />
                  <polygon points="447,35 457,35 452,43" fill="var(--accent-amber)" />
                  <polygon points="447,92 457,92 452,84" fill="var(--accent-amber)" />
                  <text x="468" y="66" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-amber)" font-weight="700" text-anchor="middle" transform="rotate(-90, 468, 66)">Δ = 4.0 °C</text>
                </g>
              </svg>
            </div>
            <div class="callout alert">
              <strong>Por qué ocurre matemáticamente:</strong> Un árbol corta el espacio en hiperrectángulos ortogonales. Cualquier dato fuera del espacio conocido cae en la última hoja terminal y recibe la media de esa hoja.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Consecuencias Operativas &amp; Soluciones</span>
            <span class="panel-badge">INGENIERÍA ROBUSTA</span>
          </div>
          <div class="panel-content">
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-red);"></span>
                <div>
                  <strong>Casos Fatales en Producción:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Olas de calor por cambio climático, hiperinflación económica, o el despegue de ventas de una startup. El árbol predecirá estancamiento total.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-emerald);"></span>
                <div>
                  <strong>Solución 1 &mdash; Diferenciar la Serie (&Delta;Y):</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Entrenar el árbol para predecir el cambio diario: <span class="mono">&Delta;Y_t = Y_t - Y_{t-1}</span>. La tendencia se acumula por sumas sucesivas.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-blue);"></span>
                <div>
                  <strong>Solución 2 &mdash; Ensamble Híbrido:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Usar una regresión lineal o spline para la tendencia de fondo y el Random Forest para modular los residuos no lineales estacionales.</p>
                </div>
              </div>
            </div>
            <div class="callout">
              <strong>Regla de Oro:</strong> Nunca uses Gradient Boosting puro sobre series con tendencia determinista sin antes desestacionalizar o diferenciar.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: PARADIGMA 2 - DEEP LEARNING LSTM VS PATCHTST -->
  <section class="slide" data-title="P2: Deep Learning Secuencial">
    <div class="slide-header">
      <span class="tag">Paradigma 2 · Redes Recurrentes &amp; Transformers</span>
      <h2 class="display slide-title">Deep Learning Secuencial: LSTM vs PatchTST</h2>
      <p class="slide-subtitle">De compuertas de olvido recurrentes punto a punto (1997) a parches de auto-atención en paralelo (Nie et al., ICLR 2023).</p>
    </div>
    <div class="slide-body">
      <div class="split-50">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Celda Recurrente LSTM &mdash; Memoria Secuencial</span>
            <span class="panel-badge">RECURRENCIA</span>
          </div>
          <div class="panel-content">
            <div class="chart-container">
              <svg class="svg-canvas" viewBox="0 0 420 200" preserveAspectRatio="xMidYMid meet">
                <!-- Cinta de memoria C: la autopista horizontal (base siempre visible) -->
                <line x1="10" y1="46" x2="396" y2="46" stroke="var(--accent-purple)" stroke-width="3" />
                <polygon points="396,40 408,46 396,52" fill="var(--accent-purple)" />
                <text x="12" y="34" font-size="9.5" font-family="IBM Plex Mono" fill="var(--accent-purple)" font-weight="700">C&#8348;&#8331;&#8321; entra</text>
                <text x="394" y="34" font-size="9.5" font-family="IBM Plex Mono" fill="var(--accent-purple)" font-weight="700" text-anchor="end">C&#8348; sale</text>
                <text x="210" y="20" font-size="9" font-family="IBM Plex Mono" fill="var(--text-light-faint)" text-anchor="middle">cinta de memoria: fluye casi intacta</text>
                <!-- Entradas h,y desde abajo (base) -->
                <line x1="70" y1="196" x2="70" y2="150" stroke="currentColor" stroke-opacity="0.45" stroke-width="1.5" />
                <text x="70" y="192" font-size="8.5" font-family="IBM Plex Mono" text-anchor="middle">h&#8348;&#8331;&#8321;</text>
                <line x1="150" y1="196" x2="150" y2="150" stroke="currentColor" stroke-opacity="0.45" stroke-width="1.5" />
                <text x="150" y="192" font-size="8.5" font-family="IBM Plex Mono" text-anchor="middle">x&#8348;</text>
                <text x="110" y="168" font-size="8.5" font-family="IBM Plex Mono" fill="var(--text-light-faint)" text-anchor="middle">se concatenan [h, x]</text>

                <!-- PASO 1: compuerta de olvido f -->
                <g data-hf-step="1">
                  <rect x="48" y="108" width="150" height="34" fill="rgba(220,38,38,0.08)" stroke="var(--accent-red)" stroke-width="1.5" />
                  <text x="123" y="122" font-size="9.5" font-family="IBM Plex Mono" fill="var(--accent-red)" font-weight="700" text-anchor="middle">f&#8348; = &#963;(W&#183;[h,x]+b)</text>
                  <text x="123" y="134" font-size="8.5" font-family="IBM Plex Mono" text-anchor="middle">olvida: 0=borra · 1=conserva</text>
                  <circle cx="42" cy="100" r="9" fill="var(--bg-light-panel)" stroke="var(--accent-red)" stroke-width="2" />
                  <text x="42" y="96" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-red)" font-weight="700" text-anchor="middle">1</text>
                  <line x1="123" y1="108" x2="123" y2="60" stroke="var(--accent-red)" stroke-width="1.5" stroke-dasharray="3,2" />
                  <circle cx="123" cy="46" r="10" fill="var(--bg-light-panel)" stroke="var(--accent-purple)" stroke-width="2" />
                  <text x="123" y="50" font-size="12" text-anchor="middle">&#215;</text>
                  <text x="140" y="72" font-size="8.5" font-family="IBM Plex Mono" fill="var(--accent-red)">filtra C&#8348;&#8331;&#8321;</text>
                </g>

                <!-- PASO 2: compuerta de entrada i + salida o -->
                <g data-hf-step="2">
                  <rect x="222" y="108" width="150" height="34" fill="rgba(5,150,105,0.08)" stroke="var(--accent-emerald)" stroke-width="1.5" />
                  <text x="297" y="122" font-size="9.5" font-family="IBM Plex Mono" fill="var(--accent-emerald)" font-weight="700" text-anchor="middle">i&#8348; = &#963;(·) · tanh(C&#771;)</text>
                  <text x="297" y="134" font-size="8.5" font-family="IBM Plex Mono" text-anchor="middle">escribe lo nuevo</text>
                  <circle cx="216" cy="100" r="9" fill="var(--bg-light-panel)" stroke="var(--accent-emerald)" stroke-width="2" />
                  <text x="216" y="96" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-emerald)" font-weight="700" text-anchor="middle">2</text>
                  <line x1="272" y1="108" x2="272" y2="60" stroke="var(--accent-emerald)" stroke-width="1.5" stroke-dasharray="3,2" />
                  <circle cx="272" cy="46" r="10" fill="var(--bg-light-panel)" stroke="var(--accent-purple)" stroke-width="2" />
                  <text x="272" y="50" font-size="12" text-anchor="middle">&#215;</text>
                  <circle cx="340" cy="46" r="10" fill="var(--bg-light-panel)" stroke="var(--accent-purple)" stroke-width="2" />
                  <text x="340" y="50" font-size="12" text-anchor="middle">+</text>
                  <text x="340" y="72" font-size="8.5" font-family="IBM Plex Mono" fill="var(--accent-purple)" text-anchor="middle">suma C&#8348;</text>
                  <text x="297" y="158" font-size="8.5" font-family="IBM Plex Mono" fill="var(--accent-blue)" text-anchor="middle">h&#8348; = o&#8348; · tanh(C&#8348;) → salida</text>
                </g>
              </svg>
            </div>
            <div class="callout">
              <strong>Mito Superado:</strong> Las LSTM procesan paso a paso ($O(N)$), lo que impide paralelizar en GPU y sufre de desvanecimiento de gradiente en secuencias de más de 100 pasos.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">PatchTST &mdash; Parches &amp; Auto-Atención</span>
            <span class="panel-badge">ESTADO DEL ARTE (ICLR 2023)</span>
          </div>
          <div class="panel-content">
            <div class="chart-container">
              <svg class="svg-canvas" viewBox="0 0 420 200" preserveAspectRatio="xMidYMid meet">
                <!-- Serie cruda (base): onda diaria ruidosa -->
                <path d="M 10,34 q 12,-14 24,0 t 24,0 t 24,0 t 24,0 t 24,0 t 24,0 t 24,0 t 24,0 t 24,0 t 24,0 t 24,0 t 24,0 t 24,0 t 24,0 t 24,0 t 24,0" fill="none" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
                <text x="10" y="14" font-size="9" font-family="IBM Plex Mono" fill="var(--text-light-faint)">serie diaria (N = 336 puntos)</text>
                <!-- Tijeras de corte (base) -->
                <line x1="112" y1="8" x2="112" y2="48" stroke="var(--accent-amber)" stroke-width="1.5" stroke-dasharray="3,2" />
                <line x1="214" y1="8" x2="214" y2="48" stroke="var(--accent-amber)" stroke-width="1.5" stroke-dasharray="3,2" />
                <line x1="316" y1="8" x2="316" y2="48" stroke="var(--accent-amber)" stroke-width="1.5" stroke-dasharray="3,2" />

                <!-- PASO 1: parches = tokens con embedding -->
                <g data-hf-step="1">
                  <rect x="12" y="62" width="92" height="52" fill="rgba(37,99,235,0.10)" stroke="var(--accent-blue)" stroke-width="1.5" />
                  <rect x="112" y="62" width="92" height="52" fill="rgba(5,150,105,0.10)" stroke="var(--accent-emerald)" stroke-width="1.5" />
                  <rect x="212" y="62" width="92" height="52" fill="rgba(217,119,6,0.10)" stroke="var(--accent-amber)" stroke-width="1.5" />
                  <rect x="312" y="62" width="92" height="52" fill="rgba(124,58,237,0.10)" stroke="var(--accent-purple)" stroke-width="1.5" />
                  <text x="58" y="80" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-blue)" font-weight="700" text-anchor="middle">P1</text>
                  <text x="158" y="80" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-emerald)" font-weight="700" text-anchor="middle">P2</text>
                  <text x="258" y="80" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-amber)" font-weight="700" text-anchor="middle">P3</text>
                  <text x="358" y="80" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-purple)" font-weight="700" text-anchor="middle">P4</text>
                  <!-- barras de embedding -->
                  <line x1="34" y1="106" x2="34" y2="92" stroke="var(--accent-blue)" stroke-width="4" />
                  <line x1="46" y1="106" x2="46" y2="98" stroke="var(--accent-blue)" stroke-width="4" />
                  <line x1="58" y1="106" x2="58" y2="88" stroke="var(--accent-blue)" stroke-width="4" />
                  <line x1="70" y1="106" x2="70" y2="96" stroke="var(--accent-blue)" stroke-width="4" />
                  <line x1="134" y1="106" x2="134" y2="94" stroke="var(--accent-emerald)" stroke-width="4" />
                  <line x1="146" y1="106" x2="146" y2="86" stroke="var(--accent-emerald)" stroke-width="4" />
                  <line x1="158" y1="106" x2="158" y2="98" stroke="var(--accent-emerald)" stroke-width="4" />
                  <line x1="170" y1="106" x2="170" y2="90" stroke="var(--accent-emerald)" stroke-width="4" />
                  <line x1="234" y1="106" x2="234" y2="96" stroke="var(--accent-amber)" stroke-width="4" />
                  <line x1="246" y1="106" x2="246" y2="90" stroke="var(--accent-amber)" stroke-width="4" />
                  <line x1="258" y1="106" x2="258" y2="100" stroke="var(--accent-amber)" stroke-width="4" />
                  <line x1="270" y1="106" x2="270" y2="94" stroke="var(--accent-amber)" stroke-width="4" />
                  <line x1="334" y1="106" x2="334" y2="88" stroke="var(--accent-purple)" stroke-width="4" />
                  <line x1="346" y1="106" x2="346" y2="96" stroke="var(--accent-purple)" stroke-width="4" />
                  <line x1="358" y1="106" x2="358" y2="92" stroke="var(--accent-purple)" stroke-width="4" />
                  <line x1="370" y1="106" x2="370" y2="100" stroke="var(--accent-purple)" stroke-width="4" />
                  <text x="210" y="128" font-size="9" font-family="IBM Plex Mono" text-anchor="middle">4 tokens × 16 días (proyección lineal del parche)</text>
                </g>

                <!-- PASO 2: atención cruzada entre parches -->
                <g data-hf-step="2">
                  <path d="M 58,132 C 58,178 358,178 358,132" fill="none" stroke="var(--accent-blue)" stroke-width="2" />
                  <polygon points="352,124 364,132 352,140" fill="var(--accent-blue)" />
                  <path d="M 158,132 C 158,158 258,158 258,132" fill="none" stroke="var(--accent-emerald)" stroke-width="2" />
                  <polygon points="252,124 264,132 252,140" fill="var(--accent-emerald)" />
                  <text x="210" y="192" font-size="9.5" font-family="IBM Plex Mono" fill="var(--accent-blue)" text-anchor="middle">softmax(QK&#7488;/&#8730;d): P1 atiende a P4 · O(P&#178;), P&#8810;N</text>
                </g>
              </svg>
            </div>
            <div class="callout success">
              <strong>Ventaja Revolucionaria:</strong> Al agrupar días en parches (tokens), retiene la información semántica local y reduce la complejidad de atención 16 veces.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: PARADIGMA 2 - CUANDO USAR DL -->
  <section class="slide" data-title="P2: Mito de la Serie Única">
    <div class="slide-header">
      <span class="tag">Paradigma 2 · Análisis Crítico de Costo / Beneficio</span>
      <h2 class="display slide-title">El Mito del Deep Learning en una Sola Serie</h2>
      <p class="slide-subtitle">Entrenar una red neuronal gigante sobre una sola estación meteorológica suele ser un desperdicio injustificado de cómputo.</p>
    </div>
    <div class="slide-body">
      <div class="split-50">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Trade-off Empírico: Datos vs Arquitectura</span>
            <span class="panel-badge">AUDITORÍA</span>
          </div>
          <div class="panel-content">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Modelo</th>
                  <th>Tiempo CPU</th>
                  <th>RMSE Holdout</th>
                  <th>Complejidad Operativa</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Naive Estacional</strong></td>
                  <td>0.001 s</td>
                  <td>2.315 &deg;C</td>
                  <td>Línea base cero costo</td>
                </tr>
                <tr>
                  <td><strong>ARIMA(2,1,1)</strong></td>
                  <td>0.12 s</td>
                  <td>2.121 &deg;C</td>
                  <td>Estadística pura</td>
                </tr>
                <tr>
                  <td><strong>ExtraTrees (Lags 1-14)</strong></td>
                  <td>0.25 s</td>
                  <td>2.166 &deg;C</td>
                  <td>Recomendado Producción</td>
                </tr>
                <tr>
                  <td><strong>LSTM PyTorch (1 Capa)</strong></td>
                  <td>14.80 s</td>
                  <td>2.097 &deg;C</td>
                  <td>Costo 60x para ganar 0.07 °C</td>
                </tr>
              </tbody>
            </table>
            <div class="callout alert">
              <strong>Veredicto:</strong> La LSTM mejoró apenas 0.069 °C respecto a ExtraTrees, requiriendo 60 veces más tiempo de cómputo y calibración de pesos.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">¿Cuándo SÍ gana Deep Learning?</span>
            <span class="panel-badge">TRANSFERENCIA MASIVA</span>
          </div>
          <div class="panel-content">
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-emerald);"></span>
                <div>
                  <strong>Transferencia Cruzada Masiva (Cross-Learning):</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Modelos como DeepAR o TFT entrenados sobre 100,000 productos de retail simultáneos. Aprenden patrones globales compartidos que ningún árbol individual puede ver.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-blue);"></span>
                <div>
                  <strong>Múltiples Horizontes con Cuantiles (Direct Multi-Horizon):</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Pronosticar simultáneamente $t+1, t+2, \dots, t+30$ sin error recursivo acumulativo, generando cuantiles P10, P50, P90 en una sola pasada de inferencia.</p>
                </div>
              </div>
            </div>
            <div class="callout success">
              <strong>Regla de Decisión Práctica:</strong> Si tienes una sola estación o menos de 10,000 puntos: usa ExtraTrees o ARIMA. Si tienes más de 100,000 series heterogéneas: usa TFT o PatchTST.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: PARADIGMA 3 - DEL PIXEL AL RENDIMIENTO -->
  <section class="slide" data-title="P3: Visión por Computador">
    <div class="slide-header">
      <span class="tag">Paradigma 3 · Visión Artificial &amp; Monitoreo Agrícola</span>
      <h2 class="display slide-title">Del Píxel a la Cosecha: Visión Local</h2>
      <p class="slide-subtitle">Cómo drones y cámaras en campo extraen biomarcadores antes de consultar el satélite orbital.</p>
    </div>
    <div class="slide-body">
      <div class="split-55">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Inferencia en Tiempo Real en Cafetales</span>
            <span class="panel-badge">DRONES &amp; ROBÓTICA</span>
          </div>
          <div class="panel-content">
            <div class="chart-container">
              <svg class="svg-canvas" viewBox="0 0 460 210" preserveAspectRatio="xMidYMid meet">
                <!-- Fondo cafetal simulado -->
                <rect x="20" y="20" width="420" height="170" fill="rgba(5,150,105,0.08)" stroke="var(--line-light)" />
                
                <!-- Arbustos de café -->
                <circle cx="120" cy="110" r="55" fill="rgba(5,150,105,0.2)" stroke="var(--accent-emerald)" stroke-width="1.5" />
                <circle cx="250" cy="100" r="65" fill="rgba(5,150,105,0.2)" stroke="var(--accent-emerald)" stroke-width="1.5" />
                <circle cx="360" cy="115" r="50" fill="rgba(5,150,105,0.2)" stroke="var(--accent-emerald)" stroke-width="1.5" />

                <!-- Detección YOLOv12 Bounding Boxes (Cerezas maduras) -->
                <rect x="100" y="85" width="22" height="22" fill="none" stroke="var(--accent-red)" stroke-width="2" />
                <rect x="130" y="110" width="20" height="20" fill="none" stroke="var(--accent-red)" stroke-width="2" />
                <rect x="235" y="75" width="24" height="24" fill="none" stroke="var(--accent-red)" stroke-width="2" />
                <rect x="260" y="105" width="22" height="22" fill="none" stroke="var(--accent-red)" stroke-width="2" />
                
                <!-- HUD Dron -->
                <text x="35" y="42" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-red)" font-weight="700">YOLOv12: Conteo Fruto [1,420 cerezas/planta]</text>
                <text x="35" y="58" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-blue)">SAM 2.1: Segmentación Copa (94.2% cobertura)</text>
              </svg>
            </div>
            <div class="callout">
              <strong>Pipeline Local:</strong> La cámara cuenta frutos y estima volumen foliar individual. Este número se convierte en una covariable exógena de alta precisión para el modelo de rendimiento.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Modelos de Visión en Agricultura</span>
            <span class="panel-badge">ARQUITECTURAS</span>
          </div>
          <div class="panel-content">
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-red);"></span>
                <div>
                  <strong>YOLOv12 (2025):</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Atención por área (Area Attention, A2) con latencia de 1.6 ms en borde. Conteo masivo de cerezas de café en distintas etapas de maduración.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-blue);"></span>
                <div>
                  <strong>SAM 2.1 (Meta, 2024):</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Segmentación zero-shot de copa de cafetos aislándolos de sombras, malezas y suelo desnudo sin requerir reentrenamiento.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-purple);"></span>
                <div>
                  <strong>DINOv2 (Representación Autosupervisada):</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Detección temprana de roya y deficiencias nutricionales mediante embeddings visuales densos.</p>
                </div>
              </div>
            </div>
            <div class="callout success">
              <strong>De la Imagen al Número:</strong> Densidad de carga ($granos/m^2$) + Cobertura de dosel (%) alimentan directamente la matriz supervisada.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: PARADIGMA 3 - BIOFISICA Y SATURACION -->
  <section class="slide" data-title="P3: Biofísica Satelital">
    <div class="slide-header">
      <span class="tag">Paradigma 3 · Teledetección Espacial &amp; Fisiología Vegetal</span>
      <h2 class="display slide-title">Biofísica Satelital y la Trampa de Saturación</h2>
      <p class="slide-subtitle">La física óptica de la hoja: absorción en Rojo vs dispersión en NIR, y por qué el NDVI se estanca cuando la planta es frondosa.</p>
    </div>
    <div class="slide-body">
      <div class="split-50">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Física de la Hoja &mdash; Espectro Óptico</span>
            <span class="panel-badge">ABSORCIÓN VS DISPERSIÓN</span>
          </div>
          <div class="panel-content">
            <div class="chart-container">
              <svg class="svg-canvas" viewBox="0 0 420 190" preserveAspectRatio="xMidYMid meet">
                <!-- Sol + rayos (base) -->
                <circle cx="34" cy="26" r="13" fill="rgba(217,119,6,0.20)" stroke="var(--accent-amber)" stroke-width="2" />
                <line x1="52" y1="14" x2="64" y2="8" stroke="var(--accent-amber)" stroke-width="2" />
                <line x1="54" y1="30" x2="68" y2="30" stroke="var(--accent-amber)" stroke-width="2" />
                <text x="34" y="52" font-size="8.5" font-family="IBM Plex Mono" fill="var(--accent-amber)" text-anchor="middle">sol</text>
                <!-- Corte de hoja con capas (base) -->
                <rect x="100" y="92" width="280" height="62" fill="rgba(5,150,105,0.07)" stroke="var(--accent-emerald)" stroke-width="2" />
                <line x1="100" y1="106" x2="380" y2="106" stroke="var(--accent-emerald)" stroke-opacity="0.5" stroke-dasharray="4,3" />
                <line x1="100" y1="140" x2="380" y2="140" stroke="var(--accent-emerald)" stroke-opacity="0.5" stroke-dasharray="4,3" />
                <text x="112" y="102" font-size="8" font-family="IBM Plex Mono" fill="var(--text-light-faint)">cutícula</text>
                <text x="240" y="128" font-size="9.5" font-family="IBM Plex Mono" fill="var(--accent-emerald)" font-weight="700" text-anchor="middle">mesófilo esponjoso + cloroplastos</text>
                <text x="112" y="150" font-size="8" font-family="IBM Plex Mono" fill="var(--text-light-faint)">envés</text>

                <!-- PASO 1: rojo B04 absorbido (fotosíntesis) -->
                <g data-hf-step="1">
                  <line x1="180" y1="30" x2="180" y2="112" stroke="var(--accent-red)" stroke-width="3" />
                  <polygon points="175,112 185,112 180,121" fill="var(--accent-red)" />
                  <circle cx="172" cy="128" r="2.5" fill="var(--accent-red)" />
                  <circle cx="188" cy="132" r="2.5" fill="var(--accent-red)" />
                  <circle cx="180" cy="136" r="2.5" fill="var(--accent-red)" />
                  <text x="180" y="22" font-size="9.5" font-family="IBM Plex Mono" fill="var(--accent-red)" font-weight="700" text-anchor="middle">① Rojo B04 · 665 nm</text>
                  <text x="180" y="170" font-size="9" font-family="IBM Plex Mono" fill="var(--accent-red)" text-anchor="middle">95% absorbido → clorofila</text>
                </g>

                <!-- PASO 2: NIR B08 dispersado (refrigeración) -->
                <g data-hf-step="2">
                  <line x1="300" y1="30" x2="300" y2="98" stroke="var(--accent-purple)" stroke-width="3" />
                  <line x1="300" y1="98" x2="368" y2="40" stroke="var(--accent-purple)" stroke-width="3" />
                  <polygon points="360,42 372,36 366,48" fill="var(--accent-purple)" />
                  <line x1="300" y1="98" x2="252" y2="62" stroke="var(--accent-purple)" stroke-width="1.5" stroke-dasharray="3,2" stroke-opacity="0.6" />
                  <text x="330" y="22" font-size="9.5" font-family="IBM Plex Mono" fill="var(--accent-purple)" font-weight="700" text-anchor="middle">② NIR B08 · 842 nm</text>
                  <text x="330" y="170" font-size="9" font-family="IBM Plex Mono" fill="var(--accent-purple)" text-anchor="middle">85% rebotado → no se hierve</text>
                </g>
              </svg>
            </div>
            <div class="callout">
              <strong>El Contraste Espectral:</strong> Una planta sana traga luz roja para hacer fotosíntesis y repele el infrarrojo para no hervir internamente.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">La Curva de Saturación del NDVI</span>
            <span class="panel-badge">LÍMITE ASINTÓTICO</span>
          </div>
          <div class="panel-content">
            <div class="chart-container">
              <svg class="svg-canvas" viewBox="0 0 420 190" preserveAspectRatio="xMidYMid meet">
                <!-- Ejes con ticks LAI (base) -->
                <line x1="44" y1="156" x2="396" y2="156" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
                <line x1="44" y1="16" x2="44" y2="156" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
                <text x="44" y="172" font-size="8.5" font-family="IBM Plex Mono" text-anchor="middle">0</text>
                <text x="161" y="172" font-size="8.5" font-family="IBM Plex Mono" text-anchor="middle">2</text>
                <text x="278" y="172" font-size="8.5" font-family="IBM Plex Mono" text-anchor="middle">4</text>
                <text x="395" y="172" font-size="8.5" font-family="IBM Plex Mono" text-anchor="end">6 · LAI</text>
                <text x="16" y="60" font-size="8.5" font-family="IBM Plex Mono" text-anchor="middle">1.0</text>
                <text x="16" y="110" font-size="8.5" font-family="IBM Plex Mono" text-anchor="middle">0.5</text>

                <!-- PASO 1: NDVI que se rinde + techo físico -->
                <g data-hf-step="1">
                  <line x1="44" y1="52" x2="396" y2="52" stroke="var(--accent-amber)" stroke-width="1.5" stroke-dasharray="5,3" />
                  <text x="392" y="44" font-size="9" font-family="IBM Plex Mono" fill="var(--accent-amber)" text-anchor="end">techo físico ≈ 0.85</text>
                  <path d="M 44,150 C 100,60 160,56 396,54" fill="none" stroke="var(--accent-red)" stroke-width="2.5" />
                  <text x="392" y="72" font-size="9.5" font-family="IBM Plex Mono" fill="var(--accent-red)" font-weight="700" text-anchor="end">① NDVI: se aplana en ~0.80</text>
                  <line x1="219" y1="16" x2="219" y2="156" stroke="var(--accent-amber)" stroke-opacity="0.6" stroke-dasharray="3,3" />
                  <text x="219" y="28" font-size="8.5" font-family="IBM Plex Mono" fill="var(--accent-amber)" text-anchor="middle">LAI = 3</text>
                </g>

                <!-- PASO 2: EVI que sí ve + la crisis 2024 que el NDVI no vio -->
                <g data-hf-step="2">
                  <path d="M 44,152 L 396,66" fill="none" stroke="var(--accent-emerald)" stroke-width="2.5" />
                  <text x="392" y="84" font-size="9.5" font-family="IBM Plex Mono" fill="var(--accent-emerald)" font-weight="700" text-anchor="end">② EVI: sigue subiendo</text>
                  <circle cx="278" cy="57" r="5" fill="var(--accent-red)" />
                  <text x="278" y="46" font-size="8.5" font-family="IBM Plex Mono" fill="var(--accent-red)" text-anchor="middle">NDVI 0.79</text>
                  <circle cx="278" cy="111" r="5" fill="none" stroke="var(--accent-emerald)" stroke-width="2.5" />
                  <text x="278" y="128" font-size="8.5" font-family="IBM Plex Mono" fill="var(--accent-emerald)" text-anchor="middle">EVI cae</text>
                  <line x1="278" y1="62" x2="278" y2="106" stroke="var(--accent-amber)" stroke-width="2" stroke-dasharray="3,2" />
                  <text x="290" y="90" font-size="8.5" font-family="IBM Plex Mono" fill="var(--accent-amber)">2024: misma hoja,</text>
                  <text x="290" y="100" font-size="8.5" font-family="IBM Plex Mono" fill="var(--accent-amber)">distinta historia</text>
                </g>
              </svg>
            </div>
            <div class="callout alert">
              <strong>El Peligro Agronómico:</strong> En cafetales maduros, el NDVI da 0.79 año tras año. Si hay sequía, el NDVI marca 0.79 pero la cosecha cae 40%. Solo el EVI y el NDRE (borde rojo B05) detectan la crisis.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: PARADIGMA 3 - FUSION MULTIMODAL -->
  <section class="slide" data-title="P3: Fusión Multimodal">
    <div class="slide-header">
      <span class="tag">Paradigma 3 · Integración Satélite &amp; Fenología</span>
      <h2 class="display slide-title">Fusión Multimodal: El Reloj Botánico</h2>
      <p class="slide-subtitle">Un índice satelital ciego no predice cosechas. Debe integrarse con las 3 fases críticas del café y el balance hídrico.</p>
    </div>
    <div class="slide-body">
      <div class="split-55">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Las 3 Ventanas Fenológicas del Café en Jaén</span>
            <span class="panel-badge">CALENDARIO BOTÁNICO</span>
          </div>
          <div class="panel-content">
            <div class="chart-container">
              <svg class="svg-canvas" viewBox="0 0 460 200" preserveAspectRatio="xMidYMid meet">
                <!-- Línea de meses anual -->
                <g transform="translate(20, 30)">
                  <!-- Fase 1: Floración (Ago-Oct) -->
                  <rect x="0" y="0" width="130" height="50" fill="rgba(217,119,6,0.15)" stroke="var(--accent-amber)" stroke-width="1.5" />
                  <text x="65" y="22" font-size="11" font-family="IBM Plex Mono" fill="var(--accent-amber)" font-weight="700" text-anchor="middle">1. Floración</text>
                  <text x="65" y="38" font-size="9" font-family="IBM Plex Mono" text-anchor="middle">Ago - Oct &middot; Agua Crítica</text>

                  <!-- Fase 2: Llenado de Grano (Nov-Feb) -->
                  <rect x="140" y="0" width="150" height="50" fill="rgba(5,150,105,0.15)" stroke="var(--accent-emerald)" stroke-width="1.5" />
                  <text x="215" y="22" font-size="11" font-family="IBM Plex Mono" fill="var(--accent-emerald)" font-weight="700" text-anchor="middle">2. Llenado Grano</text>
                  <text x="215" y="38" font-size="9" font-family="IBM Plex Mono" text-anchor="middle">Nov - Feb &middot; Radiación &amp; EVI</text>

                  <!-- Fase 3: Cosecha (Mar-Jul) -->
                  <rect x="300" y="0" width="120" height="50" fill="rgba(37,99,235,0.15)" stroke="var(--accent-blue)" stroke-width="1.5" />
                  <text x="360" y="22" font-size="11" font-family="IBM Plex Mono" fill="var(--accent-blue)" font-weight="700" text-anchor="middle">3. Cosecha</text>
                  <text x="360" y="38" font-size="9" font-family="IBM Plex Mono" text-anchor="middle">Mar - Jul &middot; Grano Madurez</text>
                </g>

                <!-- Curva hídrica superpuesta -->
                <path d="M 30,150 Q 80,100 150,160 T 300,110 T 430,170" fill="none" stroke="var(--accent-blue)" stroke-width="2" />
                <text x="30" y="175" font-size="9" font-family="IBM Plex Mono" fill="var(--accent-blue)">Lluvia Acumulada (mm)</text>

                <!-- Curva EVI superpuesta -->
                <path d="M 30,140 Q 150,90 270,120 T 430,130" fill="none" stroke="var(--accent-emerald)" stroke-width="2.5" />
                <text x="30" y="125" font-size="9" font-family="IBM Plex Mono" fill="var(--accent-emerald)">EVI Biomasa Dinámica</text>
              </svg>
            </div>
            <div class="callout success">
              <strong>Acoplamiento Clave:</strong> Una sequía en Floración destruye flores antes de que nazca el fruto. Ningún satélite verá esa pérdida en marzo si no integró la ventana de agosto-octubre.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Vector de Características Multimodal</span>
            <span class="panel-badge">9 VARIABLES BIOFÍSICAS</span>
          </div>
          <div class="panel-content">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Ventana Fenológica</th>
                  <th>Índices Espectrales</th>
                  <th>Variables Agroclimáticas</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Floración (Ago-Oct)</strong></td>
                  <td>&sum;EVI, max NDRE</td>
                  <td>Precipitación acumulada (mm)</td>
                </tr>
                <tr>
                  <td><strong>Llenado (Nov-Feb)</strong></td>
                  <td>EVI medio, &Delta;NDWI</td>
                  <td>Horas de sol &amp; T° media</td>
                </tr>
                <tr>
                  <td><strong>Cosecha (Mar-Jul)</strong></td>
                  <td>Integral EVI madurez</td>
                  <td>Déficit de presión de vapor</td>
                </tr>
              </tbody>
            </table>
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono">4.4%</span>
                <span class="kpi-lbl">MAPE Fusión Multimodal</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">5.4%</span>
                <span class="kpi-lbl">MAPE Solo NDVI Anual</span>
              </div>
            </div>
            <div class="callout">
              <strong>Resultado AgroVisión:</strong> La fusión reduce el error de pronóstico y acierta en campañas críticas con anomalías climáticas extremas.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: PARADIGMA 4 - MODELOS GLOBALES Y AGENCIAS -->
  <section class="slide" data-title="P4: Modelos Físicos Globales">
    <div class="slide-header">
      <span class="tag">Paradigma 4 · Física Atmosférica &amp; Supercómputo</span>
      <h2 class="display slide-title">Modelos Físicos Globales y Supercómputo</h2>
      <p class="slide-subtitle">Cómo pronostican el clima las grandes agencias mundiales: Ecuaciones de Navier-Stokes y asimilación 4D-Var.</p>
    </div>
    <div class="slide-body">
      <div class="split-50">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Malla Atmosférica Tridimensional</span>
            <span class="panel-badge">NAVIER-STOKES</span>
          </div>
          <div class="panel-content">
            <div class="chart-container">
              <svg class="svg-canvas" viewBox="0 0 420 180" preserveAspectRatio="xMidYMid meet">
                <!-- Cuadrícula 3D estilizada -->
                <g stroke="currentColor" stroke-opacity="0.25" stroke-width="1">
                  <line x1="60" y1="140" x2="360" y2="140" />
                  <line x1="60" y1="100" x2="360" y2="100" />
                  <line x1="60" y1="60" x2="360" y2="60" />
                  <line x1="100" y1="40" x2="100" y2="160" />
                  <line x1="180" y1="40" x2="180" y2="160" />
                  <line x1="260" y1="40" x2="260" y2="160" />
                  <line x1="340" y1="40" x2="340" y2="160" />
                </g>

                <!-- Celda elemental de cómputo -->
                <rect x="180" y="60" width="80" height="40" fill="rgba(37,99,235,0.15)" stroke="var(--accent-blue)" stroke-width="2" />
                <text x="220" y="85" font-size="10" font-family="IBM Plex Mono" fill="var(--accent-blue)" font-weight="700" text-anchor="middle">&Delta;x &Delta;y &Delta;z</text>
                
                <!-- Vectores de flujo -->
                <line x1="220" y1="60" x2="220" y2="25" stroke="var(--accent-red)" stroke-width="2" />
                <text x="230" y="35" font-size="9" font-family="IBM Plex Mono" fill="var(--accent-red)">Convección w</text>

                <line x1="260" y1="80" x2="295" y2="80" stroke="var(--accent-emerald)" stroke-width="2" />
                <text x="300" y="75" font-size="9" font-family="IBM Plex Mono" fill="var(--accent-emerald)">Viento u</text>
              </svg>
            </div>
            <div class="callout">
              <strong>El Desafío:</strong> Resolver las ecuaciones de conservación de momento, masa y energía para millones de cubos atmosféricos consume megavatios en centros de supercómputo.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Las 3 Grandes Agencias Mundiales</span>
            <span class="panel-badge">INFRAESTRUCTURA GLOBAL</span>
          </div>
          <div class="panel-content">
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-blue);"></span>
                <div>
                  <strong>NOAA GFS (Estados Unidos):</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Resolución de 13 km, 127 niveles verticales. Acceso 100% público. Tiende a sobreestimar temperaturas máximas en selva continental.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-emerald);"></span>
                <div>
                  <strong>ECMWF IFS (Europa):</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Resolución de 9 km, 137 niveles verticales. Asimilación 4D-Var continua. Considerado el estándar de oro en precisión global.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-amber);"></span>
                <div>
                  <strong>DWD ICON (Alemania):</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Malla icosaédrica triangular no-hidrostática. Excelente parametrización de nubosidad y microfísica de nubes.</p>
                </div>
              </div>
            </div>
            <div class="callout success">
              <strong>Acceso Abierto:</strong> Vía APIs modernas como Open-Meteo, podemos consultar estos modelos en paralelo para cualquier coordenada de Perú sin costo.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 14: PARADIGMA 4 - DISPARIDAD EN VIVO -->
  <section class="slide" data-title="P4: Disparidad de Agencias">
    <div class="slide-header">
      <span class="tag">Paradigma 4 · Evidencia Real para Iquitos (Open-Meteo)</span>
      <h2 class="display slide-title">La Disparidad de las Agencias: ¿Cuánto Discrepan?</h2>
      <p class="slide-subtitle">Incluso los supercomputadores más avanzados del planeta muestran desacuerdos de hasta 7.6 °C para un mismo punto geográfico.</p>
    </div>
    <div class="slide-body">
      <div class="split-60">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Pronóstico a 7 Días para Iquitos (-3.6903°, -73.2556°)</span>
            <span class="panel-badge">EN VIVO VÍA OPEN-METEO</span>
          </div>
          <div class="panel-content">
            <div class="chart-container" style="min-height: 250px;">
              <canvas id="chartNoaaEcmwf"></canvas>
            </div>
            <div class="callout">
              <strong>Observación Directa:</strong> Para el mismo día, NOAA GFS pronostica 36.9 °C (ola de calor extrema) mientras ECMWF pronostica 29.3 °C (temperatura moderada por tormenta).
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Diagnóstico Meteorológico</span>
            <span class="panel-badge">ANÁLISIS DE CAUSA</span>
          </div>
          <div class="panel-content">
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono" style="color: var(--accent-red);">&Delta; 7.6 &deg;C</span>
                <span class="kpi-lbl">Discrepancia Máxima</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">36.9 &deg;C</span>
                <span class="kpi-lbl">Pico NOAA GFS</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">29.3 &deg;C</span>
                <span class="kpi-lbl">Pico ECMWF IFS</span>
              </div>
            </div>
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-amber);"></span>
                <div>
                  <strong>¿Por qué discrepan tanto en Iquitos?</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">La selva amazónica es dominada por convección húmeda rápida. NOAA prevé sol pleno con calentamiento radiativo; ECMWF modela cobertura nubosa densa que amortigua la radiación.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-blue);"></span>
                <div>
                  <strong>Lección para Tomadores de Decisión:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Nunca construyas un plan operativo agrícola o de distribución eléctrica sobre un solo proveedor climático. El valor real está en el ensamble multimodelo.</p>
                </div>
              </div>
            </div>
            <div class="callout alert">
              <strong>Riesgo Operativo:</strong> Si eres una empresa cervecera o agrícola y crees ciegamente en NOAA, sobredimensionarás inventario; si crees en ECMWF, podrías quedarte corto.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 15: PARADIGMA 4 - GRAPHCAST Y ZERO SHOT -->
  <section class="slide" data-title="P4: GraphCast y Zero-Shot">
    <div class="slide-header">
      <span class="tag">Paradigma 4 · La Revolución AI Weather &amp; Foundation Models</span>
      <h2 class="display slide-title">GraphCast y Modelos Fundacionales Zero-Shot</h2>
      <p class="slide-subtitle">El quiebre de 2023–2026: de horas en supercomputadores a 60 segundos en GPU, y pronósticos en frío con TimesFM y Chronos.</p>
    </div>
    <div class="slide-body">
      <div class="split-50">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">GraphCast (Google DeepMind, Science 2023)</span>
            <span class="panel-badge">GNN ICOSAÉDRICA</span>
          </div>
          <div class="panel-content">
            <div class="chart-container">
              <svg class="svg-canvas" viewBox="0 0 420 180" preserveAspectRatio="xMidYMid meet">
                <!-- Globo terráqueo con malla icosaédrica -->
                <circle cx="210" cy="90" r="70" fill="rgba(37,99,235,0.06)" stroke="var(--accent-blue)" stroke-width="1.5" />
                
                <!-- Nodos icosaédricos interconectados -->
                <g stroke="var(--accent-blue)" stroke-width="1" opacity="0.6">
                  <line x1="210" y1="20" x2="160" y2="60" />
                  <line x1="210" y1="20" x2="260" y2="60" />
                  <line x1="160" y1="60" x2="180" y2="120" />
                  <line x1="260" y1="60" x2="240" y2="120" />
                  <line x1="180" y1="120" x2="210" y2="160" />
                  <line x1="240" y1="120" x2="210" y2="160" />
                  <line x1="160" y1="60" x2="260" y2="60" />
                  <line x1="180" y1="120" x2="240" y2="120" />
                </g>

                <circle cx="210" cy="20" r="4" fill="var(--accent-blue)" />
                <circle cx="160" cy="60" r="4" fill="var(--accent-blue)" />
                <circle cx="260" cy="60" r="4" fill="var(--accent-blue)" />
                <circle cx="180" cy="120" r="4" fill="var(--accent-blue)" />
                <circle cx="240" cy="120" r="4" fill="var(--accent-blue)" />
                <circle cx="210" cy="160" r="4" fill="var(--accent-blue)" />
                
                <text x="210" y="95" font-size="11" font-family="IBM Plex Mono" fill="var(--accent-blue)" font-weight="700" text-anchor="middle">60 SEGUNDOS</text>
              </svg>
            </div>
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono">90%</span>
                <span class="kpi-lbl">Variables ganadas a ECMWF</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">1 GPU</span>
                <span class="kpi-lbl">TPU v4 (Inferencia &lt; 1 min)</span>
              </div>
            </div>
            <div class="callout success">
              <strong>Hito Histórico:</strong> Publicado en <em>Science</em>. Una red neuronal de grafos entrenada con 40 años de reanálisis ERA5 supera al supercomputador físico más caro del mundo.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Modelos Fundacionales Zero-Shot</span>
            <span class="panel-badge">TIMESFM &amp; CHRONOS</span>
          </div>
          <div class="panel-content">
            <p style="font-size: 13px; color: var(--text-light-mute);">
              Modelos gigantes preentrenados con miles de millones de series temporales que pronostican en frío sin requerir fine-tuning:
            </p>
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-blue);"></span>
                <div>
                  <strong>TimesFM (Google Research, 2024):</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Transformer de 200M parámetros con tokenización de parches. Funciona en modo Zero-Shot con cualquier frecuencia temporal (horaria, diaria, mensual).</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-amber);"></span>
                <div>
                  <strong>Chronos (Amazon, 2024):</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Convierte valores continuos en tokens mediante cuantización numérica y entrena modelos tipo T5. Trata las series de tiempo como lenguaje natural.</p>
                </div>
              </div>
            </div>
            <div class="callout">
              <strong>Aplicabilidad:</strong> Ideales para pronósticos de arranque rápido cuando no existe historial suficiente para entrenar un Random Forest local.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 16: CASO A - MAPA IQUITOS -->
  <section class="slide" data-title="Caso A: Ubicación Iquitos">
    <div class="slide-header">
      <span class="tag">Caso A · Meteorología Amazónica en Perú</span>
      <h2 class="display slide-title">Estación Punchana &mdash; SENAMHI Iquitos</h2>
      <p class="slide-subtitle">Ubicación geográfica, microclima amazónico de selva baja y descarga de 7 años de datos reales vía Garúa.</p>
    </div>
    <div class="slide-body">
      <div class="split-60">
        <div class="panel" style="padding: 0; overflow: hidden;">
          <div id="mapIquitos" class="map-container"></div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Ficha Técnica de la Estación</span>
            <span class="panel-badge mono">COD: 103015</span>
          </div>
          <div class="panel-content">
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono">91 msnm</span>
                <span class="kpi-lbl">Elevación</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">2,557</span>
                <span class="kpi-lbl">Días Descargados</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">0.0%</span>
                <span class="kpi-lbl">Huecos Post-Limpieza</span>
              </div>
            </div>
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet"></span>
                <div>
                  <strong>Coordenadas:</strong> Latitud -3.6903°, Longitud -73.2556° (Punchana, Maynas, Loreto).
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet"></span>
                <div>
                  <strong>Entorno Hidroclimático:</strong> Confluencia de los ríos Nanay y Amazonas. Clima tropical hiperhúmedo con rápida convección vespertina.
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet"></span>
                <div>
                  <strong>Período Auditado:</strong> 01-Ene-2019 al 31-Dic-2025. Limpieza rigurosa con tratamiento de trazas ('T' &rarr; 0.0 mm) y valores sin dato ('S/D' &rarr; NaN).
                </div>
              </div>
            </div>
            <div class="callout success">
              <strong>Dataset Abierto:</strong> Disponible en <span class="mono">data/senamhi_diario.csv</span> (92.9 KB), listo para reproducción en el notebook 01.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 17: CASO A - BENCHMARK 7 AÑOS -->
  <section class="slide" data-title="Caso A: Benchmark 7 Años">
    <div class="slide-header">
      <span class="tag">Caso A · Evaluación Rigurosa sobre Holdout Ciego de 90 Días</span>
      <h2 class="display slide-title">Benchmark Empírico: 5 Niveles de Modelo</h2>
      <p class="slide-subtitle">Resultados reales compitiendo en igualdad de condiciones sobre la estación Punchana (2019–2025).</p>
    </div>
    <div class="slide-body">
      <div class="split-55">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Tabla Forense de Resultados</span>
            <span class="panel-badge">HOLDOUT 90 DÍAS</span>
          </div>
          <div class="panel-content">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Nivel</th>
                  <th>Modelo</th>
                  <th>RMSE (&deg;C)</th>
                  <th>MAE (&deg;C)</th>
                  <th>Tiempo CPU</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Baseline</td>
                  <td><strong>Naive Estacional</strong></td>
                  <td class="mono">2.315</td>
                  <td class="mono">1.758</td>
                  <td class="mono">&lt; 0.001 s</td>
                </tr>
                <tr>
                  <td>Clásico</td>
                  <td><strong>ARIMA(2,1,1)</strong></td>
                  <td class="mono">2.121</td>
                  <td class="mono">1.614</td>
                  <td class="mono">0.12 s</td>
                </tr>
                <tr>
                  <td>ML Tabular</td>
                  <td><strong>Random Forest</strong></td>
                  <td class="mono">2.247</td>
                  <td class="mono">1.701</td>
                  <td class="mono">0.45 s</td>
                </tr>
                <tr>
                  <td>ML Tabular</td>
                  <td><strong>ExtraTrees Regressor</strong></td>
                  <td class="mono" style="color: var(--accent-emerald); font-weight: 700;">2.166</td>
                  <td class="mono">1.632</td>
                  <td class="mono">0.25 s</td>
                </tr>
                <tr>
                  <td>Deep Learning</td>
                  <td><strong>LSTM (1 Capa, PyTorch)</strong></td>
                  <td class="mono" style="color: var(--accent-blue); font-weight: 700;">2.097</td>
                  <td class="mono">1.590</td>
                  <td class="mono">14.80 s</td>
                </tr>
              </tbody>
            </table>
            <div class="callout success">
              <strong>Conclusión Estadística:</strong> ExtraTrees y LSTM superan al modelo ingenuo (Naive) por un 6.4% y 9.4% de reducción de error respectivamente.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Análisis de Desempeño &amp; Parsimonia</span>
            <span class="panel-badge">CRITERIO INGENIERIL</span>
          </div>
          <div class="panel-content">
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono">2.097 &deg;C</span>
                <span class="kpi-lbl">Mejor RMSE (LSTM)</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">0.25 s</span>
                <span class="kpi-lbl">Tiempo ExtraTrees</span>
              </div>
            </div>
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-emerald);"></span>
                <div>
                  <strong>Por qué ExtraTrees vence a Random Forest:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Al elegir umbrales de partición 100% aleatorios, ExtraTrees reduce drásticamente la varianza y suaviza el ruido turbulento amazónico.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-blue);"></span>
                <div>
                  <strong>El Costo de la Precisión:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Para ganar 0.069 °C de mejora, la LSTM requiere entrenar pesos en PyTorch durante 15 segundos. En producción masiva, ExtraTrees es la solución óptima.</p>
                </div>
              </div>
            </div>
            <div class="callout">
              <strong>Validación Estricta:</strong> Nunca se mezclaron datos al azar (*no shuffle*). Toda la prueba se hizo en los últimos 90 días respetando la causalidad temporal.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 18: CASO A - DEMO EN VIVO -->
  <section class="slide" data-title="Caso A: Demo 1 en Vivo">
    <div class="slide-header">
      <span class="tag">Caso A · Demostración Interactiva con Incertidumbre</span>
      <h2 class="display slide-title">DEMO 1: Pronóstico 7 Días &mdash; Iquitos</h2>
      <p class="slide-subtitle">Explora los modelos compitiendo en tiempo real contra los valores reales observados, con intervalos de confianza al 90% (&plusmn;1.645&sigma;).</p>
    </div>
    <div class="slide-body">
      <div class="split-60">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Curvas de Pronóstico y Bandas de Confianza</span>
            <div class="btn-group" id="casoABtns">
              <button class="pill-btn active" onclick="toggleDatasetCasoA('observed')">Observado</button>
              <button class="pill-btn active" onclick="toggleDatasetCasoA('rf')">Random Forest</button>
              <button class="pill-btn" onclick="toggleDatasetCasoA('xgb')">XGBoost</button>
              <button class="pill-btn" onclick="toggleDatasetCasoA('lstm')">LSTM</button>
            </div>
          </div>
          <div class="panel-content">
            <div class="chart-container" style="min-height: 250px;">
              <canvas id="chartCasoA"></canvas>
            </div>
            <div class="callout">
              <strong>El Cono se Abre:</strong> Observa cómo la banda sombreada de incertidumbre se ensancha del día 1 al día 7. A mayor distancia del presente, mayor es el riesgo de dispersión.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Telemetría Operativa en Vivo</span>
            <span class="panel-badge mono">HORIZONTE 7d</span>
          </div>
          <div class="panel-content">
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono">33.4 &deg;C</span>
                <span class="kpi-lbl">Media Prevista t+48h</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">&plusmn;1.8 &deg;C</span>
                <span class="kpi-lbl">Margen de Error (90%)</span>
              </div>
            </div>
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-emerald);"></span>
                <div>
                  <strong>Probabilidad de Superar 34 °C:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Estimada en <strong>78.4%</strong> para el día 4. Activa protocolos de alerta de estrés térmico para fauna y redes de distribución eléctrica.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-blue);"></span>
                <div>
                  <strong>Consistencia Multimodelo:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Tanto ARIMA como ExtraTrees coinciden en una tendencia de enfriamiento hacia el día 6 por entrada de un frente húmedo.</p>
                </div>
              </div>
            </div>
            <div class="callout success">
              <strong>Exportación Lista:</strong> Datos servidos directamente desde <span class="mono">data/senamhi_forecast_7d.csv</span> con fallback embebido offline.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 19: CASO B - MAPA JAEN & HEATMAPS -->
  <section class="slide" data-title="Caso B: Mapa Jaén & Heatmaps">
    <div class="slide-header">
      <span class="tag">Caso B · Agricultura de Precisión en Jaén, Cajamarca</span>
      <h2 class="display slide-title">Finca Cafetalera &amp; Visor de Capas Multiespectral</h2>
      <p class="slide-subtitle">Explora la parcela cafetalera (1,100 msnm) y alterna en tiempo real entre capas satelitales Sentinel-2 (AgroVisión).</p>
    </div>
    <div class="slide-body">
      <div class="split-60">
        <div class="panel" style="padding: 0; overflow: hidden;">
          <div id="mapJaen" class="map-container"></div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Visor de Capas / Heatmap Switcher</span>
            <span class="panel-badge">SENTINEL-2 L2A</span>
          </div>
          <div class="panel-content">
            <div class="btn-group">
              <button class="pill-btn active" id="btnLayerRgb" onclick="switchJaenLayer('rgb')">🛰️ Satélite RGB</button>
              <button class="pill-btn" id="btnLayerNdvi" onclick="switchJaenLayer('ndvi')">🔴 Heatmap NDVI (Saturado)</button>
              <button class="pill-btn" id="btnLayerEvi" onclick="switchJaenLayer('evi')">🟢 Heatmap EVI (Biomasa)</button>
              <button class="pill-btn" id="btnLayerNdre" onclick="switchJaenLayer('ndre')">🟣 Heatmap NDRE (Nitrógeno)</button>
            </div>
            
            <div id="jaenLegendBox" style="background: var(--bg-light-sub); padding: 12px; border: 1px solid var(--line-light-faint);">
              <strong id="jaenLayerTitle" style="font-size: 13px;">🛰️ Imagen Satelital RGB Natural</strong>
              <p id="jaenLayerDesc" style="font-size: 12px; color: var(--text-light-mute); margin-top: 4px;">
                Vista óptica en color real de la finca cafetalera en Jaén (-5.6766°, -78.7742°, 1,100 msnm).
              </p>
            </div>

            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono">12 ha</span>
                <span class="kpi-lbl">Área Parcela</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">1,100 m</span>
                <span class="kpi-lbl">Altitud Media</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">10 m</span>
                <span class="kpi-lbl">Resolución Sentinel-2</span>
              </div>
            </div>
            <div class="callout alert">
              <strong>Observa la diferencia:</strong> Mientras el NDVI luce plano y uniforme en 0.79, las capas EVI y NDRE revelan variabilidad interna de vigor y clorofila.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 20: CASO B - EVIDENCIA DE CAMPO -->
  <section class="slide" data-title="Caso B: La Evidencia de Campo">
    <div class="slide-header">
      <span class="tag">Caso B · Auditoría de 6 Campañas Reales (2020–2025)</span>
      <h2 class="display slide-title">La Prueba de Campo: La Trampa de la Campaña 2024</h2>
      <p class="slide-subtitle">Cómo el NDVI plano no detectó la sequía en floración, mientras que la fusión multiespectral acertó con precisión milimétrica.</p>
    </div>
    <div class="slide-body">
      <div class="split-55">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Tabla Histórica de 6 Campañas de Café</span>
            <span class="panel-badge">JAÉN, CAJAMARCA</span>
          </div>
          <div class="panel-content">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Campaña</th>
                  <th>NDVI Anual</th>
                  <th>Lluvia Floración</th>
                  <th>Rendimiento Real</th>
                  <th>Solo NDVI</th>
                  <th>Fusión EVI+Clima</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>2020</strong></td>
                  <td class="mono">0.785</td>
                  <td class="mono">280 mm</td>
                  <td class="mono"><strong>22.5 qq/ha</strong></td>
                  <td class="mono">23.1</td>
                  <td class="mono" style="color: var(--accent-emerald);">22.3</td>
                </tr>
                <tr>
                  <td><strong>2021</strong></td>
                  <td class="mono">0.792</td>
                  <td class="mono">310 mm</td>
                  <td class="mono"><strong>25.0 qq/ha</strong></td>
                  <td class="mono">24.2</td>
                  <td class="mono" style="color: var(--accent-emerald);">24.8</td>
                </tr>
                <tr>
                  <td><strong>2022</strong></td>
                  <td class="mono">0.780</td>
                  <td class="mono">245 mm</td>
                  <td class="mono"><strong>21.0 qq/ha</strong></td>
                  <td class="mono">22.4</td>
                  <td class="mono" style="color: var(--accent-emerald);">21.2</td>
                </tr>
                <tr>
                  <td><strong>2023</strong></td>
                  <td class="mono">0.789</td>
                  <td class="mono">295 mm</td>
                  <td class="mono"><strong>24.0 qq/ha</strong></td>
                  <td class="mono">23.8</td>
                  <td class="mono" style="color: var(--accent-emerald);">23.9</td>
                </tr>
                <tr style="background: rgba(220,38,38,0.08);">
                  <td><strong>2024 (Crisis)</strong></td>
                  <td class="mono" style="color: var(--accent-red); font-weight: 700;">0.788 (Plano)</td>
                  <td class="mono" style="color: var(--accent-red); font-weight: 700;">140 mm (Sequía)</td>
                  <td class="mono"><strong>18.2 qq/ha</strong></td>
                  <td class="mono" style="color: var(--accent-red);">24.0 (FALLÓ)</td>
                  <td class="mono" style="color: var(--accent-emerald); font-weight: 700;">18.46 (ACERTÓ)</td>
                </tr>
                <tr>
                  <td><strong>2025</strong></td>
                  <td class="mono">0.794</td>
                  <td class="mono">325 mm</td>
                  <td class="mono"><strong>26.0 qq/ha</strong></td>
                  <td class="mono">24.5</td>
                  <td class="mono" style="color: var(--accent-emerald);">25.7</td>
                </tr>
              </tbody>
            </table>
            <div class="callout alert">
              <strong>Autopsia Campaña 2024:</strong> El NDVI anual marcó 0.788 (idéntico al 0.789 de 2023). El modelo simple predijo 24 qq/ha. La cosecha real se derrumbó a 18.2 qq/ha.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Por qué la Fusión Fenológica Salvó el Pronóstico</span>
            <span class="panel-badge">BIOFÍSICA DEL CAFÉ</span>
          </div>
          <div class="panel-content">
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono" style="color: var(--accent-emerald);">0.26 qq/ha</span>
                <span class="kpi-lbl">Error Fusión 2024</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono" style="color: var(--accent-red);">5.80 qq/ha</span>
                <span class="kpi-lbl">Error Solo NDVI 2024</span>
              </div>
            </div>
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-red);"></span>
                <div>
                  <strong>La Trampa del Dosel Verde:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Las hojas adultas del cafeto retienen clorofila y rebotan NIR incluso cuando el árbol aborta el 50% de sus flores por falta de agua.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-emerald);"></span>
                <div>
                  <strong>El Rescate Fenológico:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">El modelo de fusión leyó los 140 mm en la ventana de Floración (agosto-octubre) y la caída en el índice hídrico NDWI, recortando la predicción a 18.46 qq/ha.</p>
                </div>
              </div>
            </div>
            <div class="callout success">
              <strong>Lección Práctica:</strong> En cultivos densos, nunca tomes un índice satelital aislado sin su contexto meteorológico y fenológico.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 21: CASO B - DEMO EN VIVO -->
  <section class="slide" data-title="Caso B: Demo 2 en Vivo">
    <div class="slide-header">
      <span class="tag">Caso B · Validación Cruzada Leave-One-Year-Out (LOYO)</span>
      <h2 class="display slide-title">DEMO 2: Rendimiento Cosecha Café &mdash; Jaén</h2>
      <p class="slide-subtitle">Comparativa gráfica entre rendimiento real observado vs Fusión EVI+Clima vs modelo estancado de solo NDVI.</p>
    </div>
    <div class="slide-body">
      <div class="split-60">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Cosecha Observada vs Predicciones (2020–2025)</span>
            <div class="btn-group" id="casoBBtns">
              <button class="pill-btn active" onclick="toggleDatasetCasoB('observed')">Real Observado</button>
              <button class="pill-btn active" onclick="toggleDatasetCasoB('fusion')">Fusión EVI + Clima</button>
              <button class="pill-btn" onclick="toggleDatasetCasoB('solo_ndvi')">Solo NDVI</button>
            </div>
          </div>
          <div class="panel-content">
            <div class="chart-container" style="min-height: 250px;">
              <canvas id="chartCasoB"></canvas>
            </div>
            <div class="callout success">
              <strong>Fidelidad a las Crisis:</strong> Observa cómo la barra verde de Fusión rastrea la caída de 2024, mientras la línea roja de Solo NDVI flota desconectada en la abundancia ficticia.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Métricas de Validación &amp; Impacto Financiero</span>
            <span class="panel-badge">COOPERATIVAS CAFÉ</span>
          </div>
          <div class="panel-content">
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono" style="color: var(--accent-emerald);">4.4%</span>
                <span class="kpi-lbl">MAPE Fusión</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">1.74</span>
                <span class="kpi-lbl">RMSE (qq/ha)</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">$15,000</span>
                <span class="kpi-lbl">Riesgo Evitado / Contenedor</span>
              </div>
            </div>
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet"></span>
                <div>
                  <strong>Valor de la Validación LOYO:</strong> Cada año se predice habiendo entrenado únicamente con los 5 años restantes. Cero filtración temporal.
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet"></span>
                <div>
                  <strong>Impacto en Exportación:</strong> Sobrestimar la cosecha en 5.8 qq/ha lleva a la cooperativa a comprometer contratos a futuro que no podrá entregar, incurriendo en penalidades internacionales millonarias.
                </div>
              </div>
            </div>
            <div class="callout">
              <strong>Dataset Abierto:</strong> Disponible en <span class="mono">data/cafe_ndvi_rendimiento.csv</span> para auditar en el notebook 02.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 22: LECCIONES DESDE LAS TRINCHERAS -->
  <section class="slide" data-title="Lecciones de las Trincheras">
    <div class="slide-header">
      <span class="tag">Síntesis Operativa · Principios Innegociables</span>
      <h2 class="display slide-title">5 Lecciones desde las Trincheras</h2>
      <p class="slide-subtitle">Lo que aprendimos tras procesar millones de datos meteorológicos y satelitales en proyectos reales.</p>
    </div>
    <div class="slide-body">
      <div class="feature-list" style="gap: 12px; height: 100%; justify-content: space-around;">
        <div class="panel" style="padding: 12px 18px; flex: 1;">
          <div style="display: flex; gap: 14px; align-items: center;">
            <span class="mono" style="font-size: 24px; font-weight: 700; color: var(--accent-blue);">01</span>
            <div>
              <strong style="font-size: 14px;">Validación Temporal Estricta (No Shuffle Obligatorio)</strong>
              <p style="font-size: 12px; color: var(--text-light-mute); margin-top: 2px;">
                Mezclar aleatoriamente el pasado y el futuro (*random k-fold*) es el autoengaño más común de los científicos de datos. Usa siempre TimeSeriesSplit o holdout en bloque.
              </p>
            </div>
          </div>
        </div>

        <div class="panel" style="padding: 12px 18px; flex: 1;">
          <div style="display: flex; gap: 14px; align-items: center;">
            <span class="mono" style="font-size: 24px; font-weight: 700; color: var(--accent-emerald);">02</span>
            <div>
              <strong style="font-size: 14px;">Árboles antes que Redes Neuronales</strong>
              <p style="font-size: 12px; color: var(--text-light-mute); margin-top: 2px;">
                Arranca siempre con ExtraTrees o LightGBM con lags 1-14. Es un baseline que entrena en 0.2 segundos y bate al 90% de las arquitecturas de Deep Learning en series individuales.
              </p>
            </div>
          </div>
        </div>

        <div class="panel" style="padding: 12px 18px; flex: 1;">
          <div style="display: flex; gap: 14px; align-items: center;">
            <span class="mono" style="font-size: 24px; font-weight: 700; color: var(--accent-amber);">03</span>
            <div>
              <strong style="font-size: 14px;">El Costo del Error No es Simétrico</strong>
              <p style="font-size: 12px; color: var(--text-light-mute); margin-top: 2px;">
                El RMSE penaliza por igual hacia arriba y hacia abajo. Pero en la vida real, que sobre café en el almacén cuesta almacenamiento; que falte para cumplir un contrato cuesta la quiebra.
              </p>
            </div>
          </div>
        </div>

        <div class="panel" style="padding: 12px 18px; flex: 1;">
          <div style="display: flex; gap: 14px; align-items: center;">
            <span class="mono" style="font-size: 24px; font-weight: 700; color: var(--accent-purple);">04</span>
            <div>
              <strong style="font-size: 14px;">Respeta la Física del Sensor</strong>
              <p style="font-size: 12px; color: var(--text-light-mute); margin-top: 2px;">
                Ningún modelo matemático arregla un dato físicamente saturado. Si el NDVI se aplana en 0.79 por dosel frondoso, migra a EVI o NDRE antes de intentar afinar hiperparámetros.
              </p>
            </div>
          </div>
        </div>

        <div class="panel" style="padding: 12px 18px; flex: 1;">
          <div style="display: flex; gap: 14px; align-items: center;">
            <span class="mono" style="font-size: 24px; font-weight: 700; color: var(--accent-red);">05</span>
            <div>
              <strong style="font-size: 14px;">Interpretabilidad Operativa sobre Complejidad</strong>
              <p style="font-size: 12px; color: var(--text-light-mute); margin-top: 2px;">
                Un pronóstico con un cono de confianza que los agrónomos o ingenieros de planta entienden será adoptado; una caja negra opaca con 0.05 °C menos de error será rechazada.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 23: ARBOL DE DECISION -->
  <section class="slide" data-title="Árbol de Decisión">
    <div class="slide-header">
      <span class="tag">Guía de Decisión · De la Pregunta al Algoritmo</span>
      <h2 class="display slide-title">Árbol de Decisión Práctico de Modelado</h2>
      <p class="slide-subtitle">¿Qué modelo elegir para tu próximo proyecto según volumen de datos, latencia y requerimientos de negocio?</p>
    </div>
    <div class="slide-body">
      <div class="panel">
        <div class="chart-container">
          <svg class="svg-canvas" viewBox="0 0 900 360" preserveAspectRatio="xMidYMid meet">
            <!-- Nodo Raíz -->
            <rect x="360" y="15" width="180" height="42" fill="var(--bg-light-sub)" stroke="var(--line-light)" stroke-width="2" />
            <text x="450" y="41" font-size="12" font-family="IBM Plex Mono" font-weight="700" text-anchor="middle">¿VOLUMEN DE DATOS?</text>

            <!-- Ramas Nivel 1 -->
            <line x1="400" y1="57" x2="160" y2="105" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
            <line x1="450" y1="57" x2="450" y2="105" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
            <line x1="500" y1="57" x2="740" y2="105" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />

            <!-- Nivel 2: Cajas de Decisión -->
            <rect x="70" y="105" width="180" height="40" fill="var(--bg-light-sub)" stroke="var(--line-light)" />
            <text x="160" y="129" font-size="11" font-family="IBM Plex Mono" text-anchor="middle">&lt; 500 Observaciones</text>

            <rect x="360" y="105" width="180" height="40" fill="var(--bg-light-sub)" stroke="var(--line-light)" />
            <text x="450" y="129" font-size="11" font-family="IBM Plex Mono" text-anchor="middle">500 a 100,000 Filas Tabular</text>

            <rect x="650" y="105" width="180" height="40" fill="var(--bg-light-sub)" stroke="var(--line-light)" />
            <text x="740" y="129" font-size="11" font-family="IBM Plex Mono" text-anchor="middle">&gt; 100,000 Series Masivas</text>

            <!-- Ramas Nivel 2 a Hojas -->
            <line x1="160" y1="145" x2="160" y2="200" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
            <line x1="450" y1="145" x2="450" y2="200" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
            <line x1="740" y1="145" x2="740" y2="200" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />

            <!-- Hojas de Recomendación -->
            <!-- Rama 1: Clásicos -->
            <g transform="translate(60, 200)">
              <rect x="0" y="0" width="200" height="130" fill="rgba(37,99,235,0.06)" stroke="var(--accent-blue)" stroke-width="2" />
              <text x="100" y="25" font-size="12" font-family="IBM Plex Mono" fill="var(--accent-blue)" font-weight="700" text-anchor="middle">MODELOS CLÁSICOS</text>
              <text x="15" y="55" font-size="11" font-family="IBM Plex Sans">&bull; Curvas Logísticas (Biología)</text>
              <text x="15" y="75" font-size="11" font-family="IBM Plex Sans">&bull; Holt-Winters (Retail rápido)</text>
              <text x="15" y="95" font-size="11" font-family="IBM Plex Sans">&bull; ARIMA / SARIMAX (1-3 días)</text>
              <text x="15" y="115" font-size="11" font-family="IBM Plex Sans">&bull; Prophet (Feriados y gaps)</text>
            </g>

            <!-- Rama 2: Tabular -->
            <g transform="translate(350, 200)">
              <rect x="0" y="0" width="200" height="130" fill="rgba(5,150,105,0.06)" stroke="var(--accent-emerald)" stroke-width="2" />
              <text x="100" y="25" font-size="12" font-family="IBM Plex Mono" fill="var(--accent-emerald)" font-weight="700" text-anchor="middle">ML TABULAR CON LAGS</text>
              <text x="15" y="55" font-size="11" font-family="IBM Plex Sans">&bull; ExtraTrees (Filtra ruido)</text>
              <text x="15" y="75" font-size="11" font-family="IBM Plex Sans">&bull; LightGBM (Rápido y preciso)</text>
              <text x="15" y="95" font-size="11" font-family="IBM Plex Sans">&bull; Lags 1-14 + Rolling stats</text>
              <text x="15" y="115" font-size="11" font-family="IBM Plex Sans">&bull; &Delta;Y si hay tendencia récord</text>
            </g>

            <!-- Rama 3: Deep Learning / Zero Shot -->
            <g transform="translate(640, 200)">
              <rect x="0" y="0" width="200" height="130" fill="rgba(124,58,237,0.06)" stroke="var(--accent-purple)" stroke-width="2" />
              <text x="100" y="25" font-size="12" font-family="IBM Plex Mono" fill="var(--accent-purple)" font-weight="700" text-anchor="middle">CROSS-LEARNING / ZERO-SHOT</text>
              <text x="15" y="55" font-size="11" font-family="IBM Plex Sans">&bull; PatchTST (ICLR 2023)</text>
              <text x="15" y="75" font-size="11" font-family="IBM Plex Sans">&bull; TFT (Interpretabilidad)</text>
              <text x="15" y="95" font-size="11" font-family="IBM Plex Sans">&bull; TimesFM (Zero-shot Google)</text>
              <text x="15" y="115" font-size="11" font-family="IBM Plex Sans">&bull; Chronos (Amazon T5)</text>
            </g>
          </svg>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 24: CIERRE Y FILOSOFIA -->
  <section class="slide" data-title="Cierre y Filosofía">
    <div class="slide-header">
      <span class="tag">Conclusión Conceptual · La Respuesta Final</span>
      <h2 class="display slide-title">La IA no predice el futuro: cuantifica la incertidumbre</h2>
      <p class="slide-subtitle">El porvenir no está escrito en ningún archivo CSV; las decisiones estratégicas nacen de navegar el riesgo informado.</p>
    </div>
    <div class="slide-body">
      <div class="split-50">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">El Mensaje Clave</span>
            <span class="panel-badge">SÍNTESIS</span>
          </div>
          <div class="panel-content">
            <blockquote style="font-size: clamp(16px, 1.6vw, 20px); font-family: 'Space Grotesk', sans-serif; font-weight: 600; line-height: 1.4; color: var(--accent-blue); margin: 8px 0;">
              &ldquo;Predecir no es eliminar la duda; es cartografiar la niebla para saber qué sendero tomar con menor probabilidad de naufragio.&rdquo;
            </blockquote>
            <p style="font-size: 13px; color: var(--text-light-mute); line-height: 1.5;">
              La verdadera inteligencia aplicada no consiste en prometer una cifra mágica a 30 días, sino en construir sistemas robustos que admitan cuando no saben, revelen sus intervalos de confianza y permitan a los seres humanos tomar decisiones de inversión, cosecha y energía con los ojos abiertos.
            </p>
            <div class="kpi-row">
              <div class="kpi-box">
                <span class="kpi-val mono">&plusmn;1.65&sigma;</span>
                <span class="kpi-lbl">Rango de Confianza</span>
              </div>
              <div class="kpi-box">
                <span class="kpi-val mono">100%</span>
                <span class="kpi-lbl">Reproducible</span>
              </div>
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">El Haz de Probabilidades y la Decisión</span>
            <span class="panel-badge">VISUAL</span>
          </div>
          <div class="panel-content">
            <div class="chart-container">
              <svg class="svg-canvas" viewBox="0 0 420 200" preserveAspectRatio="xMidYMid meet">
                <!-- Presente -->
                <circle cx="50" cy="100" r="8" fill="var(--accent-blue)" />
                <text x="50" y="125" font-size="11" font-family="IBM Plex Mono" fill="var(--accent-blue)" font-weight="700" text-anchor="middle">PRESENTE</text>

                <!-- Haz de luz de probabilidades divergentes -->
                <polygon points="50,100 320,30 320,170" fill="rgba(37,99,235,0.08)" />
                
                <path d="M 50,100 Q 180,40 320,45" fill="none" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" stroke-dasharray="3,3" />
                <path d="M 50,100 Q 180,70 320,80" fill="none" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" stroke-dasharray="3,3" />
                <path d="M 50,100 Q 180,100 320,100" fill="none" stroke="var(--accent-emerald)" stroke-width="3" />
                <path d="M 50,100 Q 180,130 320,120" fill="none" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" stroke-dasharray="3,3" />
                <path d="M 50,100 Q 180,160 320,155" fill="none" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" stroke-dasharray="3,3" />

                <!-- Nodo de Decisión Informada -->
                <circle cx="320" cy="100" r="10" fill="var(--accent-emerald)" />
                <text x="320" y="125" font-size="11" font-family="IBM Plex Mono" fill="var(--accent-emerald)" font-weight="700" text-anchor="middle">DECISIÓN</text>
                <text x="320" y="140" font-size="9" font-family="IBM Plex Mono" fill="var(--text-light-faint)" text-anchor="middle">INFORMADA</text>
              </svg>
            </div>
            <div class="callout success">
              <strong>El Futuro se Construye:</strong> La IA nos da las cartas probabilísticas; la estrategia humana decide cómo jugarlas.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 25: REFERENCIAS Y RECURSOS -->
  <section class="slide" data-title="Referencias y Recursos">
    <div class="slide-header">
      <span class="tag">Ecosistema Abierto · Código &amp; Literatura Científica</span>
      <h2 class="display slide-title">Referencias, Código Abierto y Cuadernos</h2>
      <p class="slide-subtitle">Todo el material presentado hoy es 100% reproducible y está disponible en nuestro repositorio abierto.</p>
    </div>
    <div class="slide-body">
      <div class="split-50">
        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Cuadernos Reproducibles &amp; Datos</span>
            <span class="panel-badge">GITHUB OPEN SOURCE</span>
          </div>
          <div class="panel-content">
            <div class="feature-list">
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-blue);"></span>
                <div>
                  <strong>notebooks/01_clima_senamhi.ipynb:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Descarga de Punchana vía Garúa, limpieza, baseline naive, ARIMA, ExtraTrees, PyTorch LSTM y exportación con bandas.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-emerald);"></span>
                <div>
                  <strong>notebooks/02_cafe_ndvi.ipynb:</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);">Pipeline satelital Sentinel-2 (AgroVisión), fenología de 3 ventanas, validación LOYO y demostración de saturación de NDVI.</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet" style="background: var(--accent-purple);"></span>
                <div>
                  <strong>data/ (CSVs optimizados &lt; 100 KB):</strong>
                  <p style="font-size: 12px; color: var(--text-light-mute);"><span class="mono">senamhi_diario.csv, senamhi_forecast_7d.csv, cafe_ndvi_rendimiento.csv, noaa_ecmwf_forecast.csv</span>.</p>
                </div>
              </div>
            </div>
            <div class="callout">
              <strong>Clonar y Correr:</strong> <span class="mono">git clone https://github.com/alex/charla_forecasting</span>. Sin dependencias pesadas, corre en cualquier CPU.
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span class="panel-title">Bibliografía Científica Fundamental</span>
            <span class="panel-badge mono">REFS.BIB</span>
          </div>
          <div class="panel-content">
            <div class="feature-list" style="font-size: 11.5px; line-height: 1.45;">
              <div class="feature-item">
                <span class="feature-bullet"></span>
                <div><strong>Huete et al. (2002):</strong> Overview of the radiometric and biophysical performance of the MODIS vegetation indices (EVI). <em>Remote Sens. Environ.</em></div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet"></span>
                <div><strong>Ramos et al. (2020):</strong> Coffee yield estimation based on Sentinel-2 and climate features. <em>Computers and Electronics in Agriculture</em>.</div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet"></span>
                <div><strong>Nie et al. (ICLR 2023):</strong> A Time Series is Worth 64 Words: Long-term Forecasting with Transformers (PatchTST).</div>
              </div>
              <div class="feature-item">
                <span class="feature-bullet"></span>
                <div><strong>Lam et al. (DeepMind, Science 2023):</strong> Learning skillful medium-range global weather forecasting (GraphCast).</div>
              </div>
            </div>
            <div class="callout success">
              <strong>¡Muchas Gracias por su Atención!</strong> Preguntas y debate abiertos.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

</div>

<!-- DATASETS EMBEBIDOS OFFLINE -->
<script type="text/csv" id="embeddedSenamhi7d">""" + senamhi_7d_csv + """</script>
<script type="text/csv" id="embeddedCafe">""" + cafe_csv + """</script>
<script type="text/csv" id="embeddedSenamhiDiario">""" + senamhi_diario_sub + """</script>
<script type="text/csv" id="embeddedNoaaEcmwf">""" + noaa_ecmwf_csv + """</script>

<script>
// ESTADO GLOBAL
let currentSlide = 0;
const slides = document.querySelectorAll(".slide");
const totalSlides = slides.length;
const slideNumEl = document.getElementById("slideNum");
const themeToggle = document.getElementById("themeToggle");
const fsBtn = document.getElementById("fsBtn");
const tocBtn = document.getElementById("tocBtn");

let chartNoaaInstance = null;
let chartCasoAInstance = null;
let chartCasoBInstance = null;
let mapIquitosInstance = null;
let mapJaenInstance = null;

let currentJaenLayer = 'rgb';
let jaenPolygon = null;

// TEMA CLARO / OSCURO
themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark-active");
  const isDark = document.body.classList.contains("dark-active");
  localStorage.setItem("deck_theme", isDark ? "dark" : "light");
  themeToggle.textContent = isDark ? "☀️" : "🌓";
  
  if (chartNoaaInstance) chartNoaaInstance.update();
  if (chartCasoAInstance) chartCasoAInstance.update();
  if (chartCasoBInstance) chartCasoBInstance.update();
});

if (localStorage.getItem("deck_theme") === "dark") {
  document.body.classList.add("dark-active");
  themeToggle.textContent = "☀️";
}

// PANTALLA COMPLETA
fsBtn.addEventListener("click", () => {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen().catch(err => console.log(err));
  } else {
    document.exitFullscreen();
  }
});

// NAVEGACION
function updateSlide(idx) {
  if (idx < 0) idx = 0;
  if (idx >= totalSlides) idx = totalSlides - 1;
  currentSlide = idx;

  slides.forEach((s, i) => {
    s.classList.toggle("active", i === currentSlide);
  });

  slideNumEl.textContent = `${String(currentSlide + 1).padStart(2, '0')} / ${totalSlides}`;
  tocBtn.textContent = String(currentSlide + 1).padStart(2, '0');

  // Inicializar componentes dinámicos bajo demanda
  if (currentSlide === 13) initChartNoaa();
  if (currentSlide === 15) initMapIquitos();
  if (currentSlide === 17) initChartCasoA();
  if (currentSlide === 18) initMapJaen();
  if (currentSlide === 20) initChartCasoB();

  // HyperFrames: narrativa secuenciada por pasos (GSAP timeline)
  hfEnterSlide(currentSlide);
}

document.getElementById("prevBtn").addEventListener("click", () => updateSlide(currentSlide - 1));
document.getElementById("nextBtn").addEventListener("click", () => updateSlide(currentSlide + 1));
tocBtn.addEventListener("click", () => updateSlide(0));

document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowRight" || e.key === " ") {
    e.preventDefault();
    updateSlide(currentSlide + 1);
  } else if (e.key === "ArrowLeft") {
    e.preventDefault();
    updateSlide(currentSlide - 1);
  } else if (e.key === "Home") {
    e.preventDefault();
    updateSlide(0);
  } else if (e.key === "End") {
    e.preventDefault();
    updateSlide(totalSlides - 1);
  } else if (e.key.toLowerCase() === "f") {
    fsBtn.click();
  } else if (e.key >= "1" && e.key <= "3") {
    hfStep(currentSlide, parseInt(e.key, 10));
  } else if (e.key.toLowerCase() === "r") {
    hfReplay(currentSlide);
  }
});

// DESCOMPOSICION INTERACTIVA (Slide 2)
function setDecompLayer(layer) {
  const btns = document.querySelectorAll("#decompBtns .pill-btn");
  btns.forEach(b => b.classList.remove("active"));
  
  const lTrend = document.getElementById("layerTrend");
  const lSeason = document.getElementById("layerSeason");
  const lCycle = document.getElementById("layerCycle");
  const lNoise = document.getElementById("layerNoise");

  if (layer === 'all') {
    event.target.classList.add("active");
    lTrend.style.display = "block";
    lSeason.style.display = "block";
    lCycle.style.display = "block";
    lNoise.style.display = "block";
  } else if (layer === 'trend') {
    event.target.classList.add("active");
    lTrend.style.display = "block";
    lSeason.style.display = "none";
    lCycle.style.display = "none";
    lNoise.style.display = "none";
  } else if (layer === 'season') {
    event.target.classList.add("active");
    lTrend.style.display = "block";
    lSeason.style.display = "block";
    lCycle.style.display = "none";
    lNoise.style.display = "none";
  } else if (layer === 'cycle') {
    event.target.classList.add("active");
    lTrend.style.display = "block";
    lSeason.style.display = "block";
    lCycle.style.display = "block";
    lNoise.style.display = "none";
  } else if (layer === 'noise') {
    event.target.classList.add("active");
    lTrend.style.display = "none";
    lSeason.style.display = "none";
    lCycle.style.display = "none";
    lNoise.style.display = "block";
  }
}

// GRAFICO MULTI-AGENCIA (Slide 14)
function initChartNoaa() {
  if (chartNoaaInstance) return;
  const ctx = document.getElementById("chartNoaaEcmwf");
  if (!ctx) return;

  const rawCsv = document.getElementById("embeddedNoaaEcmwf").textContent.trim();
  const parsed = Papa.parse(rawCsv, { header: true, dynamicTyping: true });
  const rows = parsed.data;

  const labels = rows.map(r => r.fecha);
  const noaaData = rows.map(r => r.tmax_noaa_gfs);
  const ecmwfData = rows.map(r => r.tmax_ecmwf);
  const iconData = rows.map(r => r.tmax_dwd_icon);

  chartNoaaInstance = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'NOAA GFS (EE. UU.) - T° Máx (°C)',
          data: noaaData,
          borderColor: '#2563EB',
          backgroundColor: '#2563EB',
          borderWidth: 3,
          tension: 0.25,
          pointRadius: 5
        },
        {
          label: 'ECMWF IFS (Europa) - T° Máx (°C)',
          data: ecmwfData,
          borderColor: '#059669',
          backgroundColor: '#059669',
          borderWidth: 3,
          tension: 0.25,
          pointRadius: 5
        },
        {
          label: 'DWD ICON (Alemania) - T° Máx (°C)',
          data: iconData,
          borderColor: '#D97706',
          backgroundColor: '#D97706',
          borderWidth: 2,
          borderDash: [5, 5],
          tension: 0.25,
          pointRadius: 4
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        legend: {
          labels: {
            font: { family: 'IBM Plex Mono', size: 11 }
          }
        },
        tooltip: {
          callbacks: {
            footer: (items) => {
              const vals = items.map(i => i.parsed.y);
              const max = Math.max(...vals);
              const min = Math.min(...vals);
              return `Discrepancia entre agencias: ${(max - min).toFixed(1)} °C`;
            }
          }
        }
      },
      scales: {
        y: {
          min: 25,
          max: 40,
          title: { display: true, text: 'Temperatura Máxima (°C)', font: { family: 'IBM Plex Mono' } },
          grid: { color: 'rgba(150,150,150,0.1)' }
        },
        x: {
          grid: { color: 'rgba(150,150,150,0.1)' }
        }
      }
    }
  });
}

// MAPA IQUITOS (Slide 16)
function initMapIquitos() {
  if (mapIquitosInstance) return;
  const el = document.getElementById("mapIquitos");
  if (!el) return;

  const lat = -3.6903;
  const lon = -73.2556;

  mapIquitosInstance = L.map('mapIquitos', {
    zoomControl: true,
    attributionControl: false
  }).setView([lat, lon], 12);

  L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    maxZoom: 18
  }).addTo(mapIquitosInstance);

  L.circle([lat, lon], {
    color: '#0891B2',
    fillColor: '#0891B2',
    fillOpacity: 0.25,
    radius: 5000,
    weight: 2
  }).addTo(mapIquitosInstance);

  L.marker([lat, lon]).addTo(mapIquitosInstance)
    .bindPopup(`<b>Estación Punchana (SENAMHI)</b><br>COD: 103015<br>Elevación: 91 msnm<br>Iquitos, Loreto`)
    .openPopup();
}

// MAPA JAEN & HEATMAP SWITCHER (Slide 19)
function initMapJaen() {
  if (mapJaenInstance) return;
  const el = document.getElementById("mapJaen");
  if (!el) return;

  const lat = -5.6766;
  const lon = -78.7742;

  mapJaenInstance = L.map('mapJaen', {
    zoomControl: true,
    attributionControl: false
  }).setView([lat, lon], 14);

  L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    maxZoom: 18
  }).addTo(mapJaenInstance);

  // Polígono Parcela Cafetalera
  const coords = [
    [-5.6720, -78.7790],
    [-5.6725, -78.7690],
    [-5.6810, -78.7700],
    [-5.6800, -78.7800]
  ];

  jaenPolygon = L.polygon(coords, {
    color: '#FFFFFF',
    fillColor: 'transparent',
    fillOpacity: 0.1,
    weight: 2
  }).addTo(mapJaenInstance);

  L.marker([lat, lon]).addTo(mapJaenInstance)
    .bindPopup(`<b>Finca Cafetalera Jaén</b><br>Altitud: 1,100 msnm<br>Área: 12 ha<br>Cajamarca, Perú`)
    .openPopup();
}

function switchJaenLayer(layer) {
  currentJaenLayer = layer;
  const btns = ['btnLayerRgb', 'btnLayerNdvi', 'btnLayerEvi', 'btnLayerNdre'];
  btns.forEach(b => {
    const el = document.getElementById(b);
    if (el) el.classList.remove("active");
  });

  const tEl = document.getElementById("jaenLayerTitle");
  const dEl = document.getElementById("jaenLayerDesc");

  if (!jaenPolygon) return;

  if (layer === 'rgb') {
    document.getElementById("btnLayerRgb").classList.add("active");
    tEl.textContent = "🛰️ Imagen Satelital RGB Natural";
    dEl.textContent = "Vista óptica en color real de la finca cafetalera en Jaén (-5.6766°, -78.7742°, 1,100 msnm).";
    jaenPolygon.setStyle({ color: '#FFFFFF', fillColor: 'transparent', fillOpacity: 0.1, weight: 2 });
  } else if (layer === 'ndvi') {
    document.getElementById("btnLayerNdvi").classList.add("active");
    tEl.textContent = "🔴 Heatmap NDVI (Saturado en ~0.79)";
    dEl.textContent = "Muestra la parcela en un verde plano homogéneo saturado. Es incapaz de revelar el estrés hídrico interno de las plantas.";
    jaenPolygon.setStyle({ color: '#DC2626', fillColor: '#059669', fillOpacity: 0.7, weight: 3 });
  } else if (layer === 'evi') {
    document.getElementById("btnLayerEvi").classList.add("active");
    tEl.textContent = "🟢 Heatmap EVI (Biomasa Dinámica Foliar)";
    dEl.textContent = "Revela gradientes reales de vigor vegetal (0.35 a 0.58) eliminando la influencia del suelo y sin saturarse.";
    jaenPolygon.setStyle({ color: '#059669', fillColor: '#10B981', fillOpacity: 0.6, weight: 3 });
  } else if (layer === 'ndre') {
    document.getElementById("btnLayerNdre").classList.add("active");
    tEl.textContent = "🟣 Heatmap NDRE (Borde Rojo / Clorofila & Nitrógeno)";
    dEl.textContent = "Penetra la canopia profunda utilizando la banda B05 (705 nm). Diagnostica deficiencias de fertilización nitrogenada.";
    jaenPolygon.setStyle({ color: '#7C3AED', fillColor: '#8B5CF6', fillOpacity: 0.6, weight: 3 });
  }
}

// GRAFICO CASO A (Slide 18)
function initChartCasoA() {
  if (chartCasoAInstance) return;
  const ctx = document.getElementById("chartCasoA");
  if (!ctx) return;

  const rawCsv = document.getElementById("embeddedSenamhi7d").textContent.trim();
  const parsed = Papa.parse(rawCsv, { header: true, dynamicTyping: true });
  const rows = parsed.data;

  const labels = rows.map(r => r.fecha);
  const obs = rows.map(r => r.tmax_observada);
  const rf = rows.map(r => r.pred_random_forest);
  const xgb = rows.map(r => r.pred_xgboost);
  const lstm = rows.map(r => r.pred_lstm);
  const upper = rows.map(r => r.ci_upper_90);
  const lower = rows.map(r => r.ci_lower_90);

  chartCasoAInstance = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Observado Real',
          data: obs,
          borderColor: '#0F172A',
          backgroundColor: '#0F172A',
          borderWidth: 3,
          pointRadius: 6,
          pointBackgroundColor: '#0F172A'
        },
        {
          label: 'Random Forest (lags 1-14)',
          data: rf,
          borderColor: '#059669',
          backgroundColor: '#059669',
          borderWidth: 2.5,
          tension: 0.2,
          pointRadius: 4
        },
        {
          label: 'LSTM PyTorch',
          data: lstm,
          borderColor: '#2563EB',
          backgroundColor: '#2563EB',
          borderWidth: 2,
          tension: 0.2,
          hidden: true
        },
        {
          label: 'XGBoost (lags 1-14)',
          data: xgb,
          borderColor: '#D97706',
          backgroundColor: '#D97706',
          borderWidth: 2,
          tension: 0.2,
          pointRadius: 4,
          hidden: true
        },
        {
          label: 'Banda Superior 90% (+1.645σ)',
          data: upper,
          borderColor: 'transparent',
          backgroundColor: 'rgba(5, 150, 105, 0.12)',
          fill: '+1',
          pointRadius: 0
        },
        {
          label: 'Banda Inferior 90% (-1.645σ)',
          data: lower,
          borderColor: 'transparent',
          fill: false,
          pointRadius: 0
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          title: { display: true, text: 'Temperatura Máxima (°C)', font: { family: 'IBM Plex Mono' } },
          grid: { color: 'rgba(150,150,150,0.1)' }
        },
        x: {
          grid: { color: 'rgba(150,150,150,0.1)' }
        }
      },
      plugins: {
        legend: {
          labels: { font: { family: 'IBM Plex Mono', size: 11 } }
        }
      }
    }
  });
}

function toggleDatasetCasoA(type) {
  if (!chartCasoAInstance) return;
  const ds = chartCasoAInstance.data.datasets;
  if (type === 'observed') {
    ds[0].hidden = !ds[0].hidden;
  } else if (type === 'rf') {
    ds[1].hidden = !ds[1].hidden;
  } else if (type === 'lstm') {
    ds[2].hidden = !ds[2].hidden;
  } else if (type === 'xgb') {
    ds[3].hidden = !ds[3].hidden;
  }
  chartCasoAInstance.update();
  event.target.classList.toggle("active");
}

// GRAFICO CASO B (Slide 21)
function initChartCasoB() {
  if (chartCasoBInstance) return;
  const ctx = document.getElementById("chartCasoB");
  if (!ctx) return;

  const rawCsv = document.getElementById("embeddedCafe").textContent.trim();
  const parsed = Papa.parse(rawCsv, { header: true, dynamicTyping: true });
  const rows = parsed.data;

  const labels = rows.map(r => `Campaña ${r.campania}`);
  const obs = rows.map(r => r.rendimiento_obs_qq_ha);
  const fusion = rows.map(r => r.pred_modelo_fusion);
  const soloNdvi = rows.map(r => r.pred_solo_ndvi);

  chartCasoBInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Rendimiento Real Observado (qq/ha)',
          data: obs,
          backgroundColor: '#0F172A',
          borderRadius: 2,
          order: 2
        },
        {
          label: 'Fusión EVI + Clima (AgroVisión)',
          data: fusion,
          type: 'line',
          borderColor: '#059669',
          backgroundColor: '#059669',
          borderWidth: 3,
          tension: 0.1,
          pointRadius: 6,
          order: 1
        },
        {
          label: 'Modelo Solo NDVI (Saturado)',
          data: soloNdvi,
          type: 'line',
          borderColor: '#DC2626',
          backgroundColor: '#DC2626',
          borderWidth: 2.5,
          borderDash: [5, 5],
          pointRadius: 5,
          order: 1
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          min: 15,
          max: 28,
          title: { display: true, text: 'Rendimiento Cosecha (qq/ha)', font: { family: 'IBM Plex Mono' } },
          grid: { color: 'rgba(150,150,150,0.1)' }
        },
        x: {
          grid: { color: 'rgba(150,150,150,0.1)' }
        }
      },
      plugins: {
        legend: {
          labels: { font: { family: 'IBM Plex Mono', size: 11 } }
        }
      }
    }
  });
}

function toggleDatasetCasoB(type) {
  if (!chartCasoBInstance) return;
  const ds = chartCasoBInstance.data.datasets;
  if (type === 'observed') {
    ds[0].hidden = !ds[0].hidden;
  } else if (type === 'fusion') {
    ds[1].hidden = !ds[1].hidden;
  } else if (type === 'solo_ndvi') {
    ds[2].hidden = !ds[2].hidden;
  }
  chartCasoBInstance.update();
  event.target.classList.toggle("active");
}

// HYPERFRAMES ENGINE — storytelling secuenciado con GSAP Timelines.
// Cada diapositiva animada se revela en pasos (t=0 header, t=1 panel izq,
// t=2 panel der, t=3 KPIs/callouts). El presentador controla el ritmo con
// Replay / Paso 1-3 (botones) o teclas 1/2/3 (R = replay). Sin GSAP (CDN
// bloqueado/offline) hay fallback a visibilidad inmediata: nada queda oculto.
const HF_STEPS = {0:3, 1:4, 3:2, 5:3, 6:3, 7:3, 9:2, 10:3, 11:3, 14:2, 23:2};
let hfTimeline = null;
let hfSafety = null; // garantiza contenido visible aunque rAF vaya lento

function hfGroups(idx) {
  const slide = slides[idx];
  if (!slide) return [];
  const groups = [];
  const header = slide.querySelector(":scope > .slide-header");
  if (header) groups.push(header);
  const panels = slide.querySelectorAll(":scope .slide-body .panel");
  panels.forEach(p => groups.push(p));
  if (groups.length <= 1) {
    const body = slide.querySelector(":scope > .slide-body");
    if (body && !groups.includes(body)) groups.push(body);
  }
  return groups;
}

function hfEnsureControls(idx) {
  const slide = slides[idx];
  if (!slide || !(idx in HF_STEPS) || slide.querySelector(".hf-controls")) return;
  const n = HF_STEPS[idx];
  const bar = document.createElement("div");
  bar.className = "hf-controls";
  let btns = '<span class="hf-label">Narrar:</span>';
  btns += '<button class="pill-btn" data-hf="0">Replay</button>';
  for (let k = 1; k <= n; k++) btns += `<button class="pill-btn" data-hf="${k}">Paso ${k}</button>`;
  bar.innerHTML = btns;
  const body = slide.querySelector(":scope > .slide-body");
  if (body) body.prepend(bar);
  bar.querySelectorAll("[data-hf]").forEach(b => {
    b.addEventListener("click", (ev) => {
      ev.stopPropagation();
      const k = parseInt(b.getAttribute("data-hf"), 10);
      if (k === 0) hfReplay(idx); else hfStep(idx, k);
    });
  });
}

function hfRender(idx, upto) {
  // upto: nº de grupos visibles (0 = solo header visible tras entrar).
  const slide = slides[idx];
  const groups = hfGroups(idx);
  if (!slide || !groups.length) return;
  if (hfTimeline) { hfTimeline.kill(); hfTimeline = null; }
  const total = Math.max(1, Math.min(upto, groups.length));
  // Sub-pasos internos de diagramas SVG (estilo distill.pub): cada <g>
  // con data-hf-step="k" se revela cuando el paso k queda a la vista.
  const svgSteps = slide.querySelectorAll("[data-hf-step]");
  if (window.gsap) {
    gsap.set(groups, {opacity: 0, y: 16});
    hfTimeline = gsap.timeline();
    groups.slice(0, total).forEach((g, i) => {
      hfTimeline.to(g, {opacity: 1, y: 0, duration: 0.45, ease: "power2.out"}, i * 0.35);
    });
    if (svgSteps.length) {
      gsap.set(svgSteps, {opacity: 0});
      svgSteps.forEach(g => {
        const st = parseInt(g.getAttribute("data-hf-step"), 10) || 1;
        if (st <= upto) hfTimeline.to(g, {opacity: 1, duration: 0.4, ease: "power1.out"}, 0.3 + (st - 1) * 0.9);
      });
    }
    clearTimeout(hfSafety);
    if (total >= groups.length) {
      // autoplay/replay: nunca dejar contenido invisible si rAF va lento
      hfSafety = setTimeout(() => { if (hfTimeline) hfTimeline.progress(1); }, 2600);
    }
  } else {
    groups.forEach((g, i) => {
      g.style.opacity = i < total ? "1" : "0";
      g.style.transform = i < total ? "none" : "translateY(16px)";
    });
    svgSteps.forEach(g => {
      const st = parseInt(g.getAttribute("data-hf-step"), 10) || 1;
      g.style.opacity = st <= upto ? "1" : "0";
    });
  }
  slide.querySelectorAll(".hf-controls [data-hf]").forEach(b => {
    const k = parseInt(b.getAttribute("data-hf"), 10);
    b.classList.toggle("active", k === upto || (k === 0 && upto >= groups.length));
  });
}

function hfEnterSlide(idx) {
  hfEnsureControls(idx);
  if (!(idx in HF_STEPS)) return;
  hfRender(idx, hfGroups(idx).length); // autoplay: revela todo secuenciado
}

function hfStep(idx, k) {
  if (!(idx in HF_STEPS)) return;
  hfEnsureControls(idx);
  hfRender(idx, k);
}

function hfReplay(idx) {
  if (!(idx in HF_STEPS)) return;
  hfEnsureControls(idx);
  hfRender(idx, hfGroups(idx).length);
}

// INICIALIZACION
updateSlide(0);
</script>
</body>
</html>
"""

    out_path = Path("presentacion.html")
    out_path.write_text(html, encoding="utf-8")
    print(f"Deck avanzado de 25 diapositivas generado en: {out_path} ({out_path.stat().st_size / 1024:.1f} KB)")

if __name__ == "__main__":
    build_mega_deck()
