from deck_branding import AGENDA, AGENDA_TOTAL_MINUTES, get_separator_copy


def render_agenda_rows():
    """Devuelve las filas HTML de la agenda construidas desde AGENDA."""
    rows = []
    for index, item in enumerate(AGENDA, start=1):
        rows.append(
            f'<div class="agenda-row item-{index}">'
            f'<div class="agenda-num">{item["number"]}</div>'
            f'<div class="agenda-icon">{item["icon"]}</div>'
            f'<div class="agenda-text"><div class="agenda-question">{item["question"]}</div>'
            f'<div class="agenda-takeaway">{item["takeaway"]}</div></div>'
            f'<div class="agenda-minutes">{item["minutes"]} min</div>'
            "</div>"
        )
    return "\n".join(rows)


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
    b64_p12_html = branding.get("b64_p12_html", "")
    b64_p13_html = branding.get("b64_p13_html", "")
    b64_p14_html = branding.get("b64_p14_html", "")
    cinematic_gates = branding.get("cinematic_gates", {})
    qr_svg = branding.get("qr_svg", "")
    sep1_title, sep1_subtitle = get_separator_copy(1)
    sep2_title, sep2_subtitle = get_separator_copy(2)

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
    </div>

    <div class="cover-main">
      <h1 class="cover-title display">¿Puede la IA predecir el futuro? Casos forecasting</h1>
      <p class="cover-subtitle">Lecciones desde el mundo real con datos meteorológicos de SENAMHI y series agrícolas de Jaén</p>
      <div class="cover-pills">
        <span class="cover-pill">GEO Data Science</span>
        <span class="cover-pill">Agricultural Data Science</span>
        <span class="cover-pill">Machine Learning Engineering</span>
        <span class="cover-pill">Forecasting</span>
      </div>
      <div class="cover-speaker-card">
        <div class="cover-speaker-name display">Alex Prieto Romani</div>
        <div class="cover-speaker-role">Agriculture Data Science · Hortifrut S.A.</div>
      </div>
    </div>
  </section>

  <!-- ========================================== -->
  <!-- DIAPO 02: SOBRE EL PONENTE (page-02.png)   -->
  <!-- ========================================== -->
  <section class="slide" data-index="2" data-act="Apertura · Ponente" data-time="1.5 min">
    <h2 class="slide-main-title display">Sobre el ponente</h2>
    <div class="sp-layout">
      <aside class="sp-id">
        <div class="sp-photo"><img src="data:image/jpeg;base64,__PROFILE_IMG__" alt="Alex Prieto Romani"></div>
        <div class="sp-name display">Alex Prieto Romani</div>
        <div class="sp-headline">Ingeniero Agrónomo · Agriculture Data Scientist</div>
        <div class="sp-role mono">Agriculture Data Science · Hortifrut S.A.</div>
        <p class="sp-pitch">Uno la biología del cultivo con machine learning para predecir clima y cosechas con datos reales.</p>
        <div class="sp-contact">
          <div class="sp-socials">
            <a href="https://linkedin.com/in/alex-prieto-romani" target="_blank" class="sp-link">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4h4v16H4zM6 2a2 2 0 110 4 2 2 0 010-4zM10 9h3.6v2c.6-1.2 2-2.3 4-2.3 3.4 0 4.4 2.2 4.4 5.3V20h-4v-5.4c0-1.4-.3-2.6-1.9-2.6S14 13.2 14 14.6V20h-4z"/></svg>
              linkedin.com/in/alex-prieto-romani
            </a>
            <a href="mailto:alexprieto1997@gmail.com" class="sp-link">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18a1 1 0 011 1v12a1 1 0 01-1 1H3a1 1 0 01-1-1V6a1 1 0 011-1zm1.5 2.3V8l7.5 5 7.5-5v-.7L12 12.2z"/></svg>
              alexprieto1997@gmail.com
            </a>
            <a href="https://github.com/AlexPrietoRomani" target="_blank" class="sp-link">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 00-3.2 19.5c.5.1.7-.2.7-.5v-1.8c-2.8.6-3.4-1.2-3.4-1.2-.5-1.2-1.1-1.5-1.1-1.5-.9-.6.1-.6.1-.6 1 .1 1.5 1 1.5 1 .9 1.5 2.4 1.1 3 .8.1-.7.4-1.1.6-1.4-2.2-.3-4.6-1.1-4.6-5 0-1.1.4-2 1-2.7-.1-.3-.4-1.3.1-2.7 0 0 .8-.3 2.7 1a9.4 9.4 0 015 0c1.9-1.3 2.7-1 2.7-1 .5 1.4.2 2.4.1 2.7.6.7 1 1.6 1 2.7 0 3.9-2.4 4.7-4.6 5 .4.3.7.9.7 1.8v2.7c0 .3.2.6.7.5A10 10 0 0012 2z"/></svg>
              github.com/AlexPrietoRomani
            </a>
          </div>
          <div class="sp-qr">
            <div class="sp-qr-box" aria-label="QR a alexprietoromani.github.io">__SPEAKER_QR__</div>
            <span>Escanea para<br>ver mi web</span>
          </div>
        </div>
      </aside>

      <div class="sp-main">
        <div class="sp-cols">
          <div class="sp-col">
            <div class="sp-col-title"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3L1 9l11 6 9-4.9V17h2V9zM5 13.2V17c0 1.7 3.1 3 7 3s7-1.3 7-3v-3.8l-7 3.800z"/></svg>Formación</div>
            <ul class="sp-tl">
              <li class="sp-tl-key">
                <div class="sp-tl-what">Maestría en Big Data y Data Science</div>
                <div class="sp-tl-where">Universidad Internacional de Valencia (VIU), España · 2024–2025</div>
              </li>
              <li class="sp-tl-key">
                <div class="sp-tl-what">Especialización en Machine Learning Engineering</div>
                <div class="sp-tl-where">DMC Perú · 2024 · MLOps y despliegue de modelos</div>
              </li>
              <li>
                <div class="sp-tl-what">Ingeniero Agrónomo</div>
                <div class="sp-tl-where">Universidad Nacional Agraria La Molina (UNALM) · 2015–2020</div>
              </li>
            </ul>
          </div>
          <div class="sp-col">
            <div class="sp-col-title"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 4h4a2 2 0 012 2v1h4a2 2 0 012 2v9a2 2 0 01-2 2H4a2 2 0 01-2-2V9a2 2 0 012-2h4V6a2 2 0 012-2zm0 2v1h4V6z"/></svg>Trayectoria</div>
            <ul class="sp-tl">
              <li class="sp-tl-key">
                <div class="sp-tl-what">Agriculture Data Science</div>
                <div class="sp-tl-where">Hortifrut S.A. · 2025–hoy</div>
              </li>
              <li>
                <div class="sp-tl-what">Data Science I+D</div>
                <div class="sp-tl-where">Camposol S.A. · 2024–2025</div>
              </li>
              <li>
                <div class="sp-tl-what">Investigador de Mejoramiento Genético</div>
                <div class="sp-tl-where">Camposol S.A. · 2023–2024</div>
              </li>
            </ul>
          </div>
          <div class="sp-col">
            <div class="sp-col-title"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.4 6.600L21 11l-6.6 2.400L12 20l-2.4-6.600L3 11l6.6-2.400z"/></svg>Qué hago</div>
            <ul class="sp-do">
              <li>
                <span class="sp-do-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"/></svg></span>
                <div><div class="sp-tl-what">Agricultura de precisión</div><div class="sp-tl-where">Satélite, NDVI y clima</div></div>
              </li>
              <li>
                <span class="sp-do-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 20h18v2H3zM5 11h3v8H5zM10.5 5h3v14h-3zM16 8h3v11h-3z"/></svg></span>
                <div><div class="sp-tl-what">Modelos predictivos y visión artificial</div><div class="sp-tl-where">Rendimiento, enfermedades, conteo de fruta</div></div>
              </li>
              <li>
                <span class="sp-do-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4h16a2 2 0 012 2v10a2 2 0 01-2 2h-7l-5 4v-4H4a2 2 0 01-2-2V6a2 2 0 012-2z"/></svg></span>
                <div><div class="sp-tl-what">IA generativa y LLMs</div><div class="sp-tl-where">Asistentes RAG y reportes automáticos</div></div>
              </li>
            </ul>
          </div>
        </div>
        <div class="sp-stack">
          <span class="sp-stack-label mono">Stack</span>
          <span class="sp-chip">Python</span><span class="sp-chip">R</span><span class="sp-chip">SQL</span><span class="sp-chip">Rust</span><span class="sp-chip">PyTorch</span><span class="sp-chip">Scikit-learn</span><span class="sp-chip">MLflow</span><span class="sp-chip">Docker</span><span class="sp-chip">Google Earth Engine</span><span class="sp-chip">GCP</span>
        </div>
      </div>
    </div>
  </section>



  <!-- ========================================== -->
  <!-- DIAPO 03: AGENDA (page-03.png)             -->
  <!-- ========================================== -->
  <section class="slide" data-index="3" data-act="Apertura · Agenda" data-time="1.0 min">
    <h2 class="slide-main-title display">Agenda</h2>
    <div class="agenda-list">
__AGENDA_ROWS__
    </div>
    <div class="agenda-total mono">Duración total · __AGENDA_TOTAL__ min</div>
  </section>


  <!-- ============================================================= -->
  <!-- DIAPO 04: SECCIÓN 01: HISTORIA Y FUNDAMENTOS (page-04.png)    -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-section act-bg-1" data-index="4" data-act="Acto 1 · Historia y Fundamentos" data-time="1.0 min">
    <div class="section-huge-num">01</div>
    <h2 class="section-title display">__SEP1_TITLE__</h2>
    <p class="section-desc">__SEP1_SUBTITLE__</p>
  </section>


  <!-- ============================================================= -->
  <!-- DIAPO 05: ANATOMÍA ONTOLÓGICA 3D (SIMULADOR INTERACTIVO TOTAL) -->
  <!-- ============================================================= -->
  <section class="slide" data-index="5" data-act="Acto 1 · Anatomía de la Señal" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(18, 200, 252, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_SIM_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide5"></iframe>
      __CINEMATIC_GATE_5__
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
      __CINEMATIC_GATE_7__
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
      __CINEMATIC_GATE_9__
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 10: EL CONO DE INCERTIDUMBRE (SIMULADOR INTERACTIVO)    -->
  <!-- ============================================================= -->
  <section class="slide" data-index="10" data-act="Acto 1 · Cono de Incertidumbre" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(255, 107, 107, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_CONO_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide10"></iframe>
      __CINEMATIC_GATE_10__
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
  <!-- DIAPO 12: SECCIÓN 02: CASO 1: CLIMA EN IQUITOS (SEPARADOR)    -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-section act-bg-2" data-index="12" data-act="Acto 2 · Caso 1: Clima en Iquitos" data-time="1.0 min">
    <div class="section-huge-num">02</div>
    <h2 class="section-title display">__SEP2_TITLE__</h2>
    <p class="section-desc">__SEP2_SUBTITLE__</p>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 13: SECCIÓN 02: CASO 1: IQUITOS SENAMHI (PROTOTIPO)     -->
  <!-- ============================================================= -->
  <section class="slide" data-index="13" data-act="Acto 2 · Caso 1: Clima SENAMHI" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(18, 200, 252, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P12_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide13"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 14: DATOS QUE IMPORTAN: SENAMHI (page-07.png)           -->
  <!-- ============================================================= -->
  <section class="slide" data-index="14" data-act="Acto 2 · Datos SENAMHI" data-time="1.5 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(18, 200, 252, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P13_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide14"></iframe>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 15: LA TRAMPA DE LA NO LINEALIDAD (page-06.png)         -->
  <!-- ============================================================= -->
  <section class="slide" data-index="15" data-act="Acto 2 · Extrapolación de Árboles" data-time="2.0 min" style="inset: 6px 12px; padding: 0; display: flex; flex-direction: column;">
    <div style="width: 100%; height: 100%; flex: 1; min-height: 0; border-radius: 14px; overflow: hidden; border: 1.5px solid rgba(18, 200, 252, 0.35); background: #030712; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);">
      <iframe src="data:text/html;base64,__B64_P14_HTML__" style="width: 100%; height: 100%; border: none; display: block;" allow="fullscreen" id="iframeSlide15"></iframe>
    </div>
  </section>
"""
    return (
        slides.replace("__HEADER_LOGO__", b64_header)
        .replace("__SPEAKER_QR__", qr_svg)
        .replace("__AGENDA_ROWS__", render_agenda_rows())
        .replace("__AGENDA_TOTAL__", str(AGENDA_TOTAL_MINUTES))
        .replace("__SEP2_TITLE__", sep2_title)
        .replace("__SEP2_SUBTITLE__", sep2_subtitle)
        .replace("__SEP1_TITLE__", sep1_title)
        .replace("__SEP1_SUBTITLE__", sep1_subtitle)
        .replace("__PROFILE_IMG__", b64_profile)
        .replace("__B64_SIM_HTML__", b64_sim_html)
        .replace("__B64_ERA1_HTML__", b64_era1_html)
        .replace("__B64_ERA2_HTML__", b64_era2_html)
        .replace("__B64_ERA3_HTML__", b64_era3_html)
        .replace("__B64_ERA4_HTML__", b64_era4_html)
        .replace("__B64_CONO_HTML__", b64_cono_html)
        .replace("__B64_DECISION_HTML__", b64_decision_html)
        .replace("__B64_P12_HTML__", b64_p12_html)
        .replace("__B64_P13_HTML__", b64_p13_html)
        .replace("__B64_P14_HTML__", b64_p14_html)
        .replace("__CINEMATIC_GATE_5__", cinematic_gates.get(5, ""))
        .replace("__CINEMATIC_GATE_7__", cinematic_gates.get(7, ""))
        .replace("__CINEMATIC_GATE_9__", cinematic_gates.get(9, ""))
        .replace("__CINEMATIC_GATE_10__", cinematic_gates.get(10, ""))
    )

