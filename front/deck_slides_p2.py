def get_slides_part2(branding=None):
    if branding is None:
        branding = {}
    qr_svg = branding.get("qr_svg", "")
    b64_dw = branding.get("b64_dw", "")
    b64_header = branding.get("b64_header", "")
    b64_qr = branding.get("b64_qr", "")
    anatomy_c1_svg = branding.get("anatomy_c1_svg", "")
    anatomy_c2_svg = branding.get("anatomy_c2_svg", "")

    return f"""
  <!-- ============================================================= -->
  <!-- DIAPO 11: BENCHMARK RIGUROSO EN PUNCHANA (page-06.png)        -->
  <!-- ============================================================= -->
  <section class="slide" data-index="11" data-act="Acto 2 · Benchmark Iquitos" data-time="2.0 min">
    <h2 class="slide-main-title display">Benchmark de 14 modelos: Tierra vs Supercómputo</h2>
    <div class="graphic-layout">
      <div class="graphic-info-col">
        <ul class="standard-bullet-list">
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Protocolo estricto:</strong> 2,467 días de entrenamiento y 90 días de holdout ciego (Q4 2025). Test Diebold-Mariano con corrección Harvey-Leybourne-Newbold (HLN 1997).</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Microfísica local vs Supercómputo:</strong> ExtraTrees (1.88 °C) y TimesFM Zero-Shot (1.88 °C, p=0.71) superan a ECMWF IFS (~9 km, 2.46 °C, p=0.027) y NOAA GFS (~28 km, 2.58 °C, p=0.008).</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Regla de parsimonia:</strong> ExtraTrees en CPU (0.25s) empata estadísticamente con Random Forest (1.89 °C) y TimesFM (7.87s en GPU/NPU). En el microclima tropical, la memoria inercial local domina a la física numérica sin downscaling.</div>
          </li>
        </ul>
        <div class="graphic-source">Benchmark auditado sobre estación SENAMHI Punchana · Holdout ciego de 90 días</div>
      </div>

      <div class="graphic-card-col">
        <div class="chart-wrapper">
          <div class="chart-toolbar">
            <span style="font-size:11px; font-weight:700; color:var(--text-faint); margin-right:4px;" class="mono">MODO:</span>
            <button class="chart-filter-btn active" id="btnPunchanaChart" onclick="switchPunchanaView('chart')">Gráfico de Benchmark</button>
            <button class="chart-filter-btn" id="btnPunchanaAnatomy" onclick="switchPunchanaView('anatomy')" style="border-color:var(--fest-cyan); color:var(--fest-cyan);">📐 Anatomía del Sistema</button>
            <span style="font-size:11px; font-weight:700; color:var(--text-faint); margin:0 4px 0 10px;" class="mono">FILTRAR:</span>
            <button class="chart-filter-btn active" id="btnBmAll" onclick="filterBenchmarkPunchana('all')">Todos (14)</button>
            <button class="chart-filter-btn" id="btnBmLeaders" onclick="filterBenchmarkPunchana('leaders')">Líderes (p &gt; 0.05)</button>
            <button class="chart-filter-btn" id="btnBmNwp" onclick="filterBenchmarkPunchana('nwp')">Física Global (ECMWF/NOAA)</button>
            <button class="chart-filter-btn" id="btnBmLocal" onclick="filterBenchmarkPunchana('local')">ML Local</button>
          </div>
          <div id="punchanaChartContainer" style="flex:1; min-height:0; position:relative; width:100%; height:100%; display:flex;">
            <canvas id="chartBenchmark"></canvas>
          </div>
          <div id="punchanaAnatomyContainer" class="iso" style="flex:1; min-height:0; position:relative; width:100%; height:100%; display:none; align-items:center; justify-content:center; background:var(--bg-dark-card); border-radius:8px; overflow:hidden;">
            {anatomy_c1_svg}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 12: PRONÓSTICO 7 DÍAS EN VIVO (page-06.png)            -->
  <!-- ============================================================= -->
  <section class="slide" data-index="12" data-act="Acto 2 · Pronóstico 7 Días" data-time="2.0 min">
    <h2 class="slide-main-title display">Demostración: pronóstico operacional a 7 días</h2>
    <div class="graphic-layout">
      <div class="graphic-info-col">
        <ul class="standard-bullet-list">
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Horizonte multi-step:</strong> Proyección día por día con bandas empíricas P10–P90 derivadas de los residuos de validación.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Cobertura real:</strong> 6 de los 7 días observados (85.7%) cayeron dentro del intervalo de confianza proyectado.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Ruptura en h=7:</strong> En el día 7, el error se incrementa al duplicarse la dispersión respecto a h=1.</div>
          </li>
        </ul>
        <div class="graphic-source">Evaluación directa sobre los últimos 7 días registrados en SENAMHI Punchana</div>
      </div>

      <div class="graphic-card-col">
        <div class="chart-wrapper">
          <div class="chart-toolbar">
            <span style="font-size:11px; font-weight:700; color:var(--text-faint); margin-right:4px;" class="mono">VISTA:</span>
            <button class="chart-filter-btn active" id="btnDemoAll" onclick="filterDemo7dView('all')">Multimodelo Completo</button>
            <button class="chart-filter-btn" id="btnDemoNwp" onclick="filterDemo7dView('nwp')">Confrontar NWP vs SENAMHI</button>
            <button class="chart-filter-btn" id="btnDemoWinner" onclick="filterDemo7dView('winner')">Líder ExtraTrees + Cono P10/P90</button>
          </div>
          <div style="flex:1; min-height:0; position:relative; width:100%; height:100%;">
            <canvas id="chartDemo7d"></canvas>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 13: DEMO / CÓDIGO (page-08.png)                         -->
  <!-- ============================================================= -->
  <section class="slide" data-index="13" data-act="Acto 2 · Código del Modelo" data-time="2.0 min">
    <h2 class="slide-main-title display">Demo / Código: Pipeline de forecasting</h2>
    <div class="code-layout">
      <div class="code-editor-box">
        <div class="code-editor-header">
          <div class="code-traffic-lights">
            <div class="code-dot red"></div>
            <div class="code-dot yellow"></div>
            <div class="code-dot green"></div>
          </div>
          <div class="code-editor-title">senamhi_forecaster.py</div>
        </div>
        <div class="code-editor-body">
<span style="color:#6C7AA6;"># 1. Modelado en diferencias finitas para evitar mesetas</span>
<span style="color:#9B5CFF;">import</span> pandas <span style="color:#9B5CFF;">as</span> pd
<span style="color:#9B5CFF;">from</span> sklearn.ensemble <span style="color:#9B5CFF;">import</span> ExtraTreesRegressor

<span style="color:#6C7AA6;"># Calcular aceleración térmica (Δy = y_t - y_{{t-1}})</span>
df[<span style="color:#12C8FC;">'delta_tmax'</span>] = df[<span style="color:#12C8FC;">'tmax'</span>].diff()

<span style="color:#6C7AA6;"># 2. Generación de lags temporales (memoria inercial)</span>
<span style="color:#9B5CFF;">for</span> k <span style="color:#9B5CFF;">in</span> [<span style="color:#FFC857;">1</span>, <span style="color:#FFC857;">2</span>, <span style="color:#FFC857;">3</span>, <span style="color:#FFC857;">7</span>, <span style="color:#FFC857;">14</span>]:
    df[<span style="color:#12C8FC;">f'lag_{{k}}'</span>] = df[<span style="color:#12C8FC;">'delta_tmax'</span>].shift(k)

<span style="color:#6C7AA6;"># 3. Entrenamiento ultrarrápido y parsimonioso (CPU 0.11s)</span>
model = <span style="color:#2EE6A6;">ExtraTreesRegressor</span>(n_estimators=<span style="color:#FFC857;">100</span>, random_state=<span style="color:#FFC857;">42</span>)
model.<span style="color:#2EE6A6;">fit</span>(X_train, y_train_delta)

<span style="color:#6C7AA6;"># 4. Reconstrucción estocástica de nivel con cuantil P10-P90</span>
pred_delta = model.<span style="color:#2EE6A6;">predict</span>(X_test)
y_pred_nivel = y_last + pred_delta.<span style="color:#2EE6A6;">cumsum</span>()
        </div>
      </div>

      <div class="code-steps-col">
        <div class="code-step-item">
          <div class="code-step-badge">1</div>
          <div>
            <div class="code-step-title">Qué hace el código</div>
            <div class="code-step-desc">Diferencia la serie temporal para garantizar estacionariedad y permitir que los árboles extrapolen eventos récord.</div>
          </div>
        </div>

        <div class="code-step-item">
          <div class="code-step-badge">2</div>
          <div>
            <div class="code-step-title">Punto clave</div>
            <div class="code-step-desc">Los retardos (lags) de 7 y 14 días capturan la inercia sin requerir redes recurrentes complejas ni GPUs.</div>
          </div>
        </div>

        <div class="code-step-item">
          <div class="code-step-badge">3</div>
          <div>
            <div class="code-step-title">Resultado</div>
            <div class="code-step-desc">Inferencia instantánea en 0.11s, reduciendo el MAE a 1.15 °C con cobertura empírica del 85.7%.</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 14: SECCIÓN 03: SERIES TEMPORALES EN EL AGRO (page-04.png) -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-section" data-index="14" data-act="Acto 3 · Series Temporales en el Agro" data-time="1.0 min">
    <div class="section-huge-num">03</div>
    <h2 class="section-title display">Cómo se aplican las series temporales en el agro</h2>
    <p class="section-desc">
      Por qué la biología vegetal y la fenología imponen leyes únicas al forecasting. Dinámicas de ultrabaja frecuencia, retrasos de meses entre el estímulo y la respuesta, y por qué el sobreajuste es letal sin comprender la fisiología del cultivo.
    </p>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 15: FÍSICA BIOLÓGICA Y RETOS DEL AGRO (page-05.png)     -->
  <!-- ============================================================= -->
  <section class="slide" data-index="15" data-act="Acto 3 · Física Biológica del Agro" data-time="2.0 min">
    <h2 class="slide-main-title display">Series temporales en el agro: física biológica</h2>
    <div class="content-insight-layout">
      <div class="content-bullets-col">
        <ul class="standard-bullet-list">
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Retrasos Fenológicos Biológicos:</strong> El rendimiento final de una cosecha no depende del clima de ayer, sino de los eventos durante la floración ocurrida 6 a 8 meses atrás.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Efectos Umbral Acumulados:</strong> Los grados día de desarrollo (GDD) y el déficit de presión de vapor (VPD) tienen impactos no lineales con puntos de quiebre irreversibles.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Series de Ultrabaja Frecuencia:</strong> A diferencia de millones de ticks financieros o datos diarios de clima, en agricultura solo existe 1 dato de cosecha por año (24 datos en 24 años).</div>
          </li>
        </ul>
      </div>

      <div class="archetype-idea-card">
        <div class="archetype-idea-icon">💡</div>
        <div class="archetype-idea-label">IDEA CLAVE</div>
        <p class="archetype-idea-text">
          En series agrícolas de baja frecuencia (N=24 años), el sobreajuste es fatal. Modelar la fenología biológica y los períodos críticos de estrés hídrico reduce el error 4 veces más que agregar capas de Deep Learning.
        </p>
      </div>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 16: EL RELOJ FENOLÓGICO Y CALENDARIO VEGETAL (page-06.png)-->
  <!-- ============================================================= -->
  <section class="slide" data-index="16" data-act="Acto 3 · Reloj Fenológico" data-time="2.0 min">
    <h2 class="slide-main-title display">El reloj fenológico: la física del calendario vegetal</h2>
    <div class="graphic-layout">
      <div class="graphic-info-col">
        <ul class="standard-bullet-list">
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Floración Crítica (Ago–Oct):</strong> Temperaturas máximas &gt; 32 °C provocan esterilidad de polen y aborto floral masivo. La sequía en esta ventana destruye el rendimiento 8 meses antes de cosechar.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Llenado de Fruto (Nov–Feb):</strong> Demanda hídrica elevada; el déficit hídrico detiene el crecimiento del fruto y reduce drásticamente el peso del grano pergamino.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Cosecha y Secado (Mar–Jul):</strong> Las lluvias torrenciales retrasan la recolección, inducen hongos y pudrición; el clima seco favorece el beneficio y la calidad de taza.</div>
          </li>
        </ul>
        <div class="graphic-source">Fisiología del Café Arábica · Cenicafé / MIDAGRI · Barbosa et al. (2021)</div>
      </div>

      <div class="graphic-card-col">
        <div style="display:flex; flex-direction:column; gap:12px; height:100%; justify-content:center;">
          <div style="background:var(--bg-dark-sub); padding:16px; border-radius:12px; border-left:4px solid var(--fest-magenta); display:flex; flex-direction:column;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="color:var(--fest-magenta); font-weight:700; font-size:11px;" class="mono">VENTANA 1 · AGOSTO - OCTUBRE</span>
              <span style="font-size:11px; background:rgba(224,64,251,0.15); color:#E040FB; padding:2px 8px; border-radius:10px; font-weight:600;" class="mono">MÁXIMA SENSIBILIDAD</span>
            </div>
            <div style="font-weight:700; font-size:15px; margin:4px 0;">Floración &amp; Cuajado de Fruto</div>
            <p style="font-size:12px; color:var(--text-faint); line-height:1.4;">Un déficit hídrico de 2 semanas causa aborto floral severo. La anomalía de lluvia en esta ventana explica el 56% de la varianza de cosecha final (r = 0.751).</p>
          </div>

          <div style="background:var(--bg-dark-sub); padding:16px; border-radius:12px; border-left:4px solid var(--fest-blue); display:flex; flex-direction:column;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="color:var(--fest-blue); font-weight:700; font-size:11px;" class="mono">VENTANA 2 · NOVIEMBRE - FEBRERO</span>
              <span style="font-size:11px; background:rgba(30,123,255,0.15); color:#1E7BFF; padding:2px 8px; border-radius:10px; font-weight:600;" class="mono">ACUMULACIÓN BIOMASA</span>
            </div>
            <div style="font-weight:700; font-size:15px; margin:4px 0;">Llenado de Grano &amp; Expansión Celular</div>
            <p style="font-size:12px; color:var(--text-faint); line-height:1.4;">Se determina el peso volumétrico y calibre. La fotosíntesis activa demanda transpiración sin estrés de presión de vapor (VPD).</p>
          </div>

          <div style="background:var(--bg-dark-sub); padding:16px; border-radius:12px; border-left:4px solid var(--fest-cyan); display:flex; flex-direction:column;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="color:var(--fest-cyan); font-weight:700; font-size:11px;" class="mono">VENTANA 3 · MARZO - JULIO</span>
              <span style="font-size:11px; background:rgba(18,200,252,0.15); color:#12C8FC; padding:2px 8px; border-radius:10px; font-weight:600;" class="mono">COSECHA Y BENEFICIO</span>
            </div>
            <div style="font-weight:700; font-size:15px; margin:4px 0;">Maduración, Recolección &amp; Secado</div>
            <p style="font-size:12px; color:var(--text-faint); line-height:1.4;">El calor seco acelera la maduración y facilita el secado al sol. Las lluvias excesivas pudren cerezas y causan caída de frutos.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 17: SECCIÓN 04: CASO 2: RENDIMIENTO Y NDVI (page-04.png) -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-section" data-index="17" data-act="Acto 4 · Caso 2: Rendimiento &amp; NDVI" data-time="1.0 min">
    <div class="section-huge-num">04</div>
    <h2 class="section-title display">Caso 2: Predicción de rendimiento usando NDVI</h2>
    <p class="section-desc">
      Auditoría de 24 campañas cafetaleras en Jaén (Cajamarca), 576 compuestos satelitales MODIS NDVI y reanálisis climático ERA5. La trampa de la saturación espectral y por qué el satélite óptico fue ciego a la mayor epidemia de roya amarilla.
    </p>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 18: DATOS QUE IMPORTAN: 24 CAMPAÑAS JAÉN (page-07.png)  -->
  <!-- ============================================================= -->
  <section class="slide" data-index="18" data-act="Acto 4 · Datos Jaén" data-time="1.5 min">
    <h2 class="slide-main-title display">Datos que importan: 24 Campañas de Café en Jaén</h2>
    <p class="kpis-subtitle">Cifras del sistema agroalimentario en la cuenca cafetalera de Jaén (2000–2024).</p>
    <div class="kpis-3col-grid">
      <div class="kpi-large-card card-cyan">
        <div class="kpi-huge-number">24</div>
        <div class="kpi-card-desc">Campañas agrícolas completas auditadas de café arábica en Jaén (SIEA/MIDAGRI).</div>
      </div>
      <div class="kpi-large-card card-blue">
        <div class="kpi-huge-number">-56%</div>
        <div class="kpi-card-desc">Colapso histórico de rendimiento en 2013 por la epidemia de roya amarilla (Hemileia vastatrix).</div>
      </div>
      <div class="kpi-large-card card-purple">
        <div class="kpi-huge-number">4.51</div>
        <div class="kpi-card-desc">MAE mínimo alcanzado (qq/ha) por el modelo de Fusión Fenológica Clima + Tendencia.</div>
      </div>
    </div>
    <div class="graphic-source" style="margin-top:16px;">Fuente: Sistema Integrado de Estadísticas Agrarias (SIEA - MIDAGRI) · Jaén, Cajamarca (2000–2024)</div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 19: LA TRAMPA DEL SATÉLITE NDVI (page-06.png)           -->
  <!-- ============================================================= -->
  <section class="slide" data-index="19" data-act="Acto 4 · Trampa del NDVI" data-time="2.0 min">
    <h2 class="slide-main-title display">La trampa del satélite: NDVI vs estrés hídrico</h2>
    <div class="graphic-layout">
      <div class="graphic-info-col">
        <ul class="standard-bullet-list">
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Saturación de canopia:</strong> El satélite óptico (MODIS NDVI) satura en copas densas de café bajo sombra y presentó R² = 0.08 con el rendimiento real.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Ceguera ante la roya:</strong> En la epidemia de 2013 (-56% de producción), el NDVI se mantuvo en 0.81 por la presencia de malezas y árboles de sombra.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>La verdadera señal:</strong> El déficit hídrico en floración (septiembre-noviembre) explicó el 56% de la varianza biológica real.</div>
          </li>
        </ul>
        <div class="graphic-source">Datos NASA MODIS Terra/Aqua (250m) + ERA5-Land Reanalysis vs SIEA MIDAGRI Jaén</div>
      </div>

      <div class="graphic-card-col">
        <div class="chart-wrapper">
          <div class="chart-toolbar">
            <span style="font-size:11px; font-weight:700; color:var(--text-faint); margin-right:4px;" class="mono">MODO:</span>
            <button class="chart-filter-btn active" id="btnCafeChart" onclick="switchCafeSystemView('chart')">Dispersión Empírica</button>
            <button class="chart-filter-btn" id="btnCafeAnatomy" onclick="switchCafeSystemView('anatomy')" style="border-color:var(--fest-cyan); color:var(--fest-cyan);">📐 Anatomía: Dosel vs Satélite</button>
            <span style="font-size:11px; font-weight:700; color:var(--text-faint); margin:0 4px 0 10px;" class="mono">VARIABLE:</span>
            <button class="chart-filter-btn active" id="btnScatterNdvi" onclick="switchScatterVariable('ndvi')">MODIS NDVI (r=0.154)</button>
            <button class="chart-filter-btn" id="btnScatterDef" onclick="switchScatterVariable('deficit')">Déficit Hídrico (r=0.756)</button>
            <button class="chart-filter-btn" id="btnScatterLluvia" onclick="switchScatterVariable('lluvia')">Lluvia Floración (r=0.751)</button>
          </div>
          <div id="cafeChartContainer" style="flex:1; min-height:0; position:relative; width:100%; height:100%; display:flex;">
            <canvas id="chartScatterNdvi"></canvas>
          </div>
          <div id="cafeAnatomyContainer" class="iso" style="flex:1; min-height:0; position:relative; width:100%; height:100%; display:none; align-items:center; justify-content:center; background:var(--bg-dark-card); border-radius:8px; overflow:hidden;">
            {anatomy_c2_svg}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 20: VALIDACIÓN WALK-FORWARD Y FUSIÓN (page-06.png)     -->
  <!-- ============================================================= -->
  <section class="slide" data-index="20" data-act="Acto 4 · Validación Jaén" data-time="2.0 min">
    <h2 class="slide-main-title display">Demostración: validación Walk-Forward en Jaén</h2>
    <div class="graphic-layout">
      <div class="graphic-info-col">
        <ul class="standard-bullet-list">
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Sin fuga temporal:</strong> Validación expansiva año a año (2016, 2018–2024) entrenando únicamente con la historia previa de cosechas.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Liderazgo de fenología y árboles:</strong> Random Forest parsimonioso (MAE 3.72 qq/ha) y Solo Déficit Hídrico de floración (MAE 3.90 qq/ha) logran los menores errores out-of-sample.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Fallo del Satélite Óptico:</strong> El modelo alimentado solo con NDVI anual (MAE 5.45 qq/ha) es un 31.7% peor, colapsando ante el récord de 2020 con un error de 18.25 qq/ha.</div>
          </li>
        </ul>
        <div class="graphic-source">Evaluación Walk-Forward ciego sobre 8 campañas de test (2016, 2018–2024)</div>
      </div>

      <div class="graphic-card-col">
        <div class="chart-wrapper">
          <div class="chart-toolbar">
            <span style="font-size:11px; font-weight:700; color:var(--text-faint); margin-right:4px;" class="mono">MODO:</span>
            <button class="chart-filter-btn active" id="btnJaenTraj" onclick="switchJaenViewMode('trajectory')">Trayectorias Walk-Forward (2016–2024)</button>
            <button class="chart-filter-btn" id="btnJaenBench" onclick="switchJaenViewMode('benchmark')">Benchmark de 16 Modelos (MAE)</button>
          </div>
          <div style="flex:1; min-height:0; position:relative; width:100%; height:100%;">
            <canvas id="chartDemoJaen"></canvas>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 21: SECCIÓN 05: CONCLUSIONES (page-04.png)              -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-section" data-index="21" data-act="Acto 5 · Conclusiones y Cierre" data-time="1.0 min">
    <div class="section-huge-num">05</div>
    <h2 class="section-title display">Conclusiones y lecciones aprendidas</h2>
    <p class="section-desc">
      Principios metodológicos innegociables destilados de 2,557 días de meteorología amazónica y 24 campañas cafetaleras reales. Por qué la disciplina metodológica y la física del dominio valen más que cualquier arquitectura neuronal profunda.
    </p>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 22: CONCLUSIONES (page-09.png)                         -->
  <!-- ============================================================= -->
  <section class="slide" data-index="22" data-act="Acto 5 · Conclusiones" data-time="2.0 min">
    <h2 class="slide-main-title display">Conclusiones</h2>
    <div class="conclusions-3col-grid">
      <div class="conclusion-card card-1">
        <div class="conclusion-icon-box">🎯</div>
        <div class="conclusion-title display">Respeta la causalidad del tiempo</div>
        <p class="conclusion-desc">
          Nunca utilices validación cruzada aleatoria en series temporales. Entrena siempre en el pasado y evalúa en el futuro con ventanas rodantes para evitar fuga de información. La navaja de Ockham es ley: en Punchana, ExtraTrees en CPU (0.11s) empató con redes neuronales complejas.
        </p>
      </div>

      <div class="conclusion-card card-2">
        <div class="conclusion-icon-box">🧠</div>
        <div class="conclusion-title display">El valor está en la banda, no en el punto</div>
        <p class="conclusion-desc">
          Un pronóstico puntual (ŷ_{{t+h}}) es una ficción matemática que oculta el riesgo operacional. En horizontes más allá de 7 días, la entropía atmosférica domina la física: comunica siempre conos de incertidumbre calibrados con cuantiles empíricos (P10–P90).
        </p>
      </div>

      <div class="conclusion-card card-3">
        <div class="conclusion-icon-box">🚀</div>
        <div class="conclusion-title display">Próximo paso: física antes que algoritmo</div>
        <p class="conclusion-desc">
          Entiende los mecanismos del dominio antes de elegir la arquitectura. El satélite óptico saturó y fue ciego a la roya (-56%), mientras que el estrés hídrico en floración explicó el 56% de la varianza. La física manda antes que el hiperparámetro.
        </p>
      </div>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 23: CIERRE Y PREGUNTAS (page-10.png)                   -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-closing" data-index="23" data-act="Acto 5 · Preguntas &amp; QR" data-time="1.5 min">
    <div>
      <div class="cover-tag mono">
        IQUITOS <span style="color:#12C8FC;">DATA FEST 2026</span>
      </div>
      <div class="closing-title display">¡GRACIAS!</div>
      <div class="closing-subtitle display">
        <span>💬</span> ¿Preguntas?
      </div>

      <div class="closing-cards-wrap">
        <div class="closing-contact-card">
          <div style="font-size:20px; font-weight:700; color:#FFFFFF; margin-bottom:6px;">Alex Prieto Romani</div>
          <div style="font-size:14px; color:#CBD5E1; display:flex; flex-direction:column; gap:8px;" class="mono">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="color:#12C8FC;">🔗</span>
              <a href="https://linkedin.com/in/alex-prieto-romani" target="_blank" style="color:inherit; text-decoration:none;">linkedin.com/in/alex-prieto-romani</a>
            </div>
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="color:#12C8FC;">✉️</span>
              <a href="mailto:alexprieto1997@gmail.com" style="color:inherit; text-decoration:none;">alexprieto1997@gmail.com</a>
            </div>
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="color:#12C8FC;">🌐</span>
              <a href="https://alexprietoromani.github.io/" target="_blank" style="color:inherit; text-decoration:none;">alexprietoromani.github.io/</a>
            </div>
          </div>
        </div>

        <div class="closing-qr-card">
          <div class="closing-qr-box">
            <img src="data:image/png;base64,{b64_qr}" alt="QR alexprietoromani.github.io" style="width:100%; height:100%; object-fit:contain; border-radius:6px;">
          </div>
          <div style="font-size:11px; color:#12C8FC; text-align:center; font-weight:600;" class="mono">Tu QR (opcional)</div>
        </div>
      </div>
    </div>

    <div class="closing-bottom-logos">
      <img src="data:image/png;base64,{b64_header}" alt="UNAP · Neo Kernel · Grupo de Datos &amp; IA">
      <img src="data:image/png;base64,{b64_dw}" alt="En colaboración con Data Wizard">
    </div>
  </section>
"""
