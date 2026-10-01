# Estructura Expandida — ¿Puede la IA predecir el futuro? (25 slides, estilo Data_Wizard + HyperFrames)

Deck interactivo en un solo archivo `presentacion.html` (Chart.js + PapaParse + Leaflet satelital con capas/heatmaps + diagramas SVG interactivos, layout full-bleed borde a borde, modo claro/oscuro, soporte offline).

---

### Bloque 1: Introducción y Taxonomía Global
1. **Portada & Gancho:** ¿Puede la IA predecir el futuro? Lecciones de forecasting, teledetección multiespectral y cuantificación de incertidumbre.
2. **Anatomía de una Serie Temporal:** Descomposición ontológica desde cero: Tendencia ($T_t$), Ciclo ($C_t$), Estacionalidad ($S_t$) y Ruido/Innovación ($\epsilon_t$).
3. **El Gran Mapa de los 4 Paradigmas:** Taxonomía completa: 
   - Paradigma 1: Curvas Paramétricas y Descomposición Estadística.
   - Paradigma 2: ML Tabular & Deep Learning Secuencial.
   - Paradigma 3: Biofísica Satelital & Visión Computacional.
   - Paradigma 4: Modelos Físicos Globales, AI Weather (GraphCast) & Foundation Zero-Shot.

---

### Bloque 2: Explicación Profunda de Familias de Modelos (de Cero a la Frontera)
4. **Paradigma 1 (Curvas y Suavizado):** Crecimiento exponencial, curva logística / sigmoide y suavizado exponencial de Holt-Winters (nivel, tendencia, estacionalidad aditiva/multiplicativa).
5. **Paradigma 1 (Descomposición y Clásicos):** El mecanismo autorregresivo y de medias móviles en ARIMA / SARIMAX y GAM bayesiano en Prophet. Fortalezas en horizontes cortos vs límites ante no-linealidad.
6. **Paradigma 2 (El Puente Tabular):** ¿Cómo convierte un árbol el tiempo en tabla? Diagrama animado de ventana deslizante (*lags* 1-14, rolling stats, calendario cíclico) y partición ortogonal del espacio de estados.
7. **Paradigma 2 (La Patología de No-Extrapolación):** Por qué un Random Forest o Gradient Boosting se "aplana" y es incapaz de extrapolar tendencias fuera de su rango histórico de entrenamiento (falla fatal ante inflación o cambio climático).
8. **Paradigma 2 (Deep Learning Secuencial):** De celdas recurrentes LSTM (compuertas de olvido, entrada y estado de celda) a parches de auto-atención en PatchTST (Nie et al., ICLR 2023).
9. **Paradigma 2 (Análisis Crítico de Redes):** El mito del deep learning en una sola serie (sobreajuste y costo 100x innecesario) vs su verdadero poder en transferencia cruzada multivariada masiva (TFT / DeepAR).
10. **Paradigma 3 (Visión por Computador en el Agro):** Del píxel a la cosecha: YOLOv12 (atención por área A2 y conteo en 1.6 ms), SAM 2.1 (segmentación automática de copa) y DINOv2 (representación autosupervisada).
11. **Paradigma 3 (Biofísica Satelital & Saturación Espectral):** La curva espectral de la hoja (absorción en Rojo B04 vs dispersión en NIR B08). Fórmulas de AgroVisión (NDVI, EVI, NDRE, NDWI) y la curva física de saturación asintótica del NDVI cuando LAI > 3.
12. **Paradigma 3 (Fusión Multimodal Biofísica):** Acoplamiento biofísico: Espectro + Balance Hídrico (Open-Meteo) segmentado por las 3 ventanas fenológicas del café (Floración, Llenado, Cosecha).
13. **Paradigma 4 (Modelos Físicos Globales y Supercómputo):** Cómo pronostican las grandes agencias meteorológicas: Ecuaciones de Navier-Stokes y asimilación de datos (4D-Var) en supercomputadores (NOAA GFS de EE.UU., ECMWF IFS de Europa, DWD ICON de Alemania).
14. **Paradigma 4 (La Disparidad en Vivo - Caso Iquitos):** Comparativa directa de pronósticos a 7 días extraídos vía Open-Meteo para las coordenadas de Iquitos: discrepancia de ~8 °C entre la ola de calor proyectada por NOAA GFS (~37 °C) y la contención de ECMWF (~29 °C).
15. **Paradigma 4 (La Revolución AI Weather & Zero-Shot):** El quiebre de paradigma: GraphCast de Google DeepMind (GNNs sobre mallas icosaédricas que baten a ECMWF en 60 segundos con 1 GPU) y Modelos Fundacionales Zero-Shot (TimesFM de Google y Chronos de Amazon) con tokenización de parches.

---

### Bloque 3: Casos Reales en Perú con Mapas y Demos en Vivo
16. **Caso A (SENAMHI Iquitos - Ubicación):** Mapa satelital interactivo Leaflet (Esri World Imagery) de la estación Punchana (`103015`, Loreto, 91 msnm) y zona de influencia térmica.
17. **Caso A (Benchmark Multi-modelo 7 Años):** Tabla comparativa de métricas reales sobre 7 años de datos (2019–2025, 2,557 días) y holdout estricto de 90 días: LSTM (2.097 °C) y ExtraTrees (2.166 °C) baten al Naive (2.315 °C).
18. **Caso A (DEMO 1 EN VIVO):** Gráfico interactivo Chart.js leyendo `data/senamhi_forecast_7d.csv`: curvas multi-modelo y bandas de incertidumbre al 90% (±1.645 $\sigma$).
19. **Caso B (Café & Sentinel-2 Jaén - Ubicación):** Mapa satelital interactivo Leaflet de la finca cafetalera en Jaén (-5.6766°, -78.7742°, 1,100 msnm) con **Visor Interactivo de Capas (Heatmap Switcher)**: Satélite RGB, Heatmap NDVI (saturado), Heatmap EVI (biomasa real) y Heatmap NDRE (nitrógeno).
20. **Caso B (La Evidencia de Campo):** La prueba de las 6 campañas (2020–2025): cómo el NDVI anual plano en 0.788 no detecta el golpe de calor de 2024, mientras que la fusión fenológica acierta con solo 0.26 qq/ha de error.
21. **Caso B (DEMO 2 EN VIVO):** Gráfico interactivo Chart.js leyendo `data/cafe_ndvi_rendimiento.csv`: rendimiento real observado ($qq/ha$) vs modelo de fusión vs modelo estancado de solo NDVI (LOYO cross-validation).

---

### Bloque 4: Síntesis Operativa, Decisiones y Cierre
22. **5 Lecciones desde las Trincheras:** 1) Validación temporal obligatoria, 2) Árboles antes que redes neuronales, 3) El costo del error no es simétrico, 4) Respetar la física del sensor satelital, 5) Interpretabilidad operativa.
23. **Árbol de Decisión Práctico:** Matriz de selección de modelos para entornos de producción según volumen de datos, latencia y tolerancia al riesgo.
24. **Cierre Filosófico:** La IA no predice el futuro: cuantifica incertidumbre para habilitar decisiones estratégicas.
25. **Gracias & Referencias:** Repositorio de código abierto, notebooks reproducibles y bibliografía BibTeX (`refs.bib`).

---

### Motor HyperFrames (GSAP 3.12.5, implementado en `scripts/build_deck.py`)
Slides animadas (11): 01, 02, 04, 06, 07, 08, 10, 11, 12, 15, 24.
Coreografía por defecto: header (t=0) → panel izq (t≈1s) → panel der (t≈2s) → KPIs/callouts.
Controles de presentador por slide: `Narrar: Replay | Paso 1-3` + teclas `1/2/3` (pasos), `R` (replay).
Robustez: safety-timer fuerza `timeline.progress(1)` a los 2.6s (anti-stall si rAF va lento);
sin GSAP (CDN bloqueado) todo queda visible (fallback). Slides estáticas justificadas:
mapas Leaflet y charts Chart.js en vivo requieren pausa cognitiva + interacción (zoom,
toggle de series, heatmap switcher), superior a una animación pasiva.
