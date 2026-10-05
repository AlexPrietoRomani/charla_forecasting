# Fase 2: Caso B — Reconstrucción con Datos Reales de Café (Jaén, Cajamarca)

> **Documento de Fase:** `reference/fases/fase_2_cafe_datos_reales.md`  
> **Plan Relacionado:** [plan_detallado_diapositivas.md](../plan_detallado_diapositivas.md) (Sección 7: Protocolo Anti-Invención)  
> **Estado:** `[ ] Pendiente de Ejecución` (Requiere aprobación explícita del usuario)

---

## 1. Objetivo de la Fase
Construir el dataset del Caso B (`data/cafe_jaen_campanias.csv`) a partir de fuentes 100% verificables y públicas:
1. Rendimiento histórico oficial de café para la provincia de Jaén (MIDAGRI - SIEA).
2. Índices espectrales satelitales reales (MODIS MOD13Q1 y Sentinel-2 L2A) vía Microsoft Planetary Computer.
3. Clima diario real (ERA5 / Open-Meteo Archive).
4. Evaluación rigurosa de las 4 hipótesis científicas (H1: saturación de NDVI, H2: fenología vs NDVI, H3: ventaja de la fusión multimodal, H4: detección de choque fitosanitario/roya).

---

## 2. Entregables
1. `data/raw/cafe_real/midagri_jaen_rendimiento.csv` (Rendimiento, superficie, producción extraídos del SIEA).
2. `data/raw/cafe_real/jaen_limite.geojson` y máscara satelital de zonas cafetaleras.
3. `data/raw/cafe_real/modis_jaen_16d.csv` y `data/raw/cafe_real/s2_jaen.csv` (Reflectancias satelitales reales).
4. `data/raw/cafe_real/clima_jaen_diario.csv` (ERA5 Open-Meteo para el centroide cafetalero).
5. `scripts/build_cafe_real.py` (Script determinista, sin `np.random`, con registro SHA-256).
6. `data/cafe_jaen_campanias.csv` (Dataset consolidado campaña por campaña).
7. `data/cafe_jaen_hipotesis.json` y `data/cafe_jaen_resultados.csv` (Resultados de validación temporal expansiva).
8. Actualización del cuaderno reproducible `notebooks/02_cafe_ndvi.ipynb`.

---

## 3. Subfases y Tareas

### SF2.1 Recolección y Validación del Rendimiento Oficial (SIEA/MIDAGRI)
- [X] **T2.1.1** Localizar los compendios y anuarios estadísticos de producción agrícola del SIEA (MIDAGRI) para la serie histórica de café en la provincia de Jaén (meta: 2000–2024).
- [X] **T2.1.2** Extraer la serie a `data/raw/cafe_real/midagri_jaen_rendimiento.csv` indicando para cada registro: `anio`, `superficie_cosechada_ha`, `produccion_t`, `rendimiento_kg_ha`, `fuente`, `documento`, `pagina`.
- [X] **T2.1.3** Aplicar control de coherencia aritmética: `abs(produccion_t * 1000 / superficie_cosechada_ha - rendimiento_kg_ha) / rendimiento_kg_ha < 0.02`.
- [X] **T2.1.4** Registrar la definición temporal oficial (año calendario vs año agrícola Ago–Jul) y documentar en `data/SOURCES.md`.

### SF2.2 Extracción de Índices Satelitales Reales (Planetary Computer)
- [X] **T2.2.1** Obtener el polígono oficial de la provincia de Jaén (`jaen_limite.geojson`) de fuente IGN/INEI/GADM.
- [X] **T2.2.2** Definir la máscara cafetalera referencial con fuente bibliográfica/cartográfica citada (clase cultivo/arbórea WorldCover + franja altitudinal cafetalera).
- [X] **T2.2.3** Extraer serie MODIS MOD13Q1 (250m, 16 días, 2000–2024) filtrando por máscara de calidad QA (descarte de nubes/sombras) y calculando la mediana espacial.
- [X] **T2.2.4** Extraer serie Sentinel-2 L2A (10–20m, 2017–2024) para comparación de alta resolución (NDRE Red-Edge y NDVI).
- [X] **T2.2.5** Generar reporte de observaciones válidas por mes (`n_obs_validas`), visibilizando la estacionalidad de nubosidad.

### SF2.3 Extracción Climática Real y Agregación Fenológica
- [X] **T2.3.1** Descargar serie meteorológica ERA5 vía Open-Meteo Archive para las coordenadas cafetaleras de Jaén (2000–2024): Tmax, Tmin, lluvia, ET0, radiación.
- [X] **T2.3.2** Alinear las ventanas fenológicas con el calendario oficial de Jaén (Floración, Llenado, Cosecha) respaldado por fuente técnica.
- [X] **T2.3.3** Ejecutar `scripts/build_cafe_real.py` para generar `data/cafe_jaen_campanias.csv` sin imputaciones inventadas.

### SF2.4 Evaluación de Hipótesis y Modelado con Ventana Expansiva
- [X] **T2.4.1** Evaluar H1: Calcular correlación Pearson/Spearman entre `ndvi_anual` y `anomalia_rendimiento`.
- [X] **T2.4.2** Evaluar H2: Comparar correlación de variables de floración (`lluvia_flor`, `tmax_flor`, balance hídrico) vs NDVI.
- [X] **T2.4.3** Evaluar H3: Comparar MAE en validación por ventana expansiva entre M1 (Tendencia), M2 (Solo NDVI), M3 (Solo Clima) y M4 (Fusión Satélite + Clima).
- [X] **T2.4.4** Evaluar H4: Documentar si el choque de la roya amarilla (2012–2014) tuvo firma espectral visible en EVI/NDVI.
- [X] **T2.4.5** Exportar `data/cafe_jaen_hipotesis.json` y actualizar `notebooks/02_cafe_ndvi.ipynb` con los outputs reales.

---

## 4. Criterios de Aceptación (DoD Fase 2)
- [X] `grep -r "np.random" scripts/build_cafe_real.py` devuelve 0 ocurrencias.
- [X] `midagri_jaen_rendimiento.csv` pasa el test de coherencia aritmética $\Delta < 2\%$.
- [X] Todos los hashes SHA-256 registrados en `data/SOURCES.md`.
- [ ] Cada valor en `data/cafe_jaen_campanias.csv` tiene trazabilidad directa a archivos en `data/raw/cafe_real/`.
- [ ] Las métricas de error y correlación se derivan estrictamente de los datos reales.
- [ ] El notebook `02_cafe_ndvi.ipynb` ejecuta de principio a fin sin errores sobre los nuevos datos.
