from deck_branding import get_separator_copy


def get_slides_part2(branding=None):
    if branding is None:
        branding = {}
    qr_svg = branding.get("qr_svg", "")
    b64_dw = branding.get("b64_dw", "")
    b64_header = branding.get("b64_header", "")
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
    sep3_title, sep3_subtitle = get_separator_copy(3)
    sep4_title, sep4_subtitle = get_separator_copy(4)
    sep5_title, sep5_subtitle = get_separator_copy(5)

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
  <section class="slide slide-archetype-section act-bg-3" data-index="18" data-act="Acto 3 · Series Temporales en el Agro" data-time="1.0 min">
    <div class="section-huge-num">03</div>
    <h2 class="section-title display">__SEP3_TITLE__</h2>
    <p class="section-desc">__SEP3_SUBTITLE__</p>
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
  <section class="slide slide-archetype-section act-bg-4" data-index="24" data-act="Acto 4 · Caso 2: Rendimiento &amp; NDVI" data-time="1.0 min">
    <div class="section-huge-num">04</div>
    <h2 class="section-title display">__SEP4_TITLE__</h2>
    <p class="section-desc">__SEP4_SUBTITLE__</p>
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
  <section class="slide slide-archetype-section act-bg-5" data-index="28" data-act="Acto 5 · Conclusiones y Cierre" data-time="1.0 min">
    <div class="section-huge-num">05</div>
    <h2 class="section-title display">__SEP5_TITLE__</h2>
    <p class="section-desc">__SEP5_SUBTITLE__</p>
  </section>


  <!-- ============================================================= -->
  <!-- DIAPO 29: CONCLUSIONES (page-09.png)                         -->
  <!-- Tres lecciones en frases grandes para público sin estadística -->
  <!-- ============================================================= -->
  <section class="slide slide-lessons act-bg-5" data-index="29" data-act="Acto 5 · Conclusiones" data-time="2.0 min">
    <h2 class="slide-main-title display">Conclusiones y lecciones aprendidas</h2>
    <button type="button" id="btnCinematicIntro29"
            onclick="window.postMessage({{type:'deck_replay_video', slide:29}}, '*')"
            title="Reproyectar la introducción cinemática"
            style="position:absolute; top:6px; right:6px; z-index:20; display:inline-flex; align-items:center; gap:6px; padding:8px 12px; border:1px solid rgba(56,239,255,0.42); border-radius:10px; background:linear-gradient(120deg, rgba(8,47,73,0.9), rgba(8,15,32,0.92)); color:#7dd3fc; font:700 12px/1 'IBM Plex Mono', monospace; letter-spacing:0.06em; cursor:pointer; white-space:nowrap;">🎬 Repetir Intro</button>
    <div class="lessons-stack">
      <article class="lesson-row lesson-row-1">
        <div class="lesson-icon" aria-hidden="true">⏳</div>
        <div class="lesson-body">
          <h3 class="lesson-title display">1 · Respeta el orden del tiempo</h3>
          <p class="lesson-evidence">Entrenar mirando el futuro da notas falsas. Iquitos: 2,557 días, examen ciego de 90.</p>
        </div>
      </article>
      <article class="lesson-row lesson-row-2">
        <div class="lesson-icon" aria-hidden="true">📊</div>
        <div class="lesson-body">
          <h3 class="lesson-title display">2 · El valor está en el rango, no en el número</h3>
          <p class="lesson-evidence">Un pronóstico honesto dice «entre 29 y 36 °C», no «32.7 °C».</p>
        </div>
      </article>
      <article class="lesson-row lesson-row-3">
        <div class="lesson-icon" aria-hidden="true">🌱</div>
        <div class="lesson-body">
          <h3 class="lesson-title display">3 · Primero la física, después el algoritmo</h3>
          <p class="lesson-evidence">El satélite vio hojas verdes; la cosecha de Jaén cayó a la mitad.</p>
        </div>
      </article>
    </div>
    __CINEMATIC_GATE_29__
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 30: CIERRE Y PREGUNTAS (page-10.png)                   -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-closing act-bg-5" data-index="30" data-act="Acto 5 · Preguntas &amp; QR" data-time="1.5 min">
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
        .replace("__SEP3_TITLE__", sep3_title)
        .replace("__SEP3_SUBTITLE__", sep3_subtitle)
        .replace("__SEP4_TITLE__", sep4_title)
        .replace("__SEP4_SUBTITLE__", sep4_subtitle)
        .replace("__SEP5_TITLE__", sep5_title)
        .replace("__SEP5_SUBTITLE__", sep5_subtitle)
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
