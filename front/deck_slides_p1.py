def get_slides_part1(branding=None):
    if branding is None:
        branding = {}
    b64_header = branding.get("b64_header", "")
    b64_profile = branding.get("b64_profile", "")
    b64_sim_html = branding.get("b64_sim_html", "")
    b64_era1_html = branding.get("b64_era1_html", "")
    b64_era2_html = branding.get("b64_era2_html", "")
    b64_era3_html = branding.get("b64_era3_html", "")
    b64_era4_html = branding.get("b64_era4_html", "")
    b64_cono_html = branding.get("b64_cono_html", "")
    b64_decision_html = branding.get("b64_decision_html", "")
    b64_p13_html = branding.get("b64_p13_html", "")
    b64_p14_html = branding.get("b64_p14_html", "")

    slides = """
  <!-- ========================================== -->
  <!-- DIAPO 01: PORTADA OFICIAL (page-01.png)    -->
  <!-- ========================================== -->
  <section class="slide active slide-archetype-cover" data-index="1" data-act="Apertura · Portada" data-time="1.0 min">
    <div>
      <div class="cover-header-logos">
        <img src="data:image/png;base64,__HEADER_LOGO__" alt="UNAP · Neo Kernel · Grupo de Datos &amp; IA">
      </div>
      <div class="cover-tag mono">
        IQUITOS <span>DATA FEST 2026</span>
      </div>
      <h1 class="cover-title display">¿Puede la IA predecir el futuro? Casos forecasting</h1>
      <p class="cover-subtitle">Lecciones desde el mundo real con datos meteorológicos de SENAMHI y series agrícolas de Jaén</p>
    </div>

    <div class="cover-speaker-card">
      <div class="cover-speaker-name">Alex Prieto Romani</div>
      <div class="cover-speaker-role">Agriculture Data Science · Hortifrut SA</div>
    </div>
  </section>

  <!-- ========================================== -->
  <!-- DIAPO 02: SOBRE EL PONENTE (page-02.png)   -->
  <!-- ========================================== -->
  <section class="slide" data-index="2" data-act="Apertura · Ponente" data-time="1.5 min">
    <h2 class="slide-main-title display">Sobre el ponente</h2>
    <div class="speaker-layout">
      <div class="speaker-avatar-wrap">
        <div class="speaker-avatar">
          <img src="data:image/jpeg;base64,__PROFILE_IMG__" alt="Alex Prieto Romani">
        </div>
      </div>
      <div class="speaker-info">
        <div class="speaker-name display">Alex Prieto Romani</div>
        <div class="speaker-role mono">Agriculture Data Science · Hortifrut SA</div>
        <div style="font-size:16px; font-weight:700; color:#FFFFFF; margin-bottom:12px; font-family:'Space Grotesk',sans-serif;">Mg Sc Big Data &amp; Data Science – Ing Agrónomo</div>
        
        <ul class="speaker-bullets">
          <li class="speaker-bullet-item">
            <span class="speaker-bullet-dot"></span>
            <div>Experiencia en el sector agroindustrial desde breeding, calidad de fruta, proyecciones agrícolas, agricultura de presición y diseños estadisticos para ensayos agronómicos.</div>
          </li>
          <li class="speaker-bullet-item">
            <span class="speaker-bullet-dot"></span>
            <div>Proyectos en Computer vision, ML y DL en el sector agroindustrial.</div>
          </li>
        </ul>

        <div class="speaker-socials">
          <a href="https://linkedin.com/in/alex-prieto-romani" target="_blank" class="speaker-social-link">
            <span>🔗</span> linkedin.com/in/alex-prieto-romani
          </a>
          <a href="mailto:alexprieto1997@gmail.com" class="speaker-social-link">
            <span>✉️</span> alexprieto1997@gmail.com
          </a>
          <a href="https://github.com/AlexPrietoRomani" target="_blank" class="speaker-social-link">
            <span>🐙</span> github.com/AlexPrietoRomani
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================== -->
  <!-- DIAPO 03: AGENDA (page-03.png)             -->
  <!-- ========================================== -->
  <section class="slide" data-index="3" data-act="Apertura · Agenda" data-time="1.0 min">
    <h2 class="slide-main-title display">Agenda</h2>
    <div class="agenda-grid-5">
      <div class="agenda-card item-1">
        <div class="agenda-num">01</div>
        <div class="agenda-text-wrap">
          <div class="agenda-card-title display">Historia de los modelos</div>
          <div class="agenda-card-desc">De la descomposición canónica y ARIMA a PatchTST y Foundation Models.</div>
        </div>
      </div>

      <div class="agenda-card item-2">
        <div class="agenda-num">02</div>
        <div class="agenda-text-wrap">
          <div class="agenda-card-title display">Caso 1: Clima en Iquitos</div>
          <div class="agenda-card-desc">2,557 días en SENAMHI Punchana, la trampa de los árboles y el cono a 7 días.</div>
        </div>
      </div>

      <div class="agenda-card item-3">
        <div class="agenda-num">03</div>
        <div class="agenda-text-wrap">
          <div class="agenda-card-title display">Series temporales en el agro</div>
          <div class="agenda-card-desc">Física biológica, retrasos fenológicos de meses y series de ultrabaja frecuencia.</div>
        </div>
      </div>

      <div class="agenda-card item-4">
        <div class="agenda-num">04</div>
        <div class="agenda-text-wrap">
          <div class="agenda-card-title display">Caso 2: Predicción de rendimiento con NDVI</div>
          <div class="agenda-card-desc">24 campañas de café en Jaén: la ceguera de la roya (-56%), saturación de copas y fusión fenológica.</div>
        </div>
      </div>

      <div class="agenda-card item-5">
        <div class="agenda-num">05</div>
        <div class="agenda-text-wrap">
          <div class="agenda-card-title display">Conclusiones &amp; Lecciones</div>
          <div class="agenda-card-desc">Causalidad temporal sin trampas, valor en las bandas P10–P90 y física antes que hiperparámetros.</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 04: SECCIÓN 01: HISTORIA Y FUNDAMENTOS (page-04.png)    -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-section" data-index="4" data-act="Acto 1 · Historia y Fundamentos" data-time="1.0 min">
    <div class="section-huge-num">01</div>
    <h2 class="section-title display">Historia de los modelos de series temporales</h2>
    <p class="section-desc">
      De las ecuaciones cerradas de Verhulst y Box-Jenkins al Machine Learning tabular, Transformers y Foundation Models Zero-Shot: qué cambia en cada era y qué límites físicos permanecen inmutables.
    </p>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 05: ANATOMÍA ONTOLÓGICA 3D (SIMULADOR INTERACTIVO TOTAL) -->
  <!-- ============================================================= -->
  <section class="slide" data-index="5" data-act="Acto 1 · Anatomía de la Señal" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(18, 200, 252, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_SIM_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide5"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 06: ERA 1: LA PARSIMONIA LINEAL (SIMULADOR INTERACTIVO) -->
  <!-- ============================================================= -->
  <section class="slide" data-index="6" data-act="Acto 1 · Era 1: Clásicos Analíticos" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(56, 239, 255, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_ERA1_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide6"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 07: ERA 2: EL PUENTE TABULAR (SIMULADOR INTERACTIVO)    -->
  <!-- ============================================================= -->
  <section class="slide" data-index="7" data-act="Acto 1 · Era 2: El Puente Tabular" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(56, 239, 255, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_ERA2_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide7"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 08: ERA 3: DEEP LEARNING Y PARCHES (SIMULADOR INTERACTIVO) -->
  <!-- ============================================================= -->
  <section class="slide" data-index="8" data-act="Acto 1 · Era 3: Deep Learning" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(180, 142, 255, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_ERA3_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide8"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 09: ERA 4: FOUNDATION MODELS ZERO-SHOT (SIMULADOR INTERACTIVO) -->
  <!-- ============================================================= -->
  <section class="slide" data-index="9" data-act="Acto 1 · Era 4: Foundation Models" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(110, 240, 180, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_ERA4_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide9"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 10: EL CONO DE INCERTIDUMBRE (SIMULADOR INTERACTIVO)    -->
  <!-- ============================================================= -->
  <section class="slide" data-index="10" data-act="Acto 1 · Cono de Incertidumbre" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(255, 107, 107, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_CONO_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide10"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 11: ÁRBOL DE DECISIÓN DE ARQUITECTURA (SIMULADOR INTERACTIVO) -->
  <!-- ============================================================= -->
  <section class="slide" data-index="11" data-act="Acto 1 · Arquitectura de Decisión" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(56, 239, 255, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_DECISION_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide11"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 12: SECCIÓN 02: CASO 1: IQUITOS SENAMHI (page-04.png)   -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-section" data-index="12" data-act="Acto 2 · Caso 1: Clima SENAMHI" data-time="1.0 min">
    <div class="section-huge-num">02</div>
    <h2 class="section-title display">Caso 1: Predicción de temperatura en Iquitos</h2>
    <p class="section-desc">
      Auditoría empírica con 2,557 días de mediciones reales en la estación Punchana de SENAMHI (Loreto). Cómo la física tropical desafía a los algoritmos y por qué los modelos en niveles fallan en olas de calor récord.
    </p>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 13: DATOS QUE IMPORTAN: SENAMHI (page-07.png)           -->
  <!-- ============================================================= -->
  <section class="slide" data-index="13" data-act="Acto 2 · Datos SENAMHI" data-time="1.5 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(18, 200, 252, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P13_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide13"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 14: LA TRAMPA DE LA NO LINEALIDAD (page-06.png)         -->
  <!-- ============================================================= -->
  <section class="slide" data-index="14" data-act="Acto 2 · Extrapolación de Árboles" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(18, 200, 252, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P14_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide14"></iframe>
    </div>
  </section>
"""
    return (
        slides.replace("__HEADER_LOGO__", b64_header)
        .replace("__PROFILE_IMG__", b64_profile)
        .replace("__B64_SIM_HTML__", b64_sim_html)
        .replace("__B64_ERA1_HTML__", b64_era1_html)
        .replace("__B64_ERA2_HTML__", b64_era2_html)
        .replace("__B64_ERA3_HTML__", b64_era3_html)
        .replace("__B64_ERA4_HTML__", b64_era4_html)
        .replace("__B64_CONO_HTML__", b64_cono_html)
        .replace("__B64_DECISION_HTML__", b64_decision_html)
        .replace("__B64_P13_HTML__", b64_p13_html)
        .replace("__B64_P14_HTML__", b64_p14_html)
    )

