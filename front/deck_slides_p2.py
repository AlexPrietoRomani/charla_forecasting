def get_slides_part2(branding=None):
    if branding is None:
        branding = {}
    qr_svg = branding.get("qr_svg", "")
    b64_dw = branding.get("b64_dw", "")
    b64_header = branding.get("b64_header", "")
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
    b64_p25_html = branding.get("b64_p25_html", "")
    b64_p26_html = branding.get("b64_p26_html", "")
    b64_p27_html = branding.get("b64_p27_html", "")
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
  <!-- DIAPO 25: DATOS QUE IMPORTAN: 24 CAMPAÑAS JAÉN (PROTOTIPO)    -->
  <!-- ============================================================= -->
  <section class="slide" data-index="25" data-act="Acto 4 · Datos Jaén" data-time="1.5 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(46, 230, 166, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P25_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide25"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 26: LA TRAMPA DEL SATÉLITE NDVI (PROTOTIPO)             -->
  <!-- ============================================================= -->
  <section class="slide" data-index="26" data-act="Acto 4 · Trampa del NDVI" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(56, 239, 255, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P26_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide26"></iframe>
      __CINEMATIC_GATE_26__
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 27: VALIDACIÓN WALK-FORWARD Y FUSIÓN (PROTOTIPO)       -->
  <!-- ============================================================= -->
  <section class="slide" data-index="27" data-act="Acto 4 · Validación Jaén" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(180, 142, 255, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P27_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide27"></iframe>
      __CINEMATIC_GATE_27__
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
    <h2 class="slide-main-title display">Conclusiones y lecciones aprendidas</h2>
    <button type="button" id="btnCinematicIntro29"
            onclick="window.postMessage({{type:'deck_replay_video', slide:29}}, '*')"
            title="Reproyectar la introducción cinemática"
            style="position:absolute; top:6px; right:6px; z-index:20; display:inline-flex; align-items:center; gap:6px; padding:8px 12px; border:1px solid rgba(56,239,255,0.42); border-radius:10px; background:linear-gradient(120deg, rgba(8,47,73,0.9), rgba(8,15,32,0.92)); color:#7dd3fc; font:700 12px/1 'IBM Plex Mono', monospace; letter-spacing:0.06em; cursor:pointer; white-space:nowrap;">🎬 Repetir Intro</button>
    <div class="conclusions-3col-grid">
      <div class="conclusion-card card-1">
        <div class="conclusion-card-head">
          <div class="conclusion-pill-tag mono">AXIOMA 01 · CAUSALIDAD TEMPORAL</div>
          <div class="conclusion-card-title-row">
            <div class="conclusion-icon-box">🎯</div>
            <div class="conclusion-title display">Respeta la causalidad del tiempo</div>
          </div>
          <p class="conclusion-desc">
            En series temporales el orden cronológico es sagrado. Entrenar mirando el futuro o usar particiones aleatorias produce métricas de laboratorio que colapsan en producción.
          </p>
        </div>
        <div class="conclusion-trap-box">
          <strong>⚠️ La Trampa Habitual:</strong> K-Fold aleatorio y shuffle mezclan pasado y futuro, creando una ilusión de alta precisión por fuga temporal (data leakage).
        </div>
        <div class="conclusion-evidence">
          <div class="conclusion-evidence-title">📊 Evidencia Empírica · Caso 1 Punchana</div>
          <ul class="conclusion-evidence-list">
            <li><strong>2,557 días SENAMHI:</strong> evaluación estricta en el futuro real con split temporal continuo sin contaminación.</li>
            <li><strong>ExtraTrees en CPU (0.25 s):</strong> igualó a Foundation Models masivos al modelar incrementos causales (Δy<sub>t</sub>).</li>
          </ul>
        </div>
        <div class="conclusion-takeaway">💡 <strong>Regla Operativa:</strong> si el modelo vio el futuro para entrenar, su error es ficción; valida siempre con Walk-Forward expansivo.</div>
      </div>

      <div class="conclusion-card card-2">
        <div class="conclusion-card-head">
          <div class="conclusion-pill-tag mono">AXIOMA 02 · GESTIÓN DE RIESGO</div>
          <div class="conclusion-card-title-row">
            <div class="conclusion-icon-box">🧠</div>
            <div class="conclusion-title display">El valor está en la banda, no en el punto</div>
          </div>
          <p class="conclusion-desc">
            Un pronóstico puntual (ŷ<sub>t+h</sub>) es una ficción matemática que oculta el riesgo operacional. Con entropía y ruido irreductible, la única métrica honesta es el cono calibrado.
          </p>
        </div>
        <div class="conclusion-trap-box">
          <strong>⚠️ La Trampa Habitual:</strong> comprometer un escalar único ante el decisor: ante shocks extremos, el error puntual destruye la credibilidad del modelo.
        </div>
        <div class="conclusion-evidence">
          <div class="conclusion-evidence-title">📊 Evidencia Empírica · Ambos Casos</div>
          <ul class="conclusion-evidence-list">
            <li><strong>Cono P10–P90 (Iquitos):</strong> contuvo la ola de calor histórica de 38.0 °C dentro de la banda calibrada sin sobreajustar.</li>
            <li><strong>Split Conformal 80% (Jaén):</strong> garantizó cobertura out-of-sample en 8/8 campañas con q̂ = 6.23 qq/ha.</li>
          </ul>
        </div>
        <div class="conclusion-takeaway">💡 <strong>Regla Operativa:</strong> punto sin banda es marketing; banda conformal calibrada al 80%–90% es gestión de riesgo real.</div>
      </div>

      <div class="conclusion-card card-3">
        <div class="conclusion-card-head">
          <div class="conclusion-pill-tag mono">AXIOMA 03 · BIOLOGÍA &amp; DOMINIO</div>
          <div class="conclusion-card-title-row">
            <div class="conclusion-icon-box">🚀</div>
            <div class="conclusion-title display">Próximo paso: física antes que algoritmo</div>
          </div>
          <p class="conclusion-desc">
            Entiende los mecanismos del dominio antes de elegir la arquitectura. La IA no sustituye a la fisiología ni a la física causal: la complejidad ciega fracasa ante muestras pequeñas.
          </p>
        </div>
        <div class="conclusion-trap-box">
          <strong>⚠️ La Trampa Habitual:</strong> confiar ciegamente en datos satelitales brutos: el MODIS NDVI saturó en árboles de sombra (Inga) y no vio la epidemia floral.
        </div>
        <div class="conclusion-evidence">
          <div class="conclusion-evidence-title">📊 Evidencia Empírica · Caso 2 Jaén</div>
          <ul class="conclusion-evidence-list">
            <li><strong>24 campañas cafetaleras:</strong> el déficit hídrico en floración (r = 0.7564) domina ampliamente sobre el NDVI ciego (r = 0.1536).</li>
            <li><strong>Random Forest parsimonioso (d=2):</strong> ganó el torneo con MAE 3.72 qq/ha tras el desplome de −56.0% en la roya 2014.</li>
          </ul>
        </div>
        <div class="conclusion-takeaway">💡 <strong>Regla Operativa:</strong> la física del dominio manda antes que el hiperparámetro; modela el cuello de botella biológico.</div>
      </div>
    </div>
    __CINEMATIC_GATE_29__
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 30: CIERRE Y PREGUNTAS (page-10.png)                   -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-closing" data-index="30" data-act="Acto 5 · Preguntas &amp; QR" data-time="1.5 min">
    <div>
      <div class="cover-tag mono">
        IQUITOS <span style="color:#12C8FC;">DATA FEST 2026</span> · CHARLA MAGISTRAL
      </div>
      <div class="closing-title display">¡GRACIAS!</div>
      <div class="closing-subtitle display">
        <span>💬</span> ¿Preguntas o reflexiones?
      </div>

      <div class="closing-cards-wrap">
        <div class="closing-contact-card">
          <div>
            <div class="closing-name">Alex Prieto Romani</div>
            <div class="closing-role-tag mono"><span>⚡</span> Investigación Aplicada en Series Temporales &amp; Machine Learning</div>
          </div>
          <div class="closing-contact-list mono">
            <div class="closing-contact-item">
              <span style="color:#12C8FC;">🔗</span>
              <a href="https://linkedin.com/in/alex-prieto-romani" target="_blank">linkedin.com/in/alex-prieto-romani</a>
            </div>
            <div class="closing-contact-item">
              <span style="color:#12C8FC;">✉️</span>
              <a href="mailto:alexprieto1997@gmail.com">alexprieto1997@gmail.com</a>
            </div>
            <div class="closing-contact-item">
              <span style="color:#12C8FC;">🌐</span>
              <a href="https://alexprietoromani.github.io/" target="_blank">alexprietoromani.github.io/</a>
            </div>
            <div class="closing-contact-item">
              <span style="color:#12C8FC;">🐙</span>
              <a href="https://github.com/alexprietor/charla_forecasting" target="_blank">github.com/alexprietor/charla_forecasting</a>
            </div>
          </div>
          <div class="closing-card-footer mono">
            💡 Código fuente, simuladores interactivos, diapositivas y datasets reales 100% reproducibles.
          </div>
        </div>

        <div class="closing-qr-card">
          <div class="closing-qr-box" aria-label="QR a alexprietoromani.github.io">
            {qr_svg}
          </div>
          <div class="closing-qr-caption mono" title="alexprietoromani.github.io">
            <div class="closing-qr-title">ESCANEA EL QR</div>
            <div class="closing-qr-sub">Slides · Datos · Repo</div>
          </div>
        </div>
      </div>

      <div class="closing-badges mono">
        <span class="closing-badge">📡 2,557 Días SENAMHI + 24 Campañas SIEA</span>
        <span class="closing-badge">🏁 Benchmark de 16 Modelos Auditados</span>
        <span class="closing-badge">🛡️ Validación Walk-Forward + Conformal 80%</span>
        <span class="closing-badge">💻 Pipeline 100% Libre y Reproducible</span>
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
        .replace("__B64_P25_HTML__", b64_p25_html)
        .replace("__B64_P26_HTML__", b64_p26_html)
        .replace("__B64_P27_HTML__", b64_p27_html)
        .replace("__CINEMATIC_GATE_19__", cinematic_gates.get(19, ""))
        .replace("__CINEMATIC_GATE_21__", cinematic_gates.get(21, ""))
        .replace("__CINEMATIC_GATE_26__", cinematic_gates.get(26, ""))
        .replace("__CINEMATIC_GATE_27__", cinematic_gates.get(27, ""))
        .replace("__CINEMATIC_GATE_29__", cinematic_gates.get(29, ""))
    )
