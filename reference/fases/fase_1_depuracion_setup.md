# Fase 1: Depuración de Material Sintético, Trazabilidad y Setup de Modelos

> **Documento de Fase:** `reference/fases/fase_1_depuracion_setup.md`  
> **Plan Relacionado:** [plan_detallado_diapositivas.md](../plan_detallado_diapositivas.md) (Sección 6 y 7.7)  
> **Estado:** `[ ] Pendiente de Ejecución` (Requiere aprobación explícita del usuario)

---

## 1. Objetivo de la Fase
Aislar y archivar todo archivo con datos sintéticos no verificables para evitar contaminación cruzada, configurar el registro estricto de trazabilidad `data/SOURCES.md`, e instalar las dependencias necesarias para los modelos fundacionales (`chronos-forecasting`, `timesfm`).

---

## 2. Entregables
1. `data/deprecated/cafe_ndvi_rendimiento_SINTETICO.csv` y `data/deprecated/README.md`.
2. `data/SOURCES.md` inicializado con el registro de fuentes reales (SENAMHI, Open-Meteo).
3. Entorno de Python con `chronos-forecasting` y `timesfm` instalados y verificados.
4. Actualización preliminar de `data/README.md` documentando el estado de los datos.

---

## 3. Subfases y Tareas

### SF1.1 Depuración y Aislamiento de Datos Sintéticos
- [ ] **T1.1.1** Crear directorio `data/deprecated/` y mover `data/cafe_ndvi_rendimiento.csv` renombrándolo a `data/deprecated/cafe_ndvi_rendimiento_SINTETICO.csv`.
- [ ] **T1.1.2** Crear `data/deprecated/README.md` explicando detalladamente que dicho archivo contenía rendimientos e índices generados con fórmulas y ruido `np.random`, y que fue descartado tras la auditoría del 2026-10-04.
- [ ] **T1.1.3** Mover o renombrar temporalmente `scripts/build_agro_dataset.py` para evitar ejecuciones accidentales que sobrescriban datos reales.

### SF1.2 Registro de Trazabilidad (`data/SOURCES.md`)
- [ ] **T1.2.1** Crear `data/SOURCES.md` con la plantilla de registro: Nombre, URL/Endpoint, Fecha de Acceso, Versión, Parámetros de consulta y SHA-256 de los archivos crudos.
- [ ] **T1.2.2** Registrar la procedencia de `data/senamhi_diario.csv` (descarga `garua` de la estación Punchana 103015/150208) y de `data/noaa_ecmwf_forecast.csv`.

### SF1.3 Setup de Dependencias de Modelado
- [ ] **T1.3.1** Verificar disponibilidad de PyTorch y paquetes base (`statsmodels`, `scikit-learn`, `xgboost`, `lightgbm`).
- [ ] **T1.3.2** Instalar `chronos-forecasting` y verificar importación de `ChronosPipeline`.
- [ ] **T1.3.3** Instalar `timesfm` y verificar compatibilidad en entorno local (CPU/GPU).
- [ ] **T1.3.4** Si alguna dependencia pesada genera conflicto de versiones, documentar la alternativa ligera (ej. Chronos-Bolt tiny/small vs TimesFM checkpoint).

---

## 4. Criterios de Aceptación (DoD Fase 1)
- [ ] No existe `data/cafe_ndvi_rendimiento.csv` en la raíz de `data/` (se movió a `deprecated/`).
- [ ] `data/SOURCES.md` existe y tiene documentados los datos de Punchana y Open-Meteo.
- [ ] Un script de prueba importa `chronos` y `timesfm` sin fallos críticos.
- [ ] Cero modificación de `presentacion.html` en esta fase.
