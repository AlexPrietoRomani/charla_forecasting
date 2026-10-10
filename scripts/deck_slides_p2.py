def get_slides_part2(branding=None):
    if branding is None:
        branding = {}
    qr_svg = branding.get("qr_svg", "")
    b64_dw = branding.get("b64_dw", "")
    return f"""
  <!-- ========================================== -->
  <!-- ACTO 2 · LAS HERRAMIENTAS (Diapo 11)       -->
  <!-- ========================================== -->

  <!-- DIAPO 11 -->
  <section class="slide" data-index="11" data-act="Acto 2 · Las Herramientas" data-time="2.0 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">11 / 20 · ACTO 2: LAS HERRAMIENTAS</span>
      <div class="badge badge-evidencia">EVIDENCIA</div>
      <h2 class="slide-title display">GraphCast: la IA en la meteorología</h2>
      <p class="slide-thesis">DeepMind demostró que una Graph Neural Network sobre una malla icosaédrica terrestre supera a los supercomputadores físicos en el 90.3% de 1,380 variables evaluadas.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">DeepMind / Science 2023</span>
        <span class="metric-chip">60s en 1 TPU v4</span>
        <span class="metric-chip">90.3% Variables Ganadas</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Malla icosaédrica multiescala:</strong> Conecta celdas globales de 0.25° evitando singularidades polares mediante paso de mensajes en grafo.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Aceleración radical:</strong> Pronóstico global a 10 días en menos de 1 minuto frente a horas en miles de núcleos de supercomputador.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Transición al mundo real:</strong> La IA global funciona a gran escala. Pero, ¿qué pasa cuando bajamos a tierra en la selva peruana?</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 SALTO COMPUTACIONAL</span>
        <p class="insight-text">GraphCast sustituye la integración numérica explícita de Navier-Stokes por propagación de mensajes sobre un grafo icosaédrico, reduciendo el gasto energético en 99.8%.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"Un minuto en un chip frente a una hora en 11,664 núcleos."</p>
      </div>
    </div>

    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">GraphCast: Malla Icosaédrica & Aceleración Computacional</span>
          <span class="visual-tag mono">SCIENCE 2023 / DEEPMIND</span>
        </div>

        <div class="kpi-strip">
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">90.3% Ganadas</div>
            <div class="kpi-strip-lbl">1,246 de 1,380 variables vs ECMWF HRES</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">&lt; 60 Segundos</div>
            <div class="kpi-strip-lbl">Inferencia 10 días en 1 TPU v4</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">11,664 Cores</div>
            <div class="kpi-strip-lbl">Supercomputador Atos reemplazado</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">0.25° Malla</div>
            <div class="kpi-strip-lbl">Malla icosaédrica sin singularidad polar</div>
          </div>
        </div>

        <div style="flex:1; display:grid; grid-template-columns:1.05fr 0.95fr; gap:16px; height:100%; min-height:0;">
          <div style="background:var(--bg-light-sub); padding:16px; border-radius:10px; border:1px solid var(--line-light-faint); display:flex; flex-direction:column; justify-content:space-between; align-items:center;">
            <div style="font-size:11.5px; font-weight:700; color:#2563EB; width:100%; text-align:left;" class="mono">MALLA ICOSAÉDRICA MULTIESCALA (GNN)</div>
            
            <svg viewBox="0 0 280 230" style="width:100%; max-width:240px; height:180px;">
              <!-- Globo terráqueo con malla icosaédrica multiescala -->
              <circle cx="140" cy="115" r="95" fill="rgba(37,99,235,0.05)" stroke="#94A3B8" stroke-width="1.5" />
              <!-- Líneas de latitud / ecuador -->
              <ellipse cx="140" cy="115" rx="95" ry="32" fill="none" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="3 3" />
              <!-- Polígono icosaédrico proyectado -->
              <polygon points="140,25 220,68 205,175 75,175 60,68" fill="none" stroke="#2563EB" stroke-width="2.5" />
              <!-- Aristas internas multiescala -->
              <line x1="140" y1="25" x2="205" y2="175" stroke="#60A5FA" stroke-width="1.5" stroke-dasharray="2 2" />
              <line x1="140" y1="25" x2="75" y2="175" stroke="#60A5FA" stroke-width="1.5" stroke-dasharray="2 2" />
              <line x1="220" y1="68" x2="75" y2="175" stroke="#60A5FA" stroke-width="1.5" stroke-dasharray="2 2" />
              <line x1="60" y1="68" x2="205" y2="175" stroke="#60A5FA" stroke-width="1.5" stroke-dasharray="2 2" />
              <line x1="60" y1="68" x2="220" y2="68" stroke="#93C5FD" stroke-width="1.5" stroke-dasharray="2 2" />
              <!-- Nodos del grafo -->
              <circle cx="140" cy="25" r="5.5" fill="#2563EB" />
              <circle cx="220" cy="68" r="5.5" fill="#2563EB" />
              <circle cx="205" cy="175" r="5.5" fill="#2563EB" />
              <circle cx="75" cy="175" r="5.5" fill="#2563EB" />
              <circle cx="60" cy="68" r="5.5" fill="#2563EB" />
              <!-- Nodo central conector -->
              <circle cx="140" cy="115" r="4.5" fill="#0891B2" />
              <!-- Punto Amazonía / Perú -->
              <circle cx="112" cy="122" r="7" fill="#DC2626" class="anim-glow" />
              <circle cx="112" cy="122" r="3" fill="#FFF" />
              <rect x="122" y="112" width="95" height="20" rx="3" fill="rgba(15,23,42,0.85)" />
              <text x="126" y="126" fill="#F8FAFC" font-size="9" font-family="IBM Plex Mono" font-weight="700">Perú (-3.7° S)</text>
            </svg>

            <div style="font-size:10.5px; color:#64748B; width:100%; text-align:center;" class="mono">
              Paso de mensajes en 16 capas GNN · Resolución espacial 0.25° (~28 km)
            </div>
          </div>

          <div style="background:var(--bg-light-sub); padding:16px; border-radius:10px; border:1px solid var(--line-light-faint); display:flex; flex-direction:column; justify-content:space-around;">
            <div style="border-left:4px solid #DC2626; padding-left:12px;">
              <div style="font-size:11px; font-weight:700; color:#DC2626;" class="mono">ECMWF HRES (MODELO FÍSICO NUMÉRICO)</div>
              <div style="font-size:22px; font-weight:700; margin:4px 0; color:var(--text-light-main);">~60 Minutos</div>
              <div style="font-size:11.5px; color:var(--text-light-mute); line-height:1.35;">Supercomputador Atos BullSequana (11,664 cores x86) · Megavatios de consumo energético industrial.</div>
            </div>

            <div style="border-left:4px solid #059669; padding-left:12px; margin-top:8px;">
              <div style="font-size:11px; font-weight:700; color:#059669;" class="mono">GRAPHCAST (DEEPMIND GNN)</div>
              <div style="font-size:22px; font-weight:700; margin:4px 0; color:#059669;">&lt; 60 Segundos</div>
              <div style="font-size:11.5px; color:var(--text-light-mute); line-height:1.35;">1x TPU v4 Cloud · Gasto energético 99.8% menor · 90.3% de variables ganadas en test ciego oficial.</div>
            </div>
            
            <div style="font-size:10.5px; color:#64748B; border-top:1px solid #CBD5E1; padding-top:8px;" class="mono">
              Ambos usan ERA5 como verdad terreno base (Copernicus / ECMWF)
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================== -->
  <!-- ACTO 3: CASO A - IQUITOS (Diapos 12 - 14)   -->
  <!-- ========================================== -->

  <!-- DIAPO 12 -->
  <section class="slide" data-index="12" data-act="Acto 3 · Caso A: Iquitos" data-time="1.5 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">12 / 20 · ACTO 3: CASO A (IQUITOS)</span>
      <div class="badge badge-caso_real">CASO REAL</div>
      <h2 class="slide-title display">Contexto Punchana: datos reales</h2>
      <p class="slide-thesis">La Amazonía profunda pone a prueba cualquier algoritmo: sensores con fallas, humedad implacable del 85% y perturbaciones polares (friajes).</p>
      
      <div class="metric-chips">
        <span class="metric-chip">Punchana: -3.69°, -73.26°</span>
        <span class="metric-chip">91 msnm</span>
        <span class="metric-chip">2,557 Días (2019-2025)</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Estación Punchana (SENAMHI):</strong> Confluencia de los ríos Nanay y Amazonas en Loreto.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Imperfección de los datos:</strong> 2,557 días registrados. La temperatura máxima presenta <strong>9.7% de huecos</strong> que deben imputarse de forma estricta.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Eventos extremos:</strong> Friaje histórico con mínima de <strong>19.2 °C</strong> y olas de calor récord de hasta <strong>37.4 °C</strong>.</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 PROTOCOLO DE LIMPIEZA</span>
        <p class="insight-text">Se aplicó interpolación estricta sin fuga de información futura sobre el 9.7% de huecos de la estación Punchana (-3.693°S, -73.255°W), preservando la dinámica térmica diaria.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"Los datos reales tienen huecos; tratarlos con rigor es parte integral del modelo."</p>
      </div>
    </div>

    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">Estación Punchana SENAMHI & Serie Histórica Reciente</span>
          <span class="visual-tag mono">DATOS REALES GARÚA / SENAMHI</span>
        </div>

        <div class="kpi-strip">
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">2,557 Días</div>
            <div class="kpi-strip-lbl">Histórico diario 2019–2025</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">9.7% Huecos</div>
            <div class="kpi-strip-lbl">Imputación estricta sin fuga futura</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">37.4 °C Máx</div>
            <div class="kpi-strip-lbl">Ola de calor récord (sept-2023)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">19.2 °C Mín</div>
            <div class="kpi-strip-lbl">Friaje polar antártico anómalo</div>
          </div>
        </div>

        <div style="flex:1; display:flex; flex-direction:column; gap:10px; height:100%; min-height:0;">
          <!-- Mapa Vectorial Confluencia de Ríos Enriquecido -->
          <div style="flex: 0 0 160px; background:var(--bg-light-sub); border-radius:10px; border:1px solid var(--line-light-faint); padding:10px 16px; display:flex; flex-direction:column; justify-content:space-between; position:relative; overflow:hidden;">
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:11px; font-weight:700;" class="mono">
              <span style="color:#0891B2; display:flex; align-items:center; gap:6px;">
                <span style="width:8px; height:8px; border-radius:50%; background:#0891B2; display:inline-block;"></span>
                CONFLUENCIA RÍOS NANAY & AMAZONAS (IQUITOS, LORETO)
              </span>
              <span style="background:rgba(8,145,178,0.1); color:#0891B2; padding:2px 8px; border-radius:4px;">-3.693°S, -73.255°W · 91 msnm · Selva Baja</span>
            </div>
            
            <svg viewBox="0 0 800 100" style="width:100%; height:90px; margin:2px 0;">
              <!-- Terreno base -->
              <rect x="0" y="0" width="800" height="100" fill="rgba(16, 185, 129, 0.05)" rx="6"/>
              <!-- Huella urbana Iquitos -->
              <path d="M 320 30 Q 360 35 370 60 Q 360 85 310 75 Q 290 55 320 30 Z" fill="rgba(100, 116, 139, 0.18)" stroke="#94A3B8" stroke-width="1" stroke-dasharray="3 2" />
              <text x="315" y="65" fill="#64748B" font-size="9" font-family="IBM Plex Mono">Iquitos Metropolitano</text>
              <!-- Río Amazonas -->
              <path d="M 0 50 Q 220 35 380 60 T 800 45" fill="none" stroke="#2563EB" stroke-width="14" opacity="0.3" stroke-linecap="round" />
              <path d="M 0 50 Q 220 35 380 60 T 800 45" fill="none" stroke="#3B82F6" stroke-width="5" opacity="0.65" stroke-linecap="round" />
              <text x="560" y="40" fill="#1D4ED8" font-size="11" font-family="IBM Plex Mono" font-weight="700">Río Amazonas &rarr; (Flujo Atlántico)</text>
              <!-- Río Nanay -->
              <path d="M 340 0 Q 355 20 380 58" fill="none" stroke="#0891B2" stroke-width="9" opacity="0.35" stroke-linecap="round" />
              <path d="M 340 0 Q 355 20 380 58" fill="none" stroke="#06B6D4" stroke-width="3.5" opacity="0.75" stroke-linecap="round" />
              <text x="285" y="18" fill="#0891B2" font-size="10" font-family="IBM Plex Mono" font-weight="700">Río Nanay</text>
              <!-- Estación Punchana Pin -->
              <circle cx="380" cy="58" r="12" fill="rgba(220, 38, 38, 0.2)" class="anim-glow" />
              <circle cx="380" cy="58" r="5" fill="#DC2626" />
              <circle cx="380" cy="58" r="2" fill="#FFF" />
              <rect x="395" y="46" width="220" height="28" rx="4" fill="white" stroke="#DC2626" stroke-width="1.5" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.1))" />
              <text x="403" y="58" fill="#DC2626" font-size="9.5" font-family="IBM Plex Mono" font-weight="700">📍 Estación Punchana (SENAMHI)</text>
              <text x="403" y="69" fill="#475569" font-size="8" font-family="IBM Plex Sans">Sensor Automático Vaisala AWS · Serie 2019-2025</text>
            </svg>

            <div style="display:flex; justify-content:space-between; font-size:9.5px; color:var(--text-light-faint); border-top:1px solid var(--line-light-faint); padding-top:4px;" class="mono">
              <span>Clima Tropical Ecuatorial Af</span>
              <span>Humedad Relativa: 86.4%</span>
              <span>Precipitación Anual: ~3,100 mm</span>
              <span>Friajes Antárticos: 4-6 eventos/año</span>
            </div>
          </div>

          <!-- Serie Reciente Chart -->
          <div class="chart-wrapper" style="flex:1; min-height:0; position:relative; background:var(--bg-light-panel); border-radius:10px; border:1px solid var(--line-light-faint); padding:10px;">
            <canvas id="chartSenamhiReciente"></canvas>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- DIAPO 13 -->
  <section class="slide" data-index="13" data-act="Acto 3 · Caso A: Iquitos" data-time="3.0 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">13 / 20 · ACTO 3: CASO A (IQUITOS)</span>
      <div class="badge badge-evidencia">EVIDENCIA</div>
      <h2 class="slide-title display">Benchmark de 8 modelos: la revelación</h2>
      <p class="slide-thesis">Sometimos a prueba 8 modelos sobre un holdout ciego de 90 días en Punchana. 70 veces más cómputo no compra mayor precisión en una sola estación.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">ExtraTrees: 1.880 °C</span>
        <span class="metric-chip">TimesFM: 1.965 °C (p=0.27)</span>
        <span class="metric-chip">LSTM: 2.054 °C (p=0.03)</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Ganador por parsimonia:</strong> ExtraTrees logra RMSE de <strong>1.880 °C</strong> en apenas <strong>0.11 segundos</strong> de CPU.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Empates Diebold-Mariano (p &gt; 0.05):</strong> Random Forest (1.885 °C), ARIMA (1.964 °C) y TimesFM 200M (1.965 °C) empatan estadísticamente.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>La sorpresa Zero-Shot:</strong> TimesFM logró el menor MAE del benchmark (<strong>1.392 °C</strong>) sin haber visto la serie jamás en entrenamiento.</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 PRUEBA DIEBOLD-MARIANO</span>
        <p class="insight-text">El test estadístico confirma que ExtraTrees (RMSE 1.880 °C) empata con TimesFM (p = 0.275) y supera a LSTM profunda (p = 0.031) consumiendo 70 veces menos cómputo.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"Para una sola estación, 70 veces más cómputo no compra precisión: la parsimonia manda, aunque el Zero-Shot ya compite sin haber visto la serie."</p>
      </div>
    </div>

    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">Ranking de Modelos en Hold-out Ciego de 90 Días</span>
          <span class="visual-tag mono">DIEBOLD-MARIANO TEST / PUNCHANA</span>
        </div>

        <div class="kpi-strip">
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">1.880 °C</div>
            <div class="kpi-strip-lbl">ExtraTrees RMSE Ganador (0.11s CPU)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">1.965 °C</div>
            <div class="kpi-strip-lbl">TimesFM 200M (Empate DM p=0.27)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">2.054 °C</div>
            <div class="kpi-strip-lbl">LSTM Recurrente (Inferior p=0.03)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">70x Aceleración</div>
            <div class="kpi-strip-lbl">CPU 0.11s vs GPU 7.87s en inferencia</div>
          </div>
        </div>

        <div class="chart-wrapper">
          <canvas id="chartBenchmark"></canvas>
        </div>

        <div style="font-size:11px; color:var(--text-light-faint); border-top:1px solid var(--line-light-faint); padding-top:6px; display:flex; justify-content:space-between;" class="mono">
          <span>Verde: Ganador Operativo · Azul: Empates DM (p &gt; 0.05) · Rojo: Inferior</span>
          <span style="font-weight:700;">ExtraTrees (0.11s CPU) vs TimesFM 200M (7.87s GPU)</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIAPO 14 -->
  <section class="slide" data-index="14" data-act="Acto 3 · Caso A: Iquitos" data-time="2.5 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">14 / 20 · ACTO 3: CASO A (IQUITOS)</span>
      <div class="badge badge-demo">DEMO</div>
      <h2 class="slide-title display">DEMO 1: Pronóstico operativo a 7 días</h2>
      <p class="slide-thesis">La toma de decisiones no opera sobre predicciones puntuales sino sobre la cuantificación rigurosa del margen de incertidumbre residual.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">ExtraTrees Ganador</span>
        <span class="metric-chip">Bandas P10–P90</span>
        <span class="metric-chip">TimesFM Zero-Shot</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Pronóstico ExtraTrees:</strong> Predicción central con su banda de cuantiles empíricos (P10–P90).</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Foundation Model en vivo:</strong> Visualiza la trayectoria de TimesFM Zero-Shot frente al modelo local.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Conmutador interactivo:</strong> Alterna entre modelos para evaluar discrepancias en horizonte de 7 días.</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 GESTIÓN OPERATIVA</span>
        <p class="insight-text">La banda P10–P90 capturó el 85.7% de las observaciones reales en la ventana de prueba a 7 días. La línea central sirve de referencia; la banda define el margen de seguridad.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"El valor está en la banda, no en la línea."</p>
      </div>
    </div>

    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">DEMO INTERACTIVA: Pronóstico Operativo con Bandas P10–P90</span>
          <div style="display:flex; gap:6px;">
            <button class="nav-btn" onclick="toggleDataset(4)">TimesFM</button>
            <button class="nav-btn" onclick="toggleDataset(5)">Chronos</button>
            <button class="nav-btn" onclick="toggleDataset(6)">ARIMA</button>
          </div>
        </div>

        <div class="kpi-strip">
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">7 Días</div>
            <div class="kpi-strip-lbl">Horizonte operativo de predicción</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">P10–P90</div>
            <div class="kpi-strip-lbl">Banda de cuantiles (85.7% cobertura)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">1.62 °C MAE</div>
            <div class="kpi-strip-lbl">Error medio en ventana operativa 7d</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">Diaria</div>
            <div class="kpi-strip-lbl">Cadencia de actualización operativa</div>
          </div>
        </div>

        <div class="chart-wrapper">
          <canvas id="chartDemo7d"></canvas>
        </div>

        <div style="font-size:11px; color:var(--text-light-faint); border-top:1px solid var(--line-light-faint); padding-top:6px; display:flex; justify-content:space-between;" class="mono">
          <span>Banda Sombreada: Cuantiles P10 y P90 calibrados en hold-out</span>
          <span style="color:#059669; font-weight:700;">Datos 100% Reales SENAMHI</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================== -->
  <!-- ACTO 4: CASO B - JAÉN (Diapos 15 - 17)     -->
  <!-- ========================================== -->

  <!-- DIAPO 15 -->
  <section class="slide" data-index="15" data-act="Acto 4 · Caso B: Jaén" data-time="1.5 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">15 / 20 · ACTO 4: CASO B (JAÉN)</span>
      <div class="badge badge-caso_real">CASO REAL</div>
      <h2 class="slide-title display">Contexto Jaén: rendimiento oficial vs telemetría</h2>
      <p class="slide-thesis">Auditamos 24 campañas oficiales SIEA/MIDAGRI (2000–2024) y contrastamos la ceguera del satélite orbital con telemetría de drones Edge-AI en CENFROCAFE.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">SIEA / MIDAGRI Oficial</span>
        <span class="metric-chip">Dron Edge-AI 14.8m</span>
        <span class="metric-chip">CENFROCAFE -5.6766°</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Serie oficial auditada (2000–2024):</strong> Control de consistencia aritmética estricta (Producción = Área × Rendimiento, Δ &lt; 0.1%).</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Telemetría Dron CENFROCAFE (Jaén):</strong> Vuelos a 14.8m de altitud con visión artificial en el borde para contar cerezas maduras (1,420) y detectar roya foliar (14.2%).</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Anticipación operativa:</strong> Estima rendimiento físico y calidad <strong>90 días antes</strong> de la cosecha real, sorteando la ceguera de nubes andinas.</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 RESOLUCIÓN ESPACIAL VS FÍSICA</span>
        <p class="insight-text">A 700 km de altitud, el satélite promedia píxeles de 250 m donde el dosel oculta el grano. A 14.8 m, el dron con Edge-AI cuantifica el fruto real bajo las ramas.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"La teledetección a 700 km ve hojas verdes; la telemetría a 14 metros cuenta granos reales."</p>
      </div>
    </div>

    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">24 Años de Rendimiento Oficial & Telemetría Dron CENFROCAFE</span>
          <span class="visual-tag mono">JAÉN -5.6766° · SIEA & NOTEBOOKLM AI</span>
        </div>

        <div class="kpi-strip">
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">24 Campañas</div>
            <div class="kpi-strip-lbl">Auditadas oficialmente SIEA (2000–2024)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">14.8 m Altitud</div>
            <div class="kpi-strip-lbl">Vuelo rasante Dron Edge-AI CENFROCAFE</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">90 Días Antes</div>
            <div class="kpi-strip-lbl">Anticipación predictiva pre-cosecha</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">-56.0% Caída</div>
            <div class="kpi-strip-lbl">Colapso por roya (2012–2014)</div>
          </div>
        </div>
        
        <div style="flex:1; display:flex; flex-direction:column; gap:8px; height:100%; min-height:0;">
          <!-- FILA SUPERIOR: INFOGRAFÍA DRON TELEMETRÍA CON HUD ACTIVO Y LIGHTBOX -->
          <div style="flex: 0 0 190px; position:relative; border-radius:10px; overflow:hidden; border:1px solid var(--line-light-faint); background:var(--bg-light-sub); display:flex;">
            <div style="flex:1; position:relative; display:flex; justify-content:center; align-items:center; background:#0B1120; overflow:hidden;">
              <img src="/docs/notebooklm/infografias/telemetria_dron_jaen_cenfrocafe.jpg" 
                   alt="Telemetría Dron Jaén CENFROCAFE" 
                   class="infographic-img"
                   style="height:100%; width:auto; max-width:100%; object-fit:contain; display:block; cursor:zoom-in;"
                   onclick="openLightbox(this.src)" />
              
              <!-- HUD OVERLAY PROCEDURAL EN VIVO -->
              <div style="position:absolute; top:8px; left:10px; background:rgba(15,23,42,0.85); color:#10B981; padding:3px 8px; border-radius:4px; font-size:10px; pointer-events:none;" class="mono hud-live">
                ● LIVE TELEMETRY · ALT: 14.8m · GPS: -5.6766° Jaén
              </div>
              <div style="position:absolute; top:8px; right:10px; background:rgba(220,38,38,0.85); color:#FFF; padding:2px 6px; border-radius:4px; font-size:9.5px; font-weight:700; pointer-events:none;" class="mono">
                90 DÍAS PRE-COSECHA 🔍 Clic para ampliar
              </div>
            </div>
            
            <!-- PANEL LATERAL TELEMETRÍA RESUMEN -->
            <div style="flex: 0 0 260px; background:var(--bg-light-sub); padding:10px 14px; display:flex; flex-direction:column; justify-content:space-between; border-left:1px solid var(--line-light-faint);">
              <div>
                <div style="font-size:10.5px; font-weight:700; color:#059669; margin-bottom:4px;" class="mono">CENFROCAFE EDGE-AI INFERENCE</div>
                <div style="font-size:11.5px; color:var(--text-light-mute); line-height:1.4;">
                  • <strong>Modelo:</strong> YOLOv8-Nano en chip a bordo.<br>
                  • <strong>[ID:104]</strong> Conteo: 1,420 cerezas maduras.<br>
                  • <strong>[ID:106]</strong> Roya: 14.2% dispersión foliar.<br>
                  • <strong>Dosel:</strong> 21.9% cobertura de sombra.
                </div>
              </div>
              <div style="font-size:10px; color:#DC2626; font-weight:600; background:rgba(220,38,38,0.06); padding:4px 8px; border-radius:4px; border:1px solid rgba(220,38,38,0.15);" class="mono">
                Supera el retraso de 16 días del satélite orbital
              </div>
            </div>
          </div>

          <!-- FILA INFERIOR: SERIE HISTÓRICA OFICIAL MIDAGRI / SIEA -->
          <div class="chart-wrapper" style="flex:1; min-height:0; position:relative; background:var(--bg-light-panel); border-radius:8px; border:1px solid var(--line-light-faint); padding:8px;">
            <canvas id="chartJaenHistorico"></canvas>
          </div>
        </div>

        <div style="font-size:10px; color:var(--text-light-faint); border-top:1px solid var(--line-light-faint); padding-top:4px; display:flex; justify-content:space-between;" class="mono">
          <span>Fuente Oficial: SIEA / MIDAGRI Compendios 2000-2024 · Dron CENFROCAFE Jaén</span>
          <span style="color:#059669; font-weight:700;">Datos 100% Auditados</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIAPO 16 -->
  <section class="slide" data-index="16" data-act="Acto 4 · Caso B: Jaén" data-time="2.5 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">16 / 20 · ACTO 4: CASO B (JAÉN)</span>
      <div class="badge badge-evidencia">EVIDENCIA</div>
      <h2 class="slide-title display">¿Ve el satélite lo que ocurrió?</h2>
      <p class="slide-thesis">La correlación entre el NDVI anual y el rendimiento de café es nula (r = 0.154, p = 0.600). En la mayor catástrofe agrícola del siglo, el satélite fue completamente ciego.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">r(NDVI, Rend) = 0.154 (p=0.60)</span>
        <span class="metric-chip">Rend: -56.0%</span>
        <span class="metric-chip">NDVI: +1.4% (Ciego)</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>La Crisis de la Roya (2012–2014):</strong> El rendimiento oficial se desplomó <strong>-56.0%</strong> (de 22.7 a 10.0 qq/ha). El NDVI MODIS subió <strong>+1.4%</strong> (0.738 a 0.748).</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Costo del error:</strong> 12.7 qq/ha perdidos en 45,000 ha equivale a <strong>S/. 228 millones</strong> sin alerta óptica.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Lo que sí funcionó:</strong> La lluvia en floración (r = 0.751, p = 0.002) explicó el 56% de la varianza.</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 PATOLOGÍA VEGETAL VS SATÉLITE</span>
        <p class="insight-text">En la crisis de la roya (2012-2014), el rendimiento cayó -56.0% mientras el NDVI subió +1.4%. El hongo afectó los granos antes de defoliar el dosel; el sensor óptico fue ciego.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE (H1 & H4)</span>
        <p class="frase-text">"Un satélite verde no garantiza cosecha: en la crisis de la roya de 2014, el rendimiento cayó 56% mientras el NDVI subió 1.4%."</p>
      </div>
    </div>

    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">Correlación Satélite vs Rendimiento & La Ceguera de la Roya</span>
          <span class="visual-tag mono">AUDITORÍA FORENSE / JAÉN</span>
        </div>

        <div class="kpi-strip">
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">r = 0.154</div>
            <div class="kpi-strip-lbl">Correlación NDVI nula (p = 0.600)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">-56.0% Rend</div>
            <div class="kpi-strip-lbl">Desplome real (22.7 &rarr; 10.0 qq/ha)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">+1.4% NDVI</div>
            <div class="kpi-strip-lbl">Ceguera óptica (0.738 &rarr; 0.748)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">r = 0.751</div>
            <div class="kpi-strip-lbl">Lluvia floración clave (p = 0.002)</div>
          </div>
        </div>

        <div style="flex:1; display:grid; grid-template-columns:1.15fr 0.85fr; gap:14px; height:100%; min-height:0;">
          <div class="chart-wrapper" style="background:var(--bg-light-sub); border-radius:8px; padding:10px; border:1px solid var(--line-light-faint);">
            <canvas id="chartScatterNdvi"></canvas>
          </div>

          <div style="background:var(--bg-light-sub); border-radius:8px; padding:16px; border:1px solid var(--line-light-faint); display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="font-size:11px; font-weight:700; color:#DC2626; margin-bottom:8px;" class="mono">LA PRUEBA FORENSE (CRISIS ROYA 2012–2014)</div>
              <div style="display:flex; flex-direction:column; gap:10px;">
                <div style="border-left:3px solid #DC2626; padding-left:10px;">
                  <span style="font-size:10px; color:var(--text-light-faint);" class="mono">RENDIMIENTO REAL (SIEA)</span>
                  <div style="font-size:16px; font-weight:700; color:#DC2626;">22.7 &rarr; 10.0 qq/ha (-56.0%)</div>
                </div>
                <div style="border-left:3px solid #059669; padding-left:10px;">
                  <span style="font-size:10px; color:var(--text-light-faint);" class="mono">SATÉLITE MODIS NDVI ANUAL</span>
                  <div style="font-size:16px; font-weight:700; color:#059669;">0.7380 &rarr; 0.7483 (+1.4%)</div>
                </div>
                <div style="border-left:3px solid #2563EB; padding-left:10px;">
                  <span style="font-size:10px; color:var(--text-light-faint);" class="mono">LLUVIA EN FLORACIÓN (ERA5)</span>
                  <div style="font-size:16px; font-weight:700; color:#2563EB;">Déficit hídrico crítico (r = 0.751)</div>
                </div>
              </div>
            </div>

            <div style="background:#FEF2F2; border-radius:6px; padding:10px; border:1px solid #FECACA; font-size:11px; color:#991B1B; line-height:1.4;">
              <strong>Diagnóstico biológico:</strong> El hongo <em>Hemileia vastatrix</em> destruye el grano antes de tirar las hojas del dosel; el satélite óptico vio a Jaén totalmente verde mientras la cosecha se perdía.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- DIAPO 17 -->
  <section class="slide" data-index="17" data-act="Acto 4 · Caso B: Jaén" data-time="2.5 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">17 / 20 · ACTO 4: CASO B (JAÉN)</span>
      <div class="badge badge-demo">DEMO</div>
      <h2 class="slide-title display">DEMO 2: Validación honesta</h2>
      <p class="slide-thesis">Sin trampas de validación: evaluar año a año entrenando únicamente con campañas del pasado expone la fragilidad de modelos satelitales puros.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">Fusión: MAE 4.51</span>
        <span class="metric-chip">Clima: MAE 4.60</span>
        <span class="metric-chip">Satélite: MAE 5.32 (Peor)</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Ventana expansiva (Walk-Forward):</strong> Campaña inicial 2000–2014; evaluación ciega en 2015–2024.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Solo Satélite empeora el error:</strong> Modelo Tendencia (MAE 4.79 qq/ha) vs Solo NDVI (MAE <strong>5.32 qq/ha</strong>). Meter satélite saturado degrada la predicción.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Fusión Multimodal gana:</strong> Clima de floración + Tendencia reduce el MAE a <strong>4.51 qq/ha</strong>.</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 VALIDACIÓN EXPANSIVA HONESTA</span>
        <p class="insight-text">El protocolo Walk-Forward entrena año a año sin ver el futuro: la combinación de variables fenológicas con tendencia redujo el MAE a 4.51 qq/ha frente a 5.32 de satélite solo.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE (H3)</span>
        <p class="frase-text">"Un modelo honesto muestra dónde falla: la validación temporal sin trampas revela que ningún algoritmo anticipa una plaga sin datos de campo."</p>
      </div>
    </div>

    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">DEMO INTERACTIVA: Validación Walk-Forward en Jaén (2015–2024)</span>
          <span class="visual-tag mono">MUESTRA EXPANSIVA REAL</span>
        </div>

        <div class="kpi-strip">
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">4.51 qq/ha</div>
            <div class="kpi-strip-lbl">Fusión Multimodal MAE (Ganador)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">4.60 qq/ha</div>
            <div class="kpi-strip-lbl">Solo Clima Floración MAE</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">4.79 qq/ha</div>
            <div class="kpi-strip-lbl">Tendencia Histórica Pura MAE</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">5.32 qq/ha</div>
            <div class="kpi-strip-lbl">Solo Satélite NDVI MAE (Peor modelo)</div>
          </div>
        </div>

        <div class="chart-wrapper">
          <canvas id="chartDemoJaen"></canvas>
        </div>

        <div style="font-size:11px; color:var(--text-light-faint); border-top:1px solid var(--line-light-faint); padding-top:6px; display:flex; justify-content:space-between;" class="mono">
          <span>Tendencia: MAE 4.79 · Solo Satélite: MAE 5.32 · Solo Clima: MAE 4.60 · Fusión: MAE 4.51</span>
          <span style="color:#059669; font-weight:700;">Evaluación estricta sin fuga de futuro</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================== -->
  <!-- ACTO 5: DECIDIR (Diapos 18 - 20)           -->
  <!-- ========================================== -->

  <!-- DIAPO 18 -->
  <section class="slide" data-index="18" data-act="Acto 5 · Decidir" data-time="2.0 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">18 / 20 · ACTO 5: DECIDIR</span>
      <div class="badge badge-teoria">TEORÍA</div>
      <h2 class="slide-title display">5 lecciones innegociables</h2>
      <p class="slide-thesis">Principios metodológicos destilados de 2,557 días de meteorología amazónica y 24 campañas cafetaleras reales auditadas.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">1. Causalidad</span>
        <span class="metric-chip">2. Parsimonia</span>
        <span class="metric-chip">3. Incertidumbre</span>
        <span class="metric-chip">4. Física</span>
        <span class="metric-chip">5. Escala</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>1. Respeta el tiempo:</strong> Jamás uses k-fold aleatorio; rompe la causalidad temporal y genera sobreajuste espurio.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>2. Parsimonia primero:</strong> ExtraTrees y ARIMA empataron con modelos de 200M parámetros a 0.11s de CPU.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>3. Bandas obligatorias:</strong> Reportar un punto esconde el riesgo operativo real ante eventos extremos.</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 CONCLUSIÓN CIENTÍFICA</span>
        <p class="insight-text">Ninguna arquitectura moderna compensa la falta de rigor metodológico. La parsimonia matemática y la comprensión de los mecanismos físicos dominan sobre la complejidad bruta.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"El rigor metodológico vale más que cualquier arquitectura neuronal."</p>
      </div>
    </div>

    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">Los 5 Mandamientos del Forecasting en el Mundo Real</span>
          <span class="visual-tag mono">SÍNTESIS EMPÍRICA / RIGOR CIENTÍFICO</span>
        </div>

        <div style="flex:1; display:grid; grid-template-rows:repeat(5, 1fr); gap:10px; height:100%; min-height:0;">
          <!-- LECCIÓN 1 -->
          <div style="background:var(--bg-light-sub); padding:10px 16px; border-radius:10px; border-left:5px solid #2563EB; border-top:1px solid var(--line-light-faint); border-right:1px solid var(--line-light-faint); border-bottom:1px solid var(--line-light-faint); display:flex; align-items:center; gap:16px;">
            <div style="font-size:26px; font-weight:700; color:#2563EB; min-width:36px; text-align:center;" class="mono">01</div>
            <div style="flex:1;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
                <span style="font-weight:700; font-size:13.5px; color:var(--text-light-main);">Respeta la Causalidad del Tiempo</span>
                <span style="background:rgba(37,99,235,0.1); color:#2563EB; font-size:9.5px; padding:2px 8px; border-radius:4px; font-weight:700;" class="mono">VALIDACIÓN TEMPORAL</span>
              </div>
              <div style="font-size:12px; color:var(--text-light-mute); line-height:1.35;">Nunca uses validación cruzada aleatoria. Entrena siempre en el pasado y evalúa en el futuro mediante ventanas rodantes o Walk-Forward estricto para evitar fuga de información.</div>
            </div>
          </div>

          <!-- LECCIÓN 2 -->
          <div style="background:var(--bg-light-sub); padding:10px 16px; border-radius:10px; border-left:5px solid #059669; border-top:1px solid var(--line-light-faint); border-right:1px solid var(--line-light-faint); border-bottom:1px solid var(--line-light-faint); display:flex; align-items:center; gap:16px;">
            <div style="font-size:26px; font-weight:700; color:#059669; min-width:36px; text-align:center;" class="mono">02</div>
            <div style="flex:1;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
                <span style="font-weight:700; font-size:13.5px; color:var(--text-light-main);">La Navaja de Ockham como Baseline Obligatorio</span>
                <span style="background:rgba(5,150,105,0.1); color:#059669; font-size:9.5px; padding:2px 8px; border-radius:4px; font-weight:700;" class="mono">PARSIMONIA</span>
              </div>
              <div style="font-size:12px; color:var(--text-light-mute); line-height:1.35;">Comienza siempre con modelos simples. En Punchana, ExtraTrees (0.11s) superó a LSTM recurrente y empató con redes de 200M parámetros consumiendo 70 veces menos recursos.</div>
            </div>
          </div>

          <!-- LECCIÓN 3 -->
          <div style="background:var(--bg-light-sub); padding:10px 16px; border-radius:10px; border-left:5px solid #D97706; border-top:1px solid var(--line-light-faint); border-right:1px solid var(--line-light-faint); border-bottom:1px solid var(--line-light-faint); display:flex; align-items:center; gap:16px;">
            <div style="font-size:26px; font-weight:700; color:#D97706; min-width:36px; text-align:center;" class="mono">03</div>
            <div style="flex:1;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
                <span style="font-weight:700; font-size:13.5px; color:var(--text-light-main);">El Valor Está en la Banda, No en el Punto</span>
                <span style="background:rgba(217,119,6,0.1); color:#D97706; font-size:9.5px; padding:2px 8px; border-radius:4px; font-weight:700;" class="mono">INCERTIDUMBRE P10–P90</span>
              </div>
              <div style="font-size:12px; color:var(--text-light-mute); line-height:1.35;">Un pronóstico puntual es una ficción matemática que oculta el riesgo operativo. Comunica siempre conos de incertidumbre calibrados con cuantiles empíricos para la toma de decisiones.</div>
            </div>
          </div>

          <!-- LECCIÓN 4 -->
          <div style="background:var(--bg-light-sub); padding:10px 16px; border-radius:10px; border-left:5px solid #DC2626; border-top:1px solid var(--line-light-faint); border-right:1px solid var(--line-light-faint); border-bottom:1px solid var(--line-light-faint); display:flex; align-items:center; gap:16px;">
            <div style="font-size:26px; font-weight:700; color:#DC2626; min-width:36px; text-align:center;" class="mono">04</div>
            <div style="flex:1;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
                <span style="font-weight:700; font-size:13.5px; color:var(--text-light-main);">La Física Manda Antes que el Algoritmo</span>
                <span style="background:rgba(220,38,38,0.1); color:#DC2626; font-size:9.5px; padding:2px 8px; border-radius:4px; font-weight:700;" class="mono">MECANISMO CAUSAL</span>
              </div>
              <div style="font-size:12px; color:var(--text-light-mute); line-height:1.35;">El sensor óptico satura en copas densas y fue ciego a la roya (-56%); el déficit hídrico en floración explicó el 56% de la varianza biológica real. Entiende el dominio antes de modelar.</div>
            </div>
          </div>

          <!-- LECCIÓN 5 -->
          <div style="background:var(--bg-light-sub); padding:10px 16px; border-radius:10px; border-left:5px solid #7C3AED; border-top:1px solid var(--line-light-faint); border-right:1px solid var(--line-light-faint); border-bottom:1px solid var(--line-light-faint); display:flex; align-items:center; gap:16px;">
            <div style="font-size:26px; font-weight:700; color:#7C3AED; min-width:36px; text-align:center;" class="mono">05</div>
            <div style="flex:1;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
                <span style="font-weight:700; font-size:13.5px; color:var(--text-light-main);">Complejidad Justificada Únicamente por la Escala</span>
                <span style="background:rgba(124,58,237,0.1); color:#7C3AED; font-size:9.5px; padding:2px 8px; border-radius:4px; font-weight:700;" class="mono">ESCALABILIDAD</span>
              </div>
              <div style="font-size:12px; color:var(--text-light-mute); line-height:1.35;">Los Foundation Models Zero-Shot brillan al predecir catálogos de miles de series heterogéneas sin reentrenar, pero no justifican su peso en un sensor físico aislado donde la parsimonia domina.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- DIAPO 19 -->
  <section class="slide" data-index="19" data-act="Acto 5 · Decidir" data-time="2.0 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">19 / 20 · ACTO 5: DECIDIR</span>
      <div class="badge badge-teoria">TEORÍA</div>
      <h2 class="slide-title display">¿Qué modelo uso? Árbol de decisión</h2>
      <p class="slide-thesis">Una guía práctica y algorítmica para elegir la herramienta correcta según el volumen de datos, las covariables y el objetivo operativo.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">1 Serie: ARIMA/ETS</span>
        <span class="metric-chip">Extrapolación: Δy</span>
        <span class="metric-chip">N Series: TimesFM</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>1 serie corta (&lt;3000 pts):</strong> ETS, ARIMA o ExtraTrees con rezagos temporales.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Récords térmicos / tendencia:</strong> Modela primeras diferencias (Δy), jamás niveles directos en árboles.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Miles de series sin reentreno:</strong> Foundation Model Zero-Shot (TimesFM / Chronos).</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 MATRIZ DE DECISIÓN</span>
        <p class="insight-text">Elige la herramienta según la escala del sistema: parsimonia local para series individuales; modelos en diferencias para tendencias; modelos de frontera para catálogos masivos.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE-CLAVE</span>
        <p class="frase-text">"La complejidad se gana con evidencia, no se asume por defecto."</p>
      </div>
    </div>

    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">Árbol de Decisión Metodológico</span>
          <span class="visual-tag mono">FLUJO OPERATIVO / ARQUITECTURA</span>
        </div>

        <div class="kpi-strip">
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">1 Serie Local</div>
            <div class="kpi-strip-lbl">ETS / ARIMA / ExtraTrees</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">Récord / Tendencia</div>
            <div class="kpi-strip-lbl">Modelar diferencias (Δy)</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">Covariables Físicas</div>
            <div class="kpi-strip-lbl">Fusión Tabular con filtro causal</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">Miles de Series</div>
            <div class="kpi-strip-lbl">Foundation Models Zero-Shot</div>
          </div>
        </div>

        <div style="flex:1; display:grid; grid-template-rows:repeat(4, 1fr); gap:12px; height:100%; min-height:0;">
          <!-- RAMA 1 -->
          <div style="background:var(--bg-light-sub); padding:14px 20px; border-radius:10px; border-left:5px solid #059669; border-top:1px solid var(--line-light-faint); border-right:1px solid var(--line-light-faint); border-bottom:1px solid var(--line-light-faint); display:flex; justify-content:space-between; align-items:center;">
            <div style="flex:1; padding-right:16px;">
              <div style="font-weight:700; font-size:14px; color:var(--text-light-main);">¿Tienes 1 sola serie local y corta (&lt; 3,000 registros)?</div>
              <div style="font-size:12px; color:var(--text-light-mute); margin-top:3px;">Prioriza parsimonia, velocidad extrema en CPU (&lt;0.2s), interpretabilidad e intervalos estadísticos asintóticos directos.</div>
            </div>
            <div style="background:rgba(5,150,105,0.12); color:#059669; padding:8px 14px; border-radius:6px; font-weight:700; font-size:13px; text-align:right; white-space:nowrap;" class="mono">
              &rarr; ETS / ARIMA / ExtraTrees
            </div>
          </div>

          <!-- RAMA 2 -->
          <div style="background:var(--bg-light-sub); padding:14px 20px; border-radius:10px; border-left:5px solid #DC2626; border-top:1px solid var(--line-light-faint); border-right:1px solid var(--line-light-faint); border-bottom:1px solid var(--line-light-faint); display:flex; justify-content:space-between; align-items:center;">
            <div style="flex:1; padding-right:16px;">
              <div style="font-weight:700; font-size:14px; color:var(--text-light-main);">¿Existe riesgo de eventos récord fuera del rango histórico visto?</div>
              <div style="font-size:12px; color:var(--text-light-mute); margin-top:3px;">Los árboles de decisión colapsan en mesetas constantes si el valor supera sus hojas de entrenamiento. Nunca entrenes en niveles.</div>
            </div>
            <div style="background:rgba(220,38,38,0.12); color:#DC2626; padding:8px 14px; border-radius:6px; font-weight:700; font-size:13px; text-align:right; white-space:nowrap;" class="mono">
              &rarr; Modela diferencias (Δy)
            </div>
          </div>

          <!-- RAMA 3 -->
          <div style="background:var(--bg-light-sub); padding:14px 20px; border-radius:10px; border-left:5px solid #2563EB; border-top:1px solid var(--line-light-faint); border-right:1px solid var(--line-light-faint); border-bottom:1px solid var(--line-light-faint); display:flex; justify-content:space-between; align-items:center;">
            <div style="flex:1; padding-right:16px;">
              <div style="font-weight:700; font-size:14px; color:var(--text-light-main);">¿Cuentas con covariables físicas, fenológicas o satelitales?</div>
              <div style="font-size:12px; color:var(--text-light-mute); margin-top:3px;">Verifica la correlación real y causalidad biológica antes de incluirlas; el satélite óptico saturado empeora el error de predicción.</div>
            </div>
            <div style="background:rgba(37,99,235,0.12); color:#2563EB; padding:8px 14px; border-radius:6px; font-weight:700; font-size:13px; text-align:right; white-space:nowrap;" class="mono">
              &rarr; Fusión Tabular (Filtro Físico)
            </div>
          </div>

          <!-- RAMA 4 -->
          <div style="background:var(--bg-light-sub); padding:14px 20px; border-radius:10px; border-left:5px solid #7C3AED; border-top:1px solid var(--line-light-faint); border-right:1px solid var(--line-light-faint); border-bottom:1px solid var(--line-light-faint); display:flex; justify-content:space-between; align-items:center;">
            <div style="flex:1; padding-right:16px;">
              <div style="font-weight:700; font-size:14px; color:var(--text-light-main);">¿Tienes miles de series heterogéneas sin tiempo ni GPU para reentrenar?</div>
              <div style="font-size:12px; color:var(--text-light-mute); margin-top:3px;">Aprovecha el conocimiento previo global encapsulado en modelos pre-entrenados masivos con inferencia zero-shot inmediata.</div>
            </div>
            <div style="background:rgba(124,58,237,0.12); color:#7C3AED; padding:8px 14px; border-radius:6px; font-weight:700; font-size:13px; text-align:right; white-space:nowrap;" class="mono">
              &rarr; Foundation Zero-Shot (TimesFM)
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- DIAPO 20 -->
  <section class="slide" data-index="20" data-act="Acto 5 · Decidir" data-time="1.0 min">
    <div class="panel-narrative">
      <span class="slide-meta mono">20 / 20 · ACTO 5: DECIDIR</span>
      <div class="badge badge-teoria">TEORÍA</div>
      <h2 class="slide-title display">Cierre y recursos abiertos</h2>
      <p class="slide-thesis">Volvemos al cono inicial: la inteligencia artificial no elimina la incertidumbre del mundo, pero nos ofrece la disciplina matemática para decidir mejor.</p>
      
      <div class="metric-chips">
        <span class="metric-chip">49 Referencias</span>
        <span class="metric-chip">2 Notebooks</span>
        <span class="metric-chip">Código Abierto</span>
      </div>

      <ul class="bullets-list">
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Código y datos 100% abiertos:</strong> Repositorio completo con cuadernos reproducibles paso a paso.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>49 Citas Académicas:</strong> Respaldadas por papers en Nature, Science, ICML y reportes oficiales del INEI/MIDAGRI.</div>
        </li>
        <li class="bullet-item">
          <span class="bullet-icon"></span>
          <div><strong>Notebooks interactivos:</strong> Clima SENAMHI y Teledetección de Café disponibles para experimentación inmediata en Google Colab.</div>
        </li>
      </ul>

      <div class="card-insight">
        <span class="insight-label">💡 CIENCIA ABIERTA & REPRODUCIBLE</span>
        <p class="insight-text">Cuadernos interactivos en Google Colab con código documentado, compendios oficiales auditados y datasets limpios disponibles bajo licencia MIT para la comunidad académica.</p>
      </div>

      <div class="card-frase-clave">
        <span class="frase-label">FRASE FINAL</span>
        <p class="frase-text">"¿Puede la IA predecir el futuro? No. Puede ayudarnos a decidir mejor sin conocerlo."</p>
      </div>
    </div>

    <div class="panel-visual">
      <div class="visual-card">
        <div class="visual-header">
          <span class="visual-title display">Repositorio Abierto & Ecosistema de Investigación</span>
          <span class="visual-tag mono">ACCESO PÚBLICO / MIT LICENSE</span>
        </div>

        <div class="kpi-strip">
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">49 Citas</div>
            <div class="kpi-strip-lbl">Nature, Science, ICML, NeurIPS</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">2 Notebooks</div>
            <div class="kpi-strip-lbl">Google Colab interactivos listos</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">2,557 Días + 24a</div>
            <div class="kpi-strip-lbl">SENAMHI Punchana + SIEA Jaén</div>
          </div>
          <div class="kpi-strip-item">
            <div class="kpi-strip-val">100% Abierto</div>
            <div class="kpi-strip-lbl">Código, datasets y visualizaciones MIT</div>
          </div>
        </div>

        <div style="flex:1; display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; gap:14px; height:100%; min-height:0;">
          <!-- Tarjeta 1: QR Real Dinámico y Repositorio -->
          <div style="background:var(--bg-light-sub); padding:14px 18px; border-radius:10px; border-left:5px solid #12C8FC; border-top:1px solid var(--line-light-faint); border-right:1px solid var(--line-light-faint); border-bottom:1px solid var(--line-light-faint); display:flex; align-items:center; gap:16px;">
            <div style="width:82px; height:82px; flex-shrink:0; background:white; padding:4px; border-radius:8px; box-shadow:0 3px 8px rgba(0,0,0,0.12); display:flex; align-items:center; justify-content:center;">
              {qr_svg}
            </div>
            <div>
              <div style="font-size:10.5px; font-weight:700; color:#12C8FC;" class="mono">ACCESO INMEDIATO AL DECK & REPO</div>
              <div style="font-size:13.5px; font-weight:700; margin:2px 0; color:var(--text-light-main);"><a href="https://alexprietoromani.github.io/charla_forecasting/" target="_blank" style="color:inherit; text-decoration:none;">alexprietoromani.github.io/charla_forecasting</a></div>
              <div style="font-size:11.5px; color:var(--text-light-mute); line-height:1.4;">
                • Escanea el código para seguir el deck en vivo<br>
                • GitHub: <a href="https://github.com/AlexPrietoRomani/charla_forecasting" target="_blank" style="color:#1E7BFF;">AlexPrietoRomani/charla_forecasting</a>
              </div>
            </div>
          </div>

          <!-- Tarjeta 2: Ponente & Contacto Oficial Data Fest -->
          <div style="background:var(--bg-light-sub); padding:14px 18px; border-radius:10px; border-left:5px solid #1E7BFF; border-top:1px solid var(--line-light-faint); border-right:1px solid var(--line-light-faint); border-bottom:1px solid var(--line-light-faint); display:flex; flex-direction:column; justify-content:center;">
            <div style="font-size:10.5px; font-weight:700; color:#1E7BFF;" class="mono">PONENTE · CONTACTO DIRECTO</div>
            <div style="font-size:14px; font-weight:700; margin:2px 0; color:var(--text-light-main);">Alex Prieto Romani</div>
            <div style="font-size:11.5px; color:var(--text-light-mute); line-height:1.45;">
              ✉️ <a href="mailto:alexprieto1997@gmail.com" style="color:inherit; text-decoration:none;">alexprieto1997@gmail.com</a><br>
              🔗 <a href="https://linkedin.com/in/tu-usuario" target="_blank" style="color:inherit; text-decoration:none;">linkedin.com/in/alex-prieto-romani</a><br>
              🐙 <a href="https://github.com/AlexPrietoRomani" target="_blank" style="color:inherit; text-decoration:none;">github.com/AlexPrietoRomani</a>
            </div>
          </div>

          <!-- Tarjeta 3: Datos 100% Reales y Metodología -->
          <div style="background:var(--bg-light-sub); padding:14px 18px; border-radius:10px; border-left:5px solid #2EE6A6; border-top:1px solid var(--line-light-faint); border-right:1px solid var(--line-light-faint); border-bottom:1px solid var(--line-light-faint); display:flex; flex-direction:column; justify-content:center;">
            <div style="font-size:10.5px; font-weight:700; color:#2EE6A6;" class="mono">EVIDENCIA & CIENCIA REPRODUCIBLE</div>
            <div style="font-size:13.5px; font-weight:700; margin:2px 0; color:var(--text-light-main);">SENAMHI · MIDAGRI · NASA MODIS</div>
            <p style="font-size:11.5px; color:var(--text-light-mute); line-height:1.4;">2,557 días Punchana (Iquitos) + 24 campañas auditadas Jaén. Cero datos sintéticos; modelos evaluados bajo holdout ciego y Diebold-Mariano.</p>
          </div>

          <!-- Tarjeta 4: En Colaboración Con Data Wizard -->
          <div style="background:var(--bg-light-sub); padding:14px 18px; border-radius:10px; border-left:5px solid #9B5CFF; border-top:1px solid var(--line-light-faint); border-right:1px solid var(--line-light-faint); border-bottom:1px solid var(--line-light-faint); display:flex; align-items:center; justify-content:space-between; gap:12px;">
            <div style="flex:1;">
              <div style="font-size:10.5px; font-weight:700; color:#9B5CFF;" class="mono">¡GRACIAS! · PREGUNTAS Y DEBATE</div>
              <div style="font-size:14px; font-weight:700; margin:2px 0; color:var(--text-light-main);">Iquitos Data Fest 2026</div>
              <p style="font-size:11.5px; color:var(--text-light-mute); line-height:1.35;">Aula Magna UNAP · 30 de octubre. Abierto el espacio para discusión metodológica.</p>
            </div>
            <img src="data:image/png;base64,{b64_dw}" alt="En colaboración con Data Wizard" style="height:38px; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.15);">
          </div>
        </div>
      </div>
    </div>
  </section>
"""
