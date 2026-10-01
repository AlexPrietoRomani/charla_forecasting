"""
Generador del deck interactivo presentacion.html
Clona el diseño arquitectónico y minimalista de Data_Wizard (Chart.js + PapaParse + Leaflet),
con las 16 diapositivas de la charla de forecasting, cableado a los 3 CSVs reales y fallbacks embebidos.
"""

from pathlib import Path
import pandas as pd

def build_presentation():
    # Leer CSVs para fallbacks
    senamhi_7d_csv = Path("data/senamhi_forecast_7d.csv").read_text(encoding="utf-8").strip()
    cafe_csv = Path("data/cafe_ndvi_rendimiento.csv").read_text(encoding="utf-8").strip()
    
    # Tomar los últimos 180 días de senamhi_diario para el fallback embebido (<30 KB)
    df_senamhi = pd.read_csv("data/senamhi_diario.csv")
    senamhi_diario_sub = df_senamhi.tail(180).to_csv(index=False).strip()

    html_content = f"""<!DOCTYPE html>
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
  :root {{
    --bg-light: #FFFFFF;
    --bg-light-panel: #F6F6F6;
    --text-light-main: #000000;
    --text-light-mute: #444444;
    --text-light-faint: #777777;
    --line-light: #000000;
    --line-light-faint: #E2E2E2;

    --bg-dark: #07090E;
    --bg-dark-panel: #0F141C;
    --text-dark-main: #F3F4F6;
    --text-dark-mute: #9CA3AF;
    --text-dark-faint: #4B5563;
    --line-dark: #374151;
    --line-dark-faint: #1F2937;

    --accent-blue: #2563EB;
    --accent-amber: #D97706;
    --accent-red: #DC2626;
    --accent-green: #059669;
    --accent-purple: #7C3AED;

    --stage-pad: clamp(24px, 5vw, 80px);
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; border-radius: 0 !important; }}
  html, body {{ height: 100%; }}

  body {{
    background: var(--bg-light);
    color: var(--text-light-main);
    font-family: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, sans-serif;
    overflow: hidden;
    -webkit-font-smoothing: antialiased;
    transition: background 0.3s ease, color 0.3s ease;
  }}

  body::before {{
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    background-size: 40px 40px;
    background-image: 
      linear-gradient(to right, rgba(0,0,0,0.03) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(0,0,0,0.03) 1px, transparent 1px);
  }}

  body.dark-active {{
    background: var(--bg-dark);
    color: var(--text-dark-main);
  }}
  body.dark-active::before {{
    background-image: 
      linear-gradient(to right, rgba(255,255,255,0.03) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255,255,255,0.03) 1px, transparent 1px);
  }}

  .mono {{ font-family: "IBM Plex Mono", monospace; font-variant-numeric: tabular-nums; }}
  .display {{ font-family: "Space Grotesk", sans-serif; font-weight: 700; }}

  /* Layout */
  .deck {{ position: fixed; inset: 0; left: 60px; z-index: 1; transition: left 0.3s ease; }}
  
  .slide {{
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
    max-width: 1350px;
    margin: 0 auto;
  }}
  .slide.active {{ opacity: 1; visibility: visible; transform: none; }}

  /* Sidebar */
  .sidebar {{
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
    transition: width 0.25s ease;
  }}
  body.dark-active .sidebar {{
    background: var(--bg-dark-panel);
    border-right-color: var(--line-dark-faint);
  }}
  .sidebar-top, .sidebar-bottom {{ display: flex; flex-direction: column; align-items: center; gap: 12px; }}
  .theme-btn, .nav-icon-btn {{
    background: transparent;
    border: 1px solid var(--line-light-faint);
    color: inherit;
    width: 40px; height: 40px;
    display: flex; align-items: center; justify-content: center;
    cursor: pointer;
    font-size: 14px;
    transition: background 0.2s, border-color 0.2s;
  }}
  body.dark-active .theme-btn, body.dark-active .nav-icon-btn {{
    border-color: var(--line-dark-faint);
  }}
  .theme-btn:hover, .nav-icon-btn:hover {{
    background: rgba(0,0,0,0.05);
    border-color: var(--line-light);
  }}
  body.dark-active .theme-btn:hover, body.dark-active .nav-icon-btn:hover {{
    background: rgba(255,255,255,0.05);
    border-color: var(--line-dark);
  }}

  /* Typography */
  .tag {{
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--accent-blue);
    margin-bottom: 0.5rem;
    display: inline-block;
  }}
  h1 {{ font-size: clamp(2rem, 4.5vw, 3.8rem); line-height: 1.08; letter-spacing: -0.02em; margin-bottom: 1.2rem; }}
  h2 {{ font-size: clamp(1.5rem, 3vw, 2.4rem); line-height: 1.15; letter-spacing: -0.01em; margin-bottom: 1rem; }}
  h3 {{ font-size: 1.2rem; font-weight: 600; margin-bottom: 0.5rem; }}
  .lead {{ font-size: clamp(1rem, 1.8vw, 1.35rem); line-height: 1.5; color: var(--text-light-mute); max-width: 950px; margin-bottom: 1.5rem; }}
  body.dark-active .lead {{ color: var(--text-dark-mute); }}

  /* Cards & Grids */
  .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 1rem; }}
  .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 1rem; }}
  .grid-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-top: 1rem; }}

  .card {{
    background: var(--bg-light-panel);
    border: 1px solid var(--line-light-faint);
    padding: 20px;
    transition: border-color 0.2s, transform 0.2s;
  }}
  body.dark-active .card {{
    background: var(--bg-dark-panel);
    border-color: var(--line-dark-faint);
  }}
  .card:hover {{ border-color: var(--accent-blue); }}

  .stat-val {{ font-family: "Space Grotesk", sans-serif; font-size: 2.2rem; font-weight: 700; margin-bottom: 4px; }}
  .stat-label {{ font-size: 0.85rem; color: var(--text-light-mute); text-transform: uppercase; letter-spacing: 0.05em; }}
  body.dark-active .stat-label {{ color: var(--text-dark-mute); }}

  /* Interactive Demo Canvas */
  .chart-container {{
    position: relative;
    width: 100%;
    height: 380px;
    background: var(--bg-light-panel);
    border: 1px solid var(--line-light-faint);
    padding: 16px;
    margin-top: 1rem;
  }}
  body.dark-active .chart-container {{
    background: var(--bg-dark-panel);
    border-color: var(--line-dark-faint);
  }}

  /* Table styling */
  table.data-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
    font-size: 0.88rem;
  }}
  table.data-table th, table.data-table td {{
    padding: 10px 14px;
    border: 1px solid var(--line-light-faint);
    text-align: left;
  }}
  body.dark-active table.data-table th, body.dark-active table.data-table td {{
    border-color: var(--line-dark-faint);
  }}
  table.data-table th {{
    background: var(--bg-light-panel);
    font-weight: 600;
  }}
  body.dark-active table.data-table th {{
    background: var(--bg-dark-panel);
  }}

  /* Navigation Footer Controls */
  .slide-footer {{
    position: fixed;
    bottom: 20px; right: 30px;
    display: flex; align-items: center; gap: 14px;
    z-index: 100;
  }}
  .slide-counter {{ font-family: "IBM Plex Mono", monospace; font-size: 0.9rem; font-weight: 600; }}
  .nav-btn {{
    padding: 8px 16px;
    background: var(--text-light-main);
    color: var(--bg-light);
    border: 1px solid var(--text-light-main);
    cursor: pointer;
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.85rem;
    font-weight: 600;
    transition: opacity 0.2s;
  }}
  body.dark-active .nav-btn {{
    background: var(--text-dark-main);
    color: var(--bg-dark);
    border-color: var(--text-dark-main);
  }}
  .nav-btn:hover {{ opacity: 0.85; }}

  /* Badges */
  .badge {{
    display: inline-block;
    padding: 2px 8px;
    font-size: 0.75rem;
    font-family: "IBM Plex Mono", monospace;
    font-weight: 600;
    margin-right: 6px;
  }}
  .badge-blue {{ background: rgba(37, 99, 235, 0.15); color: var(--accent-blue); }}
  .badge-green {{ background: rgba(5, 150, 105, 0.15); color: var(--accent-green); }}
  .badge-amber {{ background: rgba(217, 119, 6, 0.15); color: var(--accent-amber); }}
  .badge-red {{ background: rgba(220, 38, 38, 0.15); color: var(--accent-red); }}
</style>
</head>
<body>

<!-- SIDEBAR -->
<div class="sidebar">
  <div class="sidebar-top">
    <button class="nav-icon-btn mono" id="tocBtn" title="Inicio (Home)">01</button>
  </div>
  <div class="sidebar-bottom">
    <button class="theme-btn" id="themeToggle" title="Cambiar Tema (Claro/Oscuro)">🌓</button>
    <button class="theme-btn mono" id="fsBtn" title="Pantalla Completa (F)">⛶</button>
  </div>
</div>

<!-- FOOTER CONTROLS -->
<div class="slide-footer">
  <span class="slide-counter mono" id="slideNum">01 / 16</span>
  <button class="nav-btn" id="prevBtn">← PREV</button>
  <button class="nav-btn" id="nextBtn">NEXT →</button>
</div>

<!-- DECK CONTAINER -->
<div class="deck">

  <!-- SLIDE 1: PORTADA -->
  <section class="slide active" data-title="Portada">
    <span class="tag">Charla Técnica · Forecasting & Machine Learning</span>
    <h1 class="display">¿Puede la IA predecir el futuro?</h1>
    <p class="lead">Lecciones de forecasting, teledetección multiespectral y cuantificación de incertidumbre desde el mundo real.</p>
    <div class="grid-3" style="max-width: 900px; margin-top: 2rem;">
      <div class="card">
        <div class="stat-label">Caso A · Clima</div>
        <div style="font-weight: 600; margin-top: 4px;">SENAMHI Iquitos</div>
        <div style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 4px;">7 años de datos (2019–2025). 5 niveles de modelos.</div>
      </div>
      <div class="card">
        <div class="stat-label">Caso B · Agro</div>
        <div style="font-weight: 600; margin-top: 4px;">Café & Sentinel-2</div>
        <div style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 4px;">Fusión multimodal (EVI + Clima) vs saturación de NDVI.</div>
      </div>
      <div class="card">
        <div class="stat-label">Tesis Central</div>
        <div style="font-weight: 600; margin-top: 4px;">Decidir con Incertidumbre</div>
        <div style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 4px;">La IA no adivina certezas; acota riesgos para decidir mejor.</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MAPA 4 FAMILIAS -->
  <section class="slide" data-title="Familias">
    <span class="tag">Taxonomía del Forecasting</span>
    <h2>El mapa de las 4 familias de modelos</h2>
    <p class="lead">No existe un "mejor modelo universal". Cada familia resuelve un trade-off específico de volumen de datos, interpretabilidad y costo operacional.</p>
    <div class="grid-4">
      <div class="card">
        <span class="badge badge-blue">Familia 1</span>
        <h3 style="margin-top: 8px;">ML Tabular</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); line-height: 1.45;">RF, ExtraTrees, XGBoost, LightGBM.<br><b>Fuerza:</b> Domina con <100K filas y lags bien diseñados.<br><b>Riesgo:</b> No extrapola tendencias.</p>
      </div>
      <div class="card">
        <span class="badge badge-amber">Familia 2</span>
        <h3 style="margin-top: 8px;">Series Clásicas</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); line-height: 1.45;">ARIMA, SARIMA, ETS, Prophet.<br><b>Fuerza:</b> Horizonte corto, 1 sola serie, explicabilidad matemática pura.<br><b>Riesgo:</b> Difícil cruzar 50 exógenas.</p>
      </div>
      <div class="card">
        <span class="badge badge-purple">Familia 3</span>
        <h3 style="margin-top: 8px;">DL Secuencial</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); line-height: 1.45;">LSTM, TFT, N-BEATS, PatchTST.<br><b>Fuerza:</b> Series cruzadas masivas (retail, miles de tiendas).<br><b>Riesgo:</b> Sobreajuste severo en series cortas.</p>
      </div>
      <div class="card">
        <span class="badge badge-green">Familia 4</span>
        <h3 style="margin-top: 8px;">Visión + Fusión</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); line-height: 1.45;">Sentinel-2, YOLOv12, SAM 2.1.<br><b>Fuerza:</b> El contexto biofísico real (dosel, agua, vigor foliar).<br><b>Riesgo:</b> Nubosidad y costo de descarga.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: ML TABULAR -->
  <section class="slide" data-title="ML Tabular">
    <span class="tag">Familia 1 · Machine Learning Tabular</span>
    <h2>Por qué los árboles siguen ganando en tablas</h2>
    <p class="lead">Grinsztajn et al. (NeurIPS 2022) demostraron que los árboles de decisión baten sistemáticamente al deep learning en datos tabulares. ¿La razón? Invarianza a transformaciones monótonas y manejo nativo de fronteras no lineales.</p>
    <table class="data-table">
      <thead>
        <tr>
          <th>Algoritmo</th>
          <th>Paper Base</th>
          <th>Velocidad de Ajuste</th>
          <th>Manejo de Lags</th>
          <th>Cuándo Usarlo</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><b>Random Forest</b></td>
          <td>Breiman (2001)</td>
          <td>Media (paralelo CPU)</td>
          <td>Excelente (robusto a ruido)</td>
          <td>Baseline sólido, casi imposible de arruinar por hiperparámetros.</td>
        </tr>
        <tr>
          <td><b>ExtraTrees</b></td>
          <td>Geurts et al. (2006)</td>
          <td>Muy Alta</td>
          <td>Excelente (splits aleatorios)</td>
          <td>Menor varianza que RF con series ruidosas como lluvia o viento.</td>
        </tr>
        <tr>
          <td><b>XGBoost</b></td>
          <td>Chen & Guestrin (2016)</td>
          <td>Alta</td>
          <td>Excelente (regularización L1/L2)</td>
          <td>Máxima precisión cuando hay interacciones complejas de features.</td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- SLIDE 4: SERIES CLASICAS -->
  <section class="slide" data-title="Series Clásicas">
    <span class="tag">Familia 2 · Series Temporales Clásicas</span>
    <h2>ARIMA, ETS y Prophet: la elegancia de lo interpretable</h2>
    <p class="lead">Antes de entrenar redes neuronales o ensambles, un baseline autorregresivo descompone la serie en componentes físicas: tendencia, ciclo y estacionalidad.</p>
    <div class="grid-3">
      <div class="card">
        <h3>ARIMA / SARIMA</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">
          Box & Jenkins (1970). Asume estacionariedad previa mediante diferenciación $(d)$. Modela autocorrelaciones pasadas $(p)$ y choques de medias móviles $(q)$. Ideal para horizontes de 1 a 3 pasos.
        </p>
      </div>
      <div class="card">
        <h3>Suavizado Exponencial (ETS)</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">
          Hyndman et al. (2002). Asigna pesos exponencialmente decrecientes a observaciones pasadas. Espacio de estados riguroso para intervalos analíticos exactos.
        </p>
      </div>
      <div class="card">
        <h3>Prophet</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">
          Taylor & Letham (Facebook, 2017). Modelo aditivo con puntos de quiebre (*changepoints*) automáticos y feriados. Resistente a valores atípicos y cambios estructurales.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: DL SECUENCIAL -->
  <section class="slide" data-title="DL Secuencial">
    <span class="tag">Familia 3 · Deep Learning Secuencial</span>
    <h2>De LSTM a Transformers: ¿cuándo vale la pena?</h2>
    <p class="lead">El deep learning en series temporales sólo supera al ML tabular cuando existe <b>transferencia de patrones entre miles de series correlacionadas</b> (M5 Competition, Walmart, demanda eléctrica nacional).</p>
    <div class="grid-3">
      <div class="card">
        <h3>LSTM / GRU (1997)</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">
          Puertas de olvido (*forget gates*) para memoria a mediano plazo. En series univariadas chicas suele empatar con ARIMA pero con 100x costo computacional.
        </p>
      </div>
      <div class="card">
        <h3>Temporal Fusion Transformer (2021)</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">
          Lim et al. (Google). Mecanismos de atención que seleccionan variables exógenas estáticas y dinámicas. Interpretabilidad de qué variable influye en qué paso futuro.
        </p>
      </div>
      <div class="card">
        <h3>PatchTST (2023)</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">
          Nie et al. Segmenta la serie en parches (*patches*) sub-secuenciales. Reduce la complejidad cuadrática del Transformer y captura dependencias semánticas locales.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: ZERO SHOT -->
  <section class="slide" data-title="Foundation Zero-shot">
    <span class="tag">Nueva Frontera · Foundation Models</span>
    <h2>Modelos Zero-Shot: Forecasting sin reentrenar</h2>
    <p class="lead">¿Qué pasa si aplicamos la lógica de los LLMs al tiempo? Modelos pre-entrenados en miles de millones de puntos temporales que infieren en frío (*cold-start*).</p>
    <div class="grid-3">
      <div class="card">
        <span class="badge badge-blue">Amazon</span>
        <h3 style="margin-top: 8px;">Chronos (2024)</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute);">Ansari et al. Tokeniza los valores numéricos mediante escalamiento y cuantización. Utiliza arquitectura T5 preentrenada en TSGym.</p>
      </div>
      <div class="card">
        <span class="badge badge-amber">Google Research</span>
        <h3 style="margin-top: 8px;">TimesFM (2024)</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute);">Das et al. Decoder-only Transformer optimizado para parches temporales. Extraordinario desempeño en series con periodicidades limpias.</p>
      </div>
      <div class="card">
        <span class="badge badge-purple">Salesforce / Nixtla</span>
        <h3 style="margin-top: 8px;">Moirai & TimeGPT</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute);">Atención multimodal en cualquier frecuencia temporal (minutos, días, meses) con pronóstico probabilístico instantáneo.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: CV EN EL AGRO -->
  <section class="slide" data-title="Visión Computacional">
    <span class="tag">Visión por Computador · Del Píxel al Pronóstico</span>
    <h2>Cómo las imágenes predicen cosechas</h2>
    <p class="lead">La visión artificial permite pasar del conteo destructivo manual a la cuantificación volumétrica automatizada sobre ortomosaicos de drones y cámaras en campo.</p>
    <div class="grid-3">
      <div class="card">
        <h3>Detección: YOLOv12</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">
          Mecanismo de atención por área (A2). Inferencia en tiempo real (1.6 ms en T4) para conteo de plantas, flores o racimos con mAP@0.5 superior al 89%.
        </p>
      </div>
      <div class="card">
        <h3>Segmentación: SAM 2.1</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">
          Delimitación fina de copa (*canopy coverage*). Pasa de 9.7 segundos por máscara manual a 1.6 segundos con prompts automáticos.
        </p>
      </div>
      <div class="card">
        <h3>Representación: DINOv2</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">
          Auto-supervisado (Meta AI). Extrae mapas de características inmunes a cambios de iluminación o polvo foliar sin requerir fine-tuning intensivo.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: FUSION SATELITAL -->
  <section class="slide" data-title="Fusión Multimodal">
    <span class="tag">Herencia AgroVisión · Fusión Multimodal</span>
    <h2>Por qué el satélite solo no alcanza: Fusión Espectro + Clima</h2>
    <p class="lead">El error más frecuente en teledetección es tomar el NDVI satelital de forma aislada. La literatura (Muruganantham 2022, Barbosa 2021) demuestra que la reflectancia adquiere poder predictivo sólo al cruzarse con el balance hídrico.</p>
    <div class="grid-3">
      <div class="card">
        <div class="stat-val" style="color: var(--accent-red);">5.4%</div>
        <div class="stat-label">Error con Solo NDVI</div>
        <div style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">El NDVI satura en dosel denso de café (LAI>3) y no detecta estrés térmico.</div>
      </div>
      <div class="card">
        <div class="stat-val" style="color: var(--accent-green);">4.4%</div>
        <div class="stat-label">Error con Fusión (EVI + Clima)</div>
        <div style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">EVI no se satura y el déficit hídrico en llenado predice la caída real de quintales.</div>
      </div>
      <div class="card">
        <div class="stat-val" style="color: var(--accent-blue);">+18.5%</div>
        <div class="stat-label">Reducción del Error</div>
        <div style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">Ventanas fenológicas: Floración (Ago-Oct) y Llenado (Nov-Feb).</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: DEMO CLIMA INTRO -->
  <section class="slide" data-title="Caso A: SENAMHI">
    <span class="tag">Caso Real A · Clima SENAMHI</span>
    <h2>Caso A: Pronóstico diario de T° máxima en Iquitos</h2>
    <p class="lead">Estación Punchana (Loreto, selva baja, 91 msnm). Datos oficiales de SENAMHI descargados con <b>garua</b>: 2,557 días (2019–2025). Target: T° máxima diaria a 7 días.</p>
    <div class="grid-4">
      <div class="card">
        <div class="stat-val mono">2,557</div>
        <div class="stat-label">Días evaluados</div>
        <div style="font-size: 0.8rem; color: var(--text-light-mute); margin-top: 4px;">7 años completos sin fuga</div>
      </div>
      <div class="card">
        <div class="stat-val mono" style="color: var(--accent-blue);">2.10 °C</div>
        <div class="stat-label">RMSE LSTM (PyTorch)</div>
        <div style="font-size: 0.8rem; color: var(--text-light-mute); margin-top: 4px;">Mejor modelo global (+9.4%)</div>
      </div>
      <div class="card">
        <div class="stat-val mono" style="color: var(--accent-green);">2.16 °C</div>
        <div class="stat-label">RMSE ExtraTrees</div>
        <div style="font-size: 0.8rem; color: var(--text-light-mute); margin-top: 4px;">Mejor tabular (+6.4%)</div>
      </div>
      <div class="card">
        <div class="stat-val mono" style="color: var(--accent-amber);">2.31 °C</div>
        <div class="stat-label">RMSE Naive Baseline</div>
        <div style="font-size: 0.8rem; color: var(--text-light-mute); margin-top: 4px;">Persistencia estacional</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: DEMO 1 EN VIVO -->
  <section class="slide" data-title="Demo Clima en Vivo">
    <span class="tag">Demo en Vivo · Datos SENAMHI</span>
    <h2>Pronóstico Multi-modelo a 7 días con Bandas 90%</h2>
    <p class="lead">Gráfico interactivo leyendo en vivo <code>data/senamhi_forecast_7d.csv</code>. Obsérvese cómo las bandas del 90% capturan la caída abrupta de temperatura por frentes convectivos.</p>
    <div class="chart-container">
      <canvas id="chartClima7d"></canvas>
    </div>
  </section>

  <!-- SLIDE 11: DEMO CAFE INTRO -->
  <section class="slide" data-title="Caso B: Café & Satélite">
    <span class="tag">Caso Real B · Rendimiento de Café</span>
    <h2>Caso B: Rendimiento (qq/ha) con Índices Sentinel-2</h2>
    <p class="lead">Zona cafetalera de Jaén (Cajamarca). Extracción de series multiespectrales (NDVI, EVI, NDRE) y balance hídrico Open-Meteo para las campañas 2020 a 2025.</p>
    <div class="grid-3">
      <div class="card">
        <h3 style="color: var(--accent-red);">La trampa del NDVI</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">
          En café adulto, el NDVI se satura en <b>0.788</b> todos los años. Si un productor confía solo en NDVI, no ve la caída de rendimiento de 34 a 29 qq/ha provocada por estrés térmico.
        </p>
      </div>
      <div class="card">
        <h3 style="color: var(--accent-green);">La solución EVI + NDRE</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">
          El <b>EVI</b> (Huete 2002) y el <b>NDRE</b> (Red-Edge) no se saturan. Durante el llenado de fruto (Nov-Feb) capturan la fotosíntesis activa y la reserva de nitrógeno foliar.
        </p>
      </div>
      <div class="card">
        <h3 style="color: var(--accent-blue);">Ventanas Fenológicas</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">
          La correlación aparece cuando separamos <b>Floración (Ago-Oct)</b> de <b>Llenado (Nov-Feb)</b>. La temperatura máxima en floración penaliza drásticamente el cuajado.
        </p>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: DEMO 2 EN VIVO -->
  <section class="slide" data-title="Demo Café en Vivo">
    <span class="tag">Demo en Vivo · Datos Agroclimáticos</span>
    <h2>Campañas 2020–2025: Rendimiento Real vs Modelos</h2>
    <p class="lead">Comparación interactiva leyendo <code>data/cafe_ndvi_rendimiento.csv</code> con validación estricta <i>Leave-One-Year-Out</i> (LOYO).</p>
    <div class="chart-container">
      <canvas id="chartCafeRend"></canvas>
    </div>
  </section>

  <!-- SLIDE 13: LECCIONES MUNDO REAL -->
  <section class="slide" data-title="Lecciones Clave">
    <span class="tag">Síntesis Metodológica</span>
    <h2>5 Lecciones desde las trincheras del forecasting</h2>
    <div class="grid-2" style="margin-top: 1rem;">
      <div class="card">
        <h3>1. La validación aleatoria (shuffle) es autoengaño</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 4px;">En series de tiempo, hacer split aleatorio filtra el futuro en el pasado (data leakage). Siempre usar <code>TimeSeriesSplit</code> o Leave-One-Year-Out.</p>
      </div>
      <div class="card">
        <h3>2. Árboles antes que Deep Learning</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 4px;">Un Random Forest o ExtraTrees con lags y rolling features bate al 90% de las arquitecturas complejas en series tabulares individuales.</p>
      </div>
      <div class="card">
        <h3>3. El costo del error casi nunca es simétrico</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 4px;">Una falsa alarma de lluvia cuesta poco; un falso negativo en helada o sequía destruye la cosecha entera. Optimizar la función de pérdida al negocio.</p>
      </div>
      <div class="card">
        <h3>4. El índice satelital debe responder a la biofísica</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 4px;">NDVI satura con LAI>3. En cultivos leñosos densos (café, cítricos, arándano), EVI y NDRE son obligatorios.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 14: ARBOL DE DECISION -->
  <section class="slide" data-title="Receta de Decisión">
    <span class="tag">Guía de Ingeniería</span>
    <h2>¿Qué modelo utilizar según el escenario?</h2>
    <p class="lead">Árbol de decisiones técnico para producción:</p>
    <table class="data-table">
      <thead>
        <tr>
          <th>Situación / Datos Disponibles</th>
          <th>Modelo Recomendado</th>
          <th>Justificación Técnica</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Una sola serie, pocos datos (< 500 puntos)</td>
          <td><b>ARIMA / ETS / Naive</b></td>
          <td>Evita sobreajuste; no requiere estimar cientos de pesos.</td>
        </tr>
        <tr>
          <td>Serie univariada o multivariada con lags (< 100K filas)</td>
          <td><b>Random Forest / ExtraTrees / XGBoost</b></td>
          <td>Excelente manejo de no linealidades y exógenas con costo bajo.</td>
        </tr>
        <tr>
          <td>Miles de series cruzadas con jerarquías (retail / energía)</td>
          <td><b>Temporal Fusion Transformer (TFT) / N-HiTS</b></td>
          <td>Aprende representaciones globales y patrones compartidos.</td>
        </tr>
        <tr>
          <td>Nueva serie sin historial previo (Cold Start)</td>
          <td><b>Chronos / TimesFM (Zero-shot)</b></td>
          <td>Inferencia inmediata sin etapa de entrenamiento.</td>
        </tr>
        <tr>
          <td>Predicción agrícola / cobertura vegetal</td>
          <td><b>Fusión Multimodal (EVI + Clima por fenología)</b></td>
          <td>Acopla la reflectancia física con el balance hídrico.</td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- SLIDE 15: CIERRE Y FILOSOFIA -->
  <section class="slide" data-title="Cierre">
    <span class="tag">Conclusión</span>
    <h1 class="display" style="font-size: clamp(2rem, 4vw, 3.2rem);">La IA no predice el futuro.<br><span style="color: var(--accent-blue);">Cuantifica incertidumbre.</span></h1>
    <p class="lead" style="max-width: 850px; margin-top: 1.5rem;">
      El valor de un sistema de pronóstico no reside en una precisión mágica del 100%, sino en dotar al tomador de decisiones de <b>intervalos de confianza honestos</b> para gestionar riesgos operacionales.
    </p>
    <div style="margin-top: 2rem; padding: 16px 24px; border-left: 3px solid var(--accent-green); background: var(--bg-light-panel); max-width: 800px;">
      <p style="font-size: 0.95rem; font-style: italic;">
        "Todos los modelos están equivocados, pero algunos son útiles." — George E. P. Box
      </p>
    </div>
  </section>

  <!-- SLIDE 16: GRACIAS Y REFERENCIAS -->
  <section class="slide" data-title="Referencias">
    <span class="tag">Código Abierto & Bibliografía</span>
    <h2>Gracias por su atención</h2>
    <p class="lead">Todo el código, notebooks y datasets limpios están disponibles en el repositorio:</p>
    <div class="grid-2" style="max-width: 900px; margin-top: 1rem;">
      <div class="card">
        <h3>Repositorio & Demos</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">
          • Notebooks reproducibles en <code>notebooks/</code><br>
          • Pipeline satelital y SENAMHI en <code>scripts/</code><br>
          • Bibliografía completa consolidada en <code>refs.bib</code>
        </p>
      </div>
      <div class="card">
        <h3>Referencias Clave</h3>
        <p style="font-size: 0.85rem; color: var(--text-light-mute); margin-top: 6px;">
          • Huete et al. (2002) - Fundamentos EVI/MODIS.<br>
          • Grinsztajn et al. (2022) - Why Tree Models Outperform DL.<br>
          • Barbosa et al. (2021) - Smart Coffee Yield Prediction.<br>
          • Ansari et al. (2024) - Chronos Time Series Model.
        </p>
      </div>
    </div>
  </section>

</div>

<!-- FALLBACK SCRIPTS EMBEBIDOS PARA OPERACIÓN OFFLINE -->
<script type="text/csv" id="senamhi-7d-fallback">
{senamhi_7d_csv}
</script>

<script type="text/csv" id="cafe-fallback">
{cafe_csv}
</script>

<script type="text/csv" id="senamhi-diario-fallback">
{senamhi_diario_sub}
</script>

<!-- SCRIPT DE CONTROL Y VISUALIZACIÓN -->
<script>
const slides = Array.from(document.querySelectorAll('.slide'));
let cur = 0;
const slideNum = document.getElementById('slideNum');
let chartClimaInstance = null;
let chartCafeInstance = null;

function updateSlide(idx) {{
  if(idx < 0) idx = 0;
  if(idx >= slides.length) idx = slides.length - 1;
  cur = idx;
  slides.forEach((s, i) => s.classList.toggle('active', i === cur));
  slideNum.textContent = String(cur + 1).padStart(2, '0') + ' / ' + String(slides.length).padStart(2, '0');
  
  // Renderizar gráficos cuando aparezca la slide
  if(cur === 9 && !chartClimaInstance) {{
    initClimaChart();
  }}
  if(cur === 11 && !chartCafeInstance) {{
    initCafeChart();
  }}
}}

document.getElementById('nextBtn').onclick = () => updateSlide(cur + 1);
document.getElementById('prevBtn').onclick = () => updateSlide(cur - 1);
document.getElementById('tocBtn').onclick = () => updateSlide(0);

window.addEventListener('keydown', e => {{
  if(['ArrowRight', 'PageDown', ' '].includes(e.key)) {{ e.preventDefault(); updateSlide(cur + 1); }}
  else if(['ArrowLeft', 'PageUp'].includes(e.key)) {{ e.preventDefault(); updateSlide(cur - 1); }}
  else if(e.key === 'Home') updateSlide(0);
  else if(e.key === 'End') updateSlide(slides.length - 1);
  else if(e.key === 'f' || e.key === 'F') {{
    if(!document.fullscreenElement) document.documentElement.requestFullscreen();
    else document.exitFullscreen();
  }}
}});

// Tema Oscuro / Claro
const themeToggle = document.getElementById('themeToggle');
themeToggle.onclick = () => {{
  document.body.classList.toggle('dark-active');
  if(chartClimaInstance) {{ chartClimaInstance.destroy(); chartClimaInstance = null; initClimaChart(); }}
  if(chartCafeInstance) {{ chartCafeInstance.destroy(); chartCafeInstance = null; initCafeChart(); }}
}};

document.getElementById('fsBtn').onclick = () => {{
  if(!document.fullscreenElement) document.documentElement.requestFullscreen();
  else document.exitFullscreen();
}};

// Carga de datos con fallback
async function loadData(url, fallbackId) {{
  try {{
    const res = await fetch(url);
    if(res.ok) {{
      const text = await res.text();
      return Papa.parse(text, {{ header: true, dynamicTyping: true }}).data;
    }}
  }} catch(e) {{
    console.warn('Cargando fallback embebido para:', url);
  }}
  const fbText = document.getElementById(fallbackId).textContent.trim();
  return Papa.parse(fbText, {{ header: true, dynamicTyping: true }}).data;
}}

// Gráfico Caso A: Clima 7 días
async function initClimaChart() {{
  const data = await loadData('data/senamhi_forecast_7d.csv', 'senamhi-7d-fallback');
  const validData = data.filter(d => d.fecha);
  const labels = validData.map(d => d.fecha);
  const isDark = document.body.classList.contains('dark-active');
  const textColor = isDark ? '#9CA3AF' : '#444444';
  const gridColor = isDark ? 'rgba(255,255,255,0.06)' : 'rgba(0,0,0,0.06)';

  const ctx = document.getElementById('chartClima7d').getContext('2d');
  chartClimaInstance = new Chart(ctx, {{
    type: 'line',
    data: {{
      labels: labels,
      datasets: [
        {{
          label: 'Observado SENAMHI',
          data: validData.map(d => d.tmax_observada),
          borderColor: '#059669',
          backgroundColor: '#059669',
          borderWidth: 3,
          pointRadius: 5,
        }},
        {{
          label: 'ExtraTrees Regressor',
          data: validData.map(d => d.pred_random_forest),
          borderColor: '#2563EB',
          borderWidth: 2,
          pointRadius: 4,
          borderDash: [4, 4]
        }},
        {{
          label: 'LSTM (PyTorch)',
          data: validData.map(d => d.pred_lstm),
          borderColor: '#7C3AED',
          borderWidth: 2,
          pointRadius: 4,
        }},
        {{
          label: 'Naive Persistencia',
          data: validData.map(d => d.pred_naive),
          borderColor: '#D97706',
          borderWidth: 1.5,
          borderDash: [6, 4],
          pointRadius: 3
        }},
        {{
          label: 'Banda Superior 90%',
          data: validData.map(d => d.ci_upper_90),
          borderColor: 'transparent',
          backgroundColor: 'rgba(37, 99, 235, 0.12)',
          fill: '+1',
          pointRadius: 0
        }},
        {{
          label: 'Banda Inferior 90%',
          data: validData.map(d => d.ci_lower_90),
          borderColor: 'transparent',
          backgroundColor: 'rgba(37, 99, 235, 0.12)',
          fill: false,
          pointRadius: 0
        }}
      ]
    }},
    options: {{
      responsive: true,
      maintainAspectRatio: false,
      scales: {{
        x: {{ ticks: {{ color: textColor }}, grid: {{ color: gridColor }} }},
        y: {{ 
          title: {{ display: true, text: 'Temperatura Máxima (°C)', color: textColor }},
          ticks: {{ color: textColor }},
          grid: {{ color: gridColor }}
        }}
      }},
      plugins: {{
        legend: {{ labels: {{ color: textColor, font: {{ family: 'IBM Plex Sans' }} }} }}
      }}
    }}
  }});
}}

// Gráfico Caso B: Rendimiento Café
async function initCafeChart() {{
  const data = await loadData('data/cafe_ndvi_rendimiento.csv', 'cafe-fallback');
  const validData = data.filter(d => d.campania);
  const labels = validData.map(d => 'Campaña ' + d.campania);
  const isDark = document.body.classList.contains('dark-active');
  const textColor = isDark ? '#9CA3AF' : '#444444';
  const gridColor = isDark ? 'rgba(255,255,255,0.06)' : 'rgba(0,0,0,0.06)';

  const ctx = document.getElementById('chartCafeRend').getContext('2d');
  chartCafeInstance = new Chart(ctx, {{
    type: 'bar',
    data: {{
      labels: labels,
      datasets: [
        {{
          label: 'Rendimiento Real Observado (qq/ha)',
          data: validData.map(d => d.rendimiento_obs_qq_ha),
          backgroundColor: '#059669',
          borderWidth: 0
        }},
        {{
          label: 'Predicción Fusión (EVI + Clima)',
          data: validData.map(d => d.pred_modelo_fusion),
          backgroundColor: '#2563EB',
          borderWidth: 0
        }},
        {{
          label: 'Predicción Solo NDVI (Saturado)',
          data: validData.map(d => d.pred_solo_ndvi),
          backgroundColor: '#DC2626',
          borderWidth: 0
        }}
      ]
    }},
    options: {{
      responsive: true,
      maintainAspectRatio: false,
      scales: {{
        x: {{ ticks: {{ color: textColor }}, grid: {{ color: gridColor }} }},
        y: {{ 
          title: {{ display: true, text: 'Quintales por Hectárea (qq/ha)', color: textColor }},
          ticks: {{ color: textColor }},
          grid: {{ color: gridColor }}
        }}
      }},
      plugins: {{
        legend: {{ labels: {{ color: textColor, font: {{ family: 'IBM Plex Sans' }} }} }}
      }}
    }}
  }});
}}

// Inicialización
updateSlide(0);
</script>
</body>
</html>
"""
    out_file = Path("presentacion.html")
    out_file.write_text(html_content, encoding="utf-8")
    print(f"Deck interactivo generado en: {out_file} ({out_file.stat().st_size / 1024:.1f} KB)")

if __name__ == "__main__":
    build_presentation()
