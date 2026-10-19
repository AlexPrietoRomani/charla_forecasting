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
10. **F10: Motor de Normalización de Estilos en el Compilador y Homologación Visual-Tipográfica de Diapositiva Real (Secciones 1, 2 y 3)** (`docs/task/fases/fase_10_motor_estilos_y_homologacion_s1_s2_s3.md`) — Creación de `front/prototype_engine.py` en `back/build_deck.py` para inyectar contrato de altura 100%, tipografía fluida de auditorio (`clamp()`), distribución anti-vacíos y `ResizeObserver` universal en los 18 prototipos (Diapos 5–17 y 19–23) y futuros HTMLs.
11. **F11: Videos Deterministas por Diapositiva (Pipeline Offline + Estructura `video/`)** (`docs/task/fases/fase_11_videos_por_diapositiva.md`) — Pipeline offline reproducible (skill `motion-design` → escena HTML determinista → captura CDP frame a frame → `ffmpeg` H.264) con estructura autocontenida `video/seccion_{N}/diapo_{M}/video_{nombre}/`; piloto `video_anatomia_senal` (Diapo 5) completado como entrada de 30 s (tramo `[4 s, 27 s]` de la escena cinemática estirado ×1.30) a 1920×1080 con fade-in al fondo exacto del slide.

---

## 6. Detalle de la Fase 9 (F9): Desaturación Cognitiva y Rediseño Pedagógico-Visual de Secciones 1 y 3

- **Macro-objetivo:** Eliminar la saturación de texto, barras de scroll verticales y solapamientos gráficos en los 12 prototipos interactivos de la **Sección 1 (Diapos 5 a 11)** y la **Sección 3 (Diapos 19 a 23)**, aplicando el estándar gerencial alcanzado en la Sección 2: reemplazar paredes de texto y guiones de orador en pantalla por síntesis ejecutiva escaneable y diagramas visuales auto-explicativos (*"Show, Don't Tell"*).
- **Entregable global:** Los 12 archivos HTML en `docs/notebooklm/seccion_1/prototipos/` y `docs/notebooklm/seccion_3/prototipos/` refactorizados, notas completas trasladadas a `front/deck_notes.py`, y bundles `presentacion.html` e `index.html` compilados sin barras de scroll internas ni solapamientos en 1366×768 y 1920×1080.
- **Criterios de Aceptación (AC) globales de F9:**
  - [X] Cero bloques `.speaker-box` ("Guía de Exposición") de múltiples líneas visibles en los prototipos; reemplazados por una píldora ejecutiva `.executive-takeaway` de 1 línea ($\le 15$ palabras).
  - [X] Reducción $\ge 40\%$ en el conteo de palabras de `.narrative-card` ($\le 110$ palabras por etapa), logrando `scrollHeight <= clientHeight` (cero barras de scroll verticales) en 1366×768 y 1920×1080.
  - [X] Cero solapamientos o recortes gráficos en los lienzos Canvas/SVG/DOM de las Diapos 11, 20, 21, 22 y 23.
  - [X] Todos los lienzos de las Diapos 5–11 y 19–23 incluyen anotaciones visuales pedagógicas directas (cotas, conectores animados, medidores de barra o zonas coloreadas de umbral) que explican el fenómeno sin depender de párrafos largos.

---

## 7. Detalle de la Fase 10 (F10): Motor de Normalización de Estilos en el Compilador y Homologación Visual-Tipográfica de Diapositiva Real (Secciones 1, 2 y 3)

- **Macro-objetivo:** Transformar las 18 diapositivas interactivas de las Secciones 1 (Diapos 5–11), 2 (Diapos 12–17) y 3 (Diapos 19–23) en **diapositivas reales de auditorio** (tipografía amplia y legible a distancia, ocupación exacta del 100% del alto sin franjas ni huecos negros, lienzos derechos con relación de aspecto armónica auto-ajustable en cualquier laptop y formato 100% unificado) mediante un **Motor de Normalización de Prototipos (`front/prototype_engine.py`)** dentro de `back/build_deck.py` y el ajuste fino de los 18 archivos HTML.
- **Entregable global:** Módulo `front/prototype_engine.py` integrado en `back/build_deck.py`, los 18 prototipos HTML de las Secciones 1, 2 y 3 homologados, validador `scripts/audit_f10_layout_typography.py` en verde y bundles `presentacion.html` e `index.html` verificados con 36 capturas en `1920×1080` y `1366×768`.
- **Criterios de Aceptación (AC) globales de F10:**
  - [ ] `front/prototype_engine.py` procesa e inyecta automáticamente las reglas de altura 100%, escala tipográfica de presentación, distribución anti-vacíos y `ResizeObserver` universal en todos los HTMLs embebidos por `back/build_deck.py` (actuales y futuros).
  - [ ] Las 18 diapositivas (`5–11`, `12–17`, `19–23`) ocupan el 100% de la altura del contenedor (`#slideFrame.clientHeight >= window.innerHeight * 0.98`), eliminando el colapso del 38% en la Diapo 5 y las franjas inferiores en las demás.
  - [ ] La tipografía explicativa alcanza escala real de diapositiva (`narr-title` $\ge 19\text{px}$, `narr-lead` $\ge 14\text{px}$, cuerpo de bloques $\ge 13\text{px}$ en 1080p) y los bloques se distribuyen sin huecos negros vacíos ni barras de scroll verticales (`scrollHeight <= clientHeight + 2`).
  - [ ] Las 18 diapositivas comparten el mismo estándar de cabecera, barra de 4 etapas, tarjeta narrativa y píldora `💡 Idea Clave` de 1 línea, con cero solapamientos en gráficos Canvas/DOM.
- **Estrategia de Pruebas de F10:**
  - **Test Unitario:** `scripts/audit_f10_layout_typography.py` que verifica el procesamiento de `front/prototype_engine.py`, la ausencia de `"GUÍA DE EXPOSICIÓN"` en los 18 prototipos y las reglas CSS/JS inyectadas.
  - **Test de Simulación de Usuario:** Auditoría en Chromium headless a `1920×1080` y `1366×768` midiendo altura al 100%, tamaños de fuente mínimos, cero scrollbars y generando las 36 capturas `screenshots/f10_s*_{1366,1920}.png`.

### SF10.1 — Creación del Motor de Normalización e Inyección de Estilos en el Compilador (`front/prototype_engine.py` + `back/build_deck.py`)
- **Micro-objetivo:** Construir un pipeline de preprocesamiento HTML/CSS/JS en el motor de compilación para que `back/build_deck.py` no incruste archivos HTML en crudo, sino que aplique automáticamente un tema maestro de diapositiva real, normalice componentes heredados y garantice adaptabilidad responsiva.
- **Entregables:** `front/prototype_engine.py` creado e integrado en `back/build_deck.py`.
- **Estrategia de Pruebas de SF10.1:**
  - **Test Unitario:** Test de transformación sobre un HTML verificando que inyecta `#deck-engine-override-css` y `#deck-engine-runtime-js`.
  - **Test de Simulación de Usuario:** Compilar el deck con `back/build_deck.py` y verificar en Chromium que todos los iframes contienen el estilo y runtime del motor.
- **Tareas de SF10.1:**
  - **T10.1.1 — Implementar `front/prototype_engine.py` con CSS Maestro de Diapositiva Real, Normalizador DOM y Runtime Responsivo**
    - *Objetivo:* Crear el módulo `front/prototype_engine.py` que inyecta `#deck-engine-override-css`, limpia patrones obsoletos y añade `#deck-engine-runtime-js`.
    - *Entregable:* `front/prototype_engine.py`.
    - *AC:* `[ ]` Expone `normalize_prototype_html()` y `load_prototype_b64()`; `[ ]` Fuerza `height: 100%`, tipografía de auditorio y `is-embedded` automático.
    - *Tests:* **Unitario:** Validar inyección CSS/JS en string HTML. **Simulación de Usuario:** Comprobar en Chromium que la Diapo 5 llena el 100% del alto.
  - **T10.1.2 — Conectar `front/prototype_engine.py` en `back/build_deck.py` con Soporte Automático Multi-Sección**
    - *Objetivo:* Reemplazar todas las lecturas crudas `base64.b64encode(path.read_bytes())` en `back/build_deck.py` por llamadas a `load_prototype_b64()`.
    - *Entregable:* `back/build_deck.py` actualizado.
    - *AC:* `[ ]` Los 18 prototipos pasan por `load_prototype_b64()`; `[ ]` `back/build_deck.py` compila con código `0`.
    - *Tests:* **Unitario:** Verificar con grep que los 18 prototipos usan `load_prototype_b64`. **Simulación de Usuario:** Cargar `presentacion.html` y verificar ausencia de errores de consola.
  - **T10.1.3 — Inyección Automática de Entrada Cinemática de Video (`#cinematicVideoGate`) y Handoff Sin Costura (`#040714`) en `front/prototype_engine.py` (Sinergia F10 ↔ F11)**
    - *Objetivo:* Detectar automáticamente cualquier video en `video/seccion_{N}/diapo_{M}/video_*/` e inyectar la compuerta `#cinematicVideoGate` como Etapa 0 dentro de la misma diapositiva (con handoff sobre `#040714` y botón `"🎬 Intro"` en `.flowbar`).
    - *Entregable:* `discover_slide_video()` e inyección de `#cinematicVideoGate` en `front/prototype_engine.py`.
    - *AC:* `[ ]` Al avanzar de la Diapo $M-1 \to M$, el video se presenta primero dentro de la misma Diapo $M$ sin alterar el contador de 30 diapositivas y luego da paso al simulador interactivo.
    - *Tests:* **Unitario:** Validar `discover_slide_video(ROOT, 1, 5)` y presencia de `#cinematicVideoGate`. **Simulación de Usuario:** Comprobar transición Diapo 4 → Diapo 5 (video → simulador) en Chromium.

### SF10.2 — Reparación de Altura, Proporción 2D/3D y Escalado Tipográfico en la Sección 1 (Diapositivas 5 a 11)
- **Micro-objetivo:** Corregir la Diapositiva 5 (aplastada al 62% superior con etiquetas 3D superpuestas) y homologar las Diapositivas 6 a 11 con tipografía de auditorio y cero huecos negros izquierdos.
- **Entregables:** Los 7 prototipos en `docs/notebooklm/seccion_1/prototipos/` (`5` a `11`) actualizados.
- **Estrategia de Pruebas de SF10.2:**
  - **Test Unitario:** Verificar `html, body { height: 100% }` y `is-embedded` en los 7 archivos HTML de la Sección 1.
  - **Test de Simulación de Usuario:** Capturas en Chromium a `1920×1080` y `1366×768` de las Diapos 5 a 11.
- **Tareas de SF10.2:**
  - **T10.2.1 — Diapo 05 (`5_Anatomia_de_la_senal_temporal_v3.html`): Corrección del Colapso Vertical (62% → 100%), Proporción 2D/3D y Separación de Etiquetas 3D**
    - *Objetivo:* Activar `is-embedded` y `height: 100%` en la Diapo 5, equilibrar `.visual-column` (`42% / 58%`) y separar con pastillas anti-colisión las 5 etiquetas 3D.
    - *Entregable:* `5_Anatomia_de_la_senal_temporal_v3.html` corregido.
    - *AC:* `[ ]` Ocupa el 100% de la altura; `[ ]` Las 5 etiquetas 3D (`Y(t)`, `T(t)`, `S(t)`, `C(t)`, `ε(t)`) tienen separación mínima de `18px` y pastilla oscura sin pisarse.
    - *Tests:* **Unitario:** Comprobar algoritmo anti-colisión `labelItems` y `is-embedded`. **Simulación de Usuario:** Inspeccionar `f10_s5_{1366,1920}.png`.
  - **T10.2.2 — Diapos 06, 07, 08, 09, 10 y 11 (`6_Era_1...` a `11_Arquitectura...`): Tipografía de Auditorio, Cero Huecos Negros Izquierdos y Etiquetas de Canvas Más Grandes**
    - *Objetivo:* Eliminar la franja vacía inferior y el hueco negro del 45% en `.narrative-card` en las Diapos 6 a 10, escalar fuentes de columna izquierda y Canvas (`ctx.font`), y equilibrar las 4 columnas de la Diapo 11.
    - *Entregable:* Prototipos `6` a `11` actualizados.
    - *AC:* `[ ]` 100% de altura sin franja inferior; `[ ]` `.narr-blocks` distribuido con `flex: 1; justify-content: space-evenly` y fuentes de `13px–16px`.
    - *Tests:* **Unitario:** Verificar reglas CSS y fuentes de Canvas en prototipos 6–11. **Simulación de Usuario:** Inspeccionar `f10_s{6..11}_{1366,1920}.png`.

### SF10.3 — Homologación Visual, Eliminación de Solapes y Unificación de Formato en la Sección 2 (Diapositivas 12 a 17)
- **Micro-objetivo:** Unificar las Diapos 12 a 17 con el mismo formato gerencial y tipográfico de las Secciones 1 y 3, eliminando los `.speaker-box` antiguos en Diapos 12–15, el solape `38.0 °C` en Diapo 12 y el vacío del 50% derecho en Diapos 16–17.
- **Entregables:** Los 6 prototipos en `docs/notebooklm/seccion_2/prototipos/` (`12` a `17`) homologados.
- **Estrategia de Pruebas de SF10.3:**
  - **Test Unitario:** `grep -c "GUIA DE EXPOSICION\|GUÍA DE EXPOSICIÓN" docs/notebooklm/seccion_2/prototipos/*.html` retorna `0`.
  - **Test de Simulación de Usuario:** Capturas en Chromium a `1920×1080` y `1366×768` de las Diapos 12 a 17.
- **Tareas de SF10.3:**
  - **T10.3.1 — Diapos 12, 13, 14 y 15 (`12_Caso_1...` a `15_Benchmark...`): Reemplazo de `.speaker-box` por `💡 Idea Clave`, Corrección del Solape `38.0 °C` en Diapo 12 y Tipografía de Auditorio**
    - *Objetivo:* Sustituir `"🎙️ GUÍA DE EXPOSICIÓN"` por `.executive-takeaway` (`💡 Idea Clave`) en las Diapos 12–15, separar el badge `"RÉCORD 38.0 °C"` de los puntos en la Diapo 12 y eliminar huecos vacíos izquierdos.
    - *Entregable:* Prototipos `12`, `13`, `14` y `15` actualizados.
    - *AC:* `[ ]` Cero `"GUÍA DE EXPOSICIÓN"` en Diapos 12–15; `[ ]` Etiqueta `38.0 °C` sin colisión en Diapo 12; `[ ]` Columna izquierda rellena al 100% con letra grande.
    - *Tests:* **Unitario:** Validar ausencia de `"GUÍA DE EXPOSICIÓN"` y longitud de `quote` $\le 16$ palabras. **Simulación de Usuario:** Inspeccionar `f10_s{12..15}_{1366,1920}.png`.
  - **T10.3.2 — Diapos 16 y 17 (`16_Pronostico_7_Dias...` y `17_Pipeline_Codigo...`): Eliminación del 50% de Vacío Derecho, Escalado de Código/KPIs y Homologación Visual**
    - *Objetivo:* Hacer que las tarjetas derechas de las Diapos 16 y 17 y el bloque de código Python ocupen el 100% de la altura con tipografía de auditorio (`13.5px–16px`).
    - *Entregable:* Prototipos `16` y `17` actualizados.
    - *AC:* `[ ]` Cero vacío negro en la mitad inferior derecha de las Diapos 16 y 17; `[ ]` Código Python en Diapo 17 con fuente `clamp(13px, 1.02vw, 15.5px)`.
    - *Tests:* **Unitario:** Verificar reglas flex y tamaños de fuente en prototipos 16 y 17. **Simulación de Usuario:** Inspeccionar `f10_s{16,17}_{1366,1920}.png`.

### SF10.4 — Escalado Tipográfico, Limpieza de Elementos Residuales y Relleno Armónico en la Sección 3 (Diapositivas 19 a 23)
- **Micro-objetivo:** Limpiar la cita larga y banners residuales en el HTML inicial de la Diapo 19, eliminar los huecos negros izquierdos en las Diapos 19 a 23 y rellenar con tipografía grande las tarjetas derechas de las Diapos 22 y 23.
- **Entregables:** Los 5 prototipos en `docs/notebooklm/seccion_3/prototipos/` (`19` a `23`) actualizados.
- **Estrategia de Pruebas de SF10.4:**
  - **Test Unitario:** Verificar HTML estático de `#speakerQuote` en Diapo 19 ($\le 15$ palabras) y reglas de fuentes en Diapos 19–23.
  - **Test de Simulación de Usuario:** Capturas `f10_s{19..23}_{1366,1920}.png`.
- **Tareas de SF10.4:**
  - **T10.4.1 — Diapos 19, 20 y 21 (`19_c_mo_el_agro...`, `20_del_almanaque...`, `21_f_sica_biol_gica...`): Limpieza Inicial de Diapo 19, Escalado Tipográfico y Gráficos a Altura Completa**
    - *Objetivo:* Sincronizar el HTML inicial de `#speakerQuote` y ocultar `.canvas-split-hint` en Diapo 19, asegurar `height: 100%` en `html, body` y escalar fuentes en Diapos 19, 20 y 21.
    - *Entregable:* Prototipos `19`, `20` y `21` actualizados.
    - *AC:* `[ ]` Diapo 19 muestra `💡 Idea Clave` de 1 línea y cero `.canvas-split-hint` desde el inicio; `[ ]` Columna izquierda sin huecos negros en Diapos 19–21.
    - *Tests:* **Unitario:** Validar `#speakerQuote` estático en Diapo 19. **Simulación de Usuario:** Inspeccionar `f10_s{19,20,21}_{1366,1920}.png`.
  - **T10.4.2 — Diapos 22 y 23 (`22_reloj_fenol_gico...` y `23_precisi_n_actual...`): Relleno Visual y Tipografía Grande en las Tarjetas Derechas de Diagnóstico y de las 3 Trampas**
    - *Objetivo:* Subir el tamaño de letra (`14px–16.5px`) y centrar el contenido de las 3 cajas derechas de la Diapo 22 y de las 3 tarjetas de trampas de la Diapo 23, eliminando el 70% de hueco vacío interno.
    - *Entregable:* Prototipos `22` y `23` actualizados.
    - *AC:* `[ ]` Cajas derechas en Diapos 22 y 23 rellenas armónicamente con letra grande y píldora de remedio destacada.
    - *Tests:* **Unitario:** Verificar reglas CSS de `.diag-item` y `.trap-card`. **Simulación de Usuario:** Inspeccionar `f10_s{22,23}_{1366,1920}.png`.

### SF10.5 — Compilación del Deck Maestro y Auditoría Automatizada Multi-Resolución (`1920×1080` y `1366×768`)
- **Micro-objetivo:** Compilar `presentacion.html` e `index.html` mediante el nuevo motor, ejecutar `scripts/audit_f10_layout_typography.py` y certificar las 36 capturas (`18 diapos × 2 resoluciones`).
- **Entregables:** `scripts/audit_f10_layout_typography.py`, `presentacion.html`, `index.html` y `screenshots/f10_s{5..17,19..23}_{1366,1920}.png`.
- **Estrategia de Pruebas de SF10.5:**
  - **Test Unitario:** `.venv/bin/python scripts/audit_f10_layout_typography.py`.
  - **Test de Simulación de Usuario:** Generación y revisión de las 36 capturas en Chromium headless.
- **Tareas de SF10.5:**
  - **T10.5.1 — Crear y Ejecutar `scripts/audit_f10_layout_typography.py` y Capturar las 36 Vistas en Chromium (`1920×1080` y `1366×768`)**
    - *Objetivo:* Validar automáticamente los 18 prototipos y el motor de estilos, compilar el deck y generar las 36 capturas finales.
    - *Entregable:* `scripts/audit_f10_layout_typography.py` en verde y 36 capturas PNG.
    - *AC:* `[ ]` `audit_f10_layout_typography.py` retorna `0`; `[ ]` Las 36 capturas confirman aspecto de diapositiva real al 100% de altura sin solapamientos.
    - *Tests:* **Unitario:** Ejecución de `scripts/audit_f10_layout_typography.py`. **Simulación de Usuario:** Inspección visual de `screenshots/f10_s*_{1366,1920}.png`.

---

## 8. Detalle de la Fase 11 (F11): Videos Deterministas por Diapositiva (Pipeline Offline + Estructura `video/`)

- **Macro-objetivo:** Producir videos explicativos deterministas (repetición exacta frame a frame) para reemplazar o acompañar zonas visuales de cualquier diapositiva del deck, con un pipeline 100% offline (sin red ni servicios externos) y todo el material fuente versionado junto al MP4 para poder re-renderizarlo en un solo comando.
- **Entregable global:** Pipeline local (`build_scene.py` → `scene.html` → `capture.mjs` vía CDP → `render.sh` → `ffmpeg` H.264 `yuv420p` `+faststart`), estructura autocontenida `video/seccion_{N}/diapo_{M}/video_{nombre}/` (escena, capturador, fuentes woff2 y MP4), piloto `video_anatomia_senal` (Diapo 5, `30 s`, `900 frames`, `1920×1080`) y backlog planificado en `SF11.4` con 6 fichas de producción adicionales:
  - **Prioridad Alta:** `video_agro_origen` (Sección 3 · Diapo 19, candidato #1 para `SF11.3`), `video_puente_tabular` (Sección 1 · Diapo 07) y `video_fisica_biologica` (Sección 3 · Diapo 21).
  - **Prioridad Media:** `video_zero_shot_tsfm` (Sección 1 · Diapo 09) y `video_cono_incertidumbre` (Sección 1 · Diapo 10).
  - **Prioridad Baja (Opcional):** `video_sintesis_cierre` (Sección 5 · Diapo 29, `25 s` / `750 frames`).
- **Criterios de Aceptación (AC) globales de F11:**
  - [X] `render.sh` regenera el MP4 sin intervención manual y `ffprobe` valida 1920×1080 @ 30 fps, 900 frames, H.264 `yuv420p` `+faststart`.
  - [X] Los videos no viven en `docs/`; cada video es dueño de sus fuentes y del MP4 final dentro de `video/seccion_{N}/diapo_{M}/video_{nombre}/`.
  - [X] Cifras canónicas auditadas dentro del video (récord 38.0 °C del 07·10·2023, n = 2,557 días, S ±1.37 °C, σ del residuo 2.18 °C, y datos verificados de `data/caso_1/` y `data/caso_2/`).
  - [ ] Decisión de integración del piloto en la Diapo 5 (reproducción como entrada al avanzar de la Diapo 4 a la 5 mediante `#cinematicVideoGate` en `T10.1.3`) y verificación del handoff con la diapositiva real.
  - [ ] Segundo video piloto en otra sección (`SF11.3`) y producción del inventario de fichas en `SF11.4` (`T11.4.1` a `T11.4.6`).

---

## 9. Apéndice A — Definition of Done (DoD) Global

Toda Tarea de este Plan Maestro se considera completada (`[X]`) única y exclusivamente cuando cumple todos los requisitos siguientes:
1. **Tests Unitarios en verde:** Validación aislada de la estructura HTML/CSS/JS, inyección del motor `front/prototype_engine.py`, límites de palabras y compilación de `back/build_deck.py` sin errores.
2. **Tests de Simulación de Usuario en verde:** Verificación en navegador real/headless a `1366×768` (laptop estándar) y `1920×1080` (FHD) confirmando 100% de ocupación vertical (`#slideFrame`), escala tipográfica de auditorio, `scrollHeight <= clientHeight` (cero barras de scroll internas), cero solapamientos de texto/botones y funcionamiento fluido de todos los controles interactivos y atajos de teclado (`1–4`, `←`, `→`, `N`).
3. **Integridad de Datos Reales:** Ninguna cifra científica o empírica (SENAMHI, MIDAGRI, MODIS, ERA5, citas de papers) es alterada ni inventada durante la síntesis textual.
4. **Autonomía Offline 100%:** `presentacion.html` e `index.html` funcionan sin conexión a internet con todos los prototipos procesados y codificados en Base64.
5. **Trazabilidad documental:** El progreso se actualiza respetando el invariante de roll-up en `docs/task/tareas.md` y el archivo de fase correspondiente.


