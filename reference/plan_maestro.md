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
- **Entregable:** `data/benchmark_punchana.csv` y `notebooks/01_clima_senamhi.ipynb`.

---

## 4. Práctica B — Rendimiento de Café con Datos Reales (Jaén, Cajamarca)

- **Protocolo Anti-Invención (Opción A):**
  - **Rendimiento Objetivo:** Serie histórica oficial de café para la provincia de Jaén reportada por MIDAGRI / SIEA (meta: 2000–2024).
  - **Predictores Satelitales Reales:** MODIS MOD13Q1 (250m, 16d, 2000–2024) y Sentinel-2 L2A (10–20m, 2017–2024) vía Planetary Computer, filtrando píxeles por máscara de calidad QA dentro de la zona cafetalera.
  - **Predictores Climáticos Reales:** Reanálisis ERA5 vía Open-Meteo Archive para las coordenadas de Jaén.
  - **Ventana Fenológica:** Floración (Ago–Oct), Llenado (Nov–Feb), Cosecha (Mar–Jul).
- **Modelos:** Tendencia (M1), Solo NDVI (M2), Solo Clima (M3), Fusión Satélite + Clima (M4).
- **Validación Principal:** Ventana temporal expansiva (entrenar con $\le t-1$, predecir $t$).
- **Entregables:** `data/cafe_jaen_campanias.csv`, `data/cafe_jaen_resultados.csv` y `notebooks/02_cafe_ndvi.ipynb`.

---

## 5. Fases de Ejecución del Proyecto

1. **F1: Depuración y Setup** (`reference/fases/fase_1_depuracion_setup.md`) — Aislar material sintético a `data/deprecated/`, crear `SOURCES.md`, instalar dependencias.
2. **F2: Caso B con Datos Reales** (`reference/fases/fase_2_cafe_datos_reales.md`) — Descargar SIEA/MIDAGRI, extraer MODIS/S2 y ERA5, evaluar hipótesis H1–H4.
3. **F3: Caso A Benchmark Iquitos** (`reference/fases/fase_3_benchmark_iquitos_fm.md`) — Ejecutar 8 modelos, test Diebold-Mariano, exportar CSVs de benchmark.
4. **F4: Experimentos y Citas** (`reference/fases/fase_4_experimentos_narrativa.md`) — Experimento propio de no-extrapolación, redactar Frases-clave ⏳ y validar con el usuario.
5. **F5: Refactorización del Deck** (`reference/fases/fase_5_deck_20_slides.md`) — Generar `presentacion.html` de 20 diapositivas conectadas a CSVs reales.
6. **F6: QA, Ensayo y Bitácora** (`reference/fases/fase_6_qa_ensayo.md`) — Auditoría 1920x1080 / 1366x768, ensayo 35 min, bitácora `docs/logs/log.md`.
