def get_deck_css(branding=None):
    if branding is None:
        branding = {}
    b64_bg_slide = branding.get("b64_bg_slide", "")
    b64_bg_portada = branding.get("b64_bg_portada", "")
    b64_bg_closing = branding.get("b64_bg_closing", "")

    bg_slide_css = f"url('data:image/png;base64,{b64_bg_slide}')" if b64_bg_slide else "#03050F"
    bg_portada_css = f"url('data:image/png;base64,{b64_bg_portada}')" if b64_bg_portada else "#03050F"
    bg_closing_css = f"url('data:image/png;base64,{b64_bg_closing}')" if b64_bg_closing else bg_portada_css
    bg_section_css = bg_portada_css

    return f"""
  :root {{
    /* PALETA OFICIAL IQUITOS DATA FEST 2026 (theme1.xml) */
    --bg-dark: #03050F;
    --bg-dark-panel: rgba(11, 22, 56, 0.85);
    --bg-dark-sub: rgba(17, 29, 66, 0.75);
    --bg-visual-dark: rgba(8, 16, 44, 0.90);
    
    --fest-cyan: #12C8FC;       /* accent1: Cian eléctrico oficial */
    --fest-blue: #1E7BFF;       /* accent2: Azul eléctrico */
    --fest-purple: #9B5CFF;     /* accent3: Morado neón */
    --fest-magenta: #E040FB;    /* accent4: Magenta neón */
    --fest-amber: #FFC857;      /* accent5: Ámbar IDEA CLAVE */
    --fest-emerald: #2EE6A6;    /* accent6: Verde menta */
    
    --text-main: #FFFFFF;       /* dk1: Blanco nítido */
    --text-sub: #CBD5E1;        /* Texto secundario */
    --text-faint: #A9B8DA;      /* dk2: Azul grisáceo oficial */
    
    --line-border: rgba(18, 200, 252, 0.28);
    --line-faint: rgba(169, 184, 218, 0.16);

    /* ALIASES PARA COMPATIBILIDAD */
    --bg-light: #03050F;
    --bg-light-panel: rgba(11, 22, 56, 0.85);
    --bg-light-sub: rgba(17, 29, 66, 0.75);
    --bg-visual-light: rgba(8, 16, 44, 0.90);
    --text-light-main: #FFFFFF;
    --text-light-mute: #CBD5E1;
    --text-light-faint: #A9B8DA;
    --line-light: rgba(18, 200, 252, 0.28);
    --line-light-faint: rgba(169, 184, 218, 0.16);
    --accent-blue: #12C8FC;
    --accent-blue-light: #60A5FA;
    
    --badge-teoria: #9B5CFF;
    --badge-teoria-bg: rgba(155, 92, 255, 0.15);
    --badge-teoria-border: rgba(155, 92, 255, 0.4);
    
    --badge-mecanismo: #12C8FC;
    --badge-mecanismo-bg: rgba(18, 200, 252, 0.15);
    --badge-mecanismo-border: rgba(18, 200, 252, 0.4);
    
    --badge-evidencia: #FFC857;
    --badge-evidencia-bg: rgba(255, 200, 87, 0.15);
    --badge-evidencia-border: rgba(255, 200, 87, 0.4);
    
    --badge-caso_real: #2EE6A6;
    --badge-caso_real-bg: rgba(46, 230, 166, 0.15);
    --badge-caso_real-border: rgba(46, 230, 166, 0.4);
    
    --badge-demo: #E040FB;
    --badge-demo-bg: rgba(224, 64, 251, 0.15);
    --badge-demo-border: rgba(224, 64, 251, 0.4);
    
    --footer-h: 56px;

    /* LAYOUT Y PROPORCIONES */
    --deck-pad-x: clamp(24px, 3.2vw, 56px);
    --deck-pad-y: clamp(18px, 2.2vh, 32px);
    --card-radius: 16px;
    --card-sub-radius: 10px;
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  
  body {{
    font-family: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background-color: var(--bg-dark);
    background-image: {bg_slide_css};
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: var(--text-main);
    overflow: hidden;
    width: 100vw;
    height: 100vh;
    display: flex;
    flex-direction: column;
    -webkit-font-smoothing: antialiased;
  }}

  .mono {{ font-family: "IBM Plex Mono", monospace; }}
  .display {{ font-family: "Space Grotesk", "Arial Black", sans-serif; }}

  /* TOP PROGRESS BAR */
  .progress-container {{
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: rgba(11, 22, 56, 0.85);
    z-index: 100;
  }}
  .progress-bar {{
    height: 100%;
    width: 5%;
    background: linear-gradient(90deg, #12C8FC, #1E7BFF, #9B5CFF);
    box-shadow: 0 0 10px rgba(18, 200, 252, 0.8);
    transition: width 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }}

  /* CONTENEDOR PRINCIPAL DE DIAPOSITIVAS */
  .deck-container {{
    width: 100vw;
    height: calc(100vh - var(--footer-h));
    padding: var(--deck-pad-y) var(--deck-pad-x);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    position: relative;
  }}

  .slide {{
    position: absolute;
    inset: var(--deck-pad-y) var(--deck-pad-x);
    opacity: 0;
    pointer-events: none;
    display: flex;
    flex-direction: column;
    transition: opacity 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }}

  .slide.active {{
    opacity: 1;
    pointer-events: auto;
    z-index: 10;
  }}

  /* TÍTULO ESTÁNDAR SUPERIOR */
  .slide-main-title {{
    font-size: clamp(26px, 2.5vw, 36px);
    font-weight: 700;
    color: var(--text-main);
    letter-spacing: -0.02em;
    margin-bottom: clamp(14px, 1.8vh, 22px);
    flex-shrink: 0;
  }}

  /* ======================================================== */
  /* ARQUETIPO 1: PORTADA OFICIAL (page-01.png)              */
  /* ======================================================== */
  .slide-archetype-cover {{
    background-image: {bg_portada_css};
    background-size: cover;
    background-position: center;
    padding: clamp(36px, 4vw, 64px) clamp(48px, 5.5vw, 90px);
    border: none;
    border-radius: 0;
    box-shadow: none;
    justify-content: space-between;
  }}
  .cover-header-logos {{
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: clamp(24px, 3vh, 36px);
  }}
  .cover-header-logos img {{
    height: clamp(64px, 5.8vw, 82px);
    width: auto;
    object-fit: contain;
    filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.7));
  }}
  .cover-tag {{
    font-size: clamp(16px, 1.25vw, 19px);
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-main);
    margin-bottom: clamp(16px, 2vh, 24px);
  }}
  .cover-tag span {{
    color: var(--fest-cyan);
  }}
  .cover-title {{
    font-size: clamp(38px, 3.8vw, 54px);
    font-weight: 700;
    line-height: 1.15;
    color: var(--text-main);
    max-width: 820px;
    margin-bottom: clamp(16px, 2vh, 24px);
  }}
  .cover-subtitle {{
    font-size: clamp(17px, 1.4vw, 21px);
    color: #94A3B8;
    max-width: 720px;
    line-height: 1.4;
    margin-bottom: clamp(28px, 3.5vh, 44px);
  }}
  .cover-speaker-card {{
    background: rgba(11, 22, 56, 0.75);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1.5px solid var(--fest-cyan);
    border-radius: 16px;
    padding: 18px 28px;
    width: fit-content;
    min-width: 380px;
    max-width: 480px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  }}
  .cover-speaker-name {{
    font-size: 21px;
    font-weight: 700;
    color: var(--text-main);
  }}
  .cover-speaker-role {{
    font-size: 15px;
    color: var(--fest-cyan);
    margin-top: 5px;
    font-family: var(--font-mono);
    font-weight: 500;
  }}

  /* ======================================================== */
  /* ARQUETIPO 2: SOBRE EL PONENTE (page-02.png)             */
  /* ======================================================== */
  .speaker-layout {{
    display: grid;
    grid-template-columns: 0.85fr 1.15fr;
    gap: clamp(24px, 3.5vw, 60px);
    align-items: center;
    flex: 1;
  }}
  .speaker-avatar-wrap {{
    display: flex;
    justify-content: center;
    align-items: center;
  }}
  .speaker-avatar {{
    width: clamp(220px, 20vw, 290px);
    height: clamp(220px, 20vw, 290px);
    border-radius: 50%;
    padding: 8px;
    border: 3.5px solid var(--fest-cyan);
    box-shadow: 0 0 35px rgba(18, 200, 252, 0.4), inset 0 0 20px rgba(18, 200, 252, 0.25);
    background: rgba(11, 22, 56, 0.9);
  }}
  .speaker-avatar img {{
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    display: block;
  }}
  .speaker-info {{
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}
  .speaker-name {{
    font-size: clamp(26px, 2.5vw, 36px);
    font-weight: 700;
    color: var(--text-main);
  }}
  .speaker-role {{
    font-size: clamp(14px, 1.1vw, 16.5px);
    color: var(--fest-cyan);
    font-weight: 600;
    margin-bottom: 8px;
    font-family: "IBM Plex Mono", monospace;
  }}
  .speaker-bullets {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 16px;
  }}
  .speaker-bullet-item {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
    font-size: clamp(13.5px, 0.95vw, 15px);
    line-height: 1.45;
    color: var(--text-sub);
  }}
  .speaker-bullet-dot {{
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--fest-cyan);
    margin-top: 8px;
    flex-shrink: 0;
  }}
  .speaker-socials {{
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin-top: 6px;
  }}
  .speaker-social-link {{
    display: inline-flex;
    align-items: center;
    gap: 10px;
    font-size: 13.5px;
    color: var(--fest-cyan);
    text-decoration: none;
    font-family: "IBM Plex Mono", monospace;
    transition: opacity 0.15s;
  }}
  .speaker-social-link:hover {{
    opacity: 0.8;
  }}

  /* ======================================================== */
  /* ARQUETIPO 3: AGENDA (page-03.png)                       */
  /* ======================================================== */
  .agenda-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: clamp(18px, 2vw, 28px);
    flex: 1;
  }}
  .agenda-card {{
    background: rgba(11, 22, 56, 0.82);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: var(--card-radius);
    padding: clamp(20px, 2.2vw, 32px);
    display: flex;
    align-items: center;
    gap: clamp(18px, 2.2vw, 32px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.55);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }}
  .agenda-card:hover {{
    transform: translateY(-3px);
  }}
  .agenda-card.item-1 {{ border: 1.5px solid var(--fest-cyan); box-shadow: 0 8px 25px rgba(18, 200, 252, 0.12); }}
  .agenda-card.item-2 {{ border: 1.5px solid var(--fest-blue); box-shadow: 0 8px 25px rgba(30, 123, 255, 0.12); }}
  .agenda-card.item-3 {{ border: 1.5px solid var(--fest-purple); box-shadow: 0 8px 25px rgba(155, 92, 255, 0.12); }}
  .agenda-card.item-4 {{ border: 1.5px solid var(--fest-magenta); box-shadow: 0 8px 25px rgba(224, 64, 251, 0.12); }}
  .agenda-card.item-5 {{ border: 1.5px solid #2EE6A6; box-shadow: 0 8px 25px rgba(46, 230, 166, 0.12); }}

  .agenda-grid-5 {{
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: 1fr 1fr;
    gap: clamp(14px, 1.6vw, 22px);
    flex: 1;
    min-height: 0;
  }}
  .agenda-grid-5 .agenda-card {{
    padding: clamp(14px, 1.4vw, 20px) clamp(16px, 1.8vw, 26px);
    gap: clamp(14px, 1.6vw, 24px);
  }}
  .agenda-grid-5 .agenda-card.item-1 {{ grid-column: span 2; }}
  .agenda-grid-5 .agenda-card.item-2 {{ grid-column: span 2; }}
  .agenda-grid-5 .agenda-card.item-3 {{ grid-column: span 2; }}
  .agenda-grid-5 .agenda-card.item-4 {{ grid-column: 1 / span 3; }}
  .agenda-grid-5 .agenda-card.item-5 {{ grid-column: 4 / span 3; }}

  .agenda-num {{
    font-size: clamp(38px, 3.4vw, 52px);
    font-weight: 700;
    line-height: 1;
    font-family: "Space Grotesk", sans-serif;
  }}
  .agenda-card.item-1 .agenda-num {{ color: var(--fest-cyan); }}
  .agenda-card.item-2 .agenda-num {{ color: var(--fest-blue); }}
  .agenda-card.item-3 .agenda-num {{ color: var(--fest-purple); }}
  .agenda-card.item-4 .agenda-num {{ color: var(--fest-magenta); }}
  .agenda-card.item-5 .agenda-num {{ color: #2EE6A6; }}

  .agenda-text-wrap {{
    display: flex;
    flex-direction: column;
    gap: 4px;
  }}
  .agenda-card-title {{
    font-size: clamp(16px, 1.25vw, 19px);
    font-weight: 700;
    color: var(--text-main);
  }}
  .agenda-card-desc {{
    font-size: clamp(12.5px, 0.95vw, 14px);
    color: var(--text-faint);
    line-height: 1.4;
  }}

  /* ======================================================== */
  /* ARQUETIPO 4: SEPARADOR DE SECCIÓN (page-04.png)         */
  /* ======================================================== */
  .slide-archetype-section {{
    background-image: {bg_section_css};
    background-size: cover;
    background-position: center;
    padding: clamp(36px, 4vw, 64px) clamp(48px, 5.5vw, 90px);
    border: none;
    border-radius: 0;
    box-shadow: none;
    justify-content: center;
  }}
  .section-huge-num {{
    font-size: clamp(64px, 6.5vw, 96px);
    font-weight: 700;
    color: var(--fest-cyan);
    line-height: 1;
    margin-bottom: 14px;
    font-family: "Space Grotesk", sans-serif;
    text-shadow: 0 0 30px rgba(18, 200, 252, 0.4);
  }}
  .section-title {{
    font-size: clamp(28px, 2.8vw, 42px);
    font-weight: 700;
    color: var(--text-main);
    line-height: 1.2;
    margin-bottom: 18px;
    max-width: 750px;
  }}
  .section-desc {{
    font-size: clamp(15px, 1.2vw, 18px);
    color: var(--text-faint);
    line-height: 1.5;
    max-width: 650px;
  }}

  /* ======================================================== */
  /* ARQUETIPO 5: CONTENIDO + IDEA CLAVE (page-05.png)       */
  /* ======================================================== */
  .content-insight-layout {{
    display: grid;
    grid-template-columns: 1.05fr 0.95fr;
    gap: clamp(24px, 3vw, 48px);
    align-items: stretch;
    flex: 1;
  }}
  .content-bullets-col {{
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 12px;
  }}
  .standard-bullet-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }}
  .standard-bullet-item {{
    display: flex;
    align-items: flex-start;
    gap: 14px;
    font-size: clamp(14px, 1.05vw, 16px);
    line-height: 1.5;
    color: var(--text-sub);
  }}
  .standard-bullet-dot {{
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--fest-cyan);
    box-shadow: 0 0 8px rgba(18, 200, 252, 0.8);
    margin-top: 8px;
    flex-shrink: 0;
  }}
  .standard-bullet-item strong {{
    color: var(--text-main);
  }}

  .archetype-idea-card {{
    background: rgba(11, 22, 56, 0.85);
    backdrop-filter: blur(14px);
    border: 1.5px solid var(--fest-amber);
    border-radius: var(--card-radius);
    padding: clamp(24px, 2.5vw, 36px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 14px;
    box-shadow: 0 0 25px rgba(255, 200, 87, 0.15), inset 0 0 15px rgba(255, 200, 87, 0.05);
  }}
  .archetype-idea-icon {{
    font-size: 38px;
    color: var(--fest-amber);
    line-height: 1;
  }}
  .archetype-idea-label {{
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: var(--fest-amber);
    font-family: "IBM Plex Mono", monospace;
  }}
  .archetype-idea-text {{
    font-size: clamp(16px, 1.25vw, 20px);
    font-weight: 600;
    line-height: 1.45;
    color: var(--text-main);
  }}

  /* ======================================================== */
  /* ARQUETIPO 6: TÍTULO CON GRÁFICO (page-06.png)           */
  /* ======================================================== */
  .graphic-layout {{
    display: grid;
    grid-template-columns: 0.38fr 0.62fr;
    gap: clamp(18px, 2vw, 28px);
    align-items: stretch;
    flex: 1;
    min-height: 0;
  }}
  .graphic-info-col {{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 6px 0;
  }}
  .graphic-card-col {{
    background: rgba(11, 22, 56, 0.85);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1.5px solid var(--line-border);
    border-radius: var(--card-radius);
    padding: clamp(16px, 1.6vw, 24px);
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
    box-shadow: 0 12px 36px -5px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(18, 200, 252, 0.15);
  }}
  .graphic-source {{
    font-size: 11.5px;
    color: var(--text-faint);
    font-family: "IBM Plex Mono", monospace;
    padding-top: 8px;
  }}

  /* ======================================================== */
  /* ARQUETIPO 7: DATOS QUE IMPORTAN / 3 KPIS (page-07.png)   */
  /* ======================================================== */
  .kpis-subtitle {{
    font-size: clamp(14px, 1.1vw, 16px);
    color: var(--text-faint);
    margin-top: -16px;
    margin-bottom: clamp(18px, 2.2vh, 28px);
  }}
  .kpis-3col-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: clamp(18px, 2vw, 28px);
    flex: 1;
    align-items: stretch;
  }}
  .kpi-large-card {{
    background: rgba(11, 22, 56, 0.85);
    backdrop-filter: blur(14px);
    border-radius: var(--card-radius);
    padding: clamp(24px, 2.5vw, 36px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    gap: 14px;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.55);
    transition: transform 0.2s ease;
  }}
  .kpi-large-card:hover {{
    transform: translateY(-3px);
  }}
  .kpi-large-card.card-cyan {{ border: 1.5px solid var(--fest-cyan); box-shadow: 0 8px 30px rgba(18, 200, 252, 0.15); }}
  .kpi-large-card.card-blue {{ border: 1.5px solid var(--fest-blue); box-shadow: 0 8px 30px rgba(30, 123, 255, 0.15); }}
  .kpi-large-card.card-purple {{ border: 1.5px solid var(--fest-purple); box-shadow: 0 8px 30px rgba(155, 92, 255, 0.15); }}

  .kpi-huge-number {{
    font-size: clamp(48px, 4.5vw, 72px);
    font-weight: 700;
    line-height: 1;
    font-family: "Space Grotesk", sans-serif;
  }}
  .kpi-large-card.card-cyan .kpi-huge-number {{ color: var(--fest-cyan); text-shadow: 0 0 20px rgba(18, 200, 252, 0.3); }}
  .kpi-large-card.card-blue .kpi-huge-number {{ color: var(--fest-blue); text-shadow: 0 0 20px rgba(30, 123, 255, 0.3); }}
  .kpi-large-card.card-purple .kpi-huge-number {{ color: var(--fest-purple); text-shadow: 0 0 20px rgba(155, 92, 255, 0.3); }}

  .kpi-card-desc {{
    font-size: clamp(13px, 1.0vw, 15px);
    color: var(--text-sub);
    line-height: 1.45;
  }}

  /* ======================================================== */
  /* ARQUETIPO 8: DEMO / CÓDIGO (page-08.png)                 */
  /* ======================================================== */
  .code-layout {{
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: clamp(24px, 3vw, 44px);
    align-items: stretch;
    flex: 1;
    min-height: 0;
  }}
  .code-editor-box {{
    background: #03050F;
    border: 1.5px solid var(--fest-purple);
    border-radius: var(--card-radius);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.7);
  }}
  .code-editor-header {{
    height: 38px;
    background: rgba(11, 22, 56, 0.8);
    display: flex;
    align-items: center;
    padding: 0 16px;
    gap: 12px;
    border-bottom: 1px solid rgba(155, 92, 255, 0.2);
  }}
  .code-traffic-lights {{
    display: flex;
    gap: 7px;
  }}
  .code-dot {{
    width: 10px;
    height: 10px;
    border-radius: 50%;
  }}
  .code-dot.red {{ background: #EF4444; }}
  .code-dot.yellow {{ background: #F59E0B; }}
  .code-dot.green {{ background: #10B981; }}
  .code-editor-title {{
    font-size: 12px;
    color: var(--text-faint);
    font-family: "IBM Plex Mono", monospace;
  }}
  .code-editor-body {{
    flex: 1;
    padding: clamp(16px, 1.8vw, 24px);
    overflow: auto;
    font-family: "IBM Plex Mono", "Courier New", monospace;
    font-size: clamp(12px, 0.95vw, 13.5px);
    line-height: 1.6;
    color: #CBD5E1;
    white-space: pre-wrap;
  }}
  .code-steps-col {{
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: clamp(16px, 2vh, 24px);
  }}
  .code-step-item {{
    display: flex;
    align-items: flex-start;
    gap: 16px;
  }}
  .code-step-badge {{
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: var(--fest-purple);
    color: #FFFFFF;
    font-weight: 700;
    font-size: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    box-shadow: 0 0 12px rgba(155, 92, 255, 0.5);
  }}
  .code-step-title {{
    font-size: 15.5px;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 3px;
  }}
  .code-step-desc {{
    font-size: 13px;
    color: var(--text-faint);
    line-height: 1.4;
  }}

  /* ======================================================== */
  /* ARQUETIPO 9: CONCLUSIONES (page-09.png)                  */
  /* ======================================================== */
  .conclusions-3col-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: clamp(18px, 2vw, 28px);
    flex: 1;
    align-items: stretch;
  }}
  .conclusion-card {{
    background: rgba(11, 22, 56, 0.85);
    backdrop-filter: blur(14px);
    border-radius: var(--card-radius);
    padding: clamp(24px, 2.5vw, 36px);
    display: flex;
    flex-direction: column;
    gap: 16px;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.55);
  }}
  .conclusion-card.card-1 {{ border: 1.5px solid var(--fest-cyan); box-shadow: 0 8px 30px rgba(18, 200, 252, 0.12); }}
  .conclusion-card.card-2 {{ border: 1.5px solid var(--fest-purple); box-shadow: 0 8px 30px rgba(155, 92, 255, 0.12); }}
  .conclusion-card.card-3 {{ border: 1.5px solid var(--fest-magenta); box-shadow: 0 8px 30px rgba(224, 64, 251, 0.12); }}

  .conclusion-icon-box {{
    width: 48px;
    height: 48px;
    font-size: 32px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
  }}
  .conclusion-card.card-1 .conclusion-icon-box {{ color: var(--fest-cyan); }}
  .conclusion-card.card-2 .conclusion-icon-box {{ color: var(--fest-purple); }}
  .conclusion-card.card-3 .conclusion-icon-box {{ color: var(--fest-magenta); }}

  .conclusion-title {{
    font-size: clamp(17px, 1.3vw, 20px);
    font-weight: 700;
    color: var(--text-main);
  }}
  .conclusion-desc {{
    font-size: clamp(13px, 1.0vw, 15px);
    color: var(--text-sub);
    line-height: 1.5;
  }}

  /* ======================================================== */
  /* ARQUETIPO 10: CIERRE Y PREGUNTAS (page-10.png)           */
  /* ======================================================== */
  .slide-archetype-closing {{
    background-image: {bg_closing_css};
    background-size: cover;
    background-position: center;
    padding: clamp(36px, 4vw, 64px) clamp(48px, 5.5vw, 90px);
    border: none;
    border-radius: 0;
    box-shadow: none;
    justify-content: space-between;
  }}
  .closing-title {{
    font-size: clamp(52px, 6vw, 84px);
    font-weight: 800;
    color: var(--text-main);
    line-height: 1;
    margin-bottom: 12px;
    letter-spacing: -0.02em;
  }}
  .closing-subtitle {{
    font-size: clamp(24px, 2.4vw, 32px);
    font-weight: 700;
    color: var(--fest-cyan);
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 24px;
  }}
  .closing-cards-wrap {{
    display: flex;
    gap: 20px;
    align-items: stretch;
    max-width: 720px;
  }}
  .closing-contact-card {{
    background: rgba(11, 22, 56, 0.75);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1.5px solid var(--fest-cyan);
    border-radius: 16px;
    padding: 20px 28px;
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 8px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  }}
  .closing-qr-card {{
    background: rgba(11, 22, 56, 0.75);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1.5px dashed var(--fest-cyan);
    border-radius: 16px;
    padding: 16px 20px;
    width: 170px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  }}
  .closing-qr-box {{
    width: 120px;
    height: 120px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .closing-qr-box img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
  }}
  .closing-bottom-logos {{
    display: flex;
    align-items: center;
    gap: 24px;
    margin-top: 16px;
  }}
  .closing-bottom-logos img:first-child {{
    height: clamp(52px, 4.8vw, 64px);
    width: auto;
    object-fit: contain;
    filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.7));
  }}
  .closing-bottom-logos img:last-child {{
    height: clamp(44px, 4.0vw, 54px);
    width: auto;
    object-fit: contain;
    border-radius: 6px;
  }}

  /* ======================================================== */
  /* FOOTER Y CONTROLES                                       */
  /* ======================================================== */
  .deck-footer {{
    height: var(--footer-h);
    background: rgba(3, 5, 15, 0.95);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-top: 1.5px solid rgba(18, 200, 252, 0.28);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 clamp(16px, 2.0vw, 32px);
    z-index: 50;
    flex-shrink: 0;
  }}
  .nav-btn {{
    background: rgba(11, 22, 56, 0.85);
    border: 1px solid rgba(18, 200, 252, 0.35);
    color: #FFFFFF;
    font-size: 12px;
    font-weight: 600;
    padding: 6px 14px;
    border-radius: 6px;
    cursor: pointer;
    font-family: "IBM Plex Mono", monospace;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.15s ease;
  }}
  .nav-btn:hover {{
    background: var(--fest-cyan);
    color: #03050F;
    border-color: var(--fest-cyan);
    box-shadow: 0 0 12px rgba(18, 200, 252, 0.45);
  }}
  .nav-btn:active {{
    transform: scale(0.96);
  }}

  /* SPEAKER DRAWER */
  .speaker-drawer {{
    position: fixed;
    bottom: 0; left: 0; right: 0;
    height: 270px;
    background: #0B1638;
    color: #FFFFFF;
    border-top: 2px solid var(--fest-cyan);
    transform: translateY(100%);
    transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
    z-index: 1000;
    display: flex;
    flex-direction: column;
    box-shadow: 0 -10px 30px rgba(0,0,0,0.7);
  }}
  .speaker-drawer.open {{
    transform: translateY(0);
  }}
  .speaker-header {{
    height: 42px;
    padding: 0 20px;
    background: #03050F;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(18, 200, 252, 0.2);
  }}
  .speaker-body {{
    flex: 1;
    padding: 16px 24px;
    overflow-y: auto;
    font-size: 14px;
    line-height: 1.6;
    color: #CBD5E1;
  }}

  /* UTILITY CHIPS & BADGES */
  .badge {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 9999px;
    width: fit-content;
    font-family: "IBM Plex Mono", monospace;
  }}
  .badge-teoria {{ color: var(--badge-teoria); background: var(--badge-teoria-bg); border: 1px solid var(--badge-teoria-border); }}
  .badge-mecanismo {{ color: var(--badge-mecanismo); background: var(--badge-mecanismo-bg); border: 1px solid var(--badge-mecanismo-border); }}
  .badge-evidencia {{ color: var(--badge-evidencia); background: var(--badge-evidencia-bg); border: 1px solid var(--badge-evidencia-border); }}
  .badge-caso_real {{ color: var(--badge-caso_real); background: var(--badge-caso_real-bg); border: 1px solid var(--badge-caso_real-border); }}
  .badge-demo {{ color: var(--badge-demo); background: var(--badge-demo-bg); border: 1px solid var(--badge-demo-border); }}

  .chart-wrapper {{
    flex: 1;
    min-height: 0;
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
  }}

  /* CONTROLES INTERACTIVOS DE GRÁFICOS (CHIPS/TABS) */
  .chart-toolbar {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 10px;
    flex-wrap: wrap;
    flex-shrink: 0;
    z-index: 5;
  }}
  .chart-filter-btn {{
    background: rgba(11, 22, 56, 0.7);
    border: 1px solid rgba(18, 200, 252, 0.25);
    color: #CBD5E1;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 6px;
    cursor: pointer;
    font-family: "IBM Plex Mono", monospace;
    transition: all 0.15s ease;
  }}
  .chart-filter-btn:hover {{
    background: rgba(18, 200, 252, 0.18);
    color: #12C8FC;
    border-color: #12C8FC;
  }}
  .chart-filter-btn.active {{
    background: #12C8FC;
    color: #03050F;
    border-color: #12C8FC;
    box-shadow: 0 0 10px rgba(18, 200, 252, 0.4);
    font-weight: 700;
  }}

  /* LIGHTBOX MODAL */
  .lightbox-modal {{
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(3, 5, 15, 0.95);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    z-index: 9999;
    justify-content: center;
    align-items: center;
    padding: 30px;
  }}
  .lightbox-modal.active {{
    display: flex;
  }}
  .lightbox-modal-content {{
    max-width: 92vw;
    max-height: 88vh;
    border-radius: 12px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.9);
    object-fit: contain;
  }}
  .lightbox-close {{
    position: absolute;
    top: 24px;
    right: 32px;
    color: #FFFFFF;
    font-size: 32px;
    cursor: pointer;
    background: rgba(18, 200, 252, 0.2);
    width: 44px;
    height: 44px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid var(--fest-cyan);
  }}
"""
