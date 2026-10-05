def get_slides_part1():
    return """
  <!-- ========================================== -->
  <!-- ACTO 1: LA PREGUNTA (Diapos 01 - 03)       -->
  <!-- ========================================== -->

  <!-- DIAPO 01 -->
  <section class="slide active" data-index="1" data-act="Acto 1 · La Pregunta" data-time="1.5 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">01 / 20 · ACTO 1: LA PREGUNTA</span>
      <div class="badge badge-teoria">TEORÍA</div>
      <h1 class="slide-title display">La ilusión de la certeza</h1>
      <p class="slide-thesis">La IA predice con aplomo absoluto, pero el futuro no es un punto determinista: es un cono estocástico que se ensancha inevitablemente con el tiempo.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">2,557 Días SENAMHI</span>
        <span class="metric-chip">24 Campañas Jaén</span>
        <span class="metric-chip">Cono P10–P90</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>El sesgo puntual:</strong> Exigir una predicción única (ŷ_{t+h}) oculta el riesgo operacional en clima y agricultura.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Entropía acumulada:</strong> Todo sistema dinámico no lineal pierde predictibilidad; la dispersión crece con σ_h ∝ √h.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Pregunta conductora:</strong> ¿Puede la IA predecir el futuro o solo reproduce correlaciones del pasado?</div>
        </li>
      </ul>
            <div class="card-insight">
        <span class="insight-label">💡 REGLA DE INGENIERÍA</span>
        <p class="insight-text">En horizontes h > 7 días, la entropía atmosférica domina la señal predictiva. Toda decisión logística debe fundamentarse en bandas de cuantil (P10–P90), jamás en un escalar.</p>
      </div>
<div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"La IA no sabe lo que no sabe: responde con la misma seguridad cuando acierta que cuando inventa."</p>
      </div>
    </div>
    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">Cono de Incertidumbre y Entropía Temporal</span>
          <span class="visual-tag mono">SIMULACIÓN ESTOCÁSTICA</span>
        </div>
        
        <div class="kpi-strip">
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">2,557 Días</div>
            <div class="kpi-strip-lbl">SENAMHI Punchana (Iquitos)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">24 Campañas</div>
            <div class="kpi-strip-lbl">SIEA/MIDAGRI (Jaén 2000–2024)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">h &gt; 7 Días</div>
            <div class="kpi-strip-lbl">Horizonte de Ruptura Entrópica</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">σ_h ∝ √h</div>
            <div class="kpi-strip-lbl">Dispersión Estocástica Temporal</div>
          </div>
        </div>

        <div class="chart-wrapper">
          <svg viewBox="0 0 840 400" style="width:100%; height:100%;">
            <defs>
              <linearGradient id="coneGrad" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#2563EB" stop-opacity="0.06" />
                <stop offset="50%" stop-color="#2563EB" stop-opacity="0.22" />
                <stop offset="100%" stop-color="#2563EB" stop-opacity="0.42" />
              </linearGradient>
              <linearGradient id="innerConeGrad" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#2563EB" stop-opacity="0.12" />
                <stop offset="100%" stop-color="#2563EB" stop-opacity="0.25" />
              </linearGradient>
            </defs>
            <line x1="50" y1="70" x2="720" y2="70" stroke="#CBD5E1" stroke-dasharray="4" opacity="0.4" />
            <line x1="50" y1="140" x2="720" y2="140" stroke="#CBD5E1" stroke-dasharray="4" opacity="0.4" />
            <line x1="50" y1="210" x2="720" y2="210" stroke="#CBD5E1" stroke-dasharray="4" opacity="0.4" />
            <line x1="50" y1="280" x2="720" y2="280" stroke="#CBD5E1" stroke-dasharray="4" opacity="0.4" />
            <line x1="50" y1="350" x2="720" y2="350" stroke="#CBD5E1" stroke-dasharray="4" opacity="0.4" />
            
            <!-- Bandas de Incertidumbre -->
            <path d="M 280 210 Q 480 180 690 70 L 690 350 Q 480 240 280 210 Z" fill="url(#coneGrad)" />
            <path d="M 280 210 Q 480 195 690 130 L 690 290 Q 480 225 280 210 Z" fill="url(#innerConeGrad)" />
            
            <!-- Trayectoria Pasada -->
            <path d="M 50 230 Q 120 180 180 220 T 280 210" fill="none" stroke="#0F172A" stroke-width="3.5" />
            
            <!-- Mediana Futura P50 -->
            <path d="M 280 210 Q 480 210 690 210" fill="none" stroke="#2563EB" stroke-width="2.5" stroke-dasharray="6 4" />
            
            <!-- Trayectorias Monte Carlo Individuales -->
            <path d="M 280 210 Q 440 170 690 100" fill="none" stroke="#3B82F6" stroke-width="1.4" opacity="0.75" />
            <path d="M 280 210 Q 450 240 690 310" fill="none" stroke="#3B82F6" stroke-width="1.4" opacity="0.75" />
            <path d="M 280 210 Q 500 195 690 170" fill="none" stroke="#60A5FA" stroke-width="1.2" opacity="0.7" />
            <path d="M 280 210 Q 430 225 690 260" fill="none" stroke="#60A5FA" stroke-width="1.2" opacity="0.7" />
            
            <!-- Línea de Presente t0 -->
            <line x1="280" y1="40" x2="280" y2="360" stroke="#DC2626" stroke-width="2.2" stroke-dasharray="5 3" />
            <text x="285" y="55" fill="#DC2626" font-size="12" font-family="IBM Plex Mono" font-weight="700">t₀ (PRESENTE)</text>
            
            <text x="60" y="360" fill="#64748B" font-size="11" font-family="IBM Plex Mono">PASADO OBSERVADO</text>
            <text x="400" y="360" fill="#2563EB" font-size="11" font-family="IBM Plex Mono">CONO DE INCERTIDUMBRE (FUTURO)</text>
            
            <!-- Cuantiles -->
            <text x="702" y="75" fill="#2563EB" font-size="11" font-family="IBM Plex Mono" font-weight="700">P90 (+2.5σ)</text>
            <text x="702" y="135" fill="#3B82F6" font-size="10" font-family="IBM Plex Mono">P75</text>
            <text x="702" y="214" fill="#2563EB" font-size="11" font-family="IBM Plex Mono" font-weight="700">P50 (Mediana)</text>
            <text x="702" y="295" fill="#3B82F6" font-size="10" font-family="IBM Plex Mono">P25</text>
            <text x="702" y="355" fill="#2563EB" font-size="11" font-family="IBM Plex Mono" font-weight="700">P10 (-2.5σ)</text>
            
            <circle cx="280" cy="210" r="6" fill="#DC2626" class="anim-glow" />
          </svg>
        </div>
        <div style="font-size:11px; color:var(--text-light-faint); border-top:1px solid var(--line-light-faint); padding-top:6px;" class="mono">
          Eje X: Horizonte temporal (días) · Eje Y: Magnitud · Dispersión estocástica creciente con el horizonte
        </div>
      </div>
    </div>
  </section>

  <!-- DIAPO 02: ANATOMÍA ONTOLÓGICA DE LA SEÑAL FÍSICA -->
  <section class="slide" data-index="2" data-act="Acto 1 · Ontología de la Señal" data-time="2.0 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">02 / 20 · ACTO 1: ONTOLOGÍA DE LA SEÑAL</span>
      <div class="badge badge-teoria">TEORÍA / ONTOLOGÍA</div>
      <h2 class="slide-title display">Anatomía ontológica: física vs ruido</h2>
      <p class="slide-thesis">Una serie temporal física no es una secuencia arbitraria: es la superposición de leyes termodinámicas, ciclos astronómicos, macro-oscilaciones oceánicas y ruido residual.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">Y(t) = T(t) + S(t) + C(t) + ε(t)</span>
        <span class="metric-chip">ENSO 3–7 Años</span>
        <span class="metric-chip">Ruido &gt; ±2.5σ</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Tendencia Secular T(t):</strong> Deriva física de fondo gobernada por calentamiento global regional (+0.20 °C/década) o envejecimiento del sensor.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Estacionalidad Solar S(t):</strong> Ciclo astronómico invariable de 365 días por la oblicuidad y traslación orbital de la Tierra.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Macro-ciclo Acoplado C(t):</strong> Oscilación océano-atmósfera cuasi-periódica (ENSO: El Niño / La Niña cada 3 a 7 años).</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Ruido Estocástico ε(t):</strong> Turbulencia aleatoria y eventos anómalos (&gt; ±2.5σ: friajes amazónicos de 19 °C, colapsos de red).</div>
        </li>
      </ul>

      <div class="card-insight" style="border-left: 3px solid #DC2626;">
        <span class="insight-label" style="color:#DC2626;">⚠️ NOTA DIAGNÓSTICA CRÍTICA</span>
        <p class="insight-text"><strong>Obligar a una red neuronal profunda a memorizar el ruido residual (ε)</strong> garantiza sobreajuste catastrófico en producción. El verdadero forecasting predice la física subyacente, jamás el ruido blanco estocástico.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"Predecir la física y los ciclos es ciencia rigurosa; forzar a la IA a predecir el ruido blanco es astrología computacional."</p>
      </div>
    </div>

    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <div style="display:flex; align-items:center; gap:8px;">
            <span class="visual-title display">Descomposición Ontológica: Y(t) = T(t) + S(t) + C(t) + ε(t)</span>
          </div>
          <span class="visual-tag mono">NOTEBOOKLM AI & SINTETIZADOR PURO</span>
        </div>
        
        <div class="infographic-wrapper">
          <!-- INFOGRAFÍA NOTEBOOKLM EMBEBIDA -->
          <div style="position:relative; width:100%; border-radius:8px; overflow:hidden; border:1px solid var(--line-light-faint); max-height:210px; background:var(--bg-light-sub); display:flex; justify-content:center; align-items:center;">
            <img src="/docs/notebooklm/infografias/anatomia_senal_descomposicion_ontologica.jpg" 
                 alt="Descomposición Ontológica de la Señal" 
                 class="infographic-img"
                 style="max-height:210px; width:auto; max-width:100%; object-fit:contain; display:block; cursor:zoom-in;"
                 onclick="openLightbox(this.src)" />
            <div style="position:absolute; bottom:6px; right:8px; background:rgba(15,23,42,0.85); color:#F8FAFC; padding:2px 8px; border-radius:4px; font-size:9.5px; font-family:'IBM Plex Mono'; pointer-events:none;">
              Infografía NotebookLM AI 🔍 (Clic para ampliar)
            </div>
          </div>

          <!-- SIMULADOR INTERACTIVO PROCEDURAL CON CÓDIGO PURO -->
          <div style="flex:1; display:flex; flex-direction:column; gap:6px; min-height:0;">
            <div class="sim-controls">
              <span style="font-size:10.5px; font-weight:700;" class="mono">Capas Activas:</span>
              <button class="sim-btn active" id="btnToggleT" onclick="toggleSignalLayer('T')">✓ T(t) Tendencia</button>
              <button class="sim-btn active" id="btnToggleS" onclick="toggleSignalLayer('S')">✓ S(t) Estacionalidad</button>
              <button class="sim-btn active" id="btnToggleC" onclick="toggleSignalLayer('C')">✓ C(t) ENSO (3-7a)</button>
              <button class="sim-btn active" id="btnToggleE" onclick="toggleSignalLayer('E')">✓ ε(t) Ruido (±2.5σ)</button>
              <span style="margin-left:auto; font-size:10.5px; color:var(--accent-blue);" class="mono" id="simLayerStatus">4 / 4 Capas Físicas</span>
            </div>

            <div class="chart-wrapper" style="background:var(--bg-light-sub); border-radius:8px; border:1px solid var(--line-light-faint); padding:6px; flex:1; min-height:0;">
              <canvas id="ontologicalWaveCanvas" style="width:100%; height:100%;"></canvas>
            </div>
          </div>
        </div>

        <div style="font-size:10px; color:var(--text-light-faint); border-top:1px solid var(--line-light-faint); padding-top:4px; display:flex; justify-content:space-between;" class="mono">
          <span>Y(t): Señal observada · T(t) secular · S(t) 365d · C(t) ENSO · ε(t) estocástico</span>
          <span style="color:var(--accent-blue);">Canvas Matemático 60 FPS</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIAPO 03: TAXONOMÍA Y EVOLUCIÓN METODOLÓGICA -->
  <section class="slide" data-index="3" data-act="Acto 1 · Taxonomía" data-time="2.0 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">03 / 20 · ACTO 1: TAXONOMÍA</span>
      <div class="badge badge-teoria">TEORÍA</div>
      <h2 class="slide-title display">Evolución: de Holt-Winters a Foundation Models</h2>
      <p class="slide-thesis">Cuatro eras metodológicas coexisten. La más reciente no siempre es la óptima para un sensor físico aislado.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">Clásico: 1960</span>
        <span class="metric-chip">ML Tabular: 2001</span>
        <span class="metric-chip">Deep Learning: 2017</span>
        <span class="metric-chip">Zero-Shot: 2024</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>1960–1980 (Clásico):</strong> ARIMA, ETS. Parsimonia lineal y garantías asintóticas en series cortas (&lt;500 obs).</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>2000–2015 (ML Tabular):</strong> ExtraTrees, LightGBM. Covariables no lineales y rezagos autoregresivos (M5 Walmart).</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>2017–2023 (Deep Learning):</strong> LSTM, PatchTST. Representaciones cruzadas en miles de series interdependientes.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>2024+ (Foundation Models):</strong> TimesFM, Chronos. Pronóstico Zero-Shot pre-entrenado en 100B de puntos temporales.</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 LEY DE PARSIMONIA</span>
        <p class="insight-text">Aumentar parámetros sin suficiente volumen genera sobreajuste espurio: un modelo simple con pocas covariables domina en series ruidosas o de estación única.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"Más parámetros no garantizan mejor pronóstico: el contexto del problema define la herramienta."</p>
      </div>
    </div>

    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">Cuadrante Metodológico: 4 Eras del Forecasting</span>
          <span class="visual-tag mono">TAXONOMÍA HISTÓRICA AUDITADA</span>
        </div>
        
        <div class="kpi-strip">
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#2563EB;">1960–1980</div>
            <div class="kpi-strip-lbl">Clásico (Parsimonia &lt; 500 obs)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#D97706;">2000–2015</div>
            <div class="kpi-strip-lbl">ML Tabular (Campeón M5 Walmart)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#7C3AED;">2017–2023</div>
            <div class="kpi-strip-lbl">Deep Learning (PatchTST / CAISO)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#059669;">2024+</div>
            <div class="kpi-strip-lbl">Zero-Shot (TimesFM 100B Tokens)</div>
          </div>
        </div>

        <div style="flex:1; display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; gap:12px; height:100%;">
          <!-- ERA 1 -->
          <div style="background:var(--bg-light-sub); padding:14px 18px; border-radius:10px; border-left:4px solid #2563EB; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:11px; font-weight:700; color:#2563EB;" class="mono">ERA 1 · CLÁSICA (1960–1980)</span>
                <span style="font-size:10px; background:rgba(37,99,235,0.1); color:#2563EB; padding:2px 8px; border-radius:4px;" class="mono">Parsimonia Pura</span>
              </div>
              <div style="font-size:16px; font-weight:700; margin:6px 0;">ARIMA & Exponential Smoothing</div>
              <div style="background:rgba(37,99,235,0.06); padding:4px 8px; border-radius:4px; font-size:11.5px; font-family:'IBM Plex Mono'; color:#1D4ED8; margin-bottom:6px; display:inline-block;">
                ŷ_{t+1} = μ + φ₁y_t + θ₁ε_t
              </div>
              <p style="font-size:12.5px; color:var(--text-light-mute); line-height:1.45;">Garantías asintóticas de Gauss-Markov. Intervalos cerrados. Cero riesgo de memorizar ruido en muestras pequeñas (N &lt; 500).</p>
            </div>
            
            <div style="display:flex; align-items:center; justify-content:space-between; border-top:1px solid var(--line-light-faint); padding-top:6px; margin-top:6px;">
              <span style="font-size:11px; color:#64748B;" class="mono">CPU: &lt; 0.01s · N &lt; 500 obs</span>
              <span style="font-size:10.5px; font-weight:600; color:#2563EB;" class="mono">MINSA / Bodegas</span>
            </div>
          </div>

          <!-- ERA 2 -->
          <div style="background:var(--bg-light-sub); padding:14px 18px; border-radius:10px; border-left:4px solid #D97706; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:11px; font-weight:700; color:#D97706;" class="mono">ERA 2 · ML TABULAR (2000–2015)</span>
                <span style="font-size:10px; background:rgba(217,119,6,0.1); color:#D97706; padding:2px 8px; border-radius:4px;" class="mono">Workhorse Industrial</span>
              </div>
              <div style="font-size:16px; font-weight:700; margin:6px 0;">ExtraTrees, RF & LightGBM</div>
              <div style="background:rgba(217,119,6,0.08); padding:4px 8px; border-radius:4px; font-size:11.5px; font-family:'IBM Plex Mono'; color:#B45309; margin-bottom:6px; display:inline-block;">
                [y_{t-1}, ... y_{t-14}] &rarr; Matriz Autoregresiva
              </div>
              <p style="font-size:12.5px; color:var(--text-light-mute); line-height:1.45;">Manejo robusto de covariables no lineales y missing values. Campeón absoluto de la competencia M5 de Walmart. Cuidado: flatlinea en anomalías récord.</p>
            </div>
            
            <div style="display:flex; align-items:center; justify-content:space-between; border-top:1px solid var(--line-light-faint); padding-top:6px; margin-top:6px;">
              <span style="font-size:11px; color:#64748B;" class="mono">CPU: 0.1s - 1s · 1k - 50k obs</span>
              <span style="font-size:10.5px; font-weight:600; color:#D97706;" class="mono">Clima Local / Retail</span>
            </div>
          </div>

          <!-- ERA 3 -->
          <div style="background:var(--bg-light-sub); padding:14px 18px; border-radius:10px; border-left:4px solid #7C3AED; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:11px; font-weight:700; color:#7C3AED;" class="mono">ERA 3 · DEEP LEARNING (2017–2023)</span>
                <span style="font-size:10px; background:rgba(124,58,237,0.1); color:#7C3AED; padding:2px 8px; border-radius:4px;" class="mono">Escala Masiva</span>
              </div>
              <div style="font-size:16px; font-weight:700; margin:6px 0;">LSTM, N-BEATS & PatchTST</div>
              <div style="background:rgba(124,58,237,0.08); padding:4px 8px; border-radius:4px; font-size:11.5px; font-family:'IBM Plex Mono'; color:#6D28D9; margin-bottom:6px; display:inline-block;">
                Parches de 16 pasos con Multi-Head Attention
              </div>
              <p style="font-size:12.5px; color:var(--text-light-mute); line-height:1.45;">Aprende dinámicas cruzadas compartidas en miles de sensores interdependientes (CAISO: 1,000 turbinas eólicas). Ineficiente en una estación individual aislada.</p>
            </div>
            
            <div style="display:flex; align-items:center; justify-content:space-between; border-top:1px solid var(--line-light-faint); padding-top:6px; margin-top:6px;">
              <span style="font-size:11px; color:#64748B;" class="mono">GPU: Horas · &gt; 100k obs</span>
              <span style="font-size:10.5px; font-weight:600; color:#7C3AED;" class="mono">Grids Nacionales</span>
            </div>
          </div>

          <!-- ERA 4 -->
          <div style="background:var(--bg-light-sub); padding:14px 18px; border-radius:10px; border-left:4px solid #059669; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:11px; font-weight:700; color:#059669;" class="mono">ERA 4 · FOUNDATION ZERO-SHOT (2024+)</span>
                <span style="font-size:10px; background:rgba(5,150,105,0.1); color:#059669; padding:2px 8px; border-radius:4px;" class="mono">Zero-Shot Frontera</span>
              </div>
              <div style="font-size:16px; font-weight:700; margin:6px 0;">TimesFM, Chronos & MOIRAI</div>
              <div style="background:rgba(5,150,105,0.08); padding:4px 8px; border-radius:4px; font-size:11.5px; font-family:'IBM Plex Mono'; color:#047857; margin-bottom:6px; display:inline-block;">
                Pre-entrenados en 100B de puntos temporales
              </div>
              <p style="font-size:12.5px; color:var(--text-light-mute); line-height:1.45;">Inferencia inmediata tratando números como tokens sin ajustar gradientes locales. Ideal para millones de SKUs nuevos o alertas tempranas sin historial.</p>
            </div>
            
            <div style="display:flex; align-items:center; justify-content:space-between; border-top:1px solid var(--line-light-faint); padding-top:6px; margin-top:6px;">
              <span style="font-size:11px; color:#64748B;" class="mono">Datos locales: 0 · Inferencia pura</span>
              <span style="font-size:10.5px; font-weight:600; color:#059669;" class="mono">Catálogos Masivos</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================== -->
  <!-- ACTO 2: LAS HERRAMIENTAS (Diapos 04 - 11)   -->
  <!-- ========================================== -->

  <!-- DIAPO 04 -->
  <section class="slide" data-index="4" data-act="Acto 2 · Las Herramientas" data-time="2.0 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">04 / 20 · ACTO 2: LAS HERRAMIENTAS</span>
      <div class="badge badge-mecanismo">MECANISMO</div>
      <h2 class="slide-title display">Memoria exponencial y límites biológicos</h2>
      <p class="slide-thesis">El mundo real impone física: la memoria de los eventos decae geométricamente y el crecimiento biológico choca contra una asíntota.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">Alisado: α(1-α)^k</span>
        <span class="metric-chip">Logística: L/(1+e^-k(t-t0))</span>
        <span class="metric-chip">Capacidad L</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Decaimiento de memoria:</strong> Holt-Winters pondera observaciones pasadas con pesos α(1-α)^k. Ajusta el control en vivo.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Techo biológico de Verhulst:</strong> El crecimiento infinito es imposible; la curva logística impone saturación real.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Implicancia práctica:</strong> Un modelo que ignora los límites de capacidad de carga sobreestimará rendimientos futuros.</div>
        </li>
      </ul>
            <div class="card-insight">
        <span class="insight-label">💡 TECHO DE CAPACIDAD</span>
        <p class="insight-text">Modelos lineales o redes densas asumen crecimiento sin cotas. En problemas agroclimáticos, acotar la salida con asíntotas biológicas evita proyecciones físicamente absurdas.</p>
      </div>
<div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"Ningún árbol crece hasta el cielo: la física y la biología siempre imponen una cota superior."</p>
      </div>
    </div>
    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">Memoria Geométrica vs Techo Logístico</span>
          <div style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:11px;" class="mono">Parámetro α:</span>
            <input type="range" id="alphaRange" min="0.1" max="0.8" step="0.05" value="0.35" oninput="updateAlpha(this.value)">
            <span id="alphaVal" style="font-size:12px; font-weight:700; width:30px;" class="mono">0.35</span>
          </div>
        </div>
        <div style="flex:1; display:grid; grid-template-columns:1fr 1fr; gap:14px; height:100%;">
          <div style="background:var(--bg-light-sub); padding:16px; border-radius:8px; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="font-size:11px; font-weight:700; margin-bottom:8px;" class="mono">PESOS EXPONENCIALES W_k = α(1-α)^k</div>
              <p style="font-size:12px; color:var(--text-light-mute); line-height:1.4;">Un α alto (0.8) olvida el pasado de inmediato; un α bajo (0.1) promedia a largo plazo.</p>
            </div>
            <div id="alphaBars" style="height:150px; display:flex; align-items:flex-end; gap:8px; border-bottom:1px solid #CBD5E1; padding-bottom:4px;">
              <!-- Se puebla dinamicamente -->
            </div>
            <div style="display:flex; justify-content:space-between; font-size:10px; color:#64748B;" class="mono">
              <span>t-0 (Hoy)</span>
              <span>t-1</span>
              <span>t-2</span>
              <span>t-3</span>
              <span>t-4 (Hace 4 d)</span>
            </div>
          </div>

          <div style="background:var(--bg-light-sub); padding:16px; border-radius:8px; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="font-size:11px; font-weight:700; color:#059669; margin-bottom:8px;" class="mono">SATURACIÓN BIOLÓGICA (CURVA LOGÍSTICA)</div>
              <p style="font-size:12px; color:var(--text-light-mute); line-height:1.4;">En agricultura y rendimiento biomasa, el crecimiento inicial exponencial se frena al acercarse a la capacidad de carga L.</p>
            </div>
            <svg viewBox="0 0 250 140" style="width:100%; height:130px;">
              <line x1="20" y1="120" x2="230" y2="120" stroke="#94A3B8" stroke-width="1.5" />
              <line x1="20" y1="20" x2="20" y2="120" stroke="#94A3B8" stroke-width="1.5" />
              <line x1="20" y1="30" x2="230" y2="30" stroke="#DC2626" stroke-dasharray="4" stroke-width="1.5" />
              <text x="140" y="25" fill="#DC2626" font-size="9" font-family="IBM Plex Mono">Capacidad L</text>
              <path d="M 20 115 Q 80 110 115 75 T 220 35" fill="none" stroke="#059669" stroke-width="2.5" />
              <circle cx="115" cy="75" r="4" fill="#059669" />
              <text x="125" y="80" fill="#059669" font-size="9" font-family="IBM Plex Mono">Punto Inflexión</text>
            </svg>
            <div style="font-size:10px; color:#64748B;" class="mono">
              Fórmula: Y(t) = L / (1 + e^-k(t-t0)) · Modelo saturante
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- DIAPO 05 -->
  <section class="slide" data-index="5" data-act="Acto 2 · Las Herramientas" data-time="2.5 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">05 / 20 · ACTO 2: LAS HERRAMIENTAS</span>
      <div class="badge badge-mecanismo">MECANISMO</div>
      <h2 class="slide-title display">Árboles: rezagos y no-extrapolación</h2>
      <p class="slide-thesis">Los árboles dividen el tiempo en cajas espaciales con rezagos, pero jamás pueden predecir un valor fuera del rango histórico visto en sus hojas de entrenamiento.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">Tope Entrenamiento: 34.0 °C</span>
        <span class="metric-chip">Ola Calor: 37.4 °C</span>
        <span class="metric-chip">Fallo RF: 5.5 °C</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Patología de partición espacial:</strong> Un árbol promedia las muestras de su hoja terminal más cercana. Ante un récord inédito, flatlinea en una meseta constante.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>El desastre de ERCOT (Texas, Feb 2021):</strong> Árboles entrenados con un techo de 10 años predijeron meseta en la tormenta Uri; la demanda real superó el pronóstico por <strong>20 GW</strong>, provocando un apagón mortal de 4 días.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Experimento propio en Punchana (SENAMHI):</strong> Con tope de 34.0 °C y ola de calor récord a 37.4 °C, RF colapsó en 31.5 °C. <strong>Modelar diferencias (Δy = y_t - y_{t-1})</strong> resolvió la meseta, subiendo a 35.45 °C.</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 DIAGNÓSTICO FORENSE</span>
        <p class="insight-text">El árbol carece del concepto de secuencia temporal: congela el tiempo en coordenadas estáticas. Para eventos extremos fuera de distribución, diferenciar la serie (Δy) o incorporar cotas físicas es innegociable.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"Un árbol nunca predice algo que no haya visto: promedia el pasado, no extrapola."</p>
      </div>
    </div>
    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <div>
            <span class="visual-title display">EXPERIMENTO PROPIO: Fallo de Extrapolación Térmica</span>
            <div style="font-size:11px; color:#DC2626; font-weight:600;" class="mono">Datos Reales SENAMHI Punchana (2023) · Análogo a ERCOT Texas</div>
          </div>
          <span class="visual-tag mono">HOLD-OUT CONTROLADO</span>
        </div>
        
        <!-- KPI STRIP SUPERIOR -->
        <div class="kpi-strip">
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#64748B;">34.0 °C</div>
            <div class="kpi-strip-lbl">Tope Entrenamiento (Límite del Árbol)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#DC2626;">37.4 °C</div>
            <div class="kpi-strip-lbl">Récord Real Ola Calor (Punchana)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#DC2626;">31.5 °C (Δ 5.5 °C)</div>
            <div class="kpi-strip-lbl">Colapso Random Forest (Meseta Plana)</div>
          </div>
          <div class="kpi-strip-item" style="border-left:3px solid #059669;">
            <div class="kpi-strip-val" style="color:#059669;">35.45 °C</div>
            <div class="kpi-strip-lbl">Solución con Primeras Diferencias (Δy)</div>
          </div>
        </div>

        <div class="chart-wrapper">
          <canvas id="chartExtrapolacion"></canvas>
        </div>
        <div style="font-size:11px; color:var(--text-light-faint); border-top:1px solid var(--line-light-faint); padding-top:6px; display:flex; justify-content:space-between;" class="mono">
          <span>Meseta RF Directo: ŷ = 31.5 °C (Error 5.5 °C)</span>
          <span style="color:#059669; font-weight:700;">Modelo con Diferencias (Δy): ŷ = 35.45 °C</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIAPO 06 -->
  <section class="slide" data-index="6" data-act="Acto 2 · Las Herramientas" data-time="2.0 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">06 / 20 · ACTO 2: LAS HERRAMIENTAS</span>
      <div class="badge badge-mecanismo">MECANISMO</div>
      <h2 class="slide-title display">Deep Learning: de LSTM a PatchTST</h2>
      <p class="slide-thesis">Tratar cada punto temporal como un token asfixia a los Transformers; agrupar el tiempo en sub-series (patches) desbloqueó la eficiencia de la atención global.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">336 Pts &rarr; 42 Tokens</span>
        <span class="metric-chip">-87.5% Memoria</span>
        <span class="metric-chip">Auto-Atención O((L/P)²)</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>El cuello recurrente:</strong> Las LSTMs procesan paso a paso (O(L)), con cuellos de botella secuenciales y desvanecimiento de gradiente.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Parches como palabras:</strong> PatchTST divide 336 observaciones en parches solapados (P=16, S=8), reduciendo la secuencia a 42 tokens (8 veces menos cómputo).</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>La pregunta de auditoría:</strong> ¿Vale la pena esta artillería profunda para predecir una estación local?</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 EFICIENCIA COMPUTACIONAL</span>
        <p class="insight-text">El mecanismo de parches de PatchTST reduce la longitud de la secuencia de 336 a 42 tokens, disminuyendo la complejidad de la matriz de atención de 112,896 a 1,764 operaciones.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"Agrupar el tiempo en parches, como palabras, hizo eficientes a los Transformers."</p>
      </div>
    </div>
    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">Recurrencia Secuencial vs Atención en Parches</span>
          <span class="visual-tag mono">ARQUITECTURAS NEURONALES</span>
        </div>

        <div class="kpi-strip">
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#DC2626;">O(L) Secuencial</div>
            <div class="kpi-strip-lbl">Latencia Recurrente (RNN / LSTM)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#059669;">42 Tokens (vs 336)</div>
            <div class="kpi-strip-lbl">Compresión PatchTST (P=16, S=8)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#2563EB;">-87.5% Memoria</div>
            <div class="kpi-strip-lbl">Ahorro en Matriz Cuadrática de Atención</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#7C3AED;">Channel-Indep.</div>
            <div class="kpi-strip-lbl">Proyección Cruzada Multi-Sensor</div>
          </div>
        </div>

        <div style="flex:1; display:grid; grid-template-rows:1fr 1fr; gap:14px; height:100%;">
          <!-- LSTM RECURRENCIA -->
          <div style="background:var(--bg-light-sub); padding:16px 20px; border-radius:10px; border-left:4px solid #DC2626; display:flex; flex-direction:column; justify-content:space-between;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <div>
                <span style="font-size:11px; font-weight:700; color:#DC2626;" class="mono">LSTM / RNN · PROCESAMIENTO SECUENCIAL PASO A PASO</span>
                <p style="font-size:12.5px; color:var(--text-light-mute); margin-top:2px;">Cada estado oculto h_t depende estrictamente del anterior h_{t-1}. La memoria temporal sufre desvanecimiento exponencial de gradiente.</p>
              </div>
              <span style="font-size:10px; background:rgba(220,38,38,0.1); color:#DC2626; padding:3px 8px; border-radius:4px;" class="mono">Cuello de Botella O(L)</span>
            </div>

            <!-- DIAGRAMA VECTORIAL RECURRENCIA -->
            <div style="background:rgba(255,255,255,0.8); border:1px solid var(--line-light-faint); border-radius:8px; padding:10px 16px; margin:4px 0;">
              <svg viewBox="0 0 760 65" style="width:100%; height:65px; display:block;">
                <g transform="translate(10, 5)">
                  <!-- Celda 1 -->
                  <rect x="30" y="10" width="70" height="38" rx="6" fill="#F1F5F9" stroke="#94A3B8" stroke-width="1.2" />
                  <text x="65" y="34" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="700" font-family="IBM Plex Mono">h(t-3)</text>
                  <text x="65" y="58" text-anchor="middle" fill="#64748B" font-size="10" font-family="IBM Plex Mono">x(t-3)</text>
                  <line x1="65" y1="48" x2="65" y2="60" stroke="#94A3B8" stroke-width="1.2" marker-end="url(#arr)" />

                  <line x1="100" y1="29" x2="150" y2="29" stroke="#DC2626" stroke-width="2" marker-end="url(#arrRed)" />

                  <!-- Celda 2 -->
                  <rect x="150" y="10" width="70" height="38" rx="6" fill="#F1F5F9" stroke="#94A3B8" stroke-width="1.2" />
                  <text x="185" y="34" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="700" font-family="IBM Plex Mono">h(t-2)</text>
                  <text x="185" y="58" text-anchor="middle" fill="#64748B" font-size="10" font-family="IBM Plex Mono">x(t-2)</text>
                  <line x1="185" y1="48" x2="185" y2="60" stroke="#94A3B8" stroke-width="1.2" />

                  <line x1="220" y1="29" x2="270" y2="29" stroke="#DC2626" stroke-width="2" />

                  <!-- Celda 3 -->
                  <rect x="270" y="10" width="70" height="38" rx="6" fill="#F1F5F9" stroke="#94A3B8" stroke-width="1.2" />
                  <text x="305" y="34" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="700" font-family="IBM Plex Mono">h(t-1)</text>
                  <text x="305" y="58" text-anchor="middle" fill="#64748B" font-size="10" font-family="IBM Plex Mono">x(t-1)</text>
                  <line x1="305" y1="48" x2="305" y2="60" stroke="#94A3B8" stroke-width="1.2" />

                  <line x1="340" y1="29" x2="390" y2="29" stroke="#DC2626" stroke-width="2" />

                  <!-- Celda Salida -->
                  <rect x="390" y="8" width="85" height="42" rx="6" fill="#DC2626" stroke="#B91C1C" stroke-width="1.5" />
                  <text x="432" y="34" text-anchor="middle" fill="#FFFFFF" font-size="13" font-weight="700" font-family="IBM Plex Mono">y(t+1)</text>
                  
                  <!-- Warning box -->
                  <text x="510" y="24" fill="#DC2626" font-size="11" font-weight="700" font-family="IBM Plex Mono">⚠ Sin paralelismo en GPU</text>
                  <text x="510" y="38" fill="#64748B" font-size="10" font-family="IBM Plex Mono">336 pasos = 336 operaciones encadenadas secuenciales</text>
                </g>
              </svg>
            </div>

            <div style="font-size:11px; color:#64748B;" class="mono">Imposible acelerar mediante matrices SIMD masivas · Gradiente se desvanece en h &gt; 30 pasos</div>
          </div>

          <!-- PATCHTST PARCHES -->
          <div style="background:var(--bg-light-sub); padding:16px 20px; border-radius:10px; border-left:4px solid #059669; display:flex; flex-direction:column; justify-content:space-between;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <div>
                <span style="font-size:11px; font-weight:700; color:#059669;" class="mono">PATCHTST · AGRUPACIÓN EN PARCHES (PATCHES) + AUTO-ATENCIÓN</span>
                <p style="font-size:12.5px; color:var(--text-light-mute); margin-top:2px;">La serie temporal se trocea en parches semánticos solapados. La auto-atención multi-cabeza procesa todos los parches simultáneamente en paralelo.</p>
              </div>
              <span style="font-size:10px; background:rgba(5,150,105,0.1); color:#059669; padding:3px 8px; border-radius:4px;" class="mono">O((L/P)²) Paralelo</span>
            </div>

            <!-- DIAGRAMA VECTORIAL PARCHES -->
            <div style="background:rgba(255,255,255,0.8); border:1px solid var(--line-light-faint); border-radius:8px; padding:10px 16px; margin:4px 0;">
              <svg viewBox="0 0 760 65" style="width:100%; height:65px; display:block;">
                <g transform="translate(10, 5)">
                  <!-- Parche 1 -->
                  <rect x="20" y="10" width="130" height="38" rx="6" fill="rgba(5,150,105,0.08)" stroke="#059669" stroke-width="1.8" stroke-dasharray="4 2" />
                  <text x="85" y="33" text-anchor="middle" fill="#065F46" font-size="11" font-weight="700" font-family="IBM Plex Mono">Parche 1 [t-32..t-16]</text>

                  <!-- Conector atención bi-direccional -->
                  <line x1="150" y1="29" x2="190" y2="29" stroke="#059669" stroke-width="2" />
                  <circle cx="170" cy="29" r="4" fill="#059669" />

                  <!-- Parche 2 -->
                  <rect x="190" y="10" width="130" height="38" rx="6" fill="rgba(5,150,105,0.08)" stroke="#059669" stroke-width="1.8" stroke-dasharray="4 2" />
                  <text x="255" y="33" text-anchor="middle" fill="#065F46" font-size="11" font-weight="700" font-family="IBM Plex Mono">Parche 2 [t-24..t-8]</text>

                  <line x1="320" y1="29" x2="360" y2="29" stroke="#059669" stroke-width="2" />
                  <circle cx="340" cy="29" r="4" fill="#059669" />

                  <!-- Parche N -->
                  <rect x="360" y="10" width="120" height="38" rx="6" fill="rgba(5,150,105,0.08)" stroke="#059669" stroke-width="1.8" stroke-dasharray="4 2" />
                  <text x="420" y="33" text-anchor="middle" fill="#065F46" font-size="11" font-weight="700" font-family="IBM Plex Mono">Parche 42 [t-16..t]</text>

                  <line x1="480" y1="29" x2="520" y2="29" stroke="#059669" stroke-width="2.5" />

                  <!-- Proyección Futura -->
                  <rect x="520" y="8" width="160" height="42" rx="6" fill="#059669" stroke="#047857" stroke-width="1.5" />
                  <text x="600" y="34" text-anchor="middle" fill="#FFFFFF" font-size="12" font-weight="700" font-family="IBM Plex Mono">Proyección [t+1..t+16]</text>
                </g>
              </svg>
            </div>

            <div style="font-size:11px; color:#059669; font-weight:600;" class="mono">
              Reducción de tokens: 336 &rarr; 42 (-87.5% memoria GPU) · Atención simultánea O((L/P)²)
            </div>
          </div>
        </div>
      </div>
  </section>

  <!-- DIAPO 07 -->
  <section class="slide" data-index="7" data-act="Acto 2 · Las Herramientas" data-time="2.0 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">07 / 20 · ACTO 2: LAS HERRAMIENTAS</span>
      <div class="badge badge-mecanismo">MECANISMO</div>
      <h2 class="slide-title display">Foundation Models: pronosticar sin entrenar</h2>
      <p class="slide-thesis">La revolución del Zero-Shot llegó a las series de tiempo: modelos pre-entrenados con miles de millones de puntos generan pronósticos instantáneos sin gradientes locales.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">TimesFM 200M Google</span>
        <span class="metric-chip">Chronos 4096 Bins AWS</span>
        <span class="metric-chip">Zero-Shot Nativo</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Tokenización de series:</strong> Chronos discretiza valores continuos en 4,096 buckets tratados como vocabulario de lenguaje en T5.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>TimesFM (Google 200M):</strong> Diseñado con atención causal en parches de 128 pasos sobre más de 100 mil millones de puntos reales y sintéticos.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>La prueba:</strong> ¿Puede un modelo que jamás conoció la Amazonía competir con modelos entrenados in situ?</div>
        </li>
      </ul>
            <div class="card-insight">
        <span class="insight-label">💡 GENERALIZACIÓN ZERO-SHOT</span>
        <p class="insight-text">Modelos como TimesFM 2.5 aprenden primitivas estadísticas universales en 100B de puntos. El prompt local de 512 días condiciona el pronóstico sin actualizar ningún peso.</p>
      </div>
<div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"Entrenados con miles de millones de puntos, pronostican series que nunca antes vieron."</p>
      </div>
    </div>
    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">Tokenización & Arquitectura Zero-Shot</span>
          <span class="visual-tag mono">TIMESFM & CHRONOS</span>
        </div>
        <div style="flex:1; display:flex; flex-direction:column; gap:12px; height:100%;">
          <div style="background:var(--bg-light-sub); padding:14px 18px; border-radius:8px; display:flex; flex-direction:column; justify-content:space-between; flex: 0 0 140px;">
            <div style="font-size:11px; font-weight:700; color:#7C3AED;" class="mono">CHRONOS: TOKENIZACIÓN EN 4,096 INTERVALOS DISCRETOS</div>
            <svg viewBox="0 0 500 55" style="width:100%; height:45px;">
              <line x1="10" y1="30" x2="490" y2="30" stroke="#CBD5E1" stroke-dasharray="2" />
              <path d="M 10 40 Q 80 10 160 30 T 320 20 T 490 25" fill="none" stroke="#2563EB" stroke-width="2" />
              <circle cx="160" cy="30" r="4" fill="#7C3AED" />
              <text x="145" y="18" fill="#7C3AED" font-size="9" font-family="IBM Plex Mono">Tok#3812</text>
              <circle cx="240" cy="40" r="4" fill="#7C3AED" />
              <text x="225" y="52" fill="#7C3AED" font-size="9" font-family="IBM Plex Mono">Tok#1940</text>
              <circle cx="380" cy="18" r="4" fill="#7C3AED" />
              <text x="365" y="10" fill="#7C3AED" font-size="9" font-family="IBM Plex Mono">Tok#4010</text>
            </svg>
            <div style="font-size:10px; color:#64748B;" class="mono">Convierte valores continuos en IDs discretos para procesarlos con Transformers de NLP (T5)</div>
          </div>

          <div style="background:var(--bg-light-sub); padding:14px 18px; border-radius:8px; flex:1; display:flex; flex-direction:column; justify-content:space-around;">
            <div style="font-size:11px; font-weight:700; margin-bottom:4px;" class="mono">MODELOS DE FRONTERA EVALUADOS EN LA CHARLA</div>
            <table style="width:100%; border-collapse:collapse; font-size:12px; font-family:'IBM Plex Mono', monospace;">
              <thead>
                <tr style="border-bottom:1px solid #CBD5E1; text-align:left; color:#64748B;">
                  <th style="padding:6px 0;">MODELO</th>
                  <th>CREADOR</th>
                  <th>PARÁMETROS</th>
                  <th>PRE-ENTRENAMIENTO</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid #E2E8F0;">
                  <td style="padding:8px 0; color:#2563EB; font-weight:700;">TimesFM 2.5</td>
                  <td>Google Research</td>
                  <td>200 Millones</td>
                  <td>~100B puntos temporales</td>
                </tr>
                <tr style="border-bottom:1px solid #E2E8F0;">
                  <td style="padding:8px 0; color:#D97706; font-weight:700;">Chronos-T5</td>
                  <td>Amazon AWS</td>
                  <td>20M a 710M</td>
                  <td>42 corpus + síntesis gaussiana</td>
                </tr>
                <tr>
                  <td style="padding:8px 0; color:#059669; font-weight:700;">MOIRAI</td>
                  <td>Salesforce</td>
                  <td>14M a 311M</td>
                  <td>LOTSA (27B observaciones)</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- DIAPO 08 -->
  <section class="slide" data-index="8" data-act="Acto 2 · Las Herramientas" data-time="2.0 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">08 / 20 · ACTO 2: LAS HERRAMIENTAS</span>
      <div class="badge badge-mecanismo">MECANISMO</div>
      <h2 class="slide-title display">Satélites: la trampa biofísica del NDVI</h2>
      <p class="slide-thesis">La clorofila y el mesófilo miden vigor fotosintético, pero cuando el dosel arbóreo cierra (LAI &gt; 3), el NDVI colapsa en una asíntota plana de 0.80, encegueciendo al modelo.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">Rojo: 665nm (90% Abs)</span>
        <span class="metric-chip">NIR: 842nm (Reflejado)</span>
        <span class="metric-chip">Saturación LAI &gt; 3</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Histología Foliar:</strong> El cloroplasto en el mesófilo en empalizada absorbe 80–95% del rojo (665 nm); el mesófilo esponjoso dispersa y refleja el NIR (842 nm).</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>La trampa de saturación:</strong> Al superar un Índice de Área Foliar LAI &gt; 3, el NDVI choca contra su asíntota en 0.80, mientras NDRE y EVI mantienen respuesta lineal hasta LAI = 5.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Caso Agro-Industrial:</strong> Copersucar y AgroVision migraron de NDVI a NDRE (RedEdge 705 nm) para detectar deficiencias de nitrógeno ocultas bajo doseles densos.</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 LÍMITE ESPECTRAL ÓPTICO</span>
        <p class="insight-text">Con dosel cerrado (LAI &gt; 3), la radiación roja fotosintéticamente activa es absorbida casi por completo. Sin contraste de absorción, el NDVI se congela; en cafetales densos, el satélite ve verde aunque el fruto colapse.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE (H1)</span>
        <p class="frase-text">"Cuando el follaje es denso, el NDVI satura: con coeficientes de variación de apenas 2.3% en la copa, el satélite óptico es ciego a lo que ocurre bajo las ramas."</p>
      </div>
    </div>

    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">Histología Foliar & Curva de Saturación Espectral (LAI &gt; 3)</span>
          <span class="visual-tag mono">INFOGRAFÍA NOTEBOOKLM & BIOFÍSICA</span>
        </div>
        
        <div class="infographic-wrapper">
          <div style="position:relative; width:100%; border-radius:8px; overflow:hidden; border:1px solid var(--line-light-faint); max-height:210px; background:var(--bg-light-sub); display:flex; justify-content:center; align-items:center;">
            <img src="/docs/notebooklm/infografias/satelite_biofisica_saturacion_ndvi.png" 
                 alt="Biofísica Satelital y Saturación NDVI" 
                 class="infographic-img"
                 style="max-height:210px; width:auto; max-width:100%; object-fit:contain; display:block;" />
            <div style="position:absolute; bottom:6px; right:8px; background:rgba(15,23,42,0.85); color:#F8FAFC; padding:2px 8px; border-radius:4px; font-size:9.5px; font-family:'IBM Plex Mono';">
              Infografía Histológica NotebookLM
            </div>
          </div>

          <div style="flex:1; display:grid; grid-template-columns:1fr 1fr; gap:12px; min-height:0;">
            <div style="background:var(--bg-light-sub); padding:12px 16px; border-radius:8px; border-left:4px solid #059669; display:flex; flex-direction:column; justify-content:space-between;">
              <div>
                <div style="font-size:11px; font-weight:700; color:#059669; margin-bottom:4px;" class="mono">HISTOLOGÍA FOLIAR (665 nm vs 842 nm)</div>
                <div style="font-size:11.5px; color:var(--text-light-mute); line-height:1.4;">
                  • <strong>Rojo (665 nm):</strong> 80–95% absorbido por clorofila en mesófilo en empalizada.<br>
                  • <strong>NIR (842 nm):</strong> Reflejado por la estructura celular del mesófilo esponjoso.
                </div>
              </div>
              
              <!-- SVG DIAGRAMA HISTOLOGÍA -->
              <div style="margin: 10px 0; background:rgba(255,255,255,0.7); border-radius:8px; padding:10px; border:1px solid var(--line-light-faint); flex:1; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 320 130" style="width:100%; height:140px; display:block;">
                  <!-- Cutícula Superior -->
                  <rect x="15" y="38" width="290" height="6" rx="2" fill="#CBD5E1" />
                  <text x="20" y="32" fill="#64748B" font-size="9" font-family="IBM Plex Mono">Cutícula Superior Cerosa</text>
                  
                  <!-- Mesófilo en empalizada (Células columnares) -->
                  <g fill="#10B981" stroke="#047857" stroke-width="1">
                    <rect x="25" y="48" width="22" height="34" rx="4" />
                    <rect x="51" y="48" width="22" height="34" rx="4" />
                    <rect x="77" y="48" width="22" height="34" rx="4" />
                    <rect x="103" y="48" width="22" height="34" rx="4" />
                    <rect x="129" y="48" width="22" height="34" rx="4" />
                    <rect x="155" y="48" width="22" height="34" rx="4" />
                    <rect x="181" y="48" width="22" height="34" rx="4" />
                    <rect x="207" y="48" width="22" height="34" rx="4" />
                    <rect x="233" y="48" width="22" height="34" rx="4" />
                    <rect x="259" y="48" width="22" height="34" rx="4" />
                  </g>
                  
                  <!-- Cloroplastos en el interior -->
                  <g fill="#065F46">
                    <circle cx="36" cy="58" r="2.5" /><circle cx="36" cy="70" r="2.5" />
                    <circle cx="62" cy="58" r="2.5" /><circle cx="62" cy="70" r="2.5" />
                    <circle cx="88" cy="58" r="2.5" /><circle cx="88" cy="70" r="2.5" />
                    <circle cx="114" cy="58" r="2.5" /><circle cx="114" cy="70" r="2.5" />
                    <circle cx="140" cy="58" r="2.5" /><circle cx="140" cy="70" r="2.5" />
                    <circle cx="166" cy="58" r="2.5" /><circle cx="166" cy="70" r="2.5" />
                    <circle cx="192" cy="58" r="2.5" /><circle cx="192" cy="70" r="2.5" />
                  </g>
                  
                  <!-- Mesófilo esponjoso (Células redondeadas y cavidades de aire) -->
                  <g fill="#6EE7B7" stroke="#059669" stroke-width="0.9" opacity="0.9">
                    <circle cx="40" cy="98" r="10" />
                    <circle cx="70" cy="100" r="9" />
                    <circle cx="100" cy="96" r="11" />
                    <circle cx="130" cy="100" r="9.5" />
                    <circle cx="160" cy="97" r="10.5" />
                    <circle cx="190" cy="100" r="9.5" />
                    <circle cx="220" cy="96" r="10.5" />
                    <circle cx="250" cy="99" r="9.5" />
                  </g>
                  
                  <!-- Cutícula Inferior -->
                  <rect x="15" y="116" width="290" height="5" rx="2" fill="#E2E8F0" />
                  <text x="20" y="127" fill="#94A3B8" font-size="8" font-family="IBM Plex Mono">Epidermis Inferior (Estomas)</text>
                  
                  <!-- Haz Rojo Incidente y Absorbido -->
                  <line x1="62" y1="5" x2="62" y2="60" stroke="#EF4444" stroke-width="2.6" stroke-linecap="round" />
                  <polygon points="62,64 58,56 66,56" fill="#EF4444" />
                  <text x="68" y="14" fill="#DC2626" font-size="9" font-weight="700" font-family="IBM Plex Mono">Rojo 665nm</text>
                  <text x="68" y="25" fill="#DC2626" font-size="8" font-family="IBM Plex Mono">90% Absorbido</text>
                  
                  <!-- Haz NIR Incidente y Reflejado -->
                  <path d="M 215 5 L 215 92 Q 215 102 226 92 L 244 5" fill="none" stroke="#2563EB" stroke-width="2.6" stroke-linecap="round" />
                  <polygon points="245,2 238,8 246,12" fill="#2563EB" />
                  <text x="145" y="14" fill="#2563EB" font-size="9" font-weight="700" font-family="IBM Plex Mono">NIR 842nm</text>
                  <text x="248" y="14" fill="#2563EB" font-size="8" font-family="IBM Plex Mono">85% Reflejado</text>
                </svg>
              </div>

              <div style="font-size:10.5px; color:#64748B; border-top:1px solid var(--line-light-faint); padding-top:4px;" class="mono">NDVI = (NIR - Red) / (NIR + Red)</div>
            </div>

            <div style="background:var(--bg-light-sub); padding:12px 16px; border-radius:8px; border-left:4px solid #DC2626; display:flex; flex-direction:column; justify-content:space-between;">
              <div>
                <div style="font-size:11px; font-weight:700; color:#DC2626; margin-bottom:4px;" class="mono">SOLUCIÓN NDRE / EVI (VENTANA RED-EDGE)</div>
                <div style="font-size:11.5px; color:var(--text-light-mute); line-height:1.4;">
                  • <strong>NDVI:</strong> Se aplana en meseta constante (~0.80) cuando LAI &gt; 3.<br>
                  • <strong>NDRE (Red-Edge 705 nm):</strong> Penetra el dosel denso con respuesta lineal hasta LAI = 5.
                </div>
              </div>

              <!-- SVG GRÁFICO DE SATURACIÓN -->
              <div style="margin: 10px 0; background:rgba(255,255,255,0.7); border-radius:8px; padding:10px; border:1px solid var(--line-light-faint); flex:1; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 320 130" style="width:100%; height:140px; display:block;">
                  <!-- Zona saturada sombreada -->
                  <rect x="175" y="10" width="130" height="98" fill="rgba(239, 68, 68, 0.08)" rx="4" />
                  <text x="185" y="20" fill="#DC2626" font-size="7.5" font-weight="700" font-family="IBM Plex Mono">ZONA SATURACIÓN (LAI &gt; 3)</text>
                  
                  <!-- Ejes -->
                  <line x1="30" y1="108" x2="305" y2="108" stroke="#94A3B8" stroke-width="1.4" />
                  <line x1="30" y1="15" x2="30" y2="108" stroke="#94A3B8" stroke-width="1.4" />
                  
                  <!-- Marcas Eje Y -->
                  <text x="10" y="32" fill="#64748B" font-size="8" font-family="IBM Plex Mono">0.8</text>
                  <text x="10" y="68" fill="#64748B" font-size="8" font-family="IBM Plex Mono">0.5</text>
                  <text x="10" y="105" fill="#64748B" font-size="8" font-family="IBM Plex Mono">0.2</text>
                  
                  <!-- Marcas Eje X -->
                  <text x="30" y="120" fill="#64748B" font-size="8" font-family="IBM Plex Mono">0</text>
                  <text x="75" y="120" fill="#64748B" font-size="8" font-family="IBM Plex Mono">LAI 1</text>
                  <text x="125" y="120" fill="#64748B" font-size="8" font-family="IBM Plex Mono">LAI 2</text>
                  <text x="170" y="120" fill="#DC2626" font-weight="700" font-size="8.5" font-family="IBM Plex Mono">LAI 3</text>
                  <text x="230" y="120" fill="#64748B" font-size="8" font-family="IBM Plex Mono">LAI 4</text>
                  <text x="285" y="120" fill="#64748B" font-size="8" font-family="IBM Plex Mono">LAI 5</text>
                  
                  <!-- Curva NDVI (Saturada en meseta plana) -->
                  <path d="M 30 100 Q 100 45 175 32 L 305 32" fill="none" stroke="#DC2626" stroke-width="2.8" />
                  <circle cx="175" cy="32" r="4" fill="#DC2626" />
                  <text x="238" y="42" fill="#DC2626" font-size="8.5" font-weight="700" font-family="IBM Plex Mono">NDVI ~0.80 (Meseta)</text>
                  
                  <!-- Curva NDRE (Lineal) -->
                  <path d="M 30 102 L 125 78 L 215 50 L 305 24" fill="none" stroke="#059669" stroke-width="2.4" stroke-dasharray="4,2" />
                  <text x="248" y="22" fill="#059669" font-size="8.5" font-weight="700" font-family="IBM Plex Mono">NDRE (Lineal)</text>
                  
                  <!-- Línea divisoria LAI 3 -->
                  <line x1="175" y1="10" x2="175" y2="108" stroke="#DC2626" stroke-width="1.2" stroke-dasharray="3,3" />
                </svg>
              </div>

              <div style="font-size:10.5px; color:#059669; font-weight:700; border-top:1px solid var(--line-light-faint); padding-top:4px;" class="mono">NDRE / Red-Edge 705nm penetra dosel maduro</div>
            </div>
          </div>
        </div>

        <div style="font-size:10px; color:var(--text-light-faint); border-top:1px solid var(--line-light-faint); padding-top:4px; display:flex; justify-content:space-between;" class="mono">
          <span>Eje X: Biomasa (LAI) · Eje Y: Sensibilidad espectral · Asíntota de saturación a LAI &gt; 3</span>
          <span style="color:#2563EB;">Biofísica de Teledetección</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIAPO 09 -->
  <section class="slide" data-index="9" data-act="Acto 2 · Las Herramientas" data-time="2.0 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">09 / 20 · ACTO 2: LAS HERRAMIENTAS</span>
      <div class="badge badge-mecanismo">MECANISMO</div>
      <h2 class="slide-title display">El reloj botánico fenológico</h2>
      <p class="slide-thesis">Un grado de calor o un milímetro de lluvia tienen impactos diametralmente opuestos según la ventana biológica en que impactan al cultivo.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">Floración: Ago-Oct</span>
        <span class="metric-chip">Llenado: Nov-Feb</span>
        <span class="metric-chip">Cosecha: Mar-Jul</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Floración crítica (Ago–Oct):</strong> Temperaturas &gt; 32 °C provocan esterilidad de polen y aborto floral masivo.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Llenado de fruto (Nov–Feb):</strong> Demanda hídrica alta; el déficit de lluvia reduce drásticamente el peso del grano.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Cosecha (Mar–Jul):</strong> Lluvias torrenciales pudren cerezas; calor seco acelera la recolección.</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 FUNCIÓN DE PÉRDIDA AGRÍCOLA</span>
        <p class="insight-text">El impacto del clima está modulado por la fenología: 30 mm de lluvia en floración aseguran el cuajado; los mismos 30 mm en plena cosecha pudren las cerezas en la planta.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"El mismo calor no daña igual en floración que en cosecha: la fenología manda."</p>
      </div>
    </div>
    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">Calendario Fenológico del Café Arábica en Jaén</span>
          <span class="visual-tag mono">BIOLOGÍA AGRÍCOLA</span>
        </div>

        <div class="kpi-strip">
          <div class="kpi-strip-item" style="border-left:3px solid #DC2626;">
            <div class="kpi-strip-val" style="color:#DC2626;">Tmax &lt; 32 °C</div>
            <div class="kpi-strip-lbl">Floración Crítica (Ago–Oct)</div>
          </div>
          <div class="kpi-strip-item" style="border-left:3px solid #2563EB;">
            <div class="kpi-strip-val" style="color:#2563EB;">Lluvia &gt; 80 mm/mes</div>
            <div class="kpi-strip-lbl">Llenado de Grano (Nov–Feb)</div>
          </div>
          <div class="kpi-strip-item" style="border-left:3px solid #059669;">
            <div class="kpi-strip-val" style="color:#059669;">Tiempo Seco</div>
            <div class="kpi-strip-lbl">Cosecha Óptima (Mar–Jul)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#7C3AED;">365 Días</div>
            <div class="kpi-strip-lbl">Ciclo Fenológico Completo</div>
          </div>
        </div>

        <div style="flex:1; display:flex; flex-direction:column; gap:12px; height:100%;">
          <div style="flex:1; display:flex; align-items:center; justify-content:center; background:var(--bg-light-sub); border-radius:10px; padding:10px;">
            <svg viewBox="0 0 740 280" style="width:100%; height:100%; max-height:280px;">
              <!-- Anillo base -->
              <circle cx="370" cy="140" r="90" fill="none" stroke="#E2E8F0" stroke-width="32" />
              <!-- Floracion: Ago-Oct (~25%) -->
              <circle cx="370" cy="140" r="90" fill="none" stroke="#DC2626" stroke-width="34" stroke-dasharray="141 424" stroke-dashoffset="0" />
              <!-- Llenado: Nov-Feb (~35%) -->
              <circle cx="370" cy="140" r="90" fill="none" stroke="#2563EB" stroke-width="34" stroke-dasharray="198 367" stroke-dashoffset="-141" />
              <!-- Cosecha: Mar-Jul (~40%) -->
              <circle cx="370" cy="140" r="90" fill="none" stroke="#059669" stroke-width="34" stroke-dasharray="226 339" stroke-dashoffset="-339" />
              
              <text x="370" y="136" text-anchor="middle" fill="#0F172A" font-size="14" font-weight="700" font-family="Space Grotesk">CICLO ANUAL</text>
              <text x="370" y="154" text-anchor="middle" fill="#64748B" font-size="11" font-family="IBM Plex Mono">JAÉN · 365 DÍAS</text>

              <!-- Conectores y etiquetas sin solapes -->
              <!-- Floración (Top Right) -->
              <line x1="435" y1="75" x2="520" y2="55" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="3 2" />
              <circle cx="435" cy="75" r="4" fill="#DC2626" />
              <text x="530" y="52" fill="#DC2626" font-size="13" font-family="IBM Plex Mono" font-weight="700">FLORACIÓN (Ago–Oct)</text>
              <text x="530" y="70" fill="#64748B" font-size="11.5">Ventana crítica: Tmax &gt; 32°C aborta flores</text>

              <!-- Llenado (Bottom Right) -->
              <line x1="435" y1="205" x2="520" y2="225" stroke="#2563EB" stroke-width="1.5" stroke-dasharray="3 2" />
              <circle cx="435" cy="205" r="4" fill="#2563EB" />
              <text x="530" y="222" fill="#2563EB" font-size="13" font-family="IBM Plex Mono" font-weight="700">LLENADO DE FRUTO (Nov–Feb)</text>
              <text x="530" y="240" fill="#64748B" font-size="11.5">Alta demanda hídrica; sequía da grano vano</text>

              <!-- Cosecha (Left) -->
              <line x1="305" y1="140" x2="220" y2="140" stroke="#059669" stroke-width="1.5" stroke-dasharray="3 2" />
              <circle cx="305" cy="140" r="4" fill="#059669" />
              <text x="210" y="136" text-anchor="end" fill="#059669" font-size="13" font-family="IBM Plex Mono" font-weight="700">COSECHA (Mar–Jul)</text>
              <text x="210" y="154" text-anchor="end" fill="#64748B" font-size="11.5">Lluvias tardías pudren cerezas en planta</text>
            </svg>
          </div>

          <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; height:90px;">
            <div style="background:var(--bg-light-sub); padding:12px 14px; border-radius:8px; border-top:3px solid #DC2626; display:flex; flex-direction:column; justify-content:center;">
              <span style="font-size:11px; font-weight:700; color:#DC2626;" class="mono">FLORACIÓN (AGO–OCT)</span>
              <p style="font-size:12px; color:var(--text-light-mute); margin-top:3px; line-height:1.35;">Estrés térmico (&gt;32°C) aborta flores antes de cuajar. Explica el 75% del rendimiento final.</p>
            </div>
            <div style="background:var(--bg-light-sub); padding:12px 14px; border-radius:8px; border-top:3px solid #2563EB; display:flex; flex-direction:column; justify-content:center;">
              <span style="font-size:11px; font-weight:700; color:#2563EB;" class="mono">LLENADO DE FRUTO (NOV–FEB)</span>
              <p style="font-size:12px; color:var(--text-light-mute); margin-top:3px; line-height:1.35;">La sequía en esta fase genera grano vano ("grano negro"), bajando drásticamente el peso.</p>
            </div>
            <div style="background:var(--bg-light-sub); padding:12px 14px; border-radius:8px; border-top:3px solid #059669; display:flex; flex-direction:column; justify-content:center;">
              <span style="font-size:11px; font-weight:700; color:#059669;" class="mono">COSECHA (MAR–JUL)</span>
              <p style="font-size:12px; color:var(--text-light-mute); margin-top:3px; line-height:1.35;">Lluvias tardías desprenden y pudren el fruto; días secos optimizan el secado.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- DIAPO 10 -->
  <section class="slide" data-index="10" data-act="Acto 2 · Las Herramientas" data-time="2.0 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">10 / 20 · ACTO 2: LAS HERRAMIENTAS</span>
      <div class="badge badge-evidencia">EVIDENCIA</div>
      <h2 class="slide-title display">Física global: discrepancia entre agencias</h2>
      <p class="slide-thesis">Las agencias meteorológicas resuelven Navier-Stokes en supercomputadores de 11,000 núcleos; aun así, discrepan intensamente en el trópico.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">NOAA GFS (0.25°)</span>
        <span class="metric-chip">ECMWF IFS (9km)</span>
        <span class="metric-chip">ΔT Media: 6.36 °C</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>ECMWF (Europa) vs NOAA GFS (EE.UU.):</strong> Modelos globales con asimilación 4D-Var de millones de observaciones satelitales.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Discrepancia real en Iquitos:</strong> Para el mismo día, la diferencia media absoluta es de 6.36 °C (máxima de 9.3 °C) y hasta 29.3 mm en lluvia.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Conclusión física:</strong> Si los modelos deterministas más caros del mundo divergen, el pronóstico puntual es una ilusión.</div>
        </li>
      </ul>
            <div class="card-insight">
        <span class="insight-label">💡 DIVERGENCIA NUMÉRICA</span>
        <p class="insight-text">Las discrepancias de hasta 9.3 °C entre NOAA GFS y ECMWF IFS demuestran que parametrizar la convección tropical en mallas de 9 a 25 km sigue siendo un problema físico abierto.</p>
      </div>
<div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"Incluso la física más cara del mundo tiene incertidumbre."</p>
      </div>
    </div>
    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">Discrepancia Real NOAA GFS vs ECMWF IFS en Iquitos</span>
          <span class="visual-tag mono">FÍSICA OPERATIVA</span>
        </div>

        <!-- KPI STRIP SUPERIOR -->
        <div class="kpi-strip">
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#D97706;">6.36 °C</div>
            <div class="kpi-strip-lbl">Discrepancia Media Absoluta (ΔT)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#DC2626;">9.30 °C</div>
            <div class="kpi-strip-lbl">Discrepancia Máxima Puntual</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#059669;">9 km (4D-Var)</div>
            <div class="kpi-strip-lbl">Resolución ECMWF IFS (Europa)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val" style="color:#2563EB;">25 km (GFS)</div>
            <div class="kpi-strip-lbl">Resolución NOAA (EE.UU.)</div>
          </div>
        </div>

        <div class="chart-wrapper">
          <canvas id="chartNoaaEcmwf"></canvas>
        </div>
        <div style="font-size:11px; color:var(--text-light-faint); border-top:1px solid var(--line-light-faint); padding-top:6px; display:flex; justify-content:space-between;" class="mono">
          <span>Fuente: Pronósticos Oficiales NOAA GFS vs ECMWF IFS</span>
          <span style="color:#D97706; font-weight:700;">Discrepancia Media: 6.36 °C · Max: 9.30 °C</span>
        </div>
      </div>
    </div>
  </section>
"""
