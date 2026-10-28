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
    b64_act_bg = branding.get("b64_act_bg", {})
    act_bg_css = "".join(
        f"\n  .slide.act-bg-{act} {{{{ background-image: url('data:image/jpeg;base64,{b64}'); "
        f"background-size: cover; background-position: center; }}}}"
        for act, b64 in b64_act_bg.items() if b64
    )

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

  /* FONDOS POR ACTO (separadores y cierre) */
  {act_bg_css}

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
  .speaker-hero {{
    display: flex;
    align-items: center;
    gap: clamp(24px, 3vw, 48px);
  }}
  .speaker-avatar {{
    width: clamp(150px, 14vw, 200px);
    height: clamp(150px, 14vw, 200px);
    flex-shrink: 0;
    border-radius: 50%;
    padding: 6px;
    border: 3px solid var(--fest-cyan);
    box-shadow: 0 0 30px rgba(18, 200, 252, 0.35), inset 0 0 18px rgba(18, 200, 252, 0.25);
    background: rgba(11, 22, 56, 0.9);
  }}
  .speaker-avatar img {{
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    display: block;
  }}
  .speaker-hero-text {{
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}
  .speaker-name {{
    font-size: clamp(30px, 3vw, 44px);
    font-weight: 700;
    color: var(--text-main);
    line-height: 1.1;
  }}
  .speaker-role {{
    font-size: clamp(14px, 1.1vw, 17px);
    color: var(--fest-cyan);
    font-weight: 600;
    font-family: "IBM Plex Mono", monospace;
  }}
  .speaker-body {{
    flex: 1;
    display: flex;
    align-items: center;
    min-height: 0;
    padding: 24px 0;
  }}
  .speaker-cards {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: clamp(16px, 1.8vw, 28px);
    width: 100%;
  }}
  .speaker-card {{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 14px;
    padding: clamp(24px, 2.8vw, 40px) clamp(18px, 2vw, 28px);
    background: rgba(11, 22, 56, 0.82);
    border-radius: var(--card-radius);
    border: 1.5px solid rgba(18, 200, 252, 0.35);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.55);
  }}
  .speaker-card-icon {{
    font-size: clamp(40px, 5vh, 56px);
    line-height: 1;
  }}
  .speaker-card-title {{
    font-size: clamp(24px, 2.2vw, 32px);
    font-weight: 700;
    color: var(--text-main);
    line-height: 1.2;
  }}
  .speaker-card-sub {{
    font-size: 18px;
    color: var(--text-sub);
    line-height: 1.35;
  }}
  .speaker-footer {{
    margin-top: 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: clamp(20px, 3vw, 48px);
    flex-shrink: 0;
  }}
  .speaker-socials {{
    display: flex;
    flex-direction: column;
    gap: 10px;
  }}
  .speaker-social-link {{
    display: inline-flex;
    align-items: center;
    gap: 10px;
    font-size: 14px;
    color: var(--fest-cyan);
    text-decoration: none;
    font-family: "IBM Plex Mono", monospace;
    transition: opacity 0.15s;
  }}
  .speaker-social-link:hover {{
    opacity: 0.8;
  }}
  .speaker-qr {{
    display: flex;
    align-items: center;
    gap: 16px;
    font-family: "IBM Plex Mono", monospace;
    font-size: 13.5px;
    color: var(--text-sub);
  }}
  .speaker-qr-box {{
    background: #FFFFFF;
    border-radius: 12px;
    padding: 8px;
    line-height: 0;
  }}
  .speaker-qr-box svg {{
    width: clamp(110px, 9vw, 140px);
    height: auto;
  }}

  /* ======================================================== */
  /* ARQUETIPO 3: AGENDA (page-03.png)                       */
  /* ======================================================== */
  .agenda-list {{
    display: flex;
    flex-direction: column;
    gap: clamp(10px, 1.4vh, 16px);
    flex: 1;
    min-height: 0;
  }}
  .agenda-row {{
    flex: 1;
    display: grid;
    grid-template-columns: clamp(64px, 5.5vw, 96px) clamp(44px, 3.6vw, 60px) 1fr auto;
    align-items: center;
    gap: clamp(14px, 1.6vw, 26px);
    padding: 0 clamp(18px, 2vw, 30px);
    background: rgba(11, 22, 56, 0.82);
    border-radius: var(--card-radius);
    border-left: 6px solid var(--row-accent);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
  }}
  .agenda-row.item-1 {{ --row-accent: var(--fest-cyan); }}
  .agenda-row.item-2 {{ --row-accent: var(--fest-blue); }}
  .agenda-row.item-3 {{ --row-accent: var(--fest-purple); }}
  .agenda-row.item-4 {{ --row-accent: var(--fest-magenta); }}
  .agenda-row.item-5 {{ --row-accent: #2EE6A6; }}
  .agenda-num {{
    font-size: clamp(40px, 3.6vw, 56px);
    font-weight: 700;
    line-height: 1;
    font-family: "Space Grotesk", sans-serif;
    color: var(--row-accent);
  }}
  .agenda-icon {{
    font-size: clamp(30px, 2.6vw, 40px);
    line-height: 1;
  }}
  .agenda-text {{
    display: flex;
    flex-direction: column;
    gap: 6px;
    min-width: 0;
  }}
  .agenda-question {{
    font-size: clamp(26px, 1.6vw, 34px);
    font-weight: 700;
    color: var(--text-main);
    line-height: 1.2;
  }}
  .agenda-takeaway {{
    font-size: 18px;
    color: var(--text-faint);
    line-height: 1.35;
  }}
  .agenda-minutes {{
    font-family: var(--font-mono);
    font-size: 22px;
    color: var(--text-sub);
    white-space: nowrap;
  }}
  .agenda-total {{
    font-family: var(--font-mono);
    font-size: 14px;
    color: var(--text-faint);
    text-align: right;
    margin-top: 12px;
    flex-shrink: 0;
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
  /* ======================================================== */
  /* ARQUETIPO 9: CONCLUSIONES (page-09.png)                  */
  /* ======================================================== */
  .conclusions-3col-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: clamp(16px, 1.8vw, 26px);
    flex: 1;
    min-height: 0;
    align-items: stretch;
  }}
  .conclusion-card {{
    background: rgba(11, 22, 56, 0.88);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-radius: var(--card-radius);
    padding: clamp(20px, 2.0vw, 28px);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: clamp(12px, 1.3vw, 16px);
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.6);
  }}
  .conclusion-card.card-1 {{ border: 1.5px solid var(--fest-cyan); box-shadow: 0 10px 32px rgba(18, 200, 252, 0.16); }}
  .conclusion-card.card-2 {{ border: 1.5px solid var(--fest-purple); box-shadow: 0 10px 32px rgba(155, 92, 255, 0.16); }}
  .conclusion-card.card-3 {{ border: 1.5px solid var(--fest-magenta); box-shadow: 0 10px 32px rgba(224, 64, 251, 0.16); }}

  .conclusion-card-head {{
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}
  .conclusion-pill-tag {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    align-self: flex-start;
    padding: 4px 11px;
    border-radius: 999px;
    font-size: 11.5px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }}
  .conclusion-card.card-1 .conclusion-pill-tag {{
    background: rgba(18, 200, 252, 0.12);
    border: 1px solid rgba(18, 200, 252, 0.45);
    color: var(--fest-cyan);
  }}
  .conclusion-card.card-2 .conclusion-pill-tag {{
    background: rgba(155, 92, 255, 0.12);
    border: 1px solid rgba(155, 92, 255, 0.45);
    color: var(--fest-purple);
  }}
  .conclusion-card.card-3 .conclusion-pill-tag {{
    background: rgba(224, 64, 251, 0.12);
    border: 1px solid rgba(224, 64, 251, 0.45);
    color: var(--fest-magenta);
  }}

  .conclusion-card-title-row {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .conclusion-icon-box {{
    width: 46px;
    height: 46px;
    font-size: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 11px;
    background: rgba(255, 255, 255, 0.05);
    flex-shrink: 0;
  }}
  .conclusion-card.card-1 .conclusion-icon-box {{ color: var(--fest-cyan); border: 1px solid rgba(18, 200, 252, 0.35); }}
  .conclusion-card.card-2 .conclusion-icon-box {{ color: var(--fest-purple); border: 1px solid rgba(155, 92, 255, 0.35); }}
  .conclusion-card.card-3 .conclusion-icon-box {{ color: var(--fest-magenta); border: 1px solid rgba(224, 64, 251, 0.35); }}

  .conclusion-title {{
    font-size: clamp(19px, 1.48vw, 23px);
    font-weight: 800;
    color: var(--text-main);
    line-height: 1.2;
    letter-spacing: -0.01em;
  }}
  .conclusion-desc {{
    font-size: clamp(13.5px, 1.02vw, 15px);
    color: var(--text-sub);
    line-height: 1.48;
  }}

  .conclusion-trap-box {{
    padding: 11px 15px;
    border-radius: 9px;
    background: rgba(239, 68, 68, 0.08);
    border-left: 3px solid #f43f5e;
    font-size: clamp(12.5px, 0.94vw, 13.8px);
    color: #fecdd3;
    line-height: 1.42;
  }}
  .conclusion-trap-box strong {{
    color: #ffe4e6;
    font-weight: 700;
  }}

  .conclusion-evidence {{
    display: flex;
    flex-direction: column;
    gap: 9px;
    padding: 13px 16px;
    border-radius: 11px;
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(148, 163, 184, 0.18);
  }}
  .conclusion-evidence-title {{
    font-size: clamp(11.5px, 0.88vw, 13px);
    font-weight: 800;
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }}
  .conclusion-card.card-1 .conclusion-evidence-title {{ color: var(--fest-cyan); }}
  .conclusion-card.card-2 .conclusion-evidence-title {{ color: var(--fest-purple); }}
  .conclusion-card.card-3 .conclusion-evidence-title {{ color: var(--fest-magenta); }}
  .conclusion-evidence-list {{
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 7px;
    font-size: clamp(12.5px, 0.94vw, 14px);
    color: var(--text-sub);
    line-height: 1.42;
  }}
  .conclusion-evidence-list li {{
    position: relative;
    padding-left: 15px;
  }}
  .conclusion-evidence-list li::before {{
    content: "▸";
    position: absolute;
    left: 0;
    font-weight: 700;
  }}
  .conclusion-card.card-1 .conclusion-evidence-list li::before {{ color: var(--fest-cyan); }}
  .conclusion-card.card-2 .conclusion-evidence-list li::before {{ color: var(--fest-purple); }}
  .conclusion-card.card-3 .conclusion-evidence-list li::before {{ color: var(--fest-magenta); }}
  .conclusion-evidence-list strong {{ color: var(--text-main); font-weight: 700; }}

  .conclusion-takeaway {{
    padding: 11px 15px;
    border-left: 3.5px solid var(--fest-cyan);
    border-radius: 0 10px 10px 0;
    background: rgba(18, 200, 252, 0.10);
    font-size: clamp(13px, 0.96vw, 14.5px);
    color: var(--text-main);
    line-height: 1.42;
  }}
  .conclusion-card.card-2 .conclusion-takeaway {{
    border-left-color: var(--fest-purple);
    background: rgba(155, 92, 255, 0.10);
  }}
  .conclusion-card.card-3 .conclusion-takeaway {{
    border-left-color: var(--fest-magenta);
    background: rgba(224, 64, 251, 0.10);
  }}

  /* ======================================================== */
  /* ARQUETIPO 10: CIERRE Y PREGUNTAS (page-10.png)           */
  /* ======================================================== */
  .slide-archetype-closing {{
    background-image: {bg_closing_css};
    background-size: cover;
    background-position: center;
    padding: clamp(34px, 3.8vw, 60px) clamp(44px, 5vw, 84px);
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
    margin-bottom: 10px;
    letter-spacing: -0.02em;
  }}
  .closing-subtitle {{
    font-size: clamp(24px, 2.4vw, 32px);
    font-weight: 700;
    color: var(--fest-cyan);
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 20px;
  }}
  .closing-cards-wrap {{
    display: flex;
    gap: 30px;
    align-items: stretch;
    max-width: 1040px;
  }}
  .closing-contact-card {{
    background: rgba(11, 22, 56, 0.85);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1.5px solid var(--fest-cyan);
    border-radius: 20px;
    padding: 26px 36px;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 16px;
    box-shadow: 0 14px 44px rgba(0, 0, 0, 0.65), 0 0 30px rgba(18, 200, 252, 0.12);
  }}
  .closing-name {{
    font-size: clamp(30px, 2.6vw, 40px);
    font-weight: 800;
    color: #FFFFFF;
    line-height: 1.1;
    letter-spacing: -0.01em;
  }}
  .closing-role-tag {{
    font-size: 14.5px;
    color: var(--fest-cyan);
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 7px;
    margin-top: 6px;
  }}
  .closing-contact-list {{
    font-size: clamp(15.5px, 1.14vw, 17.5px);
    color: #E2E8F0;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}
  .closing-contact-item {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .closing-contact-item a {{
    color: #E2E8F0;
    text-decoration: none;
    transition: color 0.2s ease;
  }}
  .closing-contact-item a:hover {{
    color: var(--fest-cyan);
    text-decoration: underline;
  }}
  .closing-card-footer {{
    padding-top: 14px;
    border-top: 1px solid rgba(148, 163, 184, 0.22);
    font-size: 13.5px;
    color: #94A3B8;
    line-height: 1.4;
  }}
  .closing-qr-card {{
    background: rgba(11, 22, 56, 0.85);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1.5px solid var(--fest-cyan);
    border-radius: 20px;
    padding: 24px 26px;
    width: 275px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 14px;
    box-shadow: 0 14px 44px rgba(0, 0, 0, 0.65), 0 0 32px rgba(18, 200, 252, 0.18);
  }}
  .closing-qr-box {{
    width: 220px;
    height: 220px;
    padding: 12px;
    border-radius: 16px;
    background: radial-gradient(circle at 50% 40%, rgba(18, 200, 252, 0.18), rgba(3, 7, 18, 0.98) 72%);
    border: 1.5px solid rgba(18, 200, 252, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 28px rgba(18, 200, 252, 0.25);
  }}
  .closing-qr-box svg {{
    width: 100%;
    height: 100%;
    display: block;
  }}
  .closing-qr-caption {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
  }}
  .closing-qr-title {{
    font-size: 14px;
    color: var(--fest-cyan);
    font-weight: 800;
    letter-spacing: 0.08em;
  }}
  .closing-qr-sub {{
    font-size: 12.5px;
    color: #94A3B8;
  }}
  .closing-badges {{
    display: flex;
    flex-wrap: wrap;
    gap: 13px;
    margin-top: 20px;
    max-width: 1040px;
  }}
  .closing-badge {{
    padding: 9px 18px;
    border-radius: 999px;
    border: 1px solid rgba(18, 200, 252, 0.4);
    background: rgba(11, 22, 56, 0.75);
    font-size: 13.5px;
    color: #E2E8F0;
    white-space: nowrap;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
  }}
  .closing-bottom-logos {{
    display: flex;
    align-items: center;
    gap: 28px;
    margin-top: 18px;
  }}
  .closing-bottom-logos img:first-child {{
    height: clamp(62px, 5.2vw, 76px);
    width: auto;
    object-fit: contain;
    filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.7));
  }}
  .closing-bottom-logos img:last-child {{
    height: clamp(52px, 4.4vw, 64px);
    width: auto;
    object-fit: contain;
    filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.7));
  }}
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

  /* ======================================================== */
  /* ANATOMY ISOMETRIC FRAMEWORK STYLES                      */
  /* ======================================================== */
  .iso {{
    --anatomy-page: #03050F;
    --anatomy-card: #070D1E;
    --anatomy-text: #94A3B8;
    --anatomy-strong: #F8FAFC;
    --anatomy-muted: #64748B;
    --anatomy-paper: #0B132B;
    --anatomy-face: #101B3B;
    --anatomy-top: #15244F;
    --anatomy-shade-0: #060B18;
    --anatomy-shade-1: #091226;
    --anatomy-shade-2: #0D1A36;
    --anatomy-shade-3: #122245;
    --anatomy-lit-top: #1E3066;
    --anatomy-lit-shade: #182855;
    --anatomy-hi: #12C8FC;
    --anatomy-mid: #4A6999;
    --anatomy-lo: #203359;
    --anatomy-faint: #121D38;
    --anatomy-lit: #FFFFFF;
    --anatomy-halo: #02040A;
    --anatomy-halo-opacity: .95;
    --anatomy-dot: #12C8FC;
    --anatomy-red: #FF4757;
    --anatomy-green: #2EE6A6;
    --anatomy-blue: #1E7BFF;
    --anatomy-weight: .75px;
    --anatomy-mono: "IBM Plex Mono", monospace;
  }}
  .iso-svg {{
    display: block;
    width: 100%;
    height: 100%;
    max-height: 100%;
    overflow: visible;
  }}
  .iso-svg path, .iso-svg circle {{
    vector-effect: non-scaling-stroke;
  }}
  .iso-fill {{ fill: var(--anatomy-paper); stroke: none; }}
  .iso-solid[data-lit] > .iso-fill {{ fill: var(--anatomy-face); }}
  .iso-shade, .iso-top {{ stroke: none; }}
  .iso-shade[data-shade="0"] {{ fill: var(--anatomy-shade-0); }}
  .iso-shade[data-shade="1"] {{ fill: var(--anatomy-shade-1); }}
  .iso-shade[data-shade="2"] {{ fill: var(--anatomy-shade-2); }}
  .iso-shade[data-shade="3"] {{ fill: var(--anatomy-shade-3); }}
  .iso-top {{ fill: var(--anatomy-top); }}
  .iso-solid[data-lit] > .iso-top {{ fill: var(--anatomy-lit-top); }}
  .iso-solid[data-lit] > .iso-shade {{ fill: var(--anatomy-lit-shade); }}
  .iso-halo {{
    fill: var(--anatomy-halo);
    stroke: none;
    filter: blur(10px);
    opacity: var(--anatomy-halo-opacity);
    transform: translateY(4px);
  }}
  .iso-line {{
    fill: none;
    stroke: var(--anatomy-lo);
    stroke-width: var(--anatomy-weight);
    stroke-linecap: round;
    stroke-linejoin: round;
  }}
  .iso-line[data-tone="hi"] {{ stroke: var(--anatomy-hi); }}
  .iso-line[data-tone="mid"] {{ stroke: var(--anatomy-mid); }}
  .iso-line[data-tone="lo"] {{ stroke: var(--anatomy-lo); }}
  .iso-line[data-tone="faint"] {{ stroke: var(--anatomy-faint); }}
  .iso-line[data-tone="lit"] {{ stroke: var(--anatomy-lit); }}
  .iso-line[data-tone="red"] {{ stroke: var(--anatomy-red); }}
  .iso-line[data-tone="green"] {{ stroke: var(--anatomy-green); }}
  .iso-line[data-tone="blue"] {{ stroke: var(--anatomy-blue); }}
  .iso-dots circle {{
    fill: var(--anatomy-dot);
    stroke: none;
    opacity: .5;
  }}
  .iso-dots[data-tone="hi"] circle {{ opacity: .95; }}
  .iso-face-text {{
    fill: var(--anatomy-mid);
    font-family: var(--anatomy-mono);
  }}
  .iso-face-text[data-tone="hi"] {{ fill: var(--anatomy-strong); }}

  /* ======================================================== */
  /* DIAPO 29: TRES LECCIONES (frases grandes, sin tarjetas)  */
  /* ======================================================== */
  .slide-lessons {{
    justify-content: center;
  }}
  .lessons-stack {{
    position: relative;
    z-index: 1;
    flex: 1;
    min-height: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: clamp(18px, 3.2vh, 40px);
    padding: clamp(64px, 11vh, 110px) clamp(24px, 4vw, 90px) clamp(24px, 4vh, 48px);
  }}
  .lesson-row {{
    display: grid;
    grid-template-columns: clamp(72px, 6vw, 112px) minmax(0, 1fr);
    align-items: center;
    gap: clamp(18px, 2vw, 36px);
    padding: clamp(10px, 1.6vh, 20px) clamp(18px, 1.8vw, 30px);
    border-left: 5px solid var(--fest-cyan);
    border-radius: 0 12px 12px 0;
    background: linear-gradient(90deg, rgba(18, 200, 252, 0.10), rgba(18, 200, 252, 0) 70%);
  }}
  .lesson-row-2 {{
    border-left-color: var(--fest-purple);
    background: linear-gradient(90deg, rgba(155, 92, 255, 0.12), rgba(155, 92, 255, 0) 70%);
  }}
  .lesson-row-3 {{
    border-left-color: var(--fest-emerald);
    background: linear-gradient(90deg, rgba(46, 230, 166, 0.10), rgba(46, 230, 166, 0) 70%);
  }}
  .lesson-icon {{
    font-size: clamp(56px, 5vw, 84px);
    line-height: 1;
    text-align: center;
  }}
  .lesson-title {{
    margin: 0;
    font-size: clamp(32px, 3vw, 52px);
    line-height: 1.12;
    color: var(--text-main);
  }}
  .lesson-evidence {{
    margin: clamp(6px, 0.8vh, 12px) 0 0;
    font-size: clamp(18px, 1.6vw, 22px);
    line-height: 1.4;
    color: var(--text-sub);
  }}
"""
