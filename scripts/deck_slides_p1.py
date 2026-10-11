def get_slides_part1(branding=None):
    if branding is None:
        branding = {}
    b64_header = branding.get("b64_header", "")
    b64_profile = branding.get("b64_profile", "")

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
    <div class="agenda-grid">
      <div class="agenda-card item-1">
        <div class="agenda-num">01</div>
        <div class="agenda-text-wrap">
          <div class="agenda-card-title display">Historia de los modelos de series temporales</div>
          <div class="agenda-card-desc">De la descomposición clásica y ARIMA al Deep Learning moderno y modelos de grafos.</div>
        </div>
      </div>

      <div class="agenda-card item-2">
        <div class="agenda-num">02</div>
        <div class="agenda-text-wrap">
          <div class="agenda-card-title display">Caso 1: Predicción de temperatura en Iquitos</div>
          <div class="agenda-card-desc">2,557 días de SENAMHI Punchana, la trampa de los árboles y la entropía a 7 días.</div>
        </div>
      </div>

      <div class="agenda-card item-3">
        <div class="agenda-num">03</div>
        <div class="agenda-text-wrap">
          <div class="agenda-card-title display">Series temporales en el agro &amp; Caso 2</div>
          <div class="agenda-card-desc">Predicción de rendimiento de café en Jaén: la trampa del NDVI y modelos fenológicos.</div>
        </div>
      </div>

      <div class="agenda-card item-4">
        <div class="agenda-num">04</div>
        <div class="agenda-text-wrap">
          <div class="agenda-card-title display">Conclusiones y próximos pasos</div>
          <div class="agenda-card-desc">Lecciones del mundo real, la navaja de Ockham y buenas prácticas en producción.</div>
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
      Cómo evolucionó la ciencia de predecir el futuro: desde las ecuaciones estadísticas clásicas de Box-Jenkins hasta las arquitecturas de grafos y transformers masivos, explorando qué cambia y qué límites físicos permanecen inalterables.
    </p>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 05: ANATOMÍA FÍSICA VS RUIDO (page-05.png)              -->
  <!-- ============================================================= -->
  <section class="slide" data-index="5" data-act="Acto 1 · Anatomía de la Señal" data-time="2.0 min">
    <h2 class="slide-main-title display">Anatomía ontológica: física vs ruido</h2>
    <div class="content-insight-layout">
      <div class="content-bullets-col">
        <ul class="standard-bullet-list">
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Tendencia Secular T(t):</strong> Deriva física de fondo gobernada por el calentamiento regional (+0.20 °C/década) o envejecimiento del sensor.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Estacionalidad Solar S(t):</strong> Ciclo astronómico invariable de 365 días por la oblicuidad y traslación orbital de la Tierra.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Macro-ciclo Acoplado C(t):</strong> Oscilación océano-atmósfera cuasi-periódica (ENSO: El Niño / La Niña cada 3 a 7 años).</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Ruido Estocástico ε(t):</strong> Turbulencia de microescala convectiva local inalcanzable determinísticamente (atractor caótico).</div>
          </li>
        </ul>
      </div>

      <div class="archetype-idea-card">
        <div class="archetype-idea-icon">💡</div>
        <div class="archetype-idea-label">IDEA CLAVE</div>
        <p class="archetype-idea-text">
          Una serie física no es una secuencia arbitraria: es la superposición de leyes termodinámicas, ciclos astronómicos y ruido residual. Ningún algoritmo puede superar el límite impuesto por su ratio señal/ruido intrínseco.
        </p>
      </div>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 06: EVOLUCIÓN DE PARADIGMAS (page-06.png)               -->
  <!-- ============================================================= -->
  <section class="slide" data-index="6" data-act="Acto 1 · Evolución de Paradigmas" data-time="2.0 min">
    <h2 class="slide-main-title display">Evolución: de ARIMA a Foundation Models</h2>
    <div class="graphic-layout">
      <div class="graphic-info-col">
        <ul class="standard-bullet-list">
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Era 1 (1970–1990):</strong> Métodos lineales parsimoniosos (ARIMA, Holt-Winters). Exigen estacionariedad e hipótesis analíticas.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Era 2 (2000–2015):</strong> ML tabular sobre retardos temporales (Random Forest, GBDT). Capturan no-linealidad pero sufren con tendencias.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Era 3 &amp; 4 (2018–2026):</strong> Deep Learning (LSTM, TFT) y Foundation Models Zero-Shot (Chronos, TimesFM, GraphCast).</div>
          </li>
        </ul>
        <div class="graphic-source">Fuente: Hyndman &amp; Athanasopoulos (2021) · Makridakis Competitions (M3, M4, M5)</div>
      </div>

      <div class="graphic-card-col">
        <div style="display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; gap:12px; height:100%;">
          <div style="background:var(--bg-dark-sub); padding:16px; border-radius:10px; border-left:4px solid var(--fest-cyan); display:flex; flex-direction:column; justify-content:center;">
            <div style="color:var(--fest-cyan); font-weight:700; font-size:11px;" class="mono">ERA 1 · ESTADÍSTICA (1970s)</div>
            <div style="font-weight:700; font-size:15px; margin:3px 0;">ARIMA / Holt-Winters</div>
            <p style="font-size:12px; color:var(--text-faint); line-height:1.4;">Parsimonia extrema, supuestos gaussianos y convergencia analítica garantizada.</p>
          </div>
          <div style="background:var(--bg-dark-sub); padding:16px; border-radius:10px; border-left:4px solid var(--fest-blue); display:flex; flex-direction:column; justify-content:center;">
            <div style="color:var(--fest-blue); font-weight:700; font-size:11px;" class="mono">ERA 2 · MACHINE LEARNING (2000s)</div>
            <div style="font-weight:700; font-size:15px; margin:3px 0;">Random Forest / XGBoost</div>
            <p style="font-size:12px; color:var(--text-faint); line-height:1.4;">Ventanas rezagadas (lags), no linealidad tabular robusta, incapacidad de extrapolar.</p>
          </div>
          <div style="background:var(--bg-dark-sub); padding:16px; border-radius:10px; border-left:4px solid var(--fest-purple); display:flex; flex-direction:column; justify-content:center;">
            <div style="color:var(--fest-purple); font-weight:700; font-size:11px;" class="mono">ERA 3 · DEEP LEARNING (2018+)</div>
            <div style="font-weight:700; font-size:15px; margin:3px 0;">LSTM / N-BEATS / TFT</div>
            <p style="font-size:12px; color:var(--text-faint); line-height:1.4;">Mecanismos de atención temporal y descomposición profunda de tendencias.</p>
          </div>
          <div style="background:var(--bg-dark-sub); padding:16px; border-radius:10px; border-left:4px solid var(--fest-magenta); display:flex; flex-direction:column; justify-content:center;">
            <div style="color:var(--fest-magenta); font-weight:700; font-size:11px;" class="mono">ERA 4 · FOUNDATION MODELS (2024+)</div>
            <div style="font-weight:700; font-size:15px; margin:3px 0;">Chronos / GraphCast</div>
            <p style="font-size:12px; color:var(--text-faint); line-height:1.4;">Zero-shot preentrenado masivo y redes sobre grafos físicos icosaédricos.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 07: CONO DE INCERTIDUMBRE (page-06.png)                 -->
  <!-- ============================================================= -->
  <section class="slide" data-index="7" data-act="Acto 1 · Cono de Incertidumbre" data-time="2.0 min">
    <h2 class="slide-main-title display">Cono de incertidumbre y dispersión temporal</h2>
    <div class="graphic-layout">
      <div class="graphic-info-col">
        <ul class="standard-bullet-list">
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>El sesgo puntual:</strong> Exigir una predicción única oculta el riesgo operacional en clima y agricultura.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Entropía acumulada:</strong> Todo sistema caótico pierde predictibilidad; la dispersión estocástica crece con σ_h ∝ √h.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Decisión estocástica:</strong> En horizontes h &gt; 7 días, toda decisión logística debe fundamentarse en bandas P10–P90.</div>
          </li>
        </ul>
        <div class="graphic-source">Simulación Estocástica Monte Carlo · Teorema de Lorenz (1963)</div>
      </div>

      <div class="graphic-card-col">
        <div class="chart-wrapper">
          <svg viewBox="0 0 840 400" style="width:100%; height:100%;">
            <defs>
              <linearGradient id="coneGrad" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#12C8FC" stop-opacity="0.08" />
                <stop offset="50%" stop-color="#12C8FC" stop-opacity="0.25" />
                <stop offset="100%" stop-color="#12C8FC" stop-opacity="0.45" />
              </linearGradient>
              <linearGradient id="innerConeGrad" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#1E7BFF" stop-opacity="0.15" />
                <stop offset="100%" stop-color="#1E7BFF" stop-opacity="0.35" />
              </linearGradient>
            </defs>
            <line x1="50" y1="70" x2="720" y2="70" stroke="rgba(169,184,218,0.2)" stroke-dasharray="4" />
            <line x1="50" y1="140" x2="720" y2="140" stroke="rgba(169,184,218,0.2)" stroke-dasharray="4" />
            <line x1="50" y1="210" x2="720" y2="210" stroke="rgba(169,184,218,0.2)" stroke-dasharray="4" />
            <line x1="50" y1="280" x2="720" y2="280" stroke="rgba(169,184,218,0.2)" stroke-dasharray="4" />
            <line x1="50" y1="350" x2="720" y2="350" stroke="rgba(169,184,218,0.2)" stroke-dasharray="4" />
            
            <!-- Bandas de Incertidumbre -->
            <path d="M 280 210 Q 480 180 690 70 L 690 350 Q 480 240 280 210 Z" fill="url(#coneGrad)" />
            <path d="M 280 210 Q 480 195 690 130 L 690 290 Q 480 225 280 210 Z" fill="url(#innerConeGrad)" />
            
            <!-- Trayectoria Pasada -->
            <path d="M 50 230 Q 120 180 180 220 T 280 210" fill="none" stroke="#FFFFFF" stroke-width="3.5" />
            
            <!-- Mediana Futura P50 -->
            <path d="M 280 210 Q 480 210 690 210" fill="none" stroke="#12C8FC" stroke-width="2.5" stroke-dasharray="6 4" />
            
            <!-- Trayectorias Monte Carlo -->
            <path d="M 280 210 Q 440 170 690 100" fill="none" stroke="#1E7BFF" stroke-width="1.4" opacity="0.8" />
            <path d="M 280 210 Q 450 240 690 310" fill="none" stroke="#1E7BFF" stroke-width="1.4" opacity="0.8" />
            <path d="M 280 210 Q 500 195 690 170" fill="none" stroke="#9B5CFF" stroke-width="1.2" opacity="0.8" />
            <path d="M 280 210 Q 430 225 690 260" fill="none" stroke="#9B5CFF" stroke-width="1.2" opacity="0.8" />
            
            <!-- Línea de Presente t0 -->
            <line x1="280" y1="40" x2="280" y2="360" stroke="#DC2626" stroke-width="2.2" stroke-dasharray="5 3" />
            <text x="285" y="55" fill="#EF4444" font-size="12" font-family="IBM Plex Mono" font-weight="700">t₀ (PRESENTE)</text>
            
            <text x="60" y="360" fill="#A9B8DA" font-size="11" font-family="IBM Plex Mono">PASADO OBSERVADO</text>
            <text x="400" y="360" fill="#12C8FC" font-size="11" font-family="IBM Plex Mono">CONO DE INCERTIDUMBRE (FUTURO)</text>
            
            <!-- Cuantiles -->
            <text x="702" y="75" fill="#12C8FC" font-size="11" font-family="IBM Plex Mono" font-weight="700">P90 (+2.5σ)</text>
            <text x="702" y="135" fill="#1E7BFF" font-size="10" font-family="IBM Plex Mono">P75</text>
            <text x="702" y="214" fill="#12C8FC" font-size="11" font-family="IBM Plex Mono" font-weight="700">P50 (Mediana)</text>
            <text x="702" y="295" fill="#1E7BFF" font-size="10" font-family="IBM Plex Mono">P25</text>
            <text x="702" y="355" fill="#12C8FC" font-size="11" font-family="IBM Plex Mono" font-weight="700">P10 (-2.5σ)</text>
            
            <circle cx="280" cy="210" r="6" fill="#EF4444" class="anim-glow" />
          </svg>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 08: SECCIÓN 02: CASO 1: IQUITOS SENAMHI (page-04.png)   -->
  <!-- ============================================================= -->
  <section class="slide slide-archetype-section" data-index="8" data-act="Acto 2 · Caso 1: Clima SENAMHI" data-time="1.0 min">
    <div class="section-huge-num">02</div>
    <h2 class="section-title display">Caso 1: Predicción de temperatura en Iquitos</h2>
    <p class="section-desc">
      Auditoría empírica con 2,557 días de mediciones reales en la estación Punchana de SENAMHI (Loreto). Cómo la física tropical desafía a los algoritmos y por qué los modelos en niveles fallan en olas de calor récord.
    </p>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 09: DATOS QUE IMPORTAN: SENAMHI (page-07.png)           -->
  <!-- ============================================================= -->
  <section class="slide" data-index="9" data-act="Acto 2 · Datos SENAMHI" data-time="1.5 min">
    <h2 class="slide-main-title display">Datos que importan: Estación SENAMHI Punchana</h2>
    <p class="kpis-subtitle">Cifras clave de la serie climatológica de Iquitos (2018–2024).</p>
    <div class="kpis-3col-grid">
      <div class="kpi-large-card card-cyan">
        <div class="kpi-huge-number">2,557</div>
        <div class="kpi-card-desc">Días continuos registrados por SENAMHI en la estación Punchana (Iquitos, Loreto).</div>
      </div>
      <div class="kpi-large-card card-blue">
        <div class="kpi-huge-number">31.8°C</div>
        <div class="kpi-card-desc">Temperatura máxima media anual en el régimen ecuatorial hiperhúmedo amazónico.</div>
      </div>
      <div class="kpi-large-card card-purple">
        <div class="kpi-huge-number">h &gt; 7d</div>
        <div class="kpi-card-desc">Horizonte de ruptura entrópica donde el error meteorológico iguala a la varianza climatológica.</div>
      </div>
    </div>
    <div class="graphic-source" style="margin-top:16px;">Fuente: Servicio Nacional de Meteorología e Hidrología del Perú (SENAMHI) · Estación Punchana (2018–2024)</div>
  </section>

  <!-- ============================================================= -->
  <!-- DIAPO 10: LA TRAMPA DE LA NO LINEALIDAD (page-06.png)         -->
  <!-- ============================================================= -->
  <section class="slide" data-index="10" data-act="Acto 2 · Extrapolación de Árboles" data-time="2.0 min">
    <h2 class="slide-main-title display">La trampa de los árboles: meseta vs diferencias</h2>
    <div class="graphic-layout">
      <div class="graphic-info-col">
        <ul class="standard-bullet-list">
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>El problema:</strong> Los árboles de decisión (Random Forest, XGBoost) dividen el espacio en hiperrectángulos cerrados. No pueden predecir valores fuera de su rango histórico de entrenamiento.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>Colapso en ola de calor:</strong> Con tope de 34.0 °C y ola récord a 37.4 °C, RF colapsó en una meseta plana de 31.5 °C.</div>
          </li>
          <li class="standard-bullet-item">
            <span class="standard-bullet-dot"></span>
            <div><strong>La solución de ingeniería:</strong> Modelar la tasa de cambio (Δy = y_t - y_{t-1}) permitió capturar la aceleración térmica hasta 35.45 °C.</div>
          </li>
        </ul>
        <div class="graphic-source">Experimento con datos reales SENAMHI Punchana · Test set ciego</div>
      </div>

      <div class="graphic-card-col">
        <div class="chart-wrapper">
          <canvas id="chartExtrap"></canvas>
        </div>
      </div>
    </div>
  </section>
"""
    return slides.replace("__HEADER_LOGO__", b64_header).replace("__PROFILE_IMG__", b64_profile)
