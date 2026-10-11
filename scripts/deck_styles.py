def get_deck_css(branding=None):
    if branding is None:
        branding = {}
    b64_bg_slide = branding.get("b64_bg_slide", "")
    b64_bg_portada = branding.get("b64_bg_portada", "")

    bg_slide_css = f"url('data:image/jpeg;base64,{b64_bg_slide}')" if b64_bg_slide else "radial-gradient(rgba(18, 200, 252, 0.12) 1px, transparent 1px)"
    bg_portada_css = f"linear-gradient(135deg, rgba(3, 5, 15, 0.92) 0%, rgba(3, 5, 15, 0.78) 55%, rgba(3, 5, 15, 0.65) 100%), url('data:image/jpeg;base64,{b64_bg_portada}')" if b64_bg_portada else "linear-gradient(135deg, #03050F 0%, #0B132B 100%)"

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

    /* ALIASES PARA COMPATIBILIDAD CON SLIDES EXISTENTES */
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
    --deck-pad-x: clamp(20px, 2.2vw, 36px);
    --deck-pad-y: clamp(14px, 1.8vh, 24px);
    --deck-gap: clamp(16px, 1.6vw, 24px);
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

  /* TOP PROGRESS BAR CON GRADIENTE CIAN-AZUL-MORADO */
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
    flex-direction: row;
    gap: var(--deck-gap);
    transition: opacity 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }}

  .slide.active {{
    opacity: 1;
    pointer-events: auto;
    z-index: 10;
  }}

  /* DIAPOSITIVA 1: ESTILO PORTADA OFICIAL IQUITOS DATA FEST */
  .slide[data-index="1"] {{
    background-image: {bg_portada_css};
    background-size: cover;
    background-position: center;
    border-radius: var(--card-radius);
    padding: clamp(24px, 2.5vw, 40px);
    border: 1.5px solid rgba(18, 200, 252, 0.35);
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8), inset 0 0 100px rgba(3, 5, 15, 0.85);
  }}

  /* PANEL NARRATIVE (38%) */
  .panel-narrative {{
    flex: 0 0 38%;
    max-width: 38%;
    height: 100%;
    padding: clamp(18px, 1.8vw, 28px);
    display: flex;
    flex-direction: column;
    gap: clamp(10px, 1.2vh, 15px);
    border-radius: var(--card-radius);
    background: var(--bg-dark-panel);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1.5px solid var(--line-border);
    box-shadow: 0 12px 36px -5px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(18, 200, 252, 0.15);
    overflow-y: auto;
    z-index: 2;
  }}

  /* PANEL VISUAL (62%) */
  .panel-visual {{
    flex: 1;
    height: 100%;
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
  }}

  .visual-card {{
    width: 100%;
    height: 100%;
    background: var(--bg-dark-panel);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1.5px solid var(--line-border);
    border-radius: var(--card-radius);
    display: flex;
    flex-direction: column;
    padding: clamp(16px, 1.6vw, 24px);
    position: relative;
    overflow: hidden;
    box-shadow: 0 12px 36px -5px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(18, 200, 252, 0.15);
  }}

  .visual-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--line-faint);
    flex-shrink: 0;
  }}

  .visual-title {{
    font-size: clamp(14px, 1.1vw, 17px);
    font-weight: 700;
    color: var(--text-main);
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .visual-tag {{
    font-size: 11px;
    font-weight: 700;
    color: var(--fest-cyan);
    letter-spacing: 0.06em;
    font-family: "IBM Plex Mono", monospace;
  }}

  .chart-wrapper {{
    flex: 1;
    min-height: 0;
    position: relative;
    width: 100%;
    height: 100%;
  }}

  /* BADGES & CHIPS */
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

  .slide-meta {{
    font-size: 11px;
    color: var(--text-faint);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
  }}

  .slide-title {{
    font-size: clamp(22px, 2.2vw, 30px);
    line-height: 1.16;
    font-weight: 700;
    letter-spacing: -0.025em;
    color: var(--text-main);
  }}

  .slide-thesis {{
    font-size: clamp(13.5px, 1.0vw, 15.5px);
    line-height: 1.48;
    color: var(--text-sub);
    font-weight: 400;
  }}

  .metric-chips {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }}
  .metric-chip {{
    font-size: 11px;
    font-family: "IBM Plex Mono", monospace;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 6px;
    background: var(--bg-dark-sub);
    color: var(--fest-cyan);
    border: 1px solid rgba(18, 200, 252, 0.25);
  }}

  /* VIÑETAS ESTILO PLANTILLA DATA FEST */
  .bullets-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 9px;
    margin: 3px 0;
  }}
  .bullet-item {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
    font-size: clamp(12.8px, 0.92vw, 14.2px);
    line-height: 1.46;
    color: var(--text-sub);
    padding: 11px 14px;
    background: var(--bg-dark-sub);
    border-radius: var(--card-sub-radius);
    border: 1px solid rgba(18, 200, 252, 0.16);
    box-shadow: 0 2px 6px rgba(0,0,0,0.25);
    transition: transform 0.2s ease, border-color 0.2s ease;
  }}
  .bullet-item:hover {{
    transform: translateX(4px);
    border-color: rgba(18, 200, 252, 0.45);
  }}
  .bullet-item strong {{
    color: #FFFFFF;
  }}
  .bullet-icon {{
    flex-shrink: 0;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin-top: 6px;
    background: var(--fest-cyan);
    box-shadow: 0 0 8px rgba(18, 200, 252, 0.85);
  }}

  /* CARD "IDEA CLAVE" (RÉPLICA EXACTA SLIDE 5 DEL PPTX) */
  .card-insight {{
    background: rgba(255, 200, 87, 0.08);
    border: 1.5px solid var(--fest-amber);
    border-radius: var(--card-sub-radius);
    padding: 13px 16px;
    margin: 3px 0;
    box-shadow: 0 0 18px rgba(255, 200, 87, 0.14);
    transition: transform 0.2s ease;
  }}
  .card-insight:hover {{
    transform: translateY(-2px);
  }}
  .insight-label {{
    font-size: 11px;
    font-weight: 700;
    color: var(--fest-amber);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
    font-family: "IBM Plex Mono", monospace;
  }}
  .insight-text {{
    font-size: clamp(12.5px, 0.88vw, 13.8px);
    line-height: 1.45;
    color: #FEF3C7;
  }}

  /* CARD FRASE-CLAVE ANCLADA */
  .card-frase-clave {{
    border-left: 5px solid var(--fest-magenta);
    background: linear-gradient(135deg, rgba(224, 64, 251, 0.12) 0%, rgba(155, 92, 255, 0.03) 100%);
    padding: 13px 18px;
    border-radius: 0 var(--card-sub-radius) var(--card-sub-radius) 0;
    margin-top: auto;
    border-top: 1px solid rgba(224, 64, 251, 0.22);
    border-right: 1px solid rgba(224, 64, 251, 0.22);
    border-bottom: 1px solid rgba(224, 64, 251, 0.22);
    box-shadow: 0 4px 14px rgba(224, 64, 251, 0.08);
    transition: transform 0.2s ease;
  }}
  .card-frase-clave:hover {{
    transform: translateY(-2px);
  }}
  .frase-label {{
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--fest-magenta);
    margin-bottom: 3px;
    display: flex;
    align-items: center;
    gap: 6px;
    font-family: "IBM Plex Mono", monospace;
  }}
  .frase-text {{
    font-size: clamp(13px, 0.92vw, 14.8px);
    font-weight: 600;
    line-height: 1.42;
    color: #FFFFFF;
    font-style: italic;
  }}

  /* STRIP DE KPIS (RÉPLICA SLIDE 7 DEL PPTX) */
  .kpi-strip {{
    display: flex;
    gap: 10px;
    margin-bottom: 12px;
    flex-wrap: wrap;
    flex-shrink: 0;
    width: 100%;
  }}
  .kpi-strip-item {{
    background: var(--bg-dark-sub);
    border: 1px solid rgba(18, 200, 252, 0.22);
    border-radius: 10px;
    padding: 8px 14px;
    display: flex;
    flex-direction: column;
    gap: 2px;
    flex: 1;
    min-width: 125px;
  }}
  .kpi-strip-val {{
    font-size: clamp(15px, 1.15vw, 19px);
    font-weight: 700;
    font-family: "Space Grotesk", sans-serif;
    color: var(--fest-cyan);
    text-shadow: 0 0 10px rgba(18, 200, 252, 0.25);
  }}
  .kpi-strip-lbl {{
    font-size: 10.5px;
    color: var(--text-faint);
    font-family: "IBM Plex Mono", monospace;
    font-weight: 500;
  }}

  /* GLOSARIO TOOLTIPS */
  .glossary {{
    text-decoration: underline dotted var(--fest-cyan);
    text-underline-offset: 3px;
    cursor: help;
    position: relative;
    font-weight: 600;
    color: var(--fest-cyan);
  }}
  .glossary:hover::after {{
    content: attr(data-tooltip);
    position: absolute;
    bottom: 125%;
    left: 50%;
    transform: translateX(-50%);
    background: #03050F;
    color: #FFFFFF;
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 12px;
    font-family: "IBM Plex Sans", sans-serif;
    font-weight: 400;
    white-space: normal;
    width: 250px;
    z-index: 500;
    box-shadow: 0 10px 25px -5px rgba(0,0,0,0.8);
    line-height: 1.35;
    pointer-events: none;
    border: 1px solid rgba(18, 200, 252, 0.35);
  }}

  /* FOOTER OFICIAL CON BRANDING IQUITOS DATA FEST */
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

  /* PROCEDURAL ANIMATIONS */
  @keyframes glow {{
    0%, 100% {{ transform: scale(1); opacity: 0.9; }}
    50% {{ transform: scale(1.3); opacity: 0.4; }}
  }}
  .anim-glow {{
    transform-origin: center;
    animation: glow 2s ease-in-out infinite;
  }}

  @keyframes springSlideIn {{
    0% {{ opacity: 0; transform: translateY(12px) scale(0.99); }}
    100% {{ opacity: 1; transform: translateY(0) scale(1); }}
  }}
  @keyframes springFadeUp {{
    0% {{ opacity: 0; transform: translateY(8px); }}
    100% {{ opacity: 1; transform: translateY(0); }}
  }}

  .slide.active .panel-narrative > * {{
    animation: springFadeUp 0.42s cubic-bezier(0.16, 1, 0.3, 1) both;
  }}
  .slide.active .panel-narrative > *:nth-child(1) {{ animation-delay: 0.02s; }}
  .slide.active .panel-narrative > *:nth-child(2) {{ animation-delay: 0.05s; }}
  .slide.active .panel-narrative > *:nth-child(3) {{ animation-delay: 0.08s; }}
  .slide.active .panel-narrative > *:nth-child(4) {{ animation-delay: 0.12s; }}
  .slide.active .panel-narrative > *:nth-child(5) {{ animation-delay: 0.16s; }}
  .slide.active .panel-narrative > *:nth-child(6) {{ animation-delay: 0.20s; }}
  .slide.active .panel-narrative > *:nth-child(7) {{ animation-delay: 0.24s; }}

  .slide.active .visual-card {{
    animation: springSlideIn 0.48s cubic-bezier(0.16, 1, 0.3, 1) 0.06s both;
  }}

  /* INFOGRAFÍAS Y SIMULACIONES */
  .infographic-wrapper {{
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: 10px;
    overflow: hidden;
  }}
  .infographic-img {{
    width: 100%;
    height: auto;
    max-height: 48%;
    object-fit: cover;
    object-position: center;
    border-radius: 8px;
    border: 1px solid var(--line-border);
    box-shadow: 0 4px 16px rgba(0,0,0,0.4);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  .infographic-img:hover {{
    transform: scale(1.01);
  }}

  .sim-controls {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    padding: 8px 12px;
    background: var(--bg-dark-sub);
    border-radius: 8px;
    border: 1px solid var(--line-border);
    flex-shrink: 0;
  }}
  .sim-btn {{
    background: rgba(11, 22, 56, 0.85);
    border: 1px solid rgba(18, 200, 252, 0.3);
    color: var(--text-sub);
    font-size: 11px;
    font-family: "IBM Plex Mono", monospace;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 6px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.18s ease;
  }}
  .sim-btn.active {{
    background: var(--fest-cyan);
    color: #03050F;
    border-color: var(--fest-cyan);
    box-shadow: 0 2px 8px rgba(18, 200, 252, 0.4);
  }}

  /* LIGHTBOX MODAL */
  .lightbox-modal {{
    position: fixed;
    inset: 0;
    background: rgba(3, 5, 15, 0.95);
    backdrop-filter: blur(12px);
    z-index: 1000;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 30px;
    cursor: zoom-out;
  }}
  .lightbox-modal.active {{ display: flex; }}
  .lightbox-img {{
    max-width: 92vw;
    max-height: 90vh;
    border-radius: 12px;
    box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.9);
    border: 1.5px solid rgba(18, 200, 252, 0.35);
    object-fit: contain;
    background: #03050F;
  }}
  .lightbox-close {{
    position: absolute;
    top: 24px;
    right: 32px;
    color: #FFFFFF;
    font-size: 32px;
    font-weight: 700;
    cursor: pointer;
    background: rgba(255,255,255,0.15);
    border-radius: 50%;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.15s;
  }}
  .lightbox-close:hover {{ background: rgba(18, 200, 252, 0.4); }}
"""
