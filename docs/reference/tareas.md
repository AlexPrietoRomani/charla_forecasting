# Tablero de Tareas — Charla Forecasting & IA (v2 Real-Data)

> **Estado General:** `[X] F1–F9 Completadas al 100% · Proyecto Verificado y Compilado`  
> **Convenciones:** `[ ]` pendiente · `[/]` en progreso · `[X]` completado y verificado.  
> **Documento Rector:** [`docs/plan/plan_maestro.md`](../plan/plan_maestro.md)  
> **Detalle por Fases:** [`docs/task/fases/`](fases/)

---

## F1: Depuración de Material Sintético, Trazabilidad y Setup
*Detalle completo en:* [`docs/reference/fases/fase_1_depuracion_setup.md`](fases/fase_1_depuracion_setup.md)

- [X] **SF1.1 Aislamiento de Datos Sintéticos**
  - [X] T1.1.1 Crear `data/deprecated/` y mover `data/cafe_ndvi_rendimiento.csv` como `cafe_ndvi_rendimiento_SINTETICO.csv`.
  - [X] T1.1.2 Crear `data/deprecated/README.md` documentando la procedencia sintética y su descarte.
  - [X] T1.1.3 Desactivar `scripts/build_agro_dataset.py` para evitar sobreescrituras accidentales.
- [X] **SF1.2 Registro de Trazabilidad (`data/SOURCES.md`)**
  - [X] T1.2.1 Crear `data/SOURCES.md` con plantilla de metadatos (URL, fecha, hash SHA-256).
  - [X] T1.2.2 Registrar datos reales existentes: SENAMHI Punchana (`garua`) y Open-Meteo.
- [X] **SF1.3 Setup de Dependencias de Modelado**
  - [X] T1.3.1 Verificar entorno PyTorch y librerías estadísticas/ML.
  - [X] T1.3.2 Instalar y verificar `chronos-forecasting`.
  - [X] T1.3.3 Instalar y verificar `timesfm`.

---

## F2: Caso B — Reconstrucción con Datos Reales de Café (Jaén)
*Detalle completo en:* [`docs/reference/fases/fase_2_cafe_datos_reales.md`](fases/fase_2_cafe_datos_reales.md)

- [X] **SF2.1 Rendimiento Oficial SIEA / MIDAGRI**
  - [X] T2.1.1 Localizar compendios y anuarios estadísticos agrícolas de Jaén (meta: 2000–2024).
  - [X] T2.1.2 Extraer serie a `data/raw/cafe_real/midagri_jaen_rendimiento.csv`.
  - [X] T2.1.3 Control aritmético de coherencia: `produccion * 1000 / superficie ≈ rendimiento` (tolerancia < 2%).
  - [X] T2.1.4 Registrar definición de año agrícola/calendario en `data/SOURCES.md`.
- [X] **SF2.2 Extracción de Índices Satelitales Reales (Planetary Computer)**
  - [X] T2.2.1 Descargar polígono oficial de Jaén en `data/raw/cafe_real/jaen_limite.geojson`.
  - [X] T2.2.2 Definir máscara cafetalera con fuente citada (WorldCover + altitud cafetalera).
  - [X] T2.2.3 Extraer serie MODIS MOD13Q1 (2000–2024) con filtro QA y mediana espacial.
  - [X] T2.2.4 Extraer serie Sentinel-2 L2A (2017–2024) para comparación NDRE / NDVI.
  - [X] T2.2.5 Generar reporte de calidad de nubosidad (`n_obs_validas` mensual).
- [X] **SF2.3 Agregación Fenológica y Clima Real**
  - [X] T2.3.1 Descargar clima ERA5 Open-Meteo para el centroide cafetalero (2000–2024).
  - [X] T2.3.2 Alinear ventanas fenológicas de Jaén (Floración, Llenado, Cosecha).
  - [X] T2.3.3 Crear `scripts/caso_2/build_cafe_real.py` (determinista, sin `np.random`) y compilar `data/caso_2/cafe_jaen_campanias.csv`.
- [X] **SF2.4 Evaluación de Hipótesis y Modelado con Ventana Expansiva**
  - [X] T2.4.1 Evaluar H1: Correlación empírica `ndvi_anual` vs `anomalia_rendimiento`.
  - [X] T2.4.2 Evaluar H2: Correlación de clima de floración vs NDVI.
  - [X] T2.4.3 Evaluar H3: Comparación de MAE en ventana expansiva (Tendencia vs NDVI vs Clima vs Fusión).
  - [X] T2.4.4 Evaluar H4: Firma espectral del impacto de la roya amarilla (2012–2014).
  - [X] T2.4.5 Exportar `data/caso_2/cafe_jaen_hipotesis.json` y actualizar `notebooks/02_cafe_ndvi.ipynb`.

---

## F3: Caso A — Benchmark de 8 Modelos en Iquitos con Foundation Models
*Detalle completo en:* [`docs/reference/fases/fase_3_benchmark_iquitos_fm.md`](fases/fase_3_benchmark_iquitos_fm.md)

- [X] **SF3.1 Preparación y Holdout Estricto**
  - [X] T3.1.1 Cargar `data/caso_1/senamhi_diario.csv` (2019–2025, 2,557 días).
  - [X] T3.1.2 Fijar split temporal estricto: Entrenamiento = 2,467 días; Holdout ciego = 90 días finales.
  - [X] T3.1.3 Construir matriz de rezagos 1–14 sin filtración futura.
- [X] **SF3.2 Ejecución de los 8 Modelos de Pronóstico**
  - [X] T3.2.1 Modelo 0: Naive estacional (baseline cero costo).
  - [X] T3.2.2 Modelo 1: ARIMA / SARIMAX calibrado por AIC.
  - [X] T3.2.3 Modelo 2: Holt-Winters con decaimiento amortiguado.
  - [X] T3.2.4 Modelo 3: Random Forest tabular con lags.
  - [X] T3.2.5 Modelo 4: ExtraTrees / LightGBM con lags y rolling mean.
  - [X] T3.2.6 Modelo 5: LSTM profunda PyTorch (promedio 5 semillas $\mu \pm \sigma$).
  - [X] T3.2.7 Modelo 6: Chronos-Bolt (Amazon) Zero-Shot (cuantiles P10/P50/P90).
  - [X] T3.2.8 Modelo 7: TimesFM (Google) Zero-Shot (patches 128).
- [X] **SF3.3 Auditoría Estadística y Exportación**
  - [X] T3.3.1 Calcular RMSE y MAE para horizontes 1d y 7d.
  - [X] T3.3.2 Prueba formal de Diebold-Mariano vs el mejor modelo (detectar empates).
  - [X] T3.3.3 Aplicar regla de parsimonia para declarar al ganador operativo.
  - [X] T3.3.4 Exportar `data/caso_1/benchmark_punchana.csv` y `data/caso_1/senamhi_forecast_7d.csv`.
  - [X] T3.3.5 Reejecutar `notebooks/01_clima_senamhi.ipynb` con celdas ejecutadas y limpias.

---

## F4: Experimentos de Respaldo, Citas y Consolidación Narrativa
*Detalle completo en:* [`docs/reference/fases/fase_4_experimentos_narrativa.md`](fases/fase_4_experimentos_narrativa.md)

- [X] **SF4.1 Experimento Propio de No-Extrapolación (Diapositiva 05)**
  - [X] T4.1.1 Configurar experimento con datos de Punchana restringidos en $T \le 34.0\,^{\circ}\text{C}$.
  - [X] T4.1.2 Demostrar la meseta plana del árbol vs la extrapolación del modelo diferenciado ($\Delta y$).
  - [X] T4.1.3 Exportar `data/caso_1/experimento_extrapolacion.csv` rotulado `EXPERIMENTO PROPIO`.
- [X] **SF4.2 Verificación Cruzada de Fuentes**
  - [X] T4.2.1 Verificar citas fenológicas y temperaturas de aborto en café.
  - [X] T4.2.2 Verificar datos de supercómputo y asimilación 4D-Var en ECMWF IFS.
  - [X] T4.2.3 Calcular discrepancia media empírica NOAA vs ECMWF en Iquitos.
- [X] **SF4.3 Redacción Definitiva de Frases-clave (⏳)**
  - [X] T4.3.1 Redactar Frase-clave Diapo 08 (siembra de saturación según H1).
  - [X] T4.3.2 Redactar Frase-clave Diapo 13 (ganador real del benchmark de Iquitos).
  - [X] T4.3.3 Redactar Frase-clave Diapo 16 (campaña crítica real en Jaén).
  - [X] T4.3.4 Redactar Frase-clave Diapo 17 (validación expansiva con fallos reales).
  - [X] T4.3.5 Consolidar 5 lecciones (Diapo 18) y árbol de decisión (Diapo 19) con los datos.
  - [X] T4.3.6 **Revisión y visto bueno del usuario sobre las frases antes de codificar la interfaz.**

---

## F5: Refactorización de la Presentación Interactiva (20 Diapositivas)
*Detalle completo en:* [`docs/reference/fases/fase_5_deck_20_slides.md`](fases/fase_5_deck_20_slides.md)

- [X] **SF5.1 Layout 40/60 Split-Screen y 5 Insignias Fijas**
  - [X] T5.1.1 Estructurar exactamente 20 diapositivas en `scripts/build_deck.py`.
  - [X] T5.1.2 Implementar layout 40% izquierda (tesis + viñetas + frase-clave) / 60% derecha (visual interactivo).
  - [X] T5.1.3 Aplicar las 5 insignias normalizadas: `TEORÍA`, `MECANISMO`, `EVIDENCIA`, `CASO REAL`, `DEMO`.
- [X] **SF5.2 Drawer de Notas del Ponente (`N`) y Glosario**
  - [X] T5.2.1 Crear drawer de Speaker Notes con tecla `N` y temporizador.
  - [X] T5.2.2 Implementar tooltips de glosario emergente para estadística básica.
- [X] **SF5.3 Animaciones Cíclicas y Accesibilidad**
  - [X] T5.3.1 Programar animaciones continuas suaves (@keyframes) con significado físico.
  - [X] T5.3.2 Controlar intensidad (loops dinámicos solo en diapos clave, lentos en el resto).
  - [X] T5.3.3 Soportar `prefers-reduced-motion`.
- [X] **SF5.4 Demos Conectadas a CSVs Reales**
  - [X] T5.4.1 Demo 1 (Diapo 14): Conectar Chart.js a `data/caso_1/senamhi_forecast_7d.csv`.
  - [X] T5.4.2 Demo 2 (Diapo 17): Conectar Chart.js a `data/caso_2/cafe_jaen_campanias.csv` y validación expansiva.
  - [X] T5.4.3 Verificar que ninguna cifra esté cableada a mano en el HTML.

---

## F6: QA Visual, Auditoría Multi-Resolución, Ensayo y Bitácora
*Detalle completo en:* [`docs/reference/fases/fase_6_qa_ensayo.md`](fases/fase_6_qa_ensayo.md)

- [X] **SF6.1 Auditoría Visual y de Responsividad**
  - [X] T6.1.1 Probar en resolución 1920×1080 (cero desborde vertical).
  - [X] T6.1.2 Probar en resolución 1366×768 (laptop estándar de auditorio).
  - [X] T6.1.3 Verificar contraste WCAG en temas claro y oscuro.
  - [X] T6.1.4 Probar navegación completa por teclado (`←`, `→`, `F`, `Home`, `End`, `N`, `D`).
- [X] **SF6.2 Ensayo Cronometrado del Ponente**
  - [X] T6.2.1 Ensayo completo de 5 actos ajustado a ventana de 30 a 40 minutos (~35 min).
  - [X] T6.2.2 Calibrar extensión de notas si alguna diapositiva supera los 2 minutos.
- [X] **SF6.3 Bitácora y Ecosistema de Investigación**
  - [X] T6.3.1 Registrar entrada forense en `docs/logs/log.md` sobre el reemplazo de datos sintéticos.
  - [X] T6.3.2 Actualizar `docs/presentacion_slides_texto.md` con las 20 diapositivas finales.
  - [X] T6.3.3 Sincronizar fuentes en NotebookLM.

---

## F7: Rediseño Visual (Front-Design) — Márgenes, Densidad y Cero Espacios Vacíos
*Detalle completo en:* [`docs/reference/fases/fase_7_rediseno_visual.md`](fases/fase_7_rediseno_visual.md)
> **Estado:** `[X]` completada — Verificado con Playwright en `scripts/audit_layout.py` (0 vacíos >31px, 0 errores de consola).

- [X] **SF7.1 Marco global y sistema de espaciado**
  - [X] T7.1.1 Tokens CSS (padding, gaps, escala tipográfica `clamp()`).
  - [X] T7.1.2 Márgenes laterales/superior/inferior en `.slide`.
  - [X] T7.1.3 Split ~38/62 con gap; panel izquierdo sin vacíos > 80 px.
  - [X] T7.1.4 Frase-clave como tarjeta destacada.
  - [X] T7.1.5 Subir tipografía; probar 1920×1080, 1600×900, 1366×768.
- [X] **SF7.2 Rediseño por diapositiva (T7.2.1–T7.2.15: slides 01–20, relleno con KPIs/figuras reales)**
- [X] **SF7.3 Re-uso de activos NotebookLM (recortes + lightbox)**
- [X] **SF7.4 QA visual automatizado y manual (`scripts/audit_layout.py`), bitácora**

---

## F8: Integración de Simuladores Interactivos Evolutivos (Diapos 5, 6, 7, 8 y 9)
> **Estado:** `[X] Completado y Verificado al 100%`  
> **Objetivo:** Reemplazar las diapositivas estáticas del Acto 1 por simuladores interactivos multi-etapa totalmente responsivos ante cualquier resolución (1080p, 1366×768, 800×600) y nivel de zoom (125%, 150%), embebidos vía Base64 autónomo con sincronización bidireccional por teclado (`postMessage`).

- [X] **SF8.1 Diapositiva 05: Simulador de Descomposición Ontológica 3D**
  - [X] T8.1.1 Integrar `5_anatomia_senal_temporal_mejorada.html` vía Base64 en `back/build_deck.py` y `front/deck_slides_p1.py`.
  - [X] T8.1.2 Sincronización y ajuste de vista responsiva sin scrollbars externas.
- [X] **SF8.2 Diapositiva 06: Era 1 — La Parsimonia Lineal (Verhulst 1838 a ARIMA 1970)**
  - [X] T8.2.1 Adaptar `6_Era_1_La_parsimonia_lineal_v3.html` con layout elástico `clamp()`, media queries (`max-width: 1200px`, `880px`, `max-height: 760px`, `620px`) y scrollbar interna delgada en `.narrative-card`.
  - [X] T8.2.2 Puente de teclado bidireccional por `postMessage` (`deck_key`, navegación de deck y avance de diapositiva).
- [X] **SF8.3 Diapositiva 07: Era 2 — El Puente Tabular (Lags, Walmart M5, Trampa de Árboles y ERCOT Texas)**
  - [X] T8.3.1 Adaptar `7_Era_2_El_puente_tabular.html` con diseño responsivo elástico, media queries de pantalla y altura reducida, y scroll interno.
  - [X] T8.3.2 Sincronizar eventos de teclado y avance entre etapas (1 a 4) y pase a Diapo 8.
  - [X] T8.3.3 Codificar en Base64 en `back/build_deck.py`, inyectar iframe en `front/deck_slides_p1.py` y actualizar notas de ponente en `front/deck_notes.py`.
- [X] **SF8.4 Diapositiva 08: Era 3 — Deep Learning y Parches (LSTM, TFT, Quiebre O(L²) y PatchTST)**
  - [X] T8.4.1 Adaptar `8_Era_3_Deep_Learning_y_Parches.html` con reglas `body.is-embedded`, media queries responsivas y scrollbar estilizada en `.narrative-card`.
  - [X] T8.4.2 Sincronizar eventos de teclado y pase a Diapo 9 en la última etapa ('era4').
  - [X] T8.4.3 Codificar en Base64 en `back/build_deck.py`, inyectar iframe en `front/deck_slides_p1.py` y actualizar notas en `front/deck_notes.py`.
- [X] **SF8.5 Diapositiva 09: Era 4 — Foundation Models Zero-Shot (Preentrenamiento, Duelo Tokens vs Parches, 5 Modelos y Conformal)**
  - [X] T8.5.1 Adaptar `9_Era_4_Modelos_Fundacionales_Zero_Shot.html` con reglas `body.is-embedded`, media queries completas y scrollbar interna.
  - [X] T8.5.2 Sincronizar eventos de teclado y pase a Diapo 10 en la última etapa ('limits').
  - [X] T8.5.3 Codificar en Base64 en `back/build_deck.py`, inyectar iframe en `front/deck_slides_p1.py` y actualizar notas en `front/deck_notes.py`.
- [X] **SF8.6 Compilación, Auditoría Multi-Resolución y Verificación Visual**
  - [X] T8.6.1 Compilar deck integral offline mediante `.venv/bin/python scripts/build_deck.py` generando `presentacion.html` e `index.html`.
  - [X] T8.6.2 Validar con Chromium headless capturas a 1920×1080 (1080p), 1366×768 (laptop estándar) y 800×600 (pantalla estrecha) verificando cero desbordes y adaptación total.
- [X] **SF8.7 Diapositiva 05 v3: Anatomía de la Señal Temporal (4 Capas Físicas, STL en COES y Trampa de Overfitting)**
  - [X] T8.7.1 Adaptar `5_Anatomia_de_la_senal_temporal_v3.html` con soporte responsivo elástico `body.is-embedded`, scrollbar interna en `.left-column`, media queries por resolución/altura y sincronización bidireccional `postMessage` (`deck_key`, pase a Diapo 6).
  - [X] T8.7.2 Conectar en `back/build_deck.py` con fallback ordenado a `5_Anatomia_de_la_senal_temporal_v3.html` en Base64, e inyectar en `front/deck_slides_p1.py` con `id="iframeSlide5"`.
  - [X] T8.7.3 Actualizar notas de ponente en `front/deck_notes.py` desglosando las 4 etapas del simulador ontológico (Placas 3D, STL COES Perú, Señal vs Friaje, Trampa Overfitting).
- [X] **SF8.8 Diapositiva 10: La Ilusión de la Certeza y el Cono de Incertidumbre (Lyapunov y Conformal Prediction)**
  - [X] T8.8.1 Adaptar `10_El_Cono_de_Incertidumbre_y_Prediccion_Conforme.html` con reglas `body.is-embedded`, scrollbar delgada en `.narrative-card`, media queries y sincronización de teclado con pase a Diapo 11 en la última etapa ('bridge11').
  - [X] T8.8.2 Codificar en Base64 en `back/build_deck.py` (`b64_cono_html`), embeber como iframe responsivo en `front/deck_slides_p1.py` (`id="iframeSlide10"`) y actualizar notas de ponente en `front/deck_notes.py`.
- [X] **SF8.9 Diapositiva 11: Arquitectura de Decisión y Cierre Ejecutivo (Árbol, 4 Vías, Matriz y 3 Axiomas)**
  - [X] T8.9.1 Adaptar `11_Arquitectura_de_Decision_y_Cierre_Ejecutivo.html` con diseño elástico `body.is-embedded`, ajuste fino de espaciado y padding, scrollbar en `.narrative-card`, media queries y pase a Diapo 12 en etapa 4 ('axioms').
  - [X] T8.9.2 Codificar en Base64 en `back/build_deck.py` (`b64_decision_html`), embeber como iframe responsivo en `front/deck_slides_p1.py` (`id="iframeSlide11"`) y actualizar notas de ponente en `front/deck_notes.py`.
  - [X] T8.9.3 Compilar y verificar en Chromium headless a 1080p y 768p la perfecta adaptación visual sin desbordes externos.
- [X] **SF8.10 Diapositiva 18: Del Almanaque al Satélite (Evolución 1950–2026, 1 dato/año a 1 dato/día/píxel)**
  - [X] T8.10.1 Extraer infografía oficial en alta resolución (`infografia_08_almanaque_al_satelite.png`) desde PPTX oficial a `docs/images/seccion_3/`.
  - [X] T8.10.2 Integrar layout split en `front/deck_slides_p2.py` con lightbox interactivo HD y notas técnicas en `front/deck_notes.py`.
- [X] **SF8.11 Diapositiva 19: Física Biológica (Retrasos τ=6–8m, Umbrales VPD y N=24)**
  - [X] T8.11.1 Normalizar infografía biofísica (`infografia_09_fisica_biologica_retos.png`) en `docs/images/seccion_3/`.
  - [X] T8.11.2 Integrar layout en `front/deck_slides_p2.py` con llamada a biofísica, $p \gg N$, y lightbox zoom HD.
- [X] **SF8.12 Diapositiva 20: Reloj Fenológico del Café y las 3 Trampas del Stack Tecnológico**
  - [X] T8.12.1 Normalizar infografías del Reloj del Café (`infografia_10_reloj_fenologico_cafe.png`) y las 3 trampas (`infografia_11_precision_tres_trampas.png`).
  - [X] T8.12.2 Desarrollar switcher interactivo de vista (`switchFenologiaView`) entre reloj botánico y trampas de precisión.
  - [X] T8.12.3 Actualizar notas de ponente y compilar deck offline verificado a 1080p y 768p sin solapamientos.
- [X] **SF8.13 Prototipos Interactivos Autónomos de Sección 03 (Diapos 19 a 23)**
  - [X] T8.13.1 Auditar y adaptar los 5 prototipos HTML/Canvas de `docs/notebooklm/seccion_3/prototipos/` (19, 20, 21, 22 y 23) asegurando total autonomía sin CDNs externos.
  - [X] T8.13.2 Implementar reglas elásticas `body.is-embedded`, scrollbar interna delgada en `.narrative-card`, `flex-shrink: 0` en `.narr-top` y `.narr-blocks` para eliminar 100% de solapamientos con `.speaker-box`.
  - [X] T8.13.3 Adaptar dinámicamente lienzos Canvas/SVG (radio del reloj fenológico, badges de floración/llenado, y tarjetas de diagnóstico en Diapo 22; banner flotante y escalones en Diapo 20; tarjetas compactas multilínea en Diapo 23).
  - [X] T8.13.4 Conectar bridge bidireccional por `postMessage` (`deck_key`, avance inteligente entre etapas y diapositivas padre).
- [X] **SF8.14 Ensamblaje y Reestructuración del Master Deck a 30 Diapositivas**
  - [X] T8.14.1 Actualizar `back/build_deck.py` para codificar en Base64 `b64_p19_html` a `b64_p23_html` e inyectar al diccionario `branding`.
  - [X] T8.14.2 Actualizar contador global `totalSlides = 30` en JavaScript y HTML del pie de página (`01 / 30`).
  - [X] T8.14.3 Reconfigurar disparadores de gráficos en `initSlideVisuals`: desplazar `chartScatterNdvi` al índice 26 y `demoJaen` al índice 27.
  - [X] T8.14.4 Actualizar `front/deck_slides_p2.py`: Portada de Sección 3 (Diapo 18), 5 iframes embebidos con layout maximizado `inset: 6px 12px; padding: 0` (Diapos 19 a 23), y renumerar Acto 4 y Acto 5 (Diapos 24 a 30).
  - [X] T8.14.5 Expandir notas del orador en `front/deck_notes.py` cubriendo las 30 diapositivas completas con guiones conversacionales ricos.
- [X] **SF8.15 Compilación Integral, Auditoría Visual y Verificación Responsiva**
  - [X] T8.15.1 Compilar presentación autónoma offline de 6.78 MB en `presentacion.html` e `index.html`.
  - [X] T8.15.2 Ejecutar suite de screenshots en Chromium headless a 1920×1080 y 1366×768 para Diapos 18, 19, 20, 21, 22, 23, 24, 26, 27 y 30.
  - [X] T8.15.3 Inspección visual forense: confirmar cero solapamientos, perfecta legibilidad y renderizado responsivo total.
- [X] **SF8.16 Rediseño Gerencial y Responsivo de Sección 02 (Diapos 12 a 17 — Caso 1 SENAMHI Iquitos)**
  - [X] T8.16.1 Rediseñar `12_Caso_1_Auditoria_Iquitos.html` y `13_Datos_SENAMHI_Punchana.html` con topbar ejecutiva, flowbar de 4 etapas y ciclo/histograma interactivo sin vacíos.
  - [X] T8.16.2 Rediseñar `14_Trampa_Arboles_Meseta_vs_Diferencias.html` y `15_Benchmark_14_Modelos_Tierra_vs_Supercomputo.html` con simulador de ola de calor récord y ranking Diebold-Mariano filtrable.
  - [X] T8.16.3 Rediseñar `16_Pronostico_7_Dias_Cono_P10_P90.html` y `17_Pipeline_Codigo_Diferencias_ExtraTrees.html` con cono P10–P90 interactivo y arquitectura en 8 líneas de Python.
  - [X] T8.16.4 Conectar `b64_p12_html` a `b64_p17_html` en `back/build_deck.py` y `front/deck_slides_p1.py`/`p2.py`, compilar deck (7.5 MB) y auditar capturas en 1366×768 y 1920×1080.

---

## F9: Desaturación Cognitiva y Rediseño Pedagógico-Visual de Secciones 1 y 3 (Diapos 5–11 y 19–23)
*Detalle completo con 🧠 Explicación, 💡 Cómo hacerlo (código), AC y Tests en:* [`docs/task/fases/fase_9_desaturacion_visual_s1_s3.md`](fases/fase_9_desaturacion_visual_s1_s3.md)
> **Estado:** `[X] Completada`  
> **Macro-objetivo:** Eliminar la saturación de texto, las barras de scroll verticales y los solapamientos gráficos en los 12 prototipos interactivos de la **Sección 1 (Diapos 5 a 11)** y la **Sección 3 (Diapos 19 a 23)**, reemplazando el teleprompter en pantalla (`.speaker-box`) por una píldora ejecutiva de 1 línea (`💡 Idea Clave`), reduciendo en $\ge 40\%$ las palabras de `.narrative-card` ($\le 110$ palabras por etapa) e incorporando cotas visuales, conectores animados, medidores de barra y etiquetas limpias (*"Show, Don't Tell"*).

- [X] **SF9.1 Desaturación Textual, Reemplazo del Teleprompter en Pantalla y Cero Scrollbars (Secciones 1 y 3)**
  - [X] **T9.1.1 Reemplazo de `.speaker-box` ("Guía de Exposición") por Píldora Ejecutiva de 1 Línea (`💡 Idea Clave`) y Traslado a `front/deck_notes.py`**
    - [X] A9.1.1.1 Actualizar `front/deck_notes.py` asegurando que contenga los guiones hablados completos de las Diapos 5–11 y 19–23.
    - [X] A9.1.1.2 Reemplazar `.speaker-box` por `.executive-takeaway` de 1 línea ($\le 15$ palabras) en los 11 prototipos (`5`–`10` y `19`–`23`).
  - [X] **T9.1.2 Síntesis Escaneable de `.narrative-card` (Reducción del 45% de Palabras y Eliminación de `#metaphorCard` Redundante en Diapo 5)**
    - [X] A9.1.2.1 Ocultar `#metaphorCard` redundante durante la Etapa 1 de `5_Anatomia_de_la_senal_temporal_v3.html` y compactar sus etapas 2–4 eliminando la barra de scroll vertical.
    - [X] A9.1.2.2 Sintetizar textos de `STAGES` (`lead` $\le 22$ palabras, cada `block.body` $\le 18$ palabras) en los prototipos `06`, `07`, `08`, `09` y `10` (Sección 1).
    - [X] A9.1.2.3 Sintetizar textos de `STAGES` (`lead` $\le 22$ palabras, cada `block.body` $\le 18$ palabras) en los prototipos `19`, `20`, `21`, `22` y `23` (Sección 3), eliminando la barra de scroll vertical de la Diapo 23.
- [X] **SF9.2 Rediseño Pedagógico-Visual ("Show, Don't Tell") de la Sección 1 (Diapositivas 5 a 11)**
  - [X] **T9.2.1 Diapo 05 (`5_Anatomia_de_la_senal_temporal_v3.html`): Barras de Peso en Tarjetas de Capas y Cotas Visuales Directas en el Monitor 2D**
    - [X] A9.2.1.1 Agregar mini-barras/badges de proporción en `#layerStack` y dibujar cotas directas (`↗ Pendiente T(t)`, `↔ Periodo S(t)`) en `#wave2d`.
  - [X] **T9.2.2 Diapos 06 y 07 (`6_Era_1...` y `7_Era_2...`): Zonas Visuales en Curva Logística y Flechas de Mapeo Serie → Tabla Supervisada**
    - [X] A9.2.2.1 Retirar banners redundantes en `6_Era_1_La_parsimonia_lineal_v3.html` y sombrear las 3 fases de crecimiento en la curva de Verhulst.
    - [X] A9.2.2.2 Retirar banners `"Arriba:/Abajo:"` en `7_Era_2_El_puente_tabular.html` y trazar flechas conectoras curvas desde los puntos de la ventana deslizante ($y_{t-1}, y_{t-7}, y_{t+1}$) hacia las columnas de la tabla supervisada.
  - [X] **T9.2.3 Diapos 08, 09 y 10 (`8_Era_3...`, `9_Era_4...`, `10_El_Cono...`): Medidores en Compuertas LSTM/PatchTST, Flujo Zero-Shot Visual y Etiquetas Limpias en el Cono**
    - [X] A9.2.3.1 Eliminar banners redundantes en Diapos 08 y 09 e incorporar barras visuales de porcentaje dentro de las 3 compuertas de memoria en Diapo 08.
    - [X] A9.2.3.2 Eliminar banners redundantes en `10_El_Cono_de_Incertidumbre_y_Prediccion_Conforme.html` y encapsular las etiquetas del cono (`Núcleo 50%`, `Pronóstico Puntual`, `Banda 80%`) en pastillas oscuras (`roundRect`) para que no se mezclen con las curvas de Monte Carlo.
  - [X] **T9.2.4 Diapo 11 (`11_Arquitectura_de_Decision_y_Cierre_Ejecutivo.html`): Eliminación del Vacío Central y Adición de Medidores Comparativos en las 4 Vías**
    - [X] A9.2.4.1 Eliminar el hueco negro central en `.lane-card`, insertar el bloque `.lane-meters` con 3 barras comparativas (`📊 Datos N`, `⚡ Cómputo`, `🚀 Extrapola`) en cada una de las 4 Vías y compactar `Condición / Ventaja / Límite` a 1 línea concisa.
- [X] **SF9.3 Rediseño Pedagógico-Visual y Corrección de Solapamientos en la Sección 3 (Diapositivas 19 a 23)**
  - [X] **T9.3.1 Diapos 19 y 20 (`19_c_mo_el_agro...` y `20_del_almanaque_al_sat_lite.html`): Espejo Histórico con Callouts Limpios y Corrección del Recorte en los 5 Escalones**
    - [X] A9.3.1.1 Retirar banners superiores redundantes y compactar las cajas flotantes del espejo histórico en Diapo 19.
    - [X] A9.3.1.2 Retirar banners superiores en Diapo 20 y reemplazar el cuadro inferior cortado por un grid `.step-kpi-strip` de 3 tarjetas KPI horizontales (`Frecuencia/Escala`, `Logro Operativo`, `Reto Matemático`).
  - [X] **T9.3.2 Diapo 21 (`21_f_sica_biol_gica_y_el_l_mite_algor_tmico.html`): Puente de Retraso ($\tau = 6\text{–}8\text{m}$) sin Solape en Engranaje y Zonas de Umbral VPD**
    - [X] A9.3.2.1 Eliminar banners superiores, colocar placa opaca `roundRect` para el rótulo `Lag τ = 6–8m` sobre el engranaje central y colorear en verde/rojo las zonas de umbral VPD en el gráfico derecho.
  - [X] **T9.3.3 Diapo 22 (`22_reloj_fenol_gico_del_caf.html`): Ampliación del Reloj Botánico con Etiquetas Externas Limpias y Diagnóstico Compacto**
    - [X] A9.3.3.1 Eliminar banners superiores para ampliar el radio del reloj fenológico en $\ge 20\%$, dibujar las etiquetas `Floración`, `Llenado` y `Cosecha` en pastillas sin truncamiento (`"Florac..."`) y resumir la tarjeta derecha en 3 filas ejecutivas de 1 línea.
  - [X] **T9.3.4 Diapo 23 (`23_precisi_n_actual_y_las_tres_trampas.html`): Eliminación de Scrollbar, Corrección de Solape en "Prueba de Fuego" y Tarjetas `❌ Error vs ✅ Remedio`**
    - [X] A9.3.4.1 Eliminar banners superiores, aplicar `display: grid; grid-template-columns: minmax(0, 1fr) auto` al banner `"🔥 LA PRUEBA DE FUEGO"` para que el botón `"Ir al Caso Jaén →"` no pise el texto, y formatear las 3 trampas con líneas `❌ Error` / `✅ Remedio`.
- [X] **SF9.4 Compilación del Deck Maestro y Auditoría Visual Multi-Resolución**
  - [X] **T9.4.1 Compilación Integral del Deck Offline (`back/build_deck.py`) y Verificación de Notas del Orador**
    - [X] A9.4.1.1 Ejecutar `.venv/bin/python back/build_deck.py` y verificar la actualización de los 12 iframes Base64 en `presentacion.html` e `index.html`.
  - [X] **T9.4.2 Auditoría Automatizada DOM + Capturas Chromium (`1366×768` y `1920×1080`)**
    - [X] A9.4.2.1 Crear y ejecutar `scripts/audit_f9_desaturacion.py` y generar las 24 capturas en `screenshots/f9_s{5..11,19..23}_{1366,1920}.png` comprobando 0 scrollbars, 0 solapes y $\le 110$ palabras por etapa.
