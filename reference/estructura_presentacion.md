# Estructura Expandida — ¿Puede la IA predecir el futuro? (22 slides, estilo Data_Wizard + HyperFrames)

Deck interactivo en un solo archivo `presentacion.html` (Chart.js + PapaParse + Leaflet satelital + diagramas SVG interactivos, modo claro/oscuro, soporte offline).

---

### Bloque 1: Introducción y Taxonomía Global
1. **Portada & Gancho:** ¿Puede la IA predecir el futuro? Lecciones de forecasting, teledetección multiespectral y cuantificación de incertidumbre.
2. **El Gran Mapa de Métodos:** Las 4 familias (ML Tabular, Series Clásicas, DL Secuencial, Visión + Fusión) + Foundation Zero-Shot y el eje de trade-offs.

---

### Bloque 2: Explicación Profunda de Familias de Modelos
3. **ML Tabular (Mecanismo):** ¿Cómo convierte un árbol el tiempo en tabla? Diagrama animado de ventana deslizante (*lags* 1-14, medias móviles, calendario cíclico) y partición ortogonal del espacio.
4. **ML Tabular (Análisis Crítico):** Fortalezas (invarianza a escalas, captura de no linealidades) vs Patología fatal (incapacidad matemática de extrapolar tendencias crecientes fuera de rango histórico).
5. **Series Clásicas (Mecanismo):** Descomposición física del proceso generativo: Tendencia ($T$), Ciclo ($C$), Estacionalidad ($S$) y Choque autorregresivo ($\epsilon_t$) en ARIMA, ETS y Prophet.
6. **Series Clásicas (Análisis Crítico):** Cuándo son imbatibles (horizontes 1-3 días con pocos datos) vs colapso ante intermitencia y múltiples variables exógenas no lineales.
7. **Deep Learning Secuencial (Mecanismo):** De celdas recurrentes LSTM (compuertas de olvido y estado de celda) a parches de auto-atención en PatchTST (Nie et al., ICLR 2023).
8. **Deep Learning (Análisis Crítico):** El mito del deep learning en una sola serie (sobreajuste y costo 100x innecesario) vs su verdadero poder en transferencia cruzada masiva (TFT / DeepAR).
9. **Foundation Models Zero-Shot:** Chronos (Amazon, 2024) y TimesFM (Google, 2024). Tokenización por cuantización numérica y pronóstico en frío (*cold-start*) sin calibración previa.
10. **Visión por Computador en el Agro:** Del píxel a la cosecha: YOLOv12 (atención por área A2 y conteo en 1.6 ms), SAM 2.1 (segmentación automática de copa) y DINOv2 (representación autosupervisada).
11. **Biofísica Satelital & Índices:** La curva espectral de la hoja (absorción en Rojo B04 vs dispersión en NIR B08). Fórmulas de AgroVisión (NDVI, EVI, NDRE, NDWI) y la curva física de saturación del NDVI cuando LAI > 3.
12. **Fusión Multimodal:** Acoplamiento biofísico: Espectro + Balance Hídrico (Open-Meteo) segmentado por las 3 ventanas fenológicas del café (Floración, Llenado, Cosecha).

---

### Bloque 3: Casos Reales en Perú con Mapas y Demos en Vivo
13. **Caso A (SENAMHI Iquitos - Ubicación):** Mapa satelital interactivo Leaflet (Esri World Imagery) de la estación Punchana (`103015`, Loreto, 91 msnm) y zona de influencia térmica.
14. **Caso A (Benchmark Multi-modelo):** Tabla comparativa de métricas reales sobre 7 años de datos (2019–2025) y holdout estricto de 90 días: LSTM (2.097 °C) y ExtraTrees (2.166 °C) baten al Naive (2.315 °C).
15. **Caso A (DEMO 1 EN VIVO):** Gráfico interactivo Chart.js leyendo `data/senamhi_forecast_7d.csv`: curvas multi-modelo y bandas de incertidumbre al 90% (±1.645 $\sigma$).
16. **Caso B (Café & Sentinel-2 Jaén - Ubicación):** Mapa satelital interactivo Leaflet de la finca cafetalera en Jaén (-5.6766°, -78.7742°, 1,100 msnm) con **Visor Interactivo de Capas (Heatmap Switcher)**: Satélite RGB, Heatmap NDVI (saturado), Heatmap EVI (biomasa real) y Heatmap NDRE (nitrógeno).
17. **Caso B (La Evidencia de Campo):** La prueba de las 6 campañas (2020–2025): cómo el NDVI anual plano en 0.788 no detecta el golpe de calor de 2024, mientras que la fusión fenológica acierta con solo 0.26 qq/ha de error.
18. **Caso B (DEMO 2 EN VIVO):** Gráfico interactivo Chart.js leyendo `data/cafe_ndvi_rendimiento.csv`: rendimiento real observado ($qq/ha$) vs modelo de fusión vs modelo estancado de solo NDVI (LOYO cross-validation).

---

### Bloque 4: Síntesis Operativa, Decisiones y Cierre
19. **5 Lecciones desde las Trincheras:** 1) Validación temporal obligatoria, 2) Árboles antes que redes neuronales, 3) El costo del error no es simétrico, 4) Respetar la física del sensor satelital, 5) Interpretabilidad operativa.
20. **Árbol de Decisión Práctico:** Matriz de selección de modelos para entornos de producción según volumen de datos, latencia y tolerancia al riesgo.
21. **Cierre Filosófico:** La IA no predice el futuro: cuantifica incertidumbre para habilitar decisiones estratégicas.
22. **Gracias & Referencias:** Repositorio de código abierto, notebooks reproducibles y bibliografía BibTeX (`refs.bib`).
