# Plan Maestro — ¿Puede la IA predecir el futuro? (v2 Datos Reales)

> **Documento Rector del Proyecto**  
> **Alineado con:** [plan_detallado_diapositivas.md](plan_detallado_diapositivas.md) y [tareas.md](tareas.md)  
> **Público:** Universitario (estadística básica). **Duración:** 30–40 min. **Diapositivas:** 20.

---

## 1. Trama Narrativa y Pregunta Conductora

Pregunta conductora: ***"¿Cuándo vale la pena un modelo complejo?"***  
Se plantea en la diapositiva 01 y se responde en la 19 mediante evidencia empírica.

### Estructura en 5 Actos (20 Diapositivas)

```
ACTO 1: LA PREGUNTA (Diapos 01–03, ~5 min)
  ├─ 01 [TEORÍA] ¿Puede la IA predecir el futuro? → No adivina: cuantifica incertidumbre
  ├─ 02 [TEORÍA] La anatomía de una serie → Señal = Tendencia + Estacionalidad + Ruido
  └─ 03 [TEORÍA] El gran mapa de las 4 familias → Ningún modelo gana siempre

ACTO 2: LAS HERRAMIENTAS (Diapos 04–11, ~13 min)
  ├─ 04 [MECANISMO] Clásicos: Suavizado, logística y STL → Pocos parámetros, mucha física
  ├─ 05 [MECANISMO] Árboles: El puente tabular y su límite → Ganan en tabular, no extrapolan (Experimento Propio)
  ├─ 06 [MECANISMO] Deep Learning: De LSTM a PatchTST → Atención en parches escala con muchas series
  ├─ 07 [MECANISMO] Foundation Models Zero-Shot → TimesFM, Chronos y Moirai sin entrenar
  ├─ 08 [MECANISMO] Satélites y la trampa del NDVI → Cuando el dosel es denso, el sensor se satura
  ├─ 09 [MECANISMO] El reloj botánico → Ventanas fenológicas críticas en agricultura
  ├─ 10 [EVIDENCIA] Física global y discrepancia entre agencias → NOAA GFS vs ECMWF IFS en Iquitos
  └─ 11 [EVIDENCIA] GraphCast y la frontera 2024–2026 → Redes en grafos vs supercómputo

ACTO 3: CASO A — CLIMA EN LA SELVA (Diapos 12–14, ~6 min)
  ├─ 12 [CASO REAL] Estación Punchana (SENAMHI Iquitos) → 7 años de datos reales, 91 msnm
  ├─ 13 [EVIDENCIA] Benchmark de 8 modelos → Holdout 90 días, test Diebold-Mariano y parsimonia
  └─ 14 [DEMO] Pronóstico a 7 días en vivo → Incertidumbre probabilística y cono de duda

ACTO 4: CASO B — CAFÉ EN JAÉN (Diapos 15–17, ~6 min)
  ├─ 15 [CASO REAL] Rendimiento oficial y satélite real → MIDAGRI/SIEA + MODIS/Sentinel-2
  ├─ 16 [EVIDENCIA] ¿Ve el satélite lo que pasó en el campo? → Evaluación empírica de saturación
  └─ 17 [DEMO] Validación temporal honesta → Ventana expansiva y reporte de fallos reales

ACTO 5: LA DECISIÓN (Diapos 18–20, ~5 min)
  ├─ 18 [TEORÍA] 5 Lecciones desde las trincheras → Principios de ingeniería innegociables
  ├─ 19 [TEORÍA] ¿Qué modelo uso? (Árbol de decisión) → Respuesta final a la pregunta conductora
  └─ 20 [TEORÍA] Cierre y recursos reproducibles → Código abierto, 49 referencias y NotebookLM
```

---

## 2. Arquitectura del Deck Interactivo (`presentacion.html`)

- **Single-file autocontenido:** Chart.js + PapaParse + Leaflet vía CDN, con paleta semántica claro/oscuro (CSS variables).
- **Layout Split-Screen 40/60:**
  - Panel izquierdo (40%): Título, insignia semántica fija, tesis en 1 frase, máximo 3 viñetas breves, y Frase-clave destacada.
  - Panel derecho (60%): Visual interactivo y animado a altura completa sin márgenes vacíos ("Zero-White-Space").
- **Drawer de Speaker Notes:** Se activa con tecla `N`. Contiene el guion narrado y el cronómetro de la diapositiva sin sobrecargar la pantalla principal.
- **5 Insignias Normalizadas:** `TEORÍA` (Violeta), `MECANISMO` (Cian), `EVIDENCIA` (Ámbar), `CASO REAL` (Esmeralda), `DEMO` (Rojo).
- **Cero cifras cableadas a mano:** Todos los valores se inyectan o parsean desde los CSVs de `data/`.

---

## 3. Práctica A — Benchmark de Clima en Iquitos (Punchana, SENAMHI)

- **Datos:** Estación 103015 / 150208, 91 msnm, 2,557 días (2019-01-01 a 2025-12-31).
- **Holdout:** 90 días finales ciegos con split temporal estricto (origen móvil).
- **8 Modelos en Competencia:**
  1. Naive estacional (persistencia 7d).
  2. ARIMA / SARIMAX calibrado por AIC.
  3. Suavizado Holt-Winters.
  4. Random Forest con lags 1–14.
  5. ExtraTrees / LightGBM con lags y rolling statistics.
  6. Red LSTM profunda (PyTorch, promedio 5 semillas).
  7. Chronos-Bolt Zero-Shot (Amazon).
  8. TimesFM 200M Zero-Shot (Google).
- **Regla de Conclusión:** Gana el de menor RMSE. En caso de empate estadístico según la prueba de Diebold-Mariano ($p > 0.05$), gana el modelo más simple y parsimonioso.
- **Entregable:** `data/caso_1/benchmark_punchana.csv` y `notebooks/01_clima_senamhi.ipynb`.

---

## 4. Práctica B — Rendimiento de Café con Datos Reales (Jaén, Cajamarca)

- **Protocolo Anti-Invención (Opción A):**
  - **Rendimiento Objetivo:** Serie histórica oficial de café para la provincia de Jaén reportada por MIDAGRI / SIEA (meta: 2000–2024).
  - **Predictores Satelitales Reales:** MODIS MOD13Q1 (250m, 16d, 2000–2024) y Sentinel-2 L2A (10–20m, 2017–2024) vía Planetary Computer, filtrando píxeles por máscara de calidad QA dentro de la zona cafetalera.
  - **Predictores Climáticos Reales:** Reanálisis ERA5 vía Open-Meteo Archive para las coordenadas de Jaén.
  - **Ventana Fenológica:** Floración (Ago–Oct), Llenado (Nov–Feb), Cosecha (Mar–Jul).
- **Modelos:** Tendencia (M1), Solo NDVI (M2), Solo Clima (M3), Fusión Satélite + Clima (M4).
- **Validación Principal:** Ventana temporal expansiva (entrenar con $\le t-1$, predecir $t$).
- **Entregables:** `data/caso_2/cafe_jaen_campanias.csv`, `data/caso_2/cafe_jaen_resultados.csv` y `notebooks/02_cafe_ndvi.ipynb`.

---

## 5. Fases de Ejecución del Proyecto

1. **F1: Depuración y Setup** (`docs/reference/fases/fase_1_depuracion_setup.md`) — Aislar material sintético a `data/deprecated/`, crear `SOURCES.md`, instalar dependencias.
2. **F2: Caso B con Datos Reales** (`docs/reference/fases/fase_2_cafe_datos_reales.md`) — Descargar SIEA/MIDAGRI, extraer MODIS/S2 y ERA5, evaluar hipótesis H1–H4.
3. **F3: Caso A Benchmark Iquitos** (`docs/reference/fases/fase_3_benchmark_iquitos_fm.md`) — Ejecutar 8 modelos, test Diebold-Mariano, exportar CSVs de benchmark.
4. **F4: Experimentos y Citas** (`docs/reference/fases/fase_4_experimentos_narrativa.md`) — Experimento propio de no-extrapolación, redactar Frases-clave ⏳ y validar con el usuario.
5. **F5: Refactorización del Deck** (`docs/reference/fases/fase_5_deck_20_slides.md`) — Generar `presentacion.html` de 20 diapositivas conectadas a CSVs reales.
6. **F6: QA, Ensayo y Bitácora** (`docs/reference/fases/fase_6_qa_ensayo.md`) — Auditoría 1920x1080 / 1366x768, ensayo 35 min, bitácora `docs/logs/log.md`.
7. **F7: Rediseño Visual (Front-Design)** (`docs/reference/fases/fase_7_rediseno_visual.md`) — Sistema de espaciado, jerarquía visual y eliminación de vacíos.
8. **F8: Integración de Simuladores Interactivos Evolutivos (Secciones 1, 2 y 3)** — Integración de 18 prototipos interactivos autónomos en Base64 (Diapos 5–11, 12–17 y 19–23) llevando el deck a 30 diapositivas 100% offline.
9. **F9: Desaturación Cognitiva y Rediseño Pedagógico-Visual de Secciones 1 y 3** (`docs/task/fases/fase_9_desaturacion_visual_s1_s3.md`) — Reducción del 45% de carga textual en paneles narrativos, eliminación de teleprompters redundantes en pantalla y transformación de los lienzos de Diapos 5–11 y 19–23 en infografías auto-explicativas sin barras de scroll ni solapamientos.

---

## 6. Detalle de la Fase 9 (F9): Desaturación Cognitiva y Rediseño Pedagógico-Visual de Secciones 1 y 3

- **Macro-objetivo:** Eliminar la saturación de texto, barras de scroll verticales y solapamientos gráficos en los 12 prototipos interactivos de la **Sección 1 (Diapos 5 a 11)** y la **Sección 3 (Diapos 19 a 23)**, aplicando el estándar gerencial alcanzado en la Sección 2: reemplazar paredes de texto y guiones de orador en pantalla por síntesis ejecutiva escaneable y diagramas visuales auto-explicativos (*"Show, Don't Tell"*).
- **Entregable global:** Los 12 archivos HTML en `docs/notebooklm/seccion_1/prototipos/` y `docs/notebooklm/seccion_3/prototipos/` refactorizados, notas completas trasladadas a `front/deck_notes.py`, y bundles `presentacion.html` e `index.html` compilados sin barras de scroll internas ni solapamientos en 1366×768 y 1920×1080.
- **Criterios de Aceptación (AC) globales de F9:**
  - [ ] Cero bloques `.speaker-box` ("Guía de Exposición") de múltiples líneas visibles en los prototipos; reemplazados por una píldora ejecutiva `.executive-takeaway` de 1 línea ($\le 15$ palabras).
  - [ ] Reducción $\ge 40\%$ en el conteo de palabras de `.narrative-card` ($\le 110$ palabras por etapa), logrando `scrollHeight <= clientHeight` (cero barras de scroll verticales) en 1366×768 y 1920×1080.
  - [ ] Cero solapamientos o recortes gráficos en los lienzos Canvas/SVG/DOM de las Diapos 11, 20, 21, 22 y 23.
  - [ ] Todos los lienzos de las Diapos 5–11 y 19–23 incluyen anotaciones visuales pedagógicas directas (cotas, conectores animados, medidores de barra o zonas coloreadas de umbral) que explican el fenómeno sin depender de párrafos largos.
- **Estrategia de Pruebas de F9:**
  - **Test Unitario:** Script en Python (`scripts/audit_f9_desaturacion.py`) que parsea los 12 prototipos HTML y sus objetos `STAGES` en JavaScript para verificar que ninguna etapa supere las 110 palabras en la columna izquierda, que no existan `.speaker-box` extensos y que `back/build_deck.py` compile con código de salida `0`.
  - **Test de Simulación de Usuario:** Ejecución en Chromium headless a `1366×768` y `1920×1080` recorriendo las 4 etapas de cada una de las 12 diapositivas (48 estados visuales), validando por inspección de layout que `scrollHeight <= clientHeight` en `.narrative-card` y verificando visualmente las capturas PNG generadas.

### SF9.1 — Desaturación Textual, Reemplazo del Teleprompter en Pantalla y Cero Scrollbars (Secciones 1 y 3)
- **Micro-objetivo:** Limpiar la columna izquierda (`.narrative-card` / `.left-column`) en los prototipos de las Diapos 5–10 y 19–23 para eliminar la redundancia textual y las barras de scroll verticales.
- **Entregables:** Prototipos 5–10 y 19–23 con `.executive-takeaway` de 1 línea, objetos `STAGES` sintetizados y `front/deck_notes.py` enriquecido con las citas completas del orador.
- **Estrategia de Pruebas de SF9.1:**
  - **Test Unitario:** Validador estático de longitud de strings en los diccionarios `STAGES` (`lead` $\le 22$ palabras, cada `block` $\le 18$ palabras, `takeaway` $\le 15$ palabras).
  - **Test de Simulación de Usuario:** Renderizado en navegador headless a 1366×768 comprobando ausencia de barra de scroll vertical (`overflow-y` sin desborde activo) en las 4 etapas de cada prototipo.
- **Tareas de SF9.1:**
  - **T9.1.1 — Reemplazo de `.speaker-box` ("Guía de Exposición") por Píldora Ejecutiva de 1 Línea (`💡 Idea Clave`) y Traslado a `front/deck_notes.py`**
    - *Objetivo:* Sustituir el bloque de teleprompter de 4 líneas en pantalla por un callout ejecutivo de 1 línea y asegurar que el texto hablado resida en el drawer `[N] Notas`.
    - *Entregable:* CSS/HTML/JS actualizado en los 11 prototipos con `.executive-takeaway` y `front/deck_notes.py` sincronizado.
    - *AC:* `[ ]` Ningún prototipo muestra párrafos entrecomillados de "Guía de Exposición"; `[ ]` Cada etapa muestra `💡 Idea Clave:` en máximo 1 línea; `[ ]` `front/deck_notes.py` conserva el guion íntegro.
    - *Tests:* **Unitario:** Regex sobre los 11 archivos HTML verificando reemplazo de `GUÍA DE EXPOSICIÓN` por `IDEA CLAVE`. **Simulación de Usuario:** Abrir drawer `[N] Notas` en `presentacion.html` en las Diapos 5–11 y 19–23 y comprobar que el guion aparece completo mientras la diapositiva luce despejada.
  - **T9.1.2 — Síntesis Escaneable de `.narrative-card` (Reducción del 45% de Palabras y Eliminación de `#metaphorCard` Redundante en Diapo 5)**
    - *Objetivo:* Reescribir los textos de `lead` y `blocks` en formato telegráfico gerencial (`Icono + Concepto: Causa → Efecto`) y eliminar el recuadro `#metaphorCard` duplicado en la Etapa 1 de la Diapo 5.
    - *Entregable:* Diccionarios `STAGES` y marcado base optimizados en los prototipos 5–10 y 19–23.
    - *AC:* `[ ]` En Diapo 5 no existe el bloque duplicado `"CAUCE, MAREAS, SEQUÍAS Y TURBULENCIA"` bajo las 5 capas; `[ ]` Cada tarjeta `.narr-block` tiene máximo 2 líneas de texto; `[ ]` Cero scrollbars verticales en 1366×768.
    - *Tests:* **Unitario:** Conteo automatizado de palabras por etapa $\le 110$. **Simulación de Usuario:** Captura en Chromium a 1366×768 de Diapos 5 y 23 verificando desaparición total de la barra de scroll vertical.

### SF9.2 — Rediseño Pedagógico-Visual ("Show, Don't Tell") de la Sección 1 (Diapositivas 5 a 11)
- **Micro-objetivo:** Transformar los simuladores del Acto 1 (Diapos 5 a 11) para que el propio gráfico explique visualmente la mecánica matemática y física sin requerir lectura densa.
- **Entregables:** Prototipos 5, 6, 7, 8, 9, 10 y 11 en `docs/notebooklm/seccion_1/prototipos/` con anotaciones visuales en Canvas/DOM y layout equilibrado sin huecos vacíos.
- **Estrategia de Pruebas de SF9.2:**
  - **Test Unitario:** Verificación de sintaxis JS y presencia de funciones de anotación gráfica y medidores visuales en los prototipos 5–11.
  - **Test de Simulación de Usuario:** Interacción en navegador headless con los controles y las 4 etapas de las Diapos 5 a 11 a 1366×768 y 1920×1080.
- **Tareas de SF9.2:**
  - **T9.2.1 — Diapo 05 (`5_Anatomia_de_la_senal_temporal_v3.html`): Barras de Peso en Tarjetas de Capas y Cotas Visuales Directas en el Monitor 2D**
    - *Objetivo:* Añadir barras visuales de aporte de varianza en las 5 tarjetas de `#layerStack` y dibujar sobre el monitor 2D cotas explicativas directas (pendiente $T$, periodo $S$, amplitud de ruido $\varepsilon$).
    - *Entregable:* `docs/notebooklm/seccion_1/prototipos/5_Anatomia_de_la_senal_temporal_v3.html` actualizado.
    - *AC:* `[ ]` Cada tarjeta de capa muestra una barra de proporción y rol físico en 1 línea; `[ ]` El monitor 2D dibuja anotaciones visuales directas al activar/inspeccionar cada capa.
    - *Tests:* **Unitario:** Validar existencia de barras `.layer-meter` y etiquetas en `#wave2d`. **Simulación de Usuario:** Alternar capas en Diapo 5 y verificar en captura 1366×768 que las cotas se ven nítidas y sin solapes.
  - **T9.2.2 — Diapos 06 y 07 (`6_Era_1...` y `7_Era_2...`): Zonas Visuales en Curva Logística y Flechas de Mapeo Serie → Tabla Supervisada**
    - *Objetivo:* Eliminar banners de texto redundantes sobre los gráficos de las Diapos 6 y 7; colorear las 3 fases de la curva de Verhulst en Diapo 6 y trazar flechas conectoras directas entre los puntos de la ventana deslizante ($y_{t-1}, y_{t-7}, y_{t+1}$) y las celdas de la tabla en Diapo 7.
    - *Entregable:* `6_Era_1_La_parsimonia_lineal_v3.html` y `7_Era_2_El_puente_tabular.html` actualizados.
    - *AC:* `[ ]` Eliminados los banners redundantes `"Arriba: ... / Abajo: ..."` que quitaban espacio vertical al gráfico; `[ ]` En Diapo 6 se distinguen visualmente las 3 zonas de Verhulst y las barras de decaimiento ARIMA; `[ ]` En Diapo 7 las flechas conectan los puntos de la curva con las columnas `Lag 1`, `Lag 7` y `Objetivo`.
    - *Tests:* **Unitario:** Comprobar eliminación de `.canvas-split-hint` redundantes y presencia de conectores en `drawLagWindow()`. **Simulación de Usuario:** Mover el slider de ventana en Diapo 7 y verificar en captura PNG que las flechas apuntan a las columnas correctas.
  - **T9.2.3 — Diapos 08, 09 y 10 (`8_Era_3...`, `9_Era_4...`, `10_El_Cono...`): Medidores en Compuertas LSTM/PatchTST, Flujo Zero-Shot Visual y Etiquetas Limpias en el Cono**
    - *Objetivo:* Reemplazar textos largos dentro de los gráficos de las Diapos 8, 9 y 10 por barras de progreso en las compuertas LSTM, visualización de empaquetado de 16 puntos en 1 parche, y etiquetas alineadas sin pisar las curvas de Monte Carlo en la Diapo 10.
    - *Entregable:* `8_Era_3_Deep_Learning_y_Parches.html`, `9_Era_4_Modelos_Fundacionales_Zero_Shot.html` y `10_El_Cono_de_Incertidumbre_y_Prediccion_Conforme.html` actualizados.
    - *AC:* `[ ]` En Diapo 8 las 3 compuertas incluyen barras visuales de porcentaje y el modo PatchTST muestra bloques agrupados; `[ ]` En Diapo 9 los 5 dominios muestran mini-iconos y métricas limpias; `[ ]` En Diapo 10 las etiquetas `Núcleo 50%`, `Punto Fijo` y `Banda 80%` tienen fondo semitransparente y no se superponen con las ondas.
    - *Tests:* **Unitario:** Verificar renderizado sin errores JS en las 4 etapas de las Diapos 8, 9 y 10. **Simulación de Usuario:** Capturas a 1366×768 de las Diapos 8, 9 y 10 verificando legibilidad inmediata.
  - **T9.2.4 — Diapo 11 (`11_Arquitectura_de_Decision_y_Cierre_Ejecutivo.html`): Eliminación del Vacío Central y Adición de Medidores Comparativos en las 4 Vías**
    - *Objetivo:* Eliminar el espacio muerto en el centro de las 4 columnas de la Diapo 11 y añadir en cada columna un bloque gráfico con **3 barras comparativas** (`Datos N`, `Cómputo CPU/GPU`, `Extrapolación`) para que las 4 arquitecturas se comparen de un vistazo.
    - *Entregable:* `docs/notebooklm/seccion_1/prototipos/11_Arquitectura_de_Decision_y_Cierre_Ejecutivo.html` actualizado.
    - *AC:* `[ ]` Cero vacíos mayores a 24px dentro de las 4 tarjetas `.lane-card`; `[ ]` Cada vía incluye las 3 barras visuales comparativas con código de color semántico; `[ ]` Textos de Condición/Ventaja/Límite reducidos a 1 línea concisa por ítem.
    - *Tests:* **Unitario:** Comprobar existencia de `.lane-meters` en las 4 columnas del DOM. **Simulación de Usuario:** Captura en Chromium a 1366×768 y 1920×1080 verificando distribución vertical uniforme sin huecos negros.

### SF9.3 — Rediseño Pedagógico-Visual y Corrección de Solapamientos en la Sección 3 (Diapositivas 19 a 23)
- **Micro-objetivo:** Corregir todos los recortes y solapamientos detectados en las Diapos 19 a 23 y reemplazar las cajas de texto anidadas por infografías visuales claras de biofísica y fenología.
- **Entregables:** Prototipos 19, 20, 21, 22 y 23 en `docs/notebooklm/seccion_3/prototipos/` corregidos y optimizados.
- **Estrategia de Pruebas de SF9.3:**
  - **Test Unitario:** Verificación de dimensiones de contenedores y ausencia de desborde (`scrollHeight <= clientHeight`) en todos los paneles internos de las Diapos 19 a 23.
  - **Test de Simulación de Usuario:** Inspección visual de capturas en Chromium headless a 1366×768 y 1920×1080 en las Diapos 19, 20, 21, 22 y 23.
- **Tareas de SF9.3:**
  - **T9.3.1 — Diapos 19 y 20 (`19_c_mo_el_agro...` y `20_del_almanaque_al_sat_lite.html`): Espejo Histórico con Callouts Limpios y Corrección del Recorte en los 5 Escalones**
    - *Objetivo:* Limpiar los banners redundantes en Diapos 19 y 20, reemplazar las cajas de texto flotantes del espejo ancestral/IA por callouts compactos, y reemplazar el recuadro inferior cortado de la Diapo 20 por 3 tarjetas KPI horizontales (`Frecuencia`, `Escala Espacial`, `Variable Clave`).
    - *Entregable:* `19_c_mo_el_agro_invent_el_forecasting.html` y `20_del_almanaque_al_sat_lite.html` actualizados.
    - *AC:* `[ ]` En Diapo 20 el detalle del escalón seleccionado no sufre ningún recorte vertical en 1366×768; `[ ]` Eliminados los banners superiores redundantes ganando $\ge 44\text{px}$ para la curva de los 5 escalones; `[ ]` En Diapo 19 la cortina interactiva muestra comparativas visuales de 1 línea a cada lado.
    - *Tests:* **Unitario:** Verificar que el contenedor inferior de Diapo 20 use `grid-template-columns: repeat(3, 1fr)` sin `overflow: hidden` que trunque texto. **Simulación de Usuario:** Captura a 1366×768 de Diapos 19 y 20 comprobando texto 100% visible.
  - **T9.3.2 — Diapo 21 (`21_f_sica_biol_gica_y_el_l_mite_algor_tmico.html`): Puente de Retraso ($\tau = 6\text{–}8\text{m}$) sin Solape en Engranaje y Zonas de Umbral VPD**
    - *Objetivo:* Separar la etiqueta `"Retraso (τ) 6-8 meses"` de los dientes del engranaje central colocándola en un badge limpio sobre el eje temporal `Ago-Oct (Floración) → May-Jul (Cosecha)`, y sombrear en el gráfico derecho la Zona Segura (`VPD < 1.8 kPa`) vs Zona de Aborto Floral (`VPD > 1.8 kPa / >32 °C`).
    - *Entregable:* `21_f_sica_biol_gica_y_el_l_mite_algor_tmico.html` actualizado.
    - *AC:* `[ ]` El texto del engranaje no pisa las líneas del dibujo; `[ ]` El gráfico derecho muestra bandas de color semántico verde/rojo que explican visualmente el colapso biológico al mover el slider de VPD.
    - *Tests:* **Unitario:** Comprobar coordenadas de texto y badge en el SVG/Canvas del engranaje. **Simulación de Usuario:** Mover el slider de estrés ambiental y validar en captura 1366×768 que no hay textos superpuestos.
  - **T9.3.3 — Diapo 22 (`22_reloj_fenol_gico_del_caf.html`): Ampliación del Reloj Botánico con Etiquetas Externas Limpias y Diagnóstico Compacto**
    - *Objetivo:* Eliminar el truncado de `"Florac..."` y `"Cosecha"` dentro de la rueda fenológica aumentando su radio y usando badges/etiquetas legibles sin colisión, y resumir el panel derecho de ventana activa en 3 tarjetas ejecutivas de 1 línea (`🌱 Fisiología`, `⚠️ Umbral Fatal`, `🤖 Regla IA`).
    - *Entregable:* `22_reloj_fenol_gico_del_caf.html` actualizado.
    - *AC:* `[ ]` Ninguna palabra dentro o alrededor del reloj fenológico aparece cortada ni superpuesta; `[ ]` El reloj ocupa $\ge 25\%$ más de área útil tras retirar los banners superiores redundantes; `[ ]` El panel derecho muestra las 3 reglas en formato visual escaneable.
    - *Tests:* **Unitario:** Verificar nombres completos (`Floración`, `Llenado`, `Cosecha`) y cálculo de radio dinámico en el Canvas/SVG. **Simulación de Usuario:** Hacer clic en las 3 ventanas del reloj a 1366×768 y comprobar cero solapamientos.
  - **T9.3.4 — Diapo 23 (`23_precisi_n_actual_y_las_tres_trampas.html`): Eliminación de Scrollbar, Corrección de Solape en "Prueba de Fuego" y Tarjetas `❌ Error vs ✅ Remedio`**
    - *Objetivo:* Eliminar la barra de scroll vertical izquierda, corregir el botón `"Ir al Caso Jaén →"` que pisaba el texto de `"🔥 LA PRUEBA DE FUEGO"`, y formatear las 3 trampas del stack con contraste visual directo `❌ Error Ingenuo` vs `✅ Remedio Biofísico`.
    - *Entregable:* `23_precisi_n_actual_y_las_tres_trampas.html` actualizado.
    - *AC:* `[ ]` Cero barra de scroll vertical en la columna izquierda a 1366×768; `[ ]` El botón `"Ir al Caso Jaén →"` está alineado en su propia columna flex/grid sin tocar el texto adyacente; `[ ]` Las 3 tarjetas derechas caben holgadamente sin truncar líneas.
    - *Tests:* **Unitario:** Verificar `boundingClientRect` de `#fireTestBox` y su botón hijo sin intersección de cajas de texto. **Simulación de Usuario:** Captura a 1366×768 de Diapo 23 verificando encaje limpio de todos los bordes.

### SF9.4 — Compilación del Deck Maestro y Auditoría Visual Multi-Resolución
- **Micro-objetivo:** Integrar los 12 prototipos rediseñados en `presentacion.html` e `index.html` y certificar con pruebas automatizadas y capturas en Chromium headless el cumplimiento del 100% de los criterios visuales.
- **Entregables:** `presentacion.html`, `index.html`, `scripts/audit_f9_desaturacion.py` y reporte de capturas verificadas en `screenshots/`.
- **Estrategia de Pruebas de SF9.4:**
  - **Test Unitario:** Ejecución de `scripts/audit_f9_desaturacion.py` validando conteos de palabras, ausencia de `.speaker-box` largos y compilación limpia de `back/build_deck.py`.
  - **Test de Simulación de Usuario:** Suite de capturas en Chromium headless a `1366×768` y `1920×1080` para las Diapos 5–11 y 19–23 verificando `0` scrollbars y `0` solapamientos.
- **Tareas de SF9.4:**
  - **T9.4.1 — Compilación Integral del Deck Offline (`back/build_deck.py`) y Verificación de Notas del Orador**
    - *Objetivo:* Compilar `presentacion.html` e `index.html` embebiendo en Base64 los 12 prototipos optimizados y las notas actualizadas de `front/deck_notes.py`.
    - *Entregable:* `presentacion.html` e `index.html` regenerados y sincronizados.
    - *AC:* `[ ]` `.venv/bin/python back/build_deck.py` termina con código `0`; `[ ]` Los 12 iframes cargan sus nuevas versiones Base64 sin errores de consola.
    - *Tests:* **Unitario:** Comprobar que los hashes Base64 en `presentacion.html` coinciden con los archivos de `docs/notebooklm/seccion_1/prototipos/` y `seccion_3/prototipos/`. **Simulación de Usuario:** Navegar de la Diapo 1 a la 30 en navegador headless sin errores de consola.
  - **T9.4.2 — Auditoría Automatizada DOM + Capturas Chromium (1366×768 y 1920×1080)**
    - *Objetivo:* Ejecutar `scripts/audit_f9_desaturacion.py` y capturar las vistas de las Diapos 5–11 y 19–23 en ambas resoluciones para certificar cero desbordes y alta claridad explicativa.
    - *Entregable:* Script `scripts/audit_f9_desaturacion.py` en verde y capturas `screenshots/f9_s{5..11,19..23}_{1366,1920}.png`.
    - *AC:* `[ ]` `audit_f9_desaturacion.py` reporta 0 violaciones de longitud o scroll; `[ ]` Las 24 capturas PNG confirman visualmente la ausencia de saturación textual y de solapamientos.
    - *Tests:* **Unitario:** Ejecución de `pytest` / `.venv/bin/python scripts/audit_f9_desaturacion.py`. **Simulación de Usuario:** Revisión visual de las capturas generadas a 1366×768 y 1920×1080.

---

## 7. Apéndice A — Definition of Done (DoD) Global

Toda Tarea de este Plan Maestro se considera completada (`[X]`) única y exclusivamente cuando cumple todos los requisitos siguientes:
1. **Tests Unitarios en verde:** Validación aislada de la estructura HTML/CSS/JS, límites de palabras y compilación de `back/build_deck.py` sin errores.
2. **Tests de Simulación de Usuario en verde:** Verificación en navegador real/headless a `1366×768` (laptop estándar) y `1920×1080` (FHD) confirmando `scrollHeight <= clientHeight` (cero barras de scroll internas), cero solapamientos de texto/botones y funcionamiento fluido de todos los controles interactivos y atajos de teclado (`1–4`, `←`, `→`, `N`).
3. **Integridad de Datos Reales:** Ninguna cifra científica o empírica (SENAMHI, MIDAGRI, MODIS, ERA5, citas de papers) es alterada ni inventada durante la síntesis textual.
4. **Autonomía Offline 100%:** `presentacion.html` e `index.html` funcionan sin conexión a internet con todos los prototipos codificados en Base64.
5. **Trazabilidad documental:** El progreso se actualiza respetando el invariante de roll-up en `docs/task/tareas.md` y el archivo de fase correspondiente.

