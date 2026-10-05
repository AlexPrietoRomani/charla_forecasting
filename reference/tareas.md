# Tablero de Tareas — Charla Forecasting & IA (v2 Real-Data)

> **Estado General:** `[X] Completado y Verificado al 100%`  
> **Convenciones:** `[ ]` pendiente · `[/]` en progreso · `[X]` completado y verificado.  
> **Documento Rector:** [plan_detallado_diapositivas.md](plan_detallado_diapositivas.md)  
> **Detalle por Fases:** [reference/fases/](fases/)

---

## F1: Depuración de Material Sintético, Trazabilidad y Setup
*Detalle completo en:* [`reference/fases/fase_1_depuracion_setup.md`](fases/fase_1_depuracion_setup.md)

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
*Detalle completo en:* [`reference/fases/fase_2_cafe_datos_reales.md`](fases/fase_2_cafe_datos_reales.md)

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
  - [X] T2.3.3 Crear `scripts/build_cafe_real.py` (determinista, sin `np.random`) y compilar `data/cafe_jaen_campanias.csv`.
- [X] **SF2.4 Evaluación de Hipótesis y Modelado con Ventana Expansiva**
  - [X] T2.4.1 Evaluar H1: Correlación empírica `ndvi_anual` vs `anomalia_rendimiento`.
  - [X] T2.4.2 Evaluar H2: Correlación de clima de floración vs NDVI.
  - [X] T2.4.3 Evaluar H3: Comparación de MAE en ventana expansiva (Tendencia vs NDVI vs Clima vs Fusión).
  - [X] T2.4.4 Evaluar H4: Firma espectral del impacto de la roya amarilla (2012–2014).
  - [X] T2.4.5 Exportar `data/cafe_jaen_hipotesis.json` y actualizar `notebooks/02_cafe_ndvi.ipynb`.

---

## F3: Caso A — Benchmark de 8 Modelos en Iquitos con Foundation Models
*Detalle completo en:* [`reference/fases/fase_3_benchmark_iquitos_fm.md`](fases/fase_3_benchmark_iquitos_fm.md)

- [X] **SF3.1 Preparación y Holdout Estricto**
  - [X] T3.1.1 Cargar `data/senamhi_diario.csv` (2019–2025, 2,557 días).
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
  - [X] T3.3.4 Exportar `data/benchmark_punchana.csv` y `data/senamhi_forecast_7d.csv`.
  - [X] T3.3.5 Reejecutar `notebooks/01_clima_senamhi.ipynb` con celdas ejecutadas y limpias.

---

## F4: Experimentos de Respaldo, Citas y Consolidación Narrativa
*Detalle completo en:* [`reference/fases/fase_4_experimentos_narrativa.md`](fases/fase_4_experimentos_narrativa.md)

- [X] **SF4.1 Experimento Propio de No-Extrapolación (Diapositiva 05)**
  - [X] T4.1.1 Configurar experimento con datos de Punchana restringidos en $T \le 34.0\,^{\circ}\text{C}$.
  - [X] T4.1.2 Demostrar la meseta plana del árbol vs la extrapolación del modelo diferenciado ($\Delta y$).
  - [X] T4.1.3 Exportar `data/experimento_extrapolacion.csv` rotulado `EXPERIMENTO PROPIO`.
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
*Detalle completo en:* [`reference/fases/fase_5_deck_20_slides.md`](fases/fase_5_deck_20_slides.md)

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
  - [X] T5.4.1 Demo 1 (Diapo 14): Conectar Chart.js a `data/senamhi_forecast_7d.csv`.
  - [X] T5.4.2 Demo 2 (Diapo 17): Conectar Chart.js a `data/cafe_jaen_campanias.csv` y validación expansiva.
  - [X] T5.4.3 Verificar que ninguna cifra esté cableada a mano en el HTML.

---

## F6: QA Visual, Auditoría Multi-Resolución, Ensayo y Bitácora
*Detalle completo en:* [`reference/fases/fase_6_qa_ensayo.md`](fases/fase_6_qa_ensayo.md)

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
*Detalle completo en:* [`reference/fases/fase_7_rediseno_visual.md`](fases/fase_7_rediseno_visual.md)
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

