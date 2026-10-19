def get_slides_part2(branding=None):
    if branding is None:
        branding = {}
    qr_svg = branding.get("qr_svg", "")
    b64_dw = branding.get("b64_dw", "")
    b64_header = branding.get("b64_header", "")
    b64_qr = branding.get("b64_qr", "")
    anatomy_c1_svg = branding.get("anatomy_c1_svg", "")
    anatomy_c2_svg = branding.get("anatomy_c2_svg", "")
    b64_p15_html = branding.get("b64_p15_html", "")
    b64_p16_html = branding.get("b64_p16_html", "")
    b64_p17_html = branding.get("b64_p17_html", "")
    b64_p19_html = branding.get("b64_p19_html", "")
    b64_p20_html = branding.get("b64_p20_html", "")
    b64_p21_html = branding.get("b64_p21_html", "")
    b64_p22_html = branding.get("b64_p22_html", "")
    b64_p23_html = branding.get("b64_p23_html", "")
    cinematic_gates = branding.get("cinematic_gates", {})

    html = f"""
  <!-- ============================================================= -->
  <!-- DIAPO 15: BENCHMARK RIGUROSO EN PUNCHANA (page-06.png)        -->
  <!-- ============================================================= -->
  <section class="slide" data-index="15" data-act="Acto 2 · Benchmark Iquitos" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(18, 200, 252, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P15_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide15"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 16: PRONÓSTICO 7 DÍAS EN VIVO (page-06.png)            -->
  <!-- ============================================================= -->
  <section class="slide" data-index="16" data-act="Acto 2 · Pronóstico 7 Días" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(18, 200, 252, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P16_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide16"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 17: DEMO / CÓDIGO (page-08.png)                         -->
  <!-- ============================================================= -->
  <section class="slide" data-index="17" data-act="Acto 2 · Código del Modelo" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(18, 200, 252, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P17_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide17"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- ============================================================= -->
  <!-- DIAPO 18: SECCIÓN 03: SERIES TEMPORALES EN EL AGRO            -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-section" data-index="18" data-act="Acto 3 · Series Temporales en el Agro" data-time="1.0 min">
    <div class="section-huge-num">03</div>
    <h2 class="section-title display">Series temporales en el agro: del almanaque al satélite</h2>
    <p class="section-desc">
      Cómo la agricultura inventó el forecasting hace 10,000 años y evolucionó de la observación astronómica empírica a la teledetección multiespectral continua. La física biológica, los desfases fenológicos (τ = 6–8 meses) y los límites computacionales en sistemas vivos (p ≫ N).
    </p>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 19: CÓMO EL AGRO INVENTÓ EL FORECASTING (PROTOTIPO)     -->
  <!-- ============================================================= -->
  <section class="slide" data-index="19" data-act="Acto 3 · Historia del Agro-Forecasting" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(18, 200, 252, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P19_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide19"></iframe>
      __CINEMATIC_GATE_19__
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 20: DEL ALMANAQUE AL SATÉLITE (PROTOTIPO)               -->
  <!-- ============================================================= -->
  <section class="slide" data-index="20" data-act="Acto 3 · Del Almanaque al Satélite" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(56, 239, 255, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P20_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide20"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 21: FÍSICA BIOLÓGICA Y EL LÍMITE ALGORÍTMICO (PROTOTIPO)-->
  <!-- ============================================================= -->
  <section class="slide" data-index="21" data-act="Acto 3 · Biofísica &amp; Límites" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(180, 142, 255, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P21_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide21"></iframe>
      __CINEMATIC_GATE_21__
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 22: RELOJ FENOLÓGICO DEL CAFÉ (PROTOTIPO)               -->
  <!-- ============================================================= -->
  <section class="slide" data-index="22" data-act="Acto 3 · Reloj Fenológico del Café" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(46, 230, 166, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P22_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide22"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 23: PRECISIÓN ACTUAL Y LAS TRES TRAMPAS (PROTOTIPO)     -->
  <!-- ============================================================= -->
  <section class="slide" data-index="23" data-act="Acto 3 · Las Tres Trampas" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(255, 107, 107, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P23_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide23"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 24: SECCIÓN 04: CASO 2: RENDIMIENTO Y NDVI (page-04.png) -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-section" data-index="24" data-act="Acto 4 · Caso 2: Rendimiento &amp; NDVI" data-time="1.0 min">
    <div class="section-huge-num">04</div>
    <h2 class="section-title display">Caso 2: Predicción de rendimiento usando NDVI</h2>
    <p class="section-desc">
      Auditoría de 24 campañas cafetaleras en Jaén (Cajamarca), 576 compuestos satelitales MODIS NDVI y reanálisis climático ERA5. La trampa de la saturación espectral y por qué el satélite óptico fue ciego a la mayor epidemia de roya amarilla.
    </p>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 25: DATOS QUE IMPORTAN: 24 CAMPAÑAS JAÉN (page-07.png)  -->
  <!-- ============================================================= -->
  <section class="slide" data-index="25" data-act="Acto 4 · Datos Jaén" data-time="1.5 min">
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
  <!-- DIAPO 26: LA TRAMPA DEL SATÉLITE NDVI (page-06.png)           -->
  <!-- ============================================================= -->
  <section class="slide" data-index="26" data-act="Acto 4 · Trampa del NDVI" data-time="2.0 min">
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
  <!-- DIAPO 27: VALIDACIÓN WALK-FORWARD Y FUSIÓN (page-06.png)     -->
  <!-- ============================================================= -->
  <section class="slide" data-index="27" data-act="Acto 4 · Validación Jaén" data-time="2.0 min">
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
  <!-- DIAPO 28: SECCIÓN 05: CONCLUSIONES (page-04.png)              -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-section" data-index="28" data-act="Acto 5 · Conclusiones y Cierre" data-time="1.0 min">
    <div class="section-huge-num">05</div>
    <h2 class="section-title display">Conclusiones y lecciones aprendidas</h2>
    <p class="section-desc">
      Principios metodológicos innegociables destilados de 2,557 días de meteorología amazónica y 24 campañas cafetaleras reales. Por qué la disciplina metodológica y la física del dominio valen más que cualquier arquitectura neuronal profunda.
    </p>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 29: CONCLUSIONES (page-09.png)                         -->
  <!-- ============================================================= -->
  <section class="slide" data-index="29" data-act="Acto 5 · Conclusiones" data-time="2.0 min">
    <h2 class="slide-main-title display">Conclusiones</h2>
    <div class="conclusions-3col-grid">
      <div class="conclusion-card card-1">
        <div class="conclusion-icon-box">🎯</div>
        <div class="conclusion-title display">Respeta la causalidad del tiempo</div>
        <p class="conclusion-desc">
          Nunca utilices validación cruzada aleatoria en series temporales. Entrena siempre en el pasado y evalúa en el futuro con ventanas rodantes para evitar fuga de información. La navaja de Ockham es ley: en Punchana, ExtraTrees en CPU (0.25s) empató con redes neuronales complejas.
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
  <!-- DIAPO 30: CIERRE Y PREGUNTAS (page-10.png)                   -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-closing" data-index="30" data-act="Acto 5 · Preguntas &amp; QR" data-time="1.5 min">
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

    return (
        html.replace("__B64_P15_HTML__", b64_p15_html)
        .replace("__B64_P16_HTML__", b64_p16_html)
        .replace("__B64_P17_HTML__", b64_p17_html)
        .replace("__B64_P19_HTML__", b64_p19_html)
        .replace("__B64_P20_HTML__", b64_p20_html)
        .replace("__B64_P21_HTML__", b64_p21_html)
        .replace("__B64_P22_HTML__", b64_p22_html)
        .replace("__B64_P23_HTML__", b64_p23_html)
        .replace("__CINEMATIC_GATE_19__", cinematic_gates.get(19, ""))
        .replace("__CINEMATIC_GATE_21__", cinematic_gates.get(21, ""))
    )
