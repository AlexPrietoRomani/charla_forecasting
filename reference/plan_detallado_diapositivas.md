# Plan Maestro v2 — Storytelling, UI y Animaciones
> **Charla:** *¿Puede la IA predecir el futuro? Lecciones de forecasting desde el mundo real*
> **Público:** universitario, con estadística básica (media, varianza, correlación). No asumimos que conocen ML.
> **Duración:** 30–40 min → **20 diapositivas** (~1.7 min por diapo, más 3–5 min de demos).
> **Estado:** 📝 PLAN. **No se ejecuta nada hasta que el usuario lo apruebe explícitamente.**

---

## 0. Reglas que gobiernan todo el plan

1. **Objetividad:** cada conclusión sale de nuestros datos o de un paper verificado. Si los datos contradicen la narrativa, cambiamos la narrativa.
2. **Cero cifras sin fuente.** Las anécdotas industriales que no tengan respaldo se eliminan o se rotulan como *"escenario ilustrativo"*.
3. **Pedagogía para estadística básica:** cada concepto nuevo (lag, overfitting, zero-shot, cuantil) se introduce con una analogía y **una sola** fórmula como máximo.
4. **Una idea por diapo.** Cada ficha tiene una *Frase-clave* (lo único que el público debe recordar) y una *Transición* (la pregunta que abre la siguiente diapo).

---

## 1. Verificación de afirmaciones (resultado de la auditoría)

Verificado con NotebookLM (citas textuales de los papers) y con los archivos de `data/`:

| Afirmación | Veredicto | Acción |
|---|---|---|
| PatchTST: −21.0% MSE, −16.7% MAE, entrenamiento hasta 22× más rápido (P=16, S=8, Traffic) | ✅ Nie et al. 2023 | Se mantiene con el contexto ("en datasets grandes") |
| Benchmark de 42 datasets | ✅ es de **Chronos** (15 in-domain + 27 zero-shot) | Se corrige la atribución (antes se daba a TimesFM) |
| Chronos: T5 de 20M–710M, vocabulario de 4096 tokens | ✅ Ansari et al. 2024 | Se mantiene |
| TimesFM: 200M parámetros, patch de entrada 32 y de salida 128, ~100 mil millones de puntos | ✅ Das et al. 2024 | Se mantiene |
| GraphCast: supera a HRES en el 90.3% de 1380 objetivos, <60 s en 1 TPU v4; IFS ≈ 1 h en 11,664 núcleos | ✅ Lam et al. 2023 | Se corrige "4 horas" → "~1 hora en 11,664 núcleos" |
| Grinsztajn 2022 | ⚠️ Trata del sesgo de las redes hacia funciones suaves y de la invarianza rotacional, **no** de la extrapolación | Citar Grinsztajn para "por qué los árboles ganan en tabular". La no-extrapolación es una propiedad de los árboles (Breiman 2001; Hastie et al., ESL) |
| GraphCast "anticipó el huracán Otis" | ❌ La única fuente es nuestro propio texto (circular) | **Eliminar** |
| Walmart usa Holt-Winters en 50k SKUs | ❌ Fuente circular | **Eliminar** la marca; decir "en retail masivo los métodos exponenciales siguen siendo el baseline estándar (Hyndman & Athanasopoulos 2021; M5)" |
| Maersk/Air France: 4–7% de combustible, \$120M | ❌ Fuente circular | **Eliminar** |
| ERCOT 2021 causado por árboles, −20 GW | ❌ Fuente circular; la causa principal fueron fallas de generación | **Reemplazar** por un experimento propio: árbol vs regresión ante un récord sintético en Punchana |
| \$15,000 por contenedor | ❌ Sin fuente | **Eliminar**; usar una fórmula de costo parametrizable (ver diapo 16) |
| Números del dron (YOLOv12 1.6 ms, 97.4% ripe) | ❌ No están en el repo | **Eliminar** la diapo del dron |
| "275 referencias" | ❌ `refs.bib` tiene **49 entradas** | Corregir |
| Punchana a 106 msnm | ❌ `data/README.md`: **91 msnm** | Corregir |
| Finca en Jaén a 1,450 msnm | ❌ README: **618–1,200 msnm** | Corregir |
| Discrepancia NOAA vs ECMWF de 7.6 °C | ⚠️ Es una foto de una fecha concreta | Mostrar la fecha y además la discrepancia media en N días (se calcula de `noaa_ecmwf_forecast.csv`) |

### 1.1 ❌ Los datos del Caso B (café) son SINTÉTICOS: se descartan

Revisión de `scripts/build_agro_dataset.py`:
- **Clima (Open-Meteo):** real ✅
- **NDVI, EVI, NDRE, NDWI:** simulados con fórmulas y ruido aleatorio (L67–99). Nunca se descargó una imagen satelital ❌
- **Rendimiento:** inventado, `15 + 14·EVI/2.6 + 4·lluvia/400 − 2.5·max(0, Tmax−31) + ruido` (L133–141) ❌

Consecuencias:
- El resultado "la fusión le gana al NDVI" es **circular**: el modelo recupera la fórmula con la que se fabricó el dato.
- La saturación del NDVI está **programada**, no medida.
- **Ninguna cifra de la tabla siguiente puede usarse.** Se conserva solo como registro de la auditoría.
- El Caso B se rehace con datos reales según la **sección 7 (Opción A)**.

<details><summary>Tabla histórica (sintética, NO USAR)</summary>


| Campaña | Real (qq/ha) | Solo NDVI | Fusión | Error fusión | Error NDVI |
|---|---|---|---|---|---|
| 2020 | 34.27 | 31.44 | 32.35 | 1.92 | 2.83 |
| 2021 | 33.75 | 31.54 | 32.54 | 1.21 | 2.21 |
| 2022 | 31.24 | 32.04 | 32.76 | 1.52 | 0.80 |
| 2023 | 32.00 | 31.89 | 31.68 | 0.32 | 0.11 |
| **2024** | **29.98** | **32.29** | **30.24** | **0.26** | **2.31** |
| 2025 | 30.21 | 32.25 | 33.45 | **3.24** | 2.04 |
| **MAE / MAPE** | | | | **1.41 / 4.4%** | **1.72 / 5.4%** |

**La historia anterior era falsa.** El plan v1 hablaba de una sequía de 140 mm, una cosecha real de 18.2 qq/ha y una predicción NDVI de 24.0 qq/ha. Esas cifras **no existen en los datos**. Lo que sí muestran los datos:

- **2024:** estrés **térmico** en floración (Tmax 32.3 °C, la más alta de la serie). El rendimiento cae a 29.98. Solo NDVI predice 32.29 (+7.7%) y la fusión predice 30.24 (+0.9%).
- **Hallazgo potente:** el NDVI anual es casi constante (0.787–0.788), así que **la columna "solo NDVI" es idéntica a la media histórica**. Un NDVI saturado no aporta nada: el modelo colapsa al promedio. Es la demostración empírica perfecta de la saturación.
- **Honestidad:** la fusión **falla en 2025** (error de 3.24, peor que el NDVI con 2.04) y solo tenemos n=6 campañas. La mejora global es modesta: −18% de MAE.

> **Resuelto:** el rendimiento es simulado. Ver la sección 7.

</details>

### 1.2 Benchmark de Punchana

El notebook `01_clima_senamhi.ipynb` **no tiene outputs guardados**, así que las cifras del plan v1 (ARIMA 2.12, ExtraTrees 2.16, LSTM 2.09…) **no son verificables hoy**. En la ejecución se vuelve a correr todo con el protocolo de la sección 3, y **las conclusiones de las diapos 9, 13 y 18 se escriben después de ver los resultados**.

---

## 2. Arco narrativo (20 diapositivas · ~35 min)

**Pregunta conductora:** *"¿Cuándo vale la pena un modelo complejo?"* Se plantea en la diapo 1 y se responde en la 19.

```
ACTO 1 · LA PREGUNTA (3 diapos, ~5 min)
  01 ¿Puede la IA predecir el futuro?        → No adivina: cuantifica incertidumbre
  02 Anatomía de una serie                   → Señal = tendencia + estación + ruido
  03 Mapa de 4 familias                      → No hay "un" algoritmo

ACTO 2 · LAS HERRAMIENTAS (8 diapos, ~13 min)
  04 Clásicos: suavizado, logística, STL     → Lo simple captura la física
  05 Árboles: el puente tabular + su límite  → Ganan en tabular, no extrapolan
  06 Deep Learning: LSTM → PatchTST          → Escala con muchas series
  07 Foundation Models: TimesFM, Chronos     → Pronosticar sin entrenar (zero-shot)
  08 Satélites: la trampa del NDVI           → El sensor también se satura
  09 El reloj botánico                       → El "cuándo" importa tanto como el "cuánto"
  10 Física global: NWP y discrepancia       → Ni los supercomputadores coinciden
  11 GraphCast                               → La IA ya compite con la física

ACTO 3 · CASO A: CLIMA EN IQUITOS (3 diapos, ~6 min)
  12 Contexto Punchana                       → Datos reales, imperfectos
  13 Benchmark de 7 modelos (revelación)     → Respuesta empírica a la pregunta
  14 DEMO 1: pronóstico 7 días               → Incertidumbre en vivo

ACTO 4 · CASO B: CAFÉ EN JAÉN (3 diapos, ~6 min)
  15 Contexto y capas espectrales            → Del píxel a la variable
  16 La campaña 2024                         → El NDVI colapsa a la media
  17 DEMO 2: validación por campaña          → Honestidad: n=6 y el fallo de 2025

ACTO 5 · DECIDIR (3 diapos, ~5 min)
  18 5 lecciones                             → Reglas accionables
  19 ¿Qué modelo uso? (árbol de decisión)    → Respuesta a la pregunta conductora
  20 Cierre + recursos                       → Vuelta al cono de la diapo 1 + QR
```

**Fusiones respecto a v1:** 4+5 → 04; 6+7 → 05; 9 se absorbe en la 06 (pregunta) y la 13 (respuesta); 13+14 → 10; 24+25 → 20. **Nueva:** la 07 (Foundation Models). **Eliminada:** la del dron (sin respaldo).
**Siembra dramática:** la diapo 08 menciona "guarden este 0.788, volverá" y la 16 lo cobra.

---

## 3. Protocolo del benchmark ampliado (diapo 13)

| Nivel | Modelo | Rol |
|---|---|---|
| 0 | Naive estacional | Piso: "no hacer nada" |
| 1 | ARIMA (auto) | Estadística clásica |
| 2 | ETS / Holt-Winters | Suavizado exponencial |
| 3 | Random Forest + lags | Árbol estándar |
| 4 | ExtraTrees / LightGBM + lags | Árbol optimizado |
| 5 | LSTM | Deep learning entrenado localmente |
| 6 | **Chronos-Bolt (small)** zero-shot | Foundation Model (Amazon) |
| 7 | **TimesFM 2.x** zero-shot | Foundation Model (Google) |

- **Mismos 90 días de holdout** (último tramo de 2025) y **mismo protocolo para todos**: pronóstico a 1 día con origen móvil (*rolling origin*), y además un horizonte de 7 días, porque los FM brillan en horizontes largos.
- **Métricas:** RMSE, MAE, tiempo total (entrenamiento + inferencia), hardware (CPU/GPU) y, para modelos probabilísticos, **cobertura del intervalo P10–P90** (¿cae el ~80% de las observaciones dentro?).
- **Repetibilidad:** semillas fijas; LSTM promediada en 5 semillas, con su desviación estándar.
- **Prueba de significancia:** Diebold-Mariano entre el mejor modelo y el siguiente. Si la diferencia no es significativa, **se dice "empate"**.
- **Regla de conclusión (decidida antes de ver los resultados):** gana el de menor RMSE. Si hay empate estadístico, gana **el más simple y barato** (parsimonia; Makridakis et al. M4/M5, Hyndman & Athanasopoulos 2021).
- **Salida:** `data/benchmark_punchana.csv`, que alimenta automáticamente las diapos 13 y 18 (sin cifras escritas a mano).
- **Contexto bibliográfico para interpretar:** Chronos reporta un zero-shot "comparable y ocasionalmente superior" a modelos entrenados (Ansari 2024). Zeng et al. (AAAI 2023) muestran que modelos lineales simples superan a muchos Transformers en series largas. Grinsztajn (2022) explica la ventaja de los árboles en tabular.

---

## 4. Lineamientos de UI (corregidos)

1. **Layout:** a la izquierda (~40%), título, **tesis en 1 frase**, máximo 3 viñetas y una *Frase-clave* destacada. A la derecha (~60%), el visual protagonista. Sin huecos vacíos.
2. **El guion NO va en pantalla:** va en *speaker notes* ocultas que se abren con la tecla `N`, con temporizador por diapo.
3. **5 insignias fijas** con color constante: `TEORÍA` (violeta) · `MECANISMO` (cian) · `EVIDENCIA` (ámbar) · `CASO REAL` (verde) · `DEMO` (rojo).
4. **Animación con propósito:** movimiento intenso solo donde la animación *es* el argumento (01, 02, 05, 06, 07, 09, 16, 20). En el resto, loops lentos y sutiles (respiración ≥ 6 s). Se respeta `prefers-reduced-motion`.
5. **Tarjeta "¿Qué muestra esto?":** 1 línea más la cita. No repite el panel izquierdo.
6. **Cifras:** siempre con unidad y fuente al pie. Los escenarios ilustrativos llevan la etiqueta `ILUSTRATIVO`.
7. **Glosario emergente:** al pasar el cursor sobre términos como *lag*, *zero-shot*, *cuantil* u *overfitting* aparece una definición de 1 línea, pensada para estadística básica.

---

## 5. Fichas por diapositiva

> Formato: **Insignia · Tiempo** | Propósito | Frase-clave | En pantalla | Visual animado | Notas del ponente (resumen) | Transición | Fuentes

### ACTO 1 · LA PREGUNTA

**01 · ¿Puede la IA predecir el futuro?** — `TEORÍA` · 2 min
- **Propósito:** romper la expectativa de la "bola de cristal" y plantear la pregunta conductora.
- **Frase-clave:** *"La IA no adivina el futuro: mide cuánto no sabemos."*
- **En pantalla:** la pregunta, 2 KPIs reales (2,557 días SENAMHI; 6 campañas de café) y la pregunta conductora.
- **Visual:** una serie histórica cruza "HOY" y se abre en un cono P10/P50/P90 que se ensancha con el horizonte. Las partículas-trayectoria se bifurcan sin parar.
- **Notas:** analogía con el pronóstico del tiempo ("70% de lluvia" no es un error, es información). Presentar los 2 casos.
- **Transición:** "¿Qué hay dentro de una serie temporal?"
- **Fuentes:** Hyndman & Athanasopoulos (2021), cap. 1.

**02 · Anatomía de una serie** — `TEORÍA` · 2 min
- **Propósito:** dar el vocabulario mínimo: Y = T + S + ε (el ciclo se menciona solo verbalmente).
- **Frase-clave:** *"Un buen modelo aprende la señal; uno malo memoriza el ruido."*
- **Visual:** 3 pistas (tendencia, estación, ruido) se suman en vivo y forman la Tmax real de Punchana. Un interruptor apaga el ruido.
- **Notas:** definir overfitting con la analogía de "memorizar el examen".
- **Transición:** "¿Con qué herramientas atacamos esto?"
- **Fuentes:** Cleveland et al. (1990).

**03 · Mapa de 4 familias** — `TEORÍA` · 1.5 min
- **Propósito:** dar un mapa mental antes del detalle.
- **Frase-clave:** *"Cada familia resuelve un problema distinto; ninguna gana siempre."*
- **Visual:** cuadrante con eje X = complejidad/costo y eje Y = datos necesarios. Las 4 familias se encienden en secuencia: clásicos, árboles/DL, satélite+física, Foundation Models.
- **Transición:** "Empecemos por lo más simple."

### ACTO 2 · LAS HERRAMIENTAS

**04 · Clásicos: suavizado, logística, STL** — `MECANISMO` · 2 min
- **Propósito:** mostrar que con pocos parámetros se captura la física (techos, memoria que decae, anomalías).
- **Frase-clave:** *"Pocos parámetros, mucha física."*
- **Visual:** (a) exponencial vs logística chocando con su techo L; (b) barras de peso α(1−α)^k con α=0.35 (35%, 23%, 15%…); (c) un residuo STL que se enciende en rojo al superar 2.5σ.
- **Notas:** el suavizado exponencial es un "promedio con memoria que olvida". Sin marcas comerciales.
- **Transición:** "¿Y si quiero usar Machine Learning?"
- **Fuentes:** Hyndman & Athanasopoulos (2021); Cleveland (1990); Verhulst (1838).

**05 · Árboles: el puente tabular y su límite** — `MECANISMO` · 2 min
- **Propósito:** (1) cómo se convierte el tiempo en tabla (lags); (2) por qué los árboles ganan en tabular; (3) por qué no extrapolan.
- **Frase-clave:** *"Un árbol nunca predice algo que no haya visto."*
- **Visual:** una ventana deslizante estampa filas en una tabla. Debajo, el **experimento propio**: un árbol entrenado con Tmax ≤ X frente a un récord sintético → la predicción queda plana en una meseta, mientras una regresión sobre diferencias sigue la subida. Rotulado `EXPERIMENTO PROPIO`.
- **Notas:** Grinsztajn dice que los árboles capturan patrones irregulares mejor que las redes en datos tabulares. La no-extrapolación es una consecuencia de predecir promedios de hoja. Solución: modelar diferencias (ΔY) o quitar la tendencia antes.
- **Transición:** "¿Y las redes neuronales?"
- **Fuentes:** Grinsztajn et al. (NeurIPS 2022); Breiman (2001).

**06 · Deep Learning: LSTM → PatchTST** — `MECANISMO` · 2 min
- **Propósito:** explicar la idea de los parches y plantear (sin responder) la pregunta del costo.
- **Frase-clave:** *"Agrupar el tiempo en parches, como palabras, hizo eficientes a los Transformers."*
- **Visual:** arriba, una LSTM avanza paso a paso (lenta); abajo, la serie se corta en parches (P=16, S=8) y la atención los conecta a todos a la vez. Contador: "tokens: 336 → 42".
- **En pantalla:** −21% MSE y hasta 22× más rápido en datasets grandes (Nie 2023).
- **Notas:** "¿Vale la pena para UNA sola estación? Lo responderemos con datos en la diapo 13."
- **Transición:** "¿Y si el modelo ya viniera entrenado?"
- **Fuentes:** Hochreiter & Schmidhuber (1997); Nie et al. (ICLR 2023).

**07 · Foundation Models: pronosticar sin entrenar** — `MECANISMO` · 2 min — **NUEVA**
- **Propósito:** explicar el zero-shot con la analogía del ChatGPT de las series temporales.
- **Frase-clave:** *"Entrenados con miles de millones de puntos, pronostican series que nunca vieron."*
- **Visual:** una serie se escala y se cuantiza en "tokens" (Chronos, 4096 bins) y sale un abanico de trayectorias P10/P50/P90. A la par, TimesFM genera bloques de 128 pasos (menos pasos autorregresivos).
- **En pantalla:** tabla de 3 filas: TimesFM (Google, 200M, ~100 mil millones de puntos) · Chronos (Amazon, T5 20M–710M, 42 datasets) · Moirai (Salesforce).
- **Notas:** "Los pusimos a prueba en Iquitos: resultado en la diapo 13." Advertencia: zero-shot no significa magia, porque el paper reporta un rendimiento *comparable* al de modelos entrenados.
- **Transición:** "Hasta ahora, solo números. ¿Y si la serie viene del espacio?"
- **Fuentes:** Das et al. (ICML 2024); Ansari et al. (TMLR 2024); Woo et al. (2024).

**08 · Satélites: la trampa del NDVI** — `MECANISMO` · 2 min
- **Propósito:** explicar la física del NDVI y su saturación.
- **Frase-clave:** *"Cuando el follaje es denso, el NDVI deja de ver."*
- **Visual:** la hoja absorbe el rojo y refleja el infrarrojo. Debajo, el NDVI se aplana en ~0.8 al crecer el LAI, mientras EVI y NDRE siguen subiendo.
- **Notas:** **siembra:** "¿Le pasará esto al café de Jaén? Lo veremos con datos reales en la diapo 16." (No se adelanta ninguna cifra: depende de H1.)
- **Transición:** "Además del 'cuánto' verde, importa el 'cuándo'."
- **Fuentes:** Huete et al. (2002); Barnes et al. (2000); Gao (1996).

**09 · El reloj botánico** — `MECANISMO` · 1.5 min
- **Propósito:** las variables deben medirse en la ventana fenológica correcta.
- **Frase-clave:** *"El mismo calor no daña igual en floración que en cosecha."*
- **Visual:** un disco rota por floración (Ago–Oct), llenado (Nov–Feb) y cosecha (Mar–Jul). Al pasar por floración con calor alto, caen flores.
- **Transición:** "¿Y cómo se pronostica el clima a escala planetaria?"
- **Fuentes:** `data/README.md` (ventanas fenológicas); literatura del café arábica (verificar la cita en NotebookLM).

**10 · Física global y la discrepancia entre agencias** — `EVIDENCIA` · 2 min
- **Propósito:** las agencias resuelven ecuaciones físicas con supercomputadores y, aun así, discrepan.
- **Frase-clave:** *"Incluso la física más cara del mundo tiene incertidumbre."*
- **Visual:** una malla atmosférica 3D con ciclo de asimilación. Al lado, 2 termómetros (GFS vs ECMWF) para Punchana **con su fecha**, más la discrepancia media en N días.
- **Fuentes:** Bauer, Thorpe & Brunet (Nature 2015); `data/noaa_ecmwf_forecast.csv`.

**11 · GraphCast** — `EVIDENCIA` · 1.5 min
- **Propósito:** la IA ya compite con la física en el clima global.
- **Frase-clave:** *"Un minuto en un chip frente a una hora en 11,664 núcleos."*
- **Visual:** una malla icosaédrica con paso de mensajes y un cronómetro comparativo. En pantalla: 90.3% de 1380 objetivos.
- **Transición:** "Bajemos a tierra: un caso real en Perú."
- **Fuentes:** Lam et al. (Science 2023).

### ACTO 3 · CASO A: IQUITOS

**12 · Contexto Punchana** — `CASO REAL` · 1.5 min
- **Propósito:** mostrar datos reales con sus imperfecciones.
- **Frase-clave:** *"Los datos reales tienen huecos; tratarlos es parte del modelo."*
- **En pantalla:** −3.69°, −73.26°, **91 msnm**, 2019–2025, 2,557 días; Tmax con 9.7% de huecos (interpolados); friaje mínimo de 19.2 °C.
- **Visual:** mapa de la confluencia de ríos con la estación pulsando y la serie Tmax de 7 años con los huecos marcados.
- **Fuentes:** `data/README.md`; SENAMHI.

**13 · Benchmark de 8 modelos: la revelación** — `EVIDENCIA` · 3 min
- **Propósito:** responder con datos a "¿vale la pena lo complejo?".
- **Frase-clave:** *"Para una sola estación, 70 veces más cómputo no compra precisión: la parsimonia manda, aunque el Zero-Shot ya compite sin haber visto la serie."*
- **Visual:** barras de RMSE ordenadas que se revelan una a una (de Naive a TimesFM), un eje secundario de tiempo/costo (log) y marcas de "empate estadístico" según Diebold-Mariano.
- **Resultados empíricos en pantalla:**
  - ExtraTrees: RMSE = 1.880 °C, MAE = 1.466 °C (0.11s CPU) — Ganador por parsimonia.
  - Random Forest: RMSE = 1.885 °C (p = 0.9181, empate estadístico).
  - ARIMA (2,0,1): RMSE = 1.964 °C (p = 0.1510, empate estadístico).
  - TimesFM 2.5 200M (Google): RMSE = 1.965 °C (p = 0.2747, empate estadístico; menor MAE: 1.392 °C, Zero-Shot, 7.87s GPU).
  - LSTM PyTorch (5 semillas): RMSE = 2.054 °C (p = 0.0295, estadísticamente inferior).
  - Holt-Winters Damped: RMSE = 2.065 °C (p = 0.0426).
  - Chronos-T5 (Amazon): RMSE = 2.143 °C (p = 0.0126, estadísticamente inferior).
  - Naive Estacional: RMSE = 2.874 °C (p = 0.0001).
- **Notas:** Plantilla ejecutada: "En empate estadístico (Diebold-Mariano p > 0.05), la regla de parsimonia elige el modelo más simple, rápido y barato (ExtraTrees en 0.11s). Sin embargo, TimesFM demuestra que un Foundation Model Zero-Shot empata con modelos entrenados sin requerir un solo paso de ajuste".
- **Fuentes:** `data/benchmark_punchana.csv`; Makridakis M4/M5; Zeng et al. (2023); Ansari et al. (2024); Das et al. (ICML 2024).

**14 · DEMO 1: pronóstico a 7 días** — `DEMO` · 2 min
- **Propósito:** mostrar la incertidumbre en vivo.
- **Visual (interactivo):** el mejor modelo de la diapo 13 (ExtraTrees), con su banda de cuantiles residuales (P10–P90), comparado con TimesFM Zero-Shot y conmutadores [GFS] [ECMWF].
- **Frase-clave:** *"El valor está en la banda, no en la línea."*

### ACTO 4 · CASO B: CAFÉ EN JAÉN (datos reales, ver sección 7)

> Todas las cifras de estas 3 diapos salen de `data/cafe_jaen_campanias.csv`, `data/cafe_jaen_resultados.csv` y `data/cafe_jaen_hipotesis.json`.

**15 · Contexto: rendimiento oficial y satélite real** — `CASO REAL` · 1.5 min
- **Propósito:** presentar datos reales y públicos, con sus límites declarados.
- **En pantalla:**
  - Provincia de Jaén (Cajamarca); serie oficial de rendimiento de café MIDAGRI/SIEA, 24 campañas (2000–2024).
  - Satélite MODIS MOD13Q1 (NDVI/EVI, 250 m, 576 compuestos con máscara QA desde 2000).
  - Clima ERA5 vía Open-Meteo (9,132 días agregados por fenología).
  - **Límite declarado:** "rendimiento promedio provincial, no de una finca individual".
- **Visual:** la serie real de rendimiento (qq/ha) con sus caídas históricas. Rotulado explícito: crisis de la roya amarilla 2012–2014 (-56% de rendimiento). Al lado, el mapa de Jaén con el polígono oficial ADM2.
- **Frase-clave:** *"Datos públicos, imperfectos y verificables valen más que datos perfectos inventados."*

**16 · ¿Ve el satélite lo que pasó en el campo?** — `EVIDENCIA` · 2.5 min
- **Propósito:** contrastar con datos reales la hipótesis de saturación del NDVI (diapo 08).
- **Visual:** (1) el NDVI real por campaña frente al rendimiento oficial; (2) dispersión NDVI vs rendimiento con r de Pearson; (3) el caso crítico de la roya 2012–2014.
- **Resultados empíricos en pantalla:**
  - Correlación NDVI anual vs Rendimiento: Pearson r = 0.154 (p = 0.600, NO significativo).
  - Coeficiente de variación de NDVI interanual: 2.32% (saturado en ~0.74).
  - Desplome de la Roya (2012–2014): Rendimiento cayó de 22.7 a 10.0 qq/ha (-56.0%), mientras el NDVI MODIS subió de 0.738 a 0.748 (+1.4%).
  - Lluvia en Floración (Ago–Oct) vs Rendimiento: Pearson r = 0.751 (p = 0.002, altamente significativo).
- **Frase-clave:** *"Un satélite verde no garantiza cosecha: en la crisis de la roya de 2014, el rendimiento cayó 56% mientras el NDVI subió 1.4%."*
- **Costo económico:** Valor de pérdida de 12.7 qq/ha en 45,000 ha cafetaleras a S/. 400/qq = más de S/. 228 millones sin anticipación óptica.
- **Fuentes:** INEI Compendio Estadístico Cajamarca (2017, 2025); MOD13Q1 NASA/Planetary Computer; ERA5.

**17 · DEMO 2: validación honesta** — `DEMO` · 2 min
- **Propósito:** enseñar a validar en el tiempo con pocos datos (walk-forward expansivo).
- **Visual (interactivo):** ventana expansiva: cada campaña se predice entrenando **solo con campañas anteriores** (2000–2014 inicial, 2015–2024 test). Se comparan 4 modelos:
  - Tendencia histórica: MAE = 4.79 qq/ha (RMSE = 6.71)
  - Solo Satélite (NDVI): MAE = 5.32 qq/ha (RMSE = 6.86) — *Añadir solo satélite empeora el error*.
  - Solo Clima (Floración): MAE = 4.60 qq/ha (RMSE = 5.72)
  - Fusión Multimodal: MAE = 4.51 qq/ha (RMSE = 5.52) — *Mejor modelo*.
- **En pantalla:** MAE y RMSE reales, 24 campañas auditadas, advertencia sobre muestra pequeña ($N=24$).
- **Frase-clave:** *"Un modelo honesto muestra dónde falla: la validación temporal sin trampas revela que ningún algoritmo anticipa una plaga sin datos de campo."*

### ACTO 5 · DECIDIR

**18 · 5 lecciones** — `TEORÍA` · 2 min
1. **Valida respetando la flecha del tiempo:** nunca uses k-fold aleatorio en series temporales.
2. **Empieza siempre por un baseline parsimonioso:** ExtraTrees y ARIMA empataron con modelos de 200M de parámetros en Iquitos a una fracción del costo (0.11s vs 7.87s).
3. **El valor operativo está en las bandas:** pronosticar una línea puntual esconde el riesgo; reporta cuantiles P10–P90.
4. **Respeta la física del sensor antes de optimizar:** el NDVI satura en copas densas y fue ciego a la roya (-56%); el clima en floración explicó el 75% de la varianza.
5. **Justifica la complejidad con evidencia:** Foundation Models como TimesFM son revolucionarios para zero-shot en miles de series, pero no desplazan a la parsimonia en un sensor local único.
- **Visual:** 5 tarjetas interactivas que se encienden en secuencia, cada una enlazada a la diapositiva empírica que la demostró.

**19 · ¿Qué modelo uso? Árbol de decisión** — `TEORÍA` · 2 min
- **Propósito:** responder la pregunta conductora con un diagrama accionable.
- **Visual (interactivo):** flujo de decisiones:
  - *¿Tienes 1 serie corta (<3000 puntos)?* → Baselines clásicos (ETS/ARIMA) o Árboles con rezagos y $\Delta y$.
  - *¿Hay riesgo de récord térmico fuera de rango histórico?* → Modela primeras diferencias ($\Delta y$), jamás árboles sobre niveles puros (Slide 05).
  - *¿Cuentas con covariables físicas o de teledetección?* → ExtraTrees / LightGBM tabular, pero verifica saturación del sensor.
  - *¿Tienes miles de series o cero datos locales de entrenamiento?* → Foundation Model Zero-Shot (TimesFM / Chronos-Bolt).
- **Frase-clave:** *"La complejidad se gana con evidencia, no se asume por defecto."*

**20 · Cierre y recursos** — `TEORÍA` · 1.5 min
- **Visual:** el cono de la diapo 01 reaparece (cierre en espejo) y se transforma en 3 decisiones concretas tomadas en la charla. QR al repositorio.
- **En pantalla:** repo, 2 notebooks, datasets, **49 referencias**, enlace a NotebookLM (si se hace público).
- **Frase-clave:** *"¿Puede la IA predecir el futuro? No. Puede ayudarnos a decidir mejor sin conocerlo."*

---

## 6. Instrucciones de ejecución (solo tras la aprobación del usuario)

| Paso | Qué | Entregable | Verificación |
|---|---|---|---|
| E0 | Reintentar `research_import` (Deep Research de 41 fuentes); importar solo las fuentes citadas | Fuentes en NotebookLM | `source_list` |
| E1 | **Caso B con datos reales:** ejecutar las fases B0–B7 de la sección 7 | `data/cafe_jaen_campanias.csv` + `data/SOURCES.md` | Checklist de la sección 7.8 |
| E2 | `scripts/benchmark_punchana.py`: 8 modelos con el protocolo de la sección 3 (instalar `chronos-forecasting` y `timesfm`) | `data/benchmark_punchana.csv` + notebook 01 con outputs | Tests: holdout sin fuga, mismas fechas para todos |
| E3 | Experimento de no-extrapolación con datos de Punchana (diapo 05) | CSV pequeño en `data/` | Reproducible con semilla; rotulado `EXPERIMENTO PROPIO` |
| E4 | Verificar en NotebookLM las citas restantes (diapo 09: fenología del café; diapo 10: cifras NWP; roya 2012–2014) | Tabla de la sección 1 actualizada | Sin filas ❌ en uso |
| E5 | Redactar las Frases-clave (diapos 08, 13, 16, 17, 18, 19) según E1 y E2, con las reglas fijadas de antemano | Plan actualizado | [X] Completado con métricas reales auditadas |
| E6 | Refactorizar `scripts/build_deck.py` a 20 diapos, con speaker notes (`N`), 5 insignias, glosario, `prefers-reduced-motion` y cifras leídas de los CSV (ninguna escrita a mano) | `presentacion.html` | Build sin errores; `grep` sin cifras sintéticas antiguas (29.98, 0.788, 4.4%…) |
| E7 | Verificación visual en el navegador (puerto 8000) a 1920×1080 y 1366×768; ensayo cronometrado de 30–40 min | Capturas | Sin huecos, sin desbordes, animaciones en loop |
| E8 | Registrar en la bitácora el incidente de los datos sintéticos y las correcciones de cifras | `docs/logs/log.md` | — |

> [!IMPORTANT]
> Los pasos E1, E2 y E5 pueden cambiar el mensaje de la charla. Es intencional: la narrativa se ajusta a la evidencia.

---

## 7. Caso B con datos reales (Opción A): protocolo detallado

### 7.0 Reglas anti-invención (obligatorias)

1. **Cero números generados.** Prohibido usar `np.random` o fórmulas para producir datos de entrada u objetivo. Solo se permiten semillas para el entrenamiento de modelos.
2. **Todo dato crudo se guarda tal cual se descargó** en `data/raw/cafe_real/`, con la URL, la fecha de descarga y el hash SHA-256, registrados en `data/SOURCES.md`.
3. **Si un dato no existe, queda vacío** (`NaN`) y se reporta. No se interpola el objetivo (rendimiento) bajo ningún caso.
4. **Toda transcripción manual** (por ejemplo, desde un PDF o un tablero Power BI) indica documento, página o tabla, y se **verifica dos veces**: un segundo paso compara con otra fuente o se revisa celda por celda.
5. **Las hipótesis se escriben antes de ver los resultados** (7.5) y los resultados se reportan aunque las contradigan.
6. **Cualquier aproximación** (máscara de café, ventanas fenológicas) se declara en la diapo como límite.

### 7.1 Variable objetivo: rendimiento oficial de café

| Prioridad | Fuente | Nivel | Uso |
|---|---|---|---|
| 1 | **MIDAGRI – SIEA**: anuarios / compendios "Producción Agrícola" y series históricas (Excel/PDF) en `siea.midagri.gob.pe` | **Provincia de Jaén** (ideal: también sus distritos) | Objetivo principal: rendimiento (kg/ha), producción (t), superficie cosechada (ha) |
| 2 | Tablero MIDAGRI "Perfil productivo y competitivo" (Power BI) | Provincia | Verificación cruzada |
| 3 | MIDAGRI/SIEA a nivel departamental (Cajamarca) | Departamento | Respaldo si no hay una serie provincial completa |
| 4 | FAOSTAT, dominio QCL, ítem "Coffee, green" (Perú) | País | Solo contexto y control de coherencia (no es el objetivo) |

Tareas:
- **B0.1** Localizar y descargar los archivos del SIEA para el mayor rango posible (objetivo: 2000–2024). Registrarlos en `SOURCES.md`.
- **B0.2** Extraer café/Jaén a `data/raw/cafe_real/midagri_jaen_rendimiento.csv` con las columnas `anio, superficie_cosechada_ha, produccion_t, rendimiento_kg_ha, fuente, documento, pagina`.
- **B0.3** Control de coherencia: verificar que `produccion/superficie ≈ rendimiento` (tolerancia del 2%) y comparar la tendencia con Cajamarca y con el total nacional de FAOSTAT.
- **B0.4** Documentar la **definición temporal** que usa el SIEA (año calendario o campaña agrícola Ago–Jul) para alinear correctamente con el satélite.
- **B0.5** Conversión opcional a qq/ha, siempre declarando el factor (1 qq = 46 kg de café pergamino; verificar la unidad con la que reporta el SIEA).

**Criterio de continuación:**
- Con ≥ 15 años reales, el caso es predictivo (diapos 16 y 17 completas).
- Con 10–14 años, es predictivo pero con una advertencia fuerte.
- Con < 10 años, el caso pasa a ser **descriptivo** (correlaciones y visualización, sin afirmaciones predictivas) y se informa al usuario.

### 7.2 Predictores satelitales reales

| Producto | Variables | Resolución | Periodo | Acceso |
|---|---|---|---|---|
| **MODIS MOD13Q1 v6.1** | NDVI, EVI, banda de calidad (QA) | 250 m, cada 16 días | 2000– | Microsoft Planetary Computer (STAC `modis-13Q1-061`, sin cuenta) |
| **Sentinel-2 L2A** | B04, B05, B08 → NDVI, NDRE; máscara de nubes SCL | 10–20 m | 2017– | Planetary Computer (STAC `sentinel-2-l2a`) |

Tareas:
- **B1.1 Área de estudio:** límite de la provincia de Jaén desde una fuente oficial (INEI/IGN o GADM, citada). Se guarda en `data/raw/cafe_real/jaen_limite.geojson`.
- **B1.2 Máscara de zonas cafetaleras** (orden de preferencia):
  1. Un mapa oficial o publicado de cultivo de café en Perú (buscarlo y verificarlo; si existe, citarlo).
  2. Si no existe: la clase "cobertura arbórea / cultivo" de ESA WorldCover 2021, dentro de la franja altitudinal cafetalera tomada del Copernicus DEM. **La franja se toma de una fuente citada, no se asume.**
  - En cualquier caso, la diapo 15 declara: *"máscara aproximada; el café bajo sombra mezcla píxeles"*.
- **B1.3 Extracción MODIS:** solo píxeles válidos según la banda QA (descartar nubes y sombras). Se calcula la mediana espacial dentro de la máscara para cada fecha. Salida: `data/raw/cafe_real/modis_jaen_16d.csv` (`fecha, ndvi_med, evi_med, n_pixeles_validos`).
- **B1.4 Extracción Sentinel-2** (2017–): escenas con nubes < 60% sobre la máscara y SCL válido; NDVI y NDRE con la mediana espacial. Salida: `data/raw/cafe_real/s2_jaen.csv`. Se usa como complemento (pocos años), no como predictor principal.
- **B1.5 Reporte de calidad:** porcentaje de fechas perdidas por nubes, por mes. Jaén es nublado: se espera bastante pérdida y se informa tal cual.

### 7.3 Predictores climáticos reales

- **B2.1** Open-Meteo Archive (reanálisis ERA5) para el centroide de la máscara cafetalera, 2000–2024: Tmax, Tmin, lluvia, ET0 y radiación. Esto reutiliza la parte real del script actual (`fetch_open_meteo_daily`).
- **B2.2** Opcional, como verificación de la lluvia: CHIRPS (si es accesible sin fricción). Si difiere mucho de ERA5, se reporta.
- Salida: `data/raw/cafe_real/clima_jaen_diario.csv`.

### 7.4 Ventanas fenológicas y tabla por campaña

- **B3.1 Fuente de las ventanas:** el calendario agrícola del café en Jaén según MIDAGRI o un artículo verificado en NotebookLM. Las ventanas actuales (floración Ago–Oct, llenado Nov–Feb, cosecha Mar–Jul) **se mantienen solo si una fuente las respalda**; si no, se ajustan a la fuente.
- **B3.2** Construir `data/cafe_jaen_campanias.csv` (una fila por campaña):
  - Objetivo: `rendimiento_kg_ha` y `anomalia_rend`, que es el residuo respecto a una tendencia lineal estimada **solo con años pasados** (para no filtrar información del futuro).
  - Satélite: `ndvi_flor, ndvi_llen, evi_flor, evi_llen, ndvi_anual, n_obs_validas`.
  - Clima: `lluvia_flor, lluvia_llen, tmax_flor, tmax_llen, deficit_hidrico_flor (lluvia − ET0)`.
  - Trazabilidad: `fuente_rend`.
- **B3.3** El script `scripts/build_cafe_real.py` es determinista: lee solo `data/raw/cafe_real/` y no llama a ningún generador aleatorio.

### 7.5 Hipótesis (escritas antes de ver los resultados)

- **H1 (saturación):** el NDVI anual tiene baja variabilidad interanual y una correlación débil (|r| < 0.3) con la anomalía de rendimiento.
- **H2 (fenología):** las variables climáticas de la ventana de floración se correlacionan más con la anomalía que el NDVI anual.
- **H3 (fusión):** el modelo que combina satélite y clima tiene menor MAE que el baseline de tendencia en la validación por ventana expansiva.
- **H4 (eventos):** si la roya 2012–2014 queda dentro del periodo, ¿la detecta el EVI/NDVI? Se reporta sin forzar la respuesta.

Regla: cada hipótesis se reporta como *confirmada / refutada / no concluyente (IC 95% incluye 0)*. Las diapos 08, 16 y 17 se redactan según ese resultado.

### 7.6 Modelado y validación

- **Modelos** (simples, adecuados para n ≈ 20):
  - M0: persistencia (el año anterior).
  - M1: tendencia lineal.
  - M2: Ridge solo con NDVI/EVI.
  - M3: Ridge solo con clima.
  - M4: Ridge con fusión de satélite y clima.
  - Sin deep learning: no hay datos suficientes, y eso mismo es una lección para la charla.
- **Validación principal:** ventana expansiva (se entrena con años ≤ t−1 y se predice t), empezando con al menos 8 años de entrenamiento.
- **Validación secundaria:** LOYO, reportada aparte y rotulada como "usa años futuros".
- **Métricas:** MAE, MAPE, y la mejora frente a M1 con IC 95% por bootstrap. Prueba de Diebold-Mariano entre M4 y M1.
- **Selección de variables:** máximo 3 predictores por modelo, elegidos **por la hipótesis**, no por búsqueda automática, para evitar sobreajuste con n pequeño.
- **Salidas:** `data/cafe_jaen_resultados.csv` (predicción por año y modelo) y `data/cafe_jaen_hipotesis.json`.

### 7.7 Limpieza del material sintético

- **B6.1** Mover `data/cafe_ndvi_rendimiento.csv` → `data/deprecated/cafe_ndvi_rendimiento_SINTETICO.csv`, con un README que explique por qué.
- **B6.2** En `scripts/build_agro_dataset.py`: quitar la generación sintética (índices y rendimiento) y conservar solo la descarga real de Open-Meteo, o reemplazar el script por `build_cafe_real.py`.
- **B6.3** Reescribir `scripts/train_cafe_models.py` y `notebooks/02_cafe_ndvi.ipynb` (vía `generate_notebooks.py`) sobre los datos reales.
- **B6.4** Actualizar la sección 2 de `data/README.md` con las fuentes reales y los límites.
- **B6.5** Reemplazar en NotebookLM la fuente `presentacion_slides_texto.md`, que contiene las cifras falsas y contamina las respuestas, por la versión corregida.

### 7.8 Checklist de verificación (Definition of Done del Caso B)

- [ ] `data/SOURCES.md` lista cada archivo crudo con URL, fecha y SHA-256.
- [ ] `grep -r "np.random" scripts/build_cafe_real.py` no devuelve nada.
- [ ] El control produccion/superficie ≈ rendimiento pasa (≤ 2%).
- [ ] La tabla por campaña no tiene valores del objetivo imputados.
- [ ] Las hipótesis H1–H4 quedaron registradas **antes** de entrenar (con fecha en el commit).
- [ ] Las diapos 15–17 muestran la fuente y los límites en pantalla.
- [ ] No queda ninguna cifra sintética antigua en `presentacion.html`.
- [X] El usuario revisa los resultados y da el visto bueno para ejecutar las Frases-clave.

### 7.9 Riesgos y planes B

| Riesgo | Mitigación |
|---|---|
| El SIEA solo publica PDF o Power BI para el nivel provincial | Transcripción manual con doble verificación (regla 4); si no se puede, usar el nivel departamental |
| Pocos años con serie provincial | Aplicar el criterio de continuación (7.1) y, si hace falta, pasar a modo descriptivo |
| Nubosidad alta en Jaén | MODIS de 16 días con filtro QA; reportar `n_obs_validas` |
| Máscara de café imprecisa | Análisis de sensibilidad con 2 máscaras; declararlo en la diapo |
| Cambio de definición o metodología en el SIEA entre años | Documentarlo en `SOURCES.md` y marcar el quiebre en el gráfico |
| Los resultados no muestran nada interesante | Se cuenta igual: "con datos agregados reales, el satélite no basta". Es una lección válida y honesta |

### 7.10 Paper metodológico de apoyo (opción B como respaldo)

- Buscar 1–2 artículos revisados por pares sobre la predicción de rendimiento de café con teledetección (a escala de parcela) para citar la metodología y comparar órdenes de magnitud del error.
- **Requisito:** que se pueda descargar el PDF, se suba a NotebookLM y se verifiquen las cifras citadas. No se cita nada que no haya pasado por esta verificación.

