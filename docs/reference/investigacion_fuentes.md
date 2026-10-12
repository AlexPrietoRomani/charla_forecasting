# Investigación de Fuentes y Especificación de Casos de Estudio

Este documento consolida la base teórica, referencias bibliográficas y la arquitectura técnica de los dos casos reales que sustentan la charla: **"¿Puede la IA predecir el futuro? Lecciones de forecasting desde el mundo real"**.

---

## 1. Caso A: Clima y Temperatura Extrema con SENAMHI (Iquitos, Loreto)

### 1.1 Formulación del Problema
* **Objetivo:** Predecir la temperatura máxima diaria ($T_{\text{max}}$) y anomalías de lluvia a un horizonte de 7 días ($h = 1 \dots 7$).
* **Zona geográfica:** Selva baja amazónica (Estación SENAMHI Iquitos, Loreto, ~100 msnm).
* **Reto técnico:** Dinámica no lineal tropical, estacionalidad marcada pero con perturbaciones de frentes fríos ("friajes") y microclima convectivo.
* **Paradigma comparativo:**
  1. *Baseline estadístico:* Naive estacional + Holt-Winters / AutoARIMA (`statsmodels`).
  2. *Modelo clásico aditivo:* Prophet con estacionalidades anual/semanal (`prophet`).
  3. *Machine Learning Tabular:* Random Forest + XGBoost / LightGBM con ingeniería de características (lags 1–14, medias móviles 7 y 30 días, seno/coseno del día del año).
  4. *Deep Learning:* LSTM recurrente de 1 capa sobre secuencias temporales.
  5. *Foundation Models Zero-shot:* Chronos / TimesFM (cold-start sin reentrenar).
* **Protocolo de Validación:**
  * `TimeSeriesSplit` (5 folds expansivos) + holdout final estricto de los últimos 90 días (cero leakage temporal).
  * Métricas: RMSE, MAE, Cobertura del intervalo de confianza del 90%.

---

## 2. Caso B: Predicción de Rendimiento de Café con Fusión Satelital y Clima (Herencia AgroVisión)

### 2.1 Aprendizajes e Integración desde AgroVisión
Desde el repositorio `AgroVision` (`d:/Github/6.Proyectos_agro/AgroVision`), adaptamos el motor de teledetección multiespectral y el conector agroclimático:

1. **Extracción Multiespectral Sentinel-2 L2A:**
   * Utiliza la API de estadísticas de Copernicus Data Space Ecosystem (CDSE) / Sentinel Hub o colecciones armonizadas de Sentinel-2.
   * Filtrado riguroso de nubosidad mediante la banda **SCL** (*Scene Classification Layer*):
     $$\text{cloudy} = \text{SCL} \in [3, 8, 9, 10, 11]$$
   * No limitarse únicamente a NDVI: calcular los 5 índices espectrales clave:
     * **NDVI** (Rouse et al., 1974): Vigor general $\frac{\text{NIR} - \text{Red}}{\text{NIR} + \text{Red}}$.
     * **EVI** (Huete et al., 2002): Corrige efectos atmosféricos (banda azul) y **resuelve la saturación en doseles densos** como el café adulto:
       $$\text{EVI} = 2.5 \times \frac{\text{B08} - \text{B04}}{\text{B08} + 6\,\text{B04} - 7.5\,\text{B02} + 1}$$
     * **SAVI** (Huete, 1988): Corrige el brillo del suelo en etapas tempranas o plantaciones jóvenes:
       $$\text{SAVI} = 1.5 \times \frac{\text{B08} - \text{B04}}{\text{B08} + \text{B04} + 0.5}$$
     * **NDRE** (Barnes et al., 2000; Gitelson & Merzlyak, 1994): Red-Edge (B05) para contenido de clorofila y nitrógeno foliar.
     * **NDWI** (Gao, 1996): Contenido de agua líquida foliar mediante NIR y SWIR/Green.

2. **Extracción Agroclimática Continua (Open-Meteo Archive API):**
   * Por latitud y longitud exacta del punto georreferenciado, sin necesidad de credenciales propietarias:
     * Temperatura 2m (media, mín, máx).
     * Precipitación acumulada y humedad relativa.
     * Déficit de presión de vapor (**VPD**) y evapotranspiración de referencia (**ET0**).
     * Radiación solar de onda corta.

3. **Agregación por Ventanas Fenológicas del Café:**
   * El error común en la literatura es correlacionar promedios anuales planos. El cultivo del café responde a etapas biológicas críticas:
     * **Ventana 1 - Floración (Agosto - Octubre):** Sensible a estrés hídrico previo + choque térmico para inducción floral.
     * **Ventana 2 - Llenado de fruto / Expansión de grano (Noviembre - Febrero):** Demanda máxima de fotosíntesis y agua ($\sum \text{EVI}$, VPD moderado).
     * **Ventana 3 - Maduración y Cosecha (Marzo - Julio):** Descenso de vigor vegetativo, acumulación de sólidos solubles.
   * **Variables de entrada por campaña:**
     * $\sum \text{EVI}_{\text{llenado}}$, $\max(\text{NDRE}_{\text{floracion}})$, $\text{NDWI}_{\text{medio}}$.
     * Lluvia acumulada en llenado, anomalía térmica en floración.
   * **Target:** Rendimiento real o normalizado en quintales por hectárea ($\text{qq/ha}$).
   * **Modelado:** Random Forest Regressor y XGBoost con validación *Leave-One-Year-Out* (LOYO).

---

## 3. Síntesis Bibliográfica (Mapeada a las Slides)

| Slide | Tema en el Deck | Referencias Principales | Hallazgo Clave para la Charla |
|---|---|---|---|
| **Slide 3** | ML Tabular | Breiman (2001), Chen & Guestrin (2016), Grinsztajn et al. (2022) | Árboles superan a DL en datos tabulares chicos/medianos con lags bien construidos. |
| **Slide 4** | Series Clásicas | Box & Jenkins (2015), Hyndman (2002), Taylor & Letham (2017) | ARIMA y Prophet son baselines transparentes y rápidos; difíciles de batir con pocos datos. |
| **Slide 5** | DL Secuencial | Hochreiter (1997), Salinas (2020), Lim (2021) | TFT y LSTMs aportan cuando hay series cruzadas masivas; en una sola serie suelen sobreajustar. |
| **Slide 6** | Foundation Zero-shot | Ansari (Chronos 2024), Das (TimesFM 2024), Garza (TimeGPT 2023) | Pronóstico en frío sin calibración: sorprendentemente competitivo en estacionalidades claras. |
| **Slide 8** | Fusión Multimodal | Huete (2002), Muruganantham (2022), Ramos (2020), Barbosa (2021) | La reflectancia satelital sola es insuficiente; cruzar espectro + clima fenológico reduce el MAPE < 15%. |
| **Slide 13** | Lecciones Mundo Real | Niedbała (2022), AgroVisión docs (2026) | 1) NDVI se satura en dosel denso ($\text{LAI} > 3$) $\rightarrow$ usar EVI/NDRE.<br>2) La validación aleatoria (shuffle) es el mayor autoengaño en forecasting.<br>3) El costo del error no es simétrico. |

---

## 4. Estado de Implementación Técnica y Siguientes Tareas

1. **Herramientas de descarga listas:**
   * Script base para SENAMHI usando `garua` (o fallback estructurado a CSV diario).
   * Módulo de extracción satelital multi-índice adaptado de `AgroVision/backend/services/remote_sensing.py` y `weather.py`.
2. **Coordenadas de referencia para el Caso B:**
   * Zona cafetalera Jaén (Cajamarca, Perú): Lat -5.70, Lon -78.80 (elevación ~1200 msnm).
   * Serie temporal histórica 2019–2025 para análisis de correlación espectro-climática.
