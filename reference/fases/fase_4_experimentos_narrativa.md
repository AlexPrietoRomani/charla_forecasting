# Fase 4: Experimentos de Respaldo, Citas Verificadas y Consolidación Narrativa

> **Documento de Fase:** `reference/fases/fase_4_experimentos_narrativa.md`  
> **Plan Relacionado:** [plan_detallado_diapositivas.md](../plan_detallado_diapositivas.md) (Sección 1 y Sección 5)  
> **Estado:** `[ ] Pendiente de Ejecución` (Requiere aprobación explícita del usuario)

---

## 1. Objetivo de la Fase
1. Reemplazar la anécdota no respaldada de Texas 2021 por un experimento propio y reproducible de fallo de extrapolación en árboles usando los datos reales de Punchana.
2. Terminar de verificar con NotebookLM las citas teóricas de fenología y física atmosférica.
3. Completar las "Frases-clave" que quedaron pendientes con marca ⏳ en las diapositivas 08, 13, 16, 17, 18 y 19, redactándolas con total fidelidad a la evidencia encontrada en las Fases 2 y 3.
4. Presentar la redacción consolidada al usuario para su visto bueno antes de modificar la presentación interactiva.

---

## 2. Entregables
1. `scripts/experimento_no_extrapolacion.py` y `data/experimento_extrapolacion.csv` (Datos de la prueba rotulada `EXPERIMENTO PROPIO`).
2. Actualización de `reference/investigacion_fuentes.md` con las citas académicas definitivas.
3. `reference/plan_detallado_diapositivas.md` actualizado con todas las Frases-clave ⏳ completadas y sin marcadores provisionales.

---

## 3. Subfases y Tareas

### SF4.1 Experimento Propio de No-Extrapolación (Diapositiva 05)
- [X] **T4.1.1** Tomar la serie diaria de Punchana y simular un escenario de entrenamiento restringido a temperaturas habituales ($T \le 34.0\,^{\circ}\text{C}$).
- [X] **T4.1.2** Someter a prueba a un Random Forest / ExtraTrees frente a una ola de calor real de $37.4\,^{\circ}\text{C}$ (2023).
- [X] **T4.1.3** Demostrar empíricamente cómo el árbol colapsa en una meseta horizontal constante ($\hat{y} = 31.5\,^{\circ}\text{C}$, error 5.5 °C), mientras que un modelo que predice diferencias acumuladas ($\Delta y$) acompaña la tendencia ($35.45\,^{\circ}\text{C}$).
- [X] **T4.1.4** Exportar `data/experimento_extrapolacion.csv` para renderizar el gráfico SVG correspondiente en la diapositiva 05 rotulado como `EXPERIMENTO PROPIO`.

### SF4.2 Verificación Cruzada de Fuentes Bibliográficas
- [X] **T4.2.1** Verificar citas de fenología del café en Perú y temperatura crítica de aborto floral.
- [X] **T4.2.2** Verificar descripción del modelo ECMWF IFS y ciclo 4D-Var en Bauer et al. (Nature 2015).
- [X] **T4.2.3** Calcular la discrepancia media absoluta en °C entre NOAA GFS y ECMWF IFS para Punchana en `data/noaa_ecmwf_forecast.csv` (Media 6.36 °C, Max 9.3 °C) y consignar la fecha exacta de la foto comparativa.

### SF4.3 Redacción Definitiva de Frases-clave (⏳)
- [X] **T4.3.1** Redactar Frase-clave de Diapositiva 08 (siembra de saturación) ajustada al resultado de H1.
- [X] **T4.3.2** Redactar Frase-clave de Diapositiva 13 (benchmark Iquitos) según el modelo ganador del test Diebold-Mariano (ExtraTrees parsimonia, TimesFM zero-shot).
- [X] **T4.3.3** Redactar Frase-clave de Diapositiva 16 (campaña crítica en Jaén) según la correlación satélite vs clima real (-56% rendimiento vs +1.4% NDVI).
- [X] **T4.3.4** Redactar Frase-clave de Diapositiva 17 (validación expansiva) reportando los fallos reales del modelo (fusión 4.51 qq/ha vs satélite 5.32 qq/ha).
- [X] **T4.3.5** Actualizar las 5 lecciones de la Diapositiva 18 y el árbol de decisión de la Diapositiva 19 asegurando que coincidan 100% con los datos.
- [X] **T4.3.6** Aprobación del usuario recibida explícitamente ("Ejecuta").

---

## 4. Criterios de Aceptación (DoD Fase 4)
- [X] Cero menciones a afirmaciones sin fuente (ERCOT/árboles, Walmart 50k, Maersk $120M).
- [X] Todas las marcas ⏳ han sido resueltas en el plan con números objetivos.
- [X] El usuario aprueba las conclusiones antes de codificar la interfaz.
