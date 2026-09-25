# Estructura propuesta — ¿Puede la IA predecir el futuro? (16 slides, estilo Data_Wizard)

Clon visual de `Data_Wizard/presentacion.html`: single-file, Chart.js + PapaParse + Leaflet, modo claro/oscuro, navegación teclado.

1. Portada + pregunta gancho (¿predecir o anticipar con incertidumbre?)
2. Mapa mental: 4 familias (ML tabular, series temporales, DL secuencial, CV + fusión) + foundation zero-shot
3. ML tabular: RF → ExtraTrees → XGBoost → LightGBM → CatBoost (tabla: categóricas, velocidad, tuning) [@breiman2001; @chen2016; @ke2017; @prokhorenkova2018; @grinsztajn2022]
4. Series clásicas: ARIMA/SARIMA, ETS, Prophet — 1 serie, horizonte corto, interpretable [@boxjenkins2015; @hyndman2002; @taylor2017; @makridakis2018]
5. DL secuencial: LSTM → DeepAR → N-BEATS/N-HiTS → TFT → PatchTST (panel grande + GPU) [@hochreiter1997; @salinas2020; @oreshkin2020; @lim2021; @challu2023; @nie2023]
6. Foundation zero-shot: TimesFM / Chronos / Lag-Llama / Moirai / TimeGPT-1 — cold-start sin reentrenar [@das2024; @ansari2024; @rasul2024; @woo2024; @garza2023]
7. CV para predecir: clasificación (ResNet/EfficientNet/ViT) vs detección (YOLO conteo) vs segmentación (U-Net/DeepLab/SAM) [@he2016deepresidual; @redmon2016yolo; @ronneberger2015unet; @dosovitskiy2020vit]
8. Fusión: NDVI/EVI + clima + suelo → CNN+LSTM supera NDVI aislado [@muruganantham2022yieldrs; @vanklompenburg2020]
9. DEMO 1 — Temperatura/heladas: Open-Meteo + RF/DNN 6–48h, RMSE ~1.5 °C, supera HRRR [@talsma2023; @noh2021; @bhakare2025] + GraphCast contexto global [@lam2023]
10. DEMO 1 en vivo: CSV `data/clima_valle_elqui.csv` + Chart.js (umbral daño, costo noche — reutiliza lógica Data_Wizard)
11. DEMO 2 — Fruta + NDVI: uva Landsat R~0.95 [@arab2021], fresa CNN-LSTM 5 sem [@chaudhary2021], arándano Sentinel-2+XGBoost MAPE 12% [@niedbala2022], manzana ∑NDVI+RF [@bai2021] → fusión UAV+satélite [@li2025]
12. DEMO 2 en vivo: CSV `data/ndvi_fruta.csv` (NDVI acumulado vs rendimiento, slider fenología)
13. Lecciones mundo real: 1) más datos ≠ mejor (ventana fenológica), 2) baseline RF/XGB antes que DL, 3) validación temporal, 4) costo del error (falso negativo helada), 5) NDVI se satura
14. Receta práctica: ¿qué modelo cuándo? (árbol decisión: pocos datos→ETS/Prophet/RF; exógenas→LGBM/CatBoost; panel grande→TFT/N-HiTS; cold-start→Chronos/TimesFM; imágenes→YOLO/U-Net)
15. Cierre: la IA no predice el futuro, cuantifica incertidumbre — decidir bajo incertidumbre
16. Gracias + refs + repo/QR (refs.bib + articles/)

Demos mínimas siguientes:
- `notebooks/01_temp_openmeteo_rf.ipynb` (base [@talsma2023])
- `notebooks/02_ndvi_sentinel_xgb.ipynb` (base [@niedbala2022], portable a Elqui)
