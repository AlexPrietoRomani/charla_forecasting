def get_deck_css():
    return """
  :root {
    --accent-blue: #2563EB;
    --accent-blue-light: #60A5FA;
    --accent-emerald: #059669;
    --accent-red: #DC2626;
    --accent-amber: #D97706;
    --accent-purple: #7C3AED;
    --accent-cyan: #0891B2;
    
    --bg-light: #F8FAFC;
    --bg-light-panel: #FFFFFF;
    --bg-light-sub: #F1F5F9;
    --bg-visual-light: #F8FAFC;
    
    --bg-dark: #090D16;
    --bg-dark-panel: #0F172A;
    --bg-dark-sub: #1E293B;
    --bg-visual-dark: #090D16;
    
    --text-light-main: #0F172A;
    --text-light-mute: #334155;
    --text-light-faint: #64748B;
    
    --text-dark-main: #F8FAFC;
    --text-dark-mute: #CBD5E1;
    --text-dark-faint: #94A3B8;
    
    --line-light: #E2E8F0;
    --line-light-faint: #E2E8F0;
    --line-dark: #334155;
    --line-dark-faint: #1E293B;
    
    --badge-teoria: #7C3AED;
    --badge-teoria-bg: #F5F3FF;
    --badge-teoria-border: #DDD6FE;
    
    --badge-mecanismo: #0891B2;
    --badge-mecanismo-bg: #ECFEFF;
    --badge-mecanismo-border: #A5F3FC;
    
    --badge-evidencia: #D97706;
    --badge-evidencia-bg: #FFFBEB;
    --badge-evidencia-border: #FDE68A;
    
    --badge-caso_real: #059669;
    --badge-caso_real-bg: #ECFDF5;
    --badge-caso_real-border: #A7F3D0;
    
    --badge-demo: #DC2626;
    --badge-demo-bg: #FEF2F2;
    --badge-demo-border: #FECACA;
    
    --header-h: 0px;
    --footer-h: 56px;

    /* FRONT-DESIGN TOKENS: MÁRGENES Y RESPONSIVIDAD */
    --deck-pad-x: clamp(24px, 2.5vw, 44px);
    --deck-pad-y: clamp(16px, 2.0vh, 28px);
    --deck-gap: clamp(18px, 1.8vw, 28px);
    --card-radius: 16px;
    --card-sub-radius: 10px;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  
  body {
    font-family: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background: var(--bg-light);
    color: var(--text-light-main);
    overflow: hidden;
    width: 100vw;
    height: 100vh;
    display: flex;
    flex-direction: column;
    transition: background 0.2s ease, color 0.2s ease;
  }
  
  body.dark-mode {
    background: var(--bg-dark);
    color: var(--text-dark-main);
  }

  .mono { font-family: "IBM Plex Mono", monospace; }
  .display { font-family: "Space Grotesk", sans-serif; }

  /* TOP PROGRESS BAR */
  .progress-container {
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: var(--line-light);
    z-index: 100;
  }
  body.dark-mode .progress-container { background: var(--line-dark); }
  .progress-bar {
    height: 100%;
    width: 5%;
    background: linear-gradient(90deg, #2563EB, #0891B2);
    transition: width 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }

  /* SLIDE VIEW CONTAINER: MÁRGENES REALES EN LOS 4 LADOS */
  .deck-container {
    width: 100vw;
    height: calc(100vh - var(--footer-h));
    padding: var(--deck-pad-y) var(--deck-pad-x);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    position: relative;
  }

  .slide {
    position: absolute;
    inset: var(--deck-pad-y) var(--deck-pad-x);
    opacity: 0;
    pointer-events: none;
    display: flex;
    flex-direction: row;
    gap: var(--deck-gap);
    transition: opacity 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .slide.active {
    opacity: 1;
    pointer-events: auto;
    z-index: 10;
  }

  /* PANEL NARRATIVE (38%) */
  .panel-narrative {
    flex: 0 0 38%;
    max-width: 38%;
    height: 100%;
    padding: clamp(20px, 2.0vw, 30px);
    display: flex;
    flex-direction: column;
    gap: clamp(10px, 1.2vh, 16px);
    border-radius: var(--card-radius);
    background: var(--bg-light-panel);
    border: 1px solid var(--line-light-faint);
    box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.05), 0 4px 6px -2px rgba(15, 23, 42, 0.02);
    overflow-y: auto;
    z-index: 2;
  }
  body.dark-mode .panel-narrative {
    background: var(--bg-dark-panel);
    border-color: var(--line-dark-faint);
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.5);
  }

  /* PANEL VISUAL (62%) */
  .panel-visual {
    flex: 1;
    height: 100%;
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
  }

  .visual-card {
    width: 100%;
    height: 100%;
    background: var(--bg-light-panel);
    border: 1px solid var(--line-light-faint);
    border-radius: var(--card-radius);
    display: flex;
    flex-direction: column;
    padding: clamp(16px, 1.6vw, 24px);
    position: relative;
    overflow: hidden;
    box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.05), 0 4px 6px -2px rgba(15, 23, 42, 0.02);
  }
  body.dark-mode .visual-card {
    background: var(--bg-dark-panel);
    border-color: var(--line-dark-faint);
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.5);
  }

  .visual-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--line-light-faint);
    flex-shrink: 0;
  }
  body.dark-mode .visual-header { border-bottom-color: var(--line-dark-faint); }

  .visual-title {
    font-size: clamp(14px, 1.1vw, 17px);
    font-weight: 700;
    color: var(--text-light-main);
    display: flex;
    align-items: center;
    gap: 8px;
  }
  body.dark-mode .visual-title { color: var(--text-dark-main); }

  .visual-tag {
    font-size: 11px;
    font-weight: 600;
    color: var(--text-light-faint);
    letter-spacing: 0.05em;
  }
  body.dark-mode .visual-tag { color: var(--text-dark-faint); }

  .chart-wrapper {
    flex: 1;
    min-height: 0;
    position: relative;
    width: 100%;
    height: 100%;
  }

  /* BADGES & CHIPS */
  .badge {
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
  }
  .badge-teoria { color: var(--badge-teoria); background: var(--badge-teoria-bg); border: 1px solid var(--badge-teoria-border); }
  .badge-mecanismo { color: var(--badge-mecanismo); background: var(--badge-mecanismo-bg); border: 1px solid var(--badge-mecanismo-border); }
  .badge-evidencia { color: var(--badge-evidencia); background: var(--badge-evidencia-bg); border: 1px solid var(--badge-evidencia-border); }
  .badge-caso_real { color: var(--badge-caso_real); background: var(--badge-caso_real-bg); border: 1px solid var(--badge-caso_real-border); }
  .badge-demo { color: var(--badge-demo); background: var(--badge-demo-bg); border: 1px solid var(--badge-demo-border); }

  .slide-meta {
    font-size: 11.5px;
    color: var(--text-light-faint);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
  }
  body.dark-mode .slide-meta { color: var(--text-dark-faint); }

  .slide-title {
    font-size: clamp(22px, 2.2vw, 30px);
    line-height: 1.15;
    font-weight: 700;
    letter-spacing: -0.025em;
    color: var(--text-light-main);
  }
  body.dark-mode .slide-title { color: var(--text-dark-main); }

  .slide-thesis {
    font-size: clamp(14px, 1.05vw, 16px);
    line-height: 1.5;
    color: var(--text-light-mute);
    font-weight: 400;
  }
  body.dark-mode .slide-thesis { color: var(--text-dark-mute); }

  .metric-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }
  .metric-chip {
    font-size: 11.5px;
    font-family: "IBM Plex Mono", monospace;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 6px;
    background: var(--bg-light-sub);
    color: var(--text-light-mute);
    border: 1px solid var(--line-light-faint);
  }
  body.dark-mode .metric-chip {
    background: var(--bg-dark-sub);
    color: var(--text-dark-mute);
    border-color: var(--line-dark-faint);
  }

  /* BULLETS AS STRUCTURED CARDS */
  .bullets-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin: 4px 0;
  }
  .bullet-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    font-size: clamp(13px, 0.94vw, 14.5px);
    line-height: 1.48;
    color: var(--text-light-mute);
    padding: 12px 14px;
    background: var(--bg-light-sub);
    border-radius: var(--card-sub-radius);
    border: 1px solid var(--line-light-faint);
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
  }
  body.dark-mode .bullet-item {
    background: var(--bg-dark-sub);
    border-color: var(--line-dark-faint);
    color: var(--text-dark-mute);
  }
  .bullet-icon {
    flex-shrink: 0;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin-top: 6px;
    background: var(--accent-blue);
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.18);
  }

  /* CARD INSIGHT METODOLÓGICO */
  .card-insight {
    background: rgba(37, 99, 235, 0.05);
    border: 1px solid rgba(37, 99, 235, 0.18);
    border-radius: var(--card-sub-radius);
    padding: 13px 16px;
    margin: 4px 0;
  }
  body.dark-mode .card-insight {
    background: rgba(96, 165, 250, 0.08);
    border-color: rgba(96, 165, 250, 0.22);
  }
  .insight-label {
    font-size: 10.5px;
    font-weight: 700;
    color: var(--accent-blue);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
    font-family: "IBM Plex Mono", monospace;
  }
  body.dark-mode .insight-label { color: #60A5FA; }
  .insight-text {
    font-size: clamp(12.5px, 0.9vw, 14px);
    line-height: 1.45;
    color: var(--text-light-mute);
  }
  body.dark-mode .insight-text { color: var(--text-dark-mute); }

  /* CARD FRASE-CLAVE ANCLADA */
  .card-frase-clave {
    border-left: 5px solid var(--accent-blue);
    background: linear-gradient(135deg, rgba(37, 99, 235, 0.09) 0%, rgba(37, 99, 235, 0.02) 100%);
    padding: 16px 20px;
    border-radius: 0 var(--card-sub-radius) var(--card-sub-radius) 0;
    margin-top: auto;
    border-top: 1px solid rgba(37, 99, 235, 0.14);
    border-right: 1px solid rgba(37, 99, 235, 0.14);
    border-bottom: 1px solid rgba(37, 99, 235, 0.14);
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.05);
  }
  body.dark-mode .card-frase-clave {
    background: linear-gradient(135deg, rgba(96, 165, 250, 0.12) 0%, rgba(96, 165, 250, 0.02) 100%);
    border-left-color: #60A5FA;
    border-top-color: rgba(96, 165, 250, 0.2);
    border-right-color: rgba(96, 165, 250, 0.2);
    border-bottom-color: rgba(96, 165, 250, 0.2);
  }
  .frase-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent-blue);
    margin-bottom: 5px;
    display: flex;
    align-items: center;
    gap: 6px;
    font-family: "IBM Plex Mono", monospace;
  }
  body.dark-mode .frase-label { color: #60A5FA; }
  .frase-text {
    font-size: clamp(14px, 1.0vw, 16px);
    font-weight: 600;
    line-height: 1.45;
    color: var(--text-light-main);
    font-style: italic;
  }
  body.dark-mode .frase-text { color: var(--text-dark-main); }

  /* STRIP DE KPIS PARA LLENAR ESPACIO SUPERIOR EN VISUAL */
  .kpi-strip {
    display: flex;
    gap: 10px;
    margin-bottom: 12px;
    flex-wrap: wrap;
    flex-shrink: 0;
    width: 100%;
  }
  .kpi-strip-item {
    background: var(--bg-light-sub);
    border: 1px solid var(--line-light-faint);
    border-radius: 8px;
    padding: 8px 14px;
    display: flex;
    flex-direction: column;
    gap: 2px;
    flex: 1;
    min-width: 130px;
  }
  body.dark-mode .kpi-strip-item {
    background: var(--bg-dark-sub);
    border-color: var(--line-dark-faint);
  }
  .kpi-strip-val {
    font-size: clamp(16px, 1.2vw, 20px);
    font-weight: 700;
    font-family: "Space Grotesk", sans-serif;
    color: var(--accent-blue);
  }
  .kpi-strip-lbl {
    font-size: 10.5px;
    color: var(--text-light-faint);
    font-family: "IBM Plex Mono", monospace;
    font-weight: 500;
  }
  body.dark-mode .kpi-strip-lbl { color: var(--text-dark-faint); }
  body.dark-mode .frase-text { color: var(--text-dark-main); }

  /* GLOSARIO TOOLTIPS */
  .glossary {
    text-decoration: underline dotted var(--badge-mecanismo);
    text-underline-offset: 3px;
    cursor: help;
    position: relative;
    font-weight: 600;
  }
  .glossary:hover::after {
    content: attr(data-tooltip);
    position: absolute;
    bottom: 125%;
    left: 50%;
    transform: translateX(-50%);
    background: #0F172A;
    color: #F8FAFC;
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 12px;
    font-family: "IBM Plex Sans", sans-serif;
    font-weight: 400;
    white-space: normal;
    width: 250px;
    z-index: 500;
    box-shadow: 0 10px 25px -5px rgba(0,0,0,0.4);
    line-height: 1.35;
    pointer-events: none;
    border: 1px solid rgba(255,255,255,0.15);
  }

  /* FOOTER */
  .deck-footer {
    height: var(--footer-h);
    background: var(--bg-light-panel);
    border-top: 1px solid var(--line-light-faint);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 clamp(14px, 1.6vw, 24px);
    z-index: 50;
    flex-shrink: 0;
  }
  body.dark-mode .deck-footer {
    background: var(--bg-dark-panel);
    border-top-color: var(--line-dark-faint);
  }

  .nav-btn {
    background: var(--bg-light-sub);
    border: 1px solid var(--line-light);
    color: var(--text-light-main);
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
  }
  body.dark-mode .nav-btn {
    background: var(--bg-dark-sub);
    border-color: var(--line-dark);
    color: var(--text-dark-main);
  }
  .nav-btn:hover {
    background: var(--accent-blue);
    color: #FFF;
    border-color: var(--accent-blue);
  }

  /* SPEAKER DRAWER */
  .speaker-drawer {
    position: fixed;
    bottom: 0; left: 0; right: 0;
    height: 270px;
    background: #0B1120;
    color: #F8FAFC;
    border-top: 2px solid var(--accent-blue);
    transform: translateY(100%);
    transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
    z-index: 1000;
    display: flex;
    flex-direction: column;
    box-shadow: 0 -10px 30px rgba(0,0,0,0.5);
  }
  .speaker-drawer.open {
    transform: translateY(0);
  }
  .speaker-header {
    height: 42px;
    padding: 0 20px;
    background: #020617;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #1E293B;
  }
  .speaker-body {
    flex: 1;
    padding: 16px 24px;
    overflow-y: auto;
    font-size: 14px;
    line-height: 1.6;
    color: #E2E8F0;
  }

  /* ======================================================== */
  /* PURE-CODE ANIMATIONS (Emil Kowalski / Procedural Film)   */
  /* ======================================================== */

  @keyframes glow {
    0%, 100% { transform: scale(1); opacity: 0.9; }
    50% { transform: scale(1.3); opacity: 0.4; }
  }
  .anim-glow {
    transform-origin: center;
    animation: glow 2s ease-in-out infinite;
  }

  /* Spring entrance physics */
  @keyframes springSlideIn {
    0% {
      opacity: 0;
      transform: translateY(12px) scale(0.99);
    }
    100% {
      opacity: 1;
      transform: translateY(0) scale(1);
    }
  }

  @keyframes springFadeUp {
    0% {
      opacity: 0;
      transform: translateY(8px);
    }
    100% {
      opacity: 1;
      transform: translateY(0);
    }
  }

  /* Staggered entrance on slide activation */
  .slide.active .panel-narrative > * {
    animation: springFadeUp 0.42s cubic-bezier(0.16, 1, 0.3, 1) both;
  }
  .slide.active .panel-narrative > *:nth-child(1) { animation-delay: 0.02s; }
  .slide.active .panel-narrative > *:nth-child(2) { animation-delay: 0.05s; }
  .slide.active .panel-narrative > *:nth-child(3) { animation-delay: 0.08s; }
  .slide.active .panel-narrative > *:nth-child(4) { animation-delay: 0.12s; }
  .slide.active .panel-narrative > *:nth-child(5) { animation-delay: 0.16s; }
  .slide.active .panel-narrative > *:nth-child(6) { animation-delay: 0.20s; }
  .slide.active .panel-narrative > *:nth-child(7) { animation-delay: 0.24s; }

  .slide.active .visual-card {
    animation: springSlideIn 0.48s cubic-bezier(0.16, 1, 0.3, 1) 0.06s both;
  }

  /* Micro-interactions: Tactile feedback on hover and press */
  .bullet-item {
    transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s ease, border-color 0.2s ease;
  }
  .bullet-item:hover {
    transform: translateX(4px);
    border-color: rgba(37, 99, 235, 0.35);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
  }

  .card-insight, .card-frase-clave {
    transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.22s ease;
  }
  .card-insight:hover, .card-frase-clave:hover {
    transform: translateY(-2px);
  }

  .nav-btn {
    transition: transform 0.12s cubic-bezier(0.16, 1, 0.3, 1), background 0.15s ease, border-color 0.15s ease;
  }
  .nav-btn:active {
    transform: scale(0.96);
  }

  .metric-chip {
    transition: transform 0.15s ease, border-color 0.15s ease;
  }
  .metric-chip:hover {
    transform: translateY(-1px);
    border-color: var(--accent-blue);
  }

  /* Procedural & Infographic Visual Layout Containers */
  .infographic-wrapper {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: 10px;
    overflow: hidden;
  }

  .infographic-img {
    width: 100%;
    height: auto;
    max-height: 48%;
    object-fit: cover;
    object-position: center;
    border-radius: 8px;
    border: 1px solid var(--line-light-faint);
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }
  body.dark-mode .infographic-img {
    border-color: var(--line-dark-faint);
    box-shadow: 0 4px 16px rgba(0,0,0,0.3);
  }
  .infographic-img:hover {
    transform: scale(1.01);
  }

  .sim-controls {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    padding: 8px 12px;
    background: var(--bg-light-sub);
    border-radius: 8px;
    border: 1px solid var(--line-light-faint);
    flex-shrink: 0;
  }
  body.dark-mode .sim-controls {
    background: var(--bg-dark-sub);
    border-color: var(--line-dark-faint);
  }

  .sim-btn {
    background: var(--bg-light-panel);
    border: 1px solid var(--line-light);
    color: var(--text-light-mute);
    font-size: 11px;
    font-family: "IBM Plex Mono", monospace;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 6px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
  }
  body.dark-mode .sim-btn {
    background: var(--bg-dark-panel);
    border-color: var(--line-dark);
    color: var(--text-dark-mute);
  }
  .sim-btn.active {
    background: var(--accent-blue);
    color: #FFF;
    border-color: var(--accent-blue);
    box-shadow: 0 2px 8px rgba(37, 99, 235, 0.3);
  }

  /* Radar / Drone HUD procedural animation */
  @keyframes radarSweep {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
  .radar-scanner {
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: conic-gradient(from 0deg at 50% 50%, rgba(5, 150, 105, 0) 0deg, rgba(5, 150, 105, 0.25) 340deg, rgba(5, 150, 105, 0.6) 360deg);
    animation: radarSweep 4s linear infinite;
    pointer-events: none;
  }

  @keyframes hudBlink {
    0%, 100% { opacity: 0.9; }
    50% { opacity: 0.35; }
  }
  .hud-live {
    animation: hudBlink 1.4s ease-in-out infinite;
  }

  /* LIGHTBOX MODAL PARA AMPLIAR INFOGRAFÍAS NOTEBOOKLM */
  .lightbox-modal {
    position: fixed;
    inset: 0;
    background: rgba(15, 23, 42, 0.92);
    backdrop-filter: blur(10px);
    z-index: 1000;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 30px;
    cursor: zoom-out;
  }
  .lightbox-modal.active { display: flex; }
  .lightbox-img {
    max-width: 92vw;
    max-height: 90vh;
    border-radius: 12px;
    box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.2);
    object-fit: contain;
    background: #0B0F19;
  }
  .lightbox-close {
    position: absolute;
    top: 24px;
    right: 32px;
    color: #F8FAFC;
    font-size: 32px;
    font-weight: 700;
    cursor: pointer;
    background: rgba(255,255,255,0.12);
    border-radius: 50%;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.15s;
  }
  .lightbox-close:hover { background: rgba(255,255,255,0.25); }
"""

