# Contenido Completo y Guion de la Presentación: ¿Puede la IA predecir el futuro?

**Título:** ¿Puede la IA predecir el futuro? Lecciones de forecasting, teledetección multiespectral y cuantificación de incertidumbre en el mundo real  
**Audiencia:** Estudiantes universitarios con conocimientos básicos de estadística  
**Duración proyectada:** 30 a 40 minutos (5 Actos, 20 Diapositivas)  
**Trazabilidad:** Datos 100% reales auditados (SENAMHI Punchana 2,557 días, SIEA/MIDAGRI Jaén 24 campañas, MODIS MOD13Q1 NASA, ERA5 ECMWF, NOAA GFS). Cero datos sintéticos.

---

## ACTO 1: LA PREGUNTA (~5 min)

### Diapositiva 01: La ilusión de la certeza
- **Insignia:** `TEORÍA` | **Tiempo sugerido:** 1.5 min
- **Tesis:** La inteligencia artificial responde con aplomo absoluto, pero el futuro no es un punto en el espacio: es un cono estocástico que se expande con el tiempo.
- **Puntos clave:**
  1. *El sesgo puntual:* Exigir a un algoritmo un valor único (\(\hat{y}_{t+h}\)) oculta el riesgo operativo en meteorología, agricultura y finanzas.
  2. *Entropía acumulada:* Todo sistema dinámico no lineal pierde predictibilidad; la dispersión del error crece asintóticamente con el horizonte de pronóstico (\(\sigma_h \propto \sqrt{h}\)).
  3. *La pregunta central:* ¿Puede la IA predecir el futuro o solo reproduce correlaciones del pasado?
- **Frase-clave:** *"La IA no sabe lo que no sabe: responde con la misma seguridad cuando acierta que cuando inventa."*
- **Visual:** Cono de incertidumbre animado: serie histórica observada, punto presente \(t_0\), abanico estocástico Monte Carlo y cuantiles P10, P50 y P90.
- **Guion del orador:** "Cuando le pedimos a ChatGPT o a una red neuronal que nos dé un número para mañana, responde con aplomo instantáneo. Pero el mundo real no es determinista. El futuro es un cono que se expande. En esta charla vamos a desmontar las promesas del forecasting y ver qué funciona de verdad cuando bajamos a tierra con datos peruanos."

---

### Diapositiva 02: Anatomía del tiempo: los 4 componentes
- **Insignia:** `MECANISMO` | **Tiempo sugerido:** 2.0 min
- **Tesis:** Antes de ajustar una red neuronal, debemos comprender la física de la señal: toda serie temporal \(Y(t)\) combina cuatro dinámicas superpuestas.
- **Puntos clave:**
  1. *Tendencia (\(T_t\)):* Dirección a largo plazo gobernada por cambio climático, demografía o tecnología.
  2. *Estacionalidad (\(S_t\)):* Ciclos astronómicos fijos e inmutables (día/noche, solsticios anuales, ventanas de floración).
  3. *Ciclo (\(C_t\)) y Ruido (\(\epsilon_t\)):* Oscilaciones aperiódicas acopladas (como El Niño-Oscilación del Sur) más entropía térmica irreductible.
- **Frase-clave:** *"Si no separas la estacionalidad, tu modelo más complejo solo estará memorizando qué mes del año es."*
- **Visual:** 4 pistas sincronizadas con la descomposición aditiva/multiplicativa sobre la temperatura de Punchana, resaltando la detección de anomalías térmicas (\(> 2.5\sigma\)) que corresponden a friajes reales (19.2 °C).
- **Guion del orador:** "Antes de entrenar redes complejas, miren la señal. Toda serie temporal tiene tendencia de largo plazo, ciclos estacionales y residuo. Si un modelo no sabe aislar la estacionalidad, no es inteligente: solo memorizó qué mes del año es."

---

### Diapositiva 03: El mapa de las 4 familias metodológicas
- **Insignia:** `TEORÍA` | **Tiempo sugerido:** 1.5 min
- **Tesis:** No existe una única arquitectura universal. En forecasting coexisten cuatro paradigmas con supuestos, costos y límites radicalmente distintos.
- **Puntos clave:**
  1. *Clásicos estadísticos (ARIMA, Holt-Winters, STL):* Estimación analítica, inferencia en microsegundos, rigurosos con pocas observaciones.
  2. *Tabulares / ML (Random Forest, ExtraTrees, LightGBM):* Convierten el tiempo en rezagos (lags); excelentes para covariables multimodales.
  3. *Física & Teledetección (NWP, ECMWF, Satélites):* Ecuaciones de fluidos y radiancia espectral. Cobertura global pero cómputo intensivo.
  4. *Foundation Models (TimesFM, Chronos):* Modelos pre-entrenados masivos para pronóstico zero-shot sin ajuste local.
- **Frase-clave:** *"Cada familia resuelve un problema distinto; ninguna domina en todos los regímenes."*
- **Visual:** Cuadrante 2x2 que cruza Volumen de Datos Requerido vs Complejidad Computacional.
- **Guion del orador:** "Hay 4 escuelas. Los clásicos de pocos parámetros, el Machine Learning con rezagos, la física de supercomputadores y los Foundation Models masivos. Cada una sirve para una escala distinta; ninguna gana siempre."

---

## ACTO 2: LAS HERRAMIENTAS (~13 min)

### Diapositiva 04: Clásicos: memoria y techos asintóticos
- **Insignia:** `MECANISMO` | **Tiempo sugerido:** 2.0 min
- **Tesis:** Con apenas dos o tres parámetros, los modelos analíticos encapsulan leyes físicas inviolables: memoria que decae geométricamente y capacidades asintóticas de carga.
- **Puntos clave:**
  1. *Decaimiento de memoria:* Holt-Winters pondera observaciones pasadas mediante \(\alpha(1-\alpha)^k\). El pasado remoto nunca se anula por completo, pero pierde influencia.
  2. *Techo biológico de Verhulst:* El crecimiento exponencial indefinido no existe en la biosfera; la logística impone una asíntota superior \(L\).
  3. *Parsimonia:* Sin GPUs ni matrices gigantescas; converge en milisegundos con interpretabilidad absoluta.
- **Frase-clave:** *"Pocos parámetros, mucha física."*
- **Visual:** Control interactivo de \(\alpha\) (0.1 a 0.8) mostrando la caída de peso histórico, frente al techo asintótico de Verhulst en biomasa.
- **Guion del orador:** "Con solo alpha y un techo asintótico, Holt-Winters y Verhulst capturan realidades biológicas. El crecimiento infinito no existe en la naturaleza. Los modelos con pocos parámetros son rápidos e inmunes a memorizar ruido."

---

### Diapositiva 05: Árboles: el puente tabular y el fallo de extrapolación
- **Insignia:** `MECANISMO` | **Tiempo sugerido:** 2.0 min
- **Tesis:** Los ensambles de árboles dominan datos tabulares, pero sufren una limitación matemática fundamental: jamás pueden predecir un valor fuera del rango que vieron sus hojas de entrenamiento.
- **Puntos clave:**
  1. *El puente tabular:* El tiempo se descompone en una matriz de rezagos (\(y_{t-1}, y_{t-2}, \dots\)).
  2. *El experimento propio (Punchana):* Entrenamos un Random Forest restringido a \(T \le 34.0^\circ\text{C}\) y lo evaluamos en la ola de calor real de 2023 (\(37.4^\circ\text{C}\)).
  3. *Fallo y solución:* El árbol colapsó en una meseta constante (\(31.5^\circ\text{C}\), error de 5.5 °C). Solo un modelo sobre primeras diferencias (\(\Delta y\)) acompaña el récord (\(35.45^\circ\text{C}\)).
- **Frase-clave:** *"Un árbol nunca predice algo que no haya visto."*
- **Visual:** Curva real de la ola de calor de 2023 en Punchana contrastando la meseta plana del Random Forest frente a la extrapolación del modelo diferenciado.
- **Guion del orador:** "Muchos usan Random Forest sin entender cómo funciona. Un árbol corta el espacio en cajas y promedia. Si viene una ola de calor histórica que nunca antes vio, el árbol colapsa en una meseta constante. Aquí lo demostramos con datos de SENAMHI: el árbol falló por 5.5 °C. Para arreglarlo, hay que modelar diferencias."

---

### Diapositiva 06: Deep Learning: de LSTM a PatchTST
- **Insignia:** `MECANISMO` | **Tiempo sugerido:** 2.0 min
- **Tesis:** Tratar cada punto temporal como un token asfixia a los Transformers; agrupar el tiempo en sub-series (patches) desbloqueó la eficiencia de la atención global.
- **Puntos clave:**
  1. *El cuello recurrente:* Las LSTMs procesan paso a paso (\(\mathcal{O}(L)\)), con cuellos de botella secuenciales y desvanecimiento de gradiente.
  2. *Parches como palabras:* PatchTST divide 336 observaciones temporales en parches solapados (\(P=16, S=8\)), reduciendo la secuencia a 42 tokens (\(8\times\) menos memoria y cómputo).
  3. *La pregunta de auditoría:* ¿Vale la pena esta artillería profunda para predecir una estación local?
- **Frase-clave:** *"Agrupar el tiempo en parches, como palabras, hizo eficientes a los Transformers."*
- **Visual:** Diagrama interactivo comparando la recurrencia secuencial frente a la matriz de atención cruzada entre parches temporales.
- **Guion del orador:** "Las redes recurrentes procesaban día por día, como quien lee una frase deletreando letra por letra. PatchTST agrupa los días en bloques o parches, como palabras completas. Eso redujo el costo 8 veces y permitió aplicar Transformers a series temporales."

---

### Diapositiva 07: Foundation Models: pronosticar sin entrenar
- **Insignia:** `MECANISMO` | **Tiempo sugerido:** 2.0 min
- **Tesis:** La revolución del Zero-Shot llegó a las series de tiempo: modelos pre-entrenados con miles de millones de puntos generan pronósticos instantáneos sin gradientes locales.
- **Puntos clave:**
  1. *Tokenización continua:* Chronos (Amazon) discretiza valores continuos en 4,096 buckets tratados como vocabulario de lenguaje en T5.
  2. *TimesFM (Google 200M):* Diseñado con atención causal en parches de 128 pasos sobre más de 100 mil millones de puntos reales y sintéticos.
  3. *La promesa evaluada:* ¿Puede un modelo que jamás conoció la Amazonía competir con modelos entrenados in situ?
- **Frase-clave:** *"Entrenados con miles de millones de puntos, pronostican series que nunca antes vieron."*
- **Visual:** Tokenización en buckets discretos de Chronos y tabla de especificaciones técnicas (TimesFM, Chronos, MOIRAI).
- **Guion del orador:** "Así como los LLMs leen todo internet, TimesFM de Google y Chronos de Amazon se entrenaron con miles de millones de puntos. Pueden pronosticar una serie sin entrenarse en ella. ¿Funcionarán en la selva peruana? Lo probamos en Iquitos."

---

### Diapositiva 08: Satélites: la trampa biofísica del NDVI
- **Insignia:** `MECANISMO` | **Tiempo sugerido:** 2.0 min
- **Tesis:** El infrarrojo cercano y el rojo miden vigor fotosintético, pero cuando el dosel arbóreo cierra, el índice se satura asintóticamente y se vuelve ciego a lo que ocurre bajo las ramas.
- **Puntos clave:**
  1. *Física espectral:* Clorofila absorbe rojo (660nm); estructura celular mesófila refleja infrarrojo cercano (860nm): \(\text{NDVI} = \frac{\text{NIR}-\text{Red}}{\text{NIR}+\text{Red}}\).
  2. *Asíntota de saturación:* Con Índice de Área Foliar (\(\text{LAI} > 3\)), el NDVI se estanca en \(\sim 0.75-0.80\) mientras la biomasa leñosa y el fruto siguen variando.
  3. *Sospecha biofísica:* En cultivos bajo sombra como el café en Jaén, la copa siempre verde puede enmascarar un colapso en la producción del grano.
- **Frase-clave (H1):** *"Cuando el follaje es denso, el NDVI satura: con coeficientes de variación de apenas 2.3% en la copa, el satélite óptico es ciego a lo que ocurre bajo las ramas."*
- **Visual:** Firma espectral de la hoja viva y curva no lineal de saturación del NDVI frente al ascenso continuo de EVI y NDRE.
- **Guion del orador:** "El satélite mide cómo la clorofila absorbe luz roja y refleja infrarrojo. Pero cuando el bosque o cafetal cierra su dosel, el índice satura cerca a 0.8. Si las hojas de arriba están verdes, el satélite cree que todo va perfecto, aunque abajo no haya grano."

---

### Diapositiva 09: El reloj botánico fenológico
- **Insignia:** `MECANISMO` | **Tiempo sugerido:** 1.5 min
- **Tesis:** Un grado de calor o un milímetro de lluvia tienen impactos diametralmente opuestos según la ventana biológica en que impactan al cultivo.
- **Puntos clave:**
  1. *Floración crítica (Ago–Oct):* Temperaturas máximas superiores a 32 °C provocan esterilidad de polen y aborto floral masivo.
  2. *Llenado de fruto (Nov–Feb):* Demanda hídrica alta; el estrés hídrico reduce drásticamente el peso del grano pergamino.
  3. *Cosecha (Mar–Jul):* Lluvias torrenciales retrasan el secado y pudren las cerezas; calor seco moderado beneficia la recolección.
- **Frase-clave:** *"El mismo calor no daña igual en floración que en cosecha."*
- **Visual:** Anillo fenológico circular de 365 días sincronizado con las ventanas climáticas de Jaén.
- **Guion del orador:** "El tiempo biológico no es lineal. 35 °C en época de cosecha solo seca el café más rápido; 35 °C en plena floración quema la flor y destruye la campaña completa."

---

### Diapositiva 10: Física global: discrepancia entre agencias
- **Insignia:** `EVIDENCIA` | **Tiempo sugerido:** 2.0 min
- **Tesis:** Las agencias meteorológicas resuelven Navier-Stokes con asimilación 4D-Var en supercomputadores de 11,000 núcleos; aun así, divergen intensamente en el trópico.
- **Puntos clave:**
  1. *ECMWF vs NOAA GFS:* Modelos globales de frontera con resolución de 9km a 25km.
  2. *Discrepancia real en Iquitos:* Para idénticos horizontes temporales, la diferencia media absoluta alcanza **6.36 °C** (máxima de 9.3 °C) y hasta **29.3 mm** de lluvia diaria.
  3. *Conclusión epistemológica:* Si la física determinista multimillonaria no llega a un valor único, un pronóstico puntual carece de honestidad científica.
- **Frase-clave:** *"Incluso la física más cara del mundo tiene incertidumbre."*
- **Visual:** Gráfico comparativo de barras de la discrepancia térmica real NOAA GFS vs ECMWF IFS en Punchana.
- **Guion del orador:** "La física atmosférica no es perfecta. Comparamos los pronósticos de NOAA y ECMWF para Punchana: difieren en promedio por más de 6 °C. Si los supercomputadores más caros no se ponen de acuerdo, un pronóstico de una sola línea es una ilusión."

---

### Diapositiva 11: GraphCast: la IA en la meteorología planetaria
- **Insignia:** `EVIDENCIA` | **Tiempo sugerido:** 1.5 min
- **Tesis:** DeepMind demostró que una Graph Neural Network sobre una malla icosaédrica terrestre supera a los supercomputadores físicos en el 90.3% de 1,380 variables meteorológicas.
- **Puntos clave:**
  1. *Malla icosaédrica multiescala:* Resuelve singularidades polares conectando celdas de 0.25° mediante propagación de mensajes espaciales.
  2. *Eficiencia computacional:* Pronóstico global a 10 días en **menos de 60 segundos** en una sola TPU v4, frente a horas en supercomputadores de 11,664 núcleos.
  3. *Transición al mundo real:* La IA global triunfa a gran escala. Pero, ¿qué ocurre en un sensor local en la Amazonía?
- **Frase-clave:** *"Un minuto en un chip frente a una hora en 11,664 núcleos."*
- **Visual:** Esquema de la malla icosaédrica de GraphCast y comparativa de tiempo/hardware con el ECMWF.
- **Guion del orador:** "DeepMind usó redes neuronales en grafos para superar a los modelos físicos globales en el 90% de variables, pasando de horas en miles de núcleos a menos de un minuto en un solo chip."

---

## ACTO 3: CASO A - IQUITOS (~6.5 min)

### Diapositiva 12: Contexto Punchana: datos reales en la Amazonía
- **Insignia:** `CASO REAL` | **Tiempo sugerido:** 1.5 min
- **Tesis:** La Amazonía profunda pone a prueba cualquier modelo: sensores que fallan, humedad implacable del 85% y perturbaciones sinópticas polares (friajes).
- **Puntos clave:**
  1. *Estación Punchana (SENAMHI):* Confluencia Nanay–Amazonas (-3.69°S, -73.26°W, 91 msnm).
  2. *Imperfección de datos:* 2,557 días (2019–2025). La temperatura máxima tiene **9.7% de huecos** que deben tratarse con interpolación transparente sin invención.
  3. *Régimen térmico:* Friaje histórico con mínima de **19.2 °C** y olas de calor de hasta **37.4 °C**.
- **Frase-clave:** *"Los datos reales tienen huecos; tratarlos es parte del modelo."*
- **Visual:** Mapa Leaflet centrado en Punchana y serie temporal de 120 días con eventos de friaje destacados.
- **Guion del orador:** "Entramos al Caso A: Iquitos. 7 años de datos de SENAMHI. Los sensores reales se caen, tienen 9.7% de datos faltantes y sufren friajes que bajan la temperatura a 19 °C. Limpiar y tratar estos datos es el 80% del trabajo."

---

### Diapositiva 13: Benchmark de 8 modelos: la revelación de la parsimonia
- **Insignia:** `EVIDENCIA` | **Tiempo sugerido:** 3.0 min
- **Tesis:** Sometimos a prueba 8 modelos sobre un holdout ciego de 90 días en Punchana. 70 veces más cómputo no compra mayor precisión en una sola estación.
- **Puntos clave:**
  1. *Ganador por parsimonia:* **ExtraTrees** logra RMSE de **1.880 °C** en apenas **0.11 segundos** de CPU.
  2. *Empates Diebold-Mariano (\(p > 0.05\)):* Random Forest (1.885 °C, \(p=0.918\)), ARIMA (1.964 °C, \(p=0.151\)) y TimesFM 200M (1.965 °C, \(p=0.275\)) empatan estadísticamente.
  3. *Sorpresa Zero-Shot:* TimesFM logró el menor MAE del benchmark (**1.392 °C**) sin conocer la serie previamente. Redes profundas (LSTM PyTorch) resultaron estadísticamente inferiores (2.054 °C, \(p=0.029\)).
- **Frase-clave:** *"Para una sola estación, 70 veces más cómputo no compra precisión: la parsimonia manda, aunque el Zero-Shot ya compite sin haber visto la serie."*
- **Visual:** Gráfico de barras horizontales de RMSE ordenadas, con codificación de colores para el ganador, empates estadísticos e inferiores.
- **Guion del orador:** "Aquí está el resultado sin filtros. ExtraTrees en 0.11 segundos de CPU empató estadísticamente con TimesFM de Google de 200 millones de parámetros y con ARIMA. La regla de parsimonia manda: para una sola estación, no gastes cómputo innecesario. Sin embargo, TimesFM logró el menor MAE en puro zero-shot."

---

### Diapositiva 14: DEMO 1: Pronóstico operativo a 7 días
- **Insignia:** `DEMO` | **Tiempo sugerido:** 2.0 min
- **Tesis:** La toma de decisiones operativas no se apoya en predicciones puntuales sino en la cuantificación honesta de las bandas de incertidumbre residual.
- **Puntos clave:**
  1. *Pronóstico ExtraTrees:* Curva central acoplada a la banda de cuantiles empíricos P10–P90.
  2. *TimesFM Zero-Shot:* Trayectoria proyectada por el modelo fundacional de Google sin entrenamiento local.
  3. *Conmutadores interactivos:* Superposición en tiempo real de los pronósticos de NOAA GFS y ECMWF IFS.
- **Frase-clave:** *"El valor está en la banda, no en la línea."*
- **Visual:** Chart.js dinámico conectado a `data/caso_1/senamhi_forecast_7d.csv` con botones interactivos para activar/desactivar agencias globales.
- **Guion del orador:** "Miren esta demo interactiva conectada a los datos reales. La línea central es solo una guía; lo que importa para la toma de decisiones son las bandas P10 y P90. Podemos comparar en vivo con GFS y ECMWF."

---

## ACTO 4: CASO B - JAÉN (~6 min)

### Diapositiva 15: Contexto Jaén: rendimiento oficial y satélite real
- **Insignia:** `CASO REAL` | **Tiempo sugerido:** 1.5 min
- **Tesis:** Auditamos 24 campañas cafetaleras oficiales (2000–2024), 576 compuestos satelitales MODIS Terra y el reanálisis ERA5 para contrastar la teoría con la realidad.
- **Puntos clave:**
  1. *SIEA / MIDAGRI / INEI:* Serie oficial de rendimiento auditada con control de consistencia aritmética (\(\Delta < 0.1\%\)).
  2. *MODIS MOD13Q1:* Mediana espacial con máscara de píxeles fiables dentro del polígono oficial de Jaén.
  3. *Límite declarado:* Rendimiento promedio provincial de \(\sim 45,000\text{ ha}\), no de una chacra experimental aislada.
- **Frase-clave:** *"Datos públicos, imperfectos y verificables valen más que datos perfectos inventados."*
- **Visual:** Mapa interactivo de Jaén con polígono vectorial y serie histórica de 24 años de rendimiento oficial.
- **Guion del orador:** "Pasamos a Jaén: 24 campañas auditadas del Ministerio de Agricultura y 576 pasadas del satélite MODIS. Aquí no hay datos inventados; es la producción real provincial."

---

### Diapositiva 16: ¿Ve el satélite lo que ocurrió? La ceguera de la roya
- **Insignia:** `EVIDENCIA` | **Tiempo sugerido:** 2.5 min
- **Tesis:** La correlación entre el NDVI anual y el rendimiento de café es nula (\(r=0.154, p=0.600\)). En la mayor catástrofe agrícola del siglo, el satélite fue completamente ciego.
- **Puntos clave:**
  1. *La Crisis de la Roya (2012–2014):* El rendimiento oficial cayó **-56.0%** (de 22.7 a 10.0 qq/ha). El NDVI MODIS subió **+1.4%** (de 0.738 a 0.748).
  2. *Costo del error óptico:* 12.7 qq/ha perdidos en 45,000 ha a S/. 400/qq equivale a **S/. 228 millones** sin alerta satelital.
  3. *Lo que sí predijo la cosecha:* La lluvia en floración (\(r = 0.751, p = 0.002\)) y el balance hídrico (\(r = 0.756\)) explicaron más del 56% de la variabilidad.
- **Frase-clave (H1 & H4):** *"Un satélite verde no garantiza cosecha: en la crisis de la roya de 2014, el rendimiento cayó 56% mientras el NDVI subió 1.4%."*
- **Visual:** Diagrama de dispersión NDVI vs Rendimiento y desglose forense de la crisis de la roya 2012–2014.
- **Guion del orador:** "Este es el hallazgo más contundente: en la crisis de la roya de 2014, el rendimiento de Jaén cayó 56%. Pero el satélite MODIS marcó un NDVI idéntico (+1.4%). El satélite vio el follaje verde y no se enteró del desastre. En cambio, la lluvia en floración sí anticipó el rendimiento con r = 0.75."

---

### Diapositiva 17: DEMO 2: Validación honesta por ventana expansiva
- **Insignia:** `DEMO` | **Tiempo sugerido:** 2.0 min
- **Tesis:** Sin trampas de validación: evaluar año a año entrenando únicamente con campañas del pasado expone la fragilidad de modelos satelitales puros.
- **Puntos clave:**
  1. *Ventana expansiva (Walk-Forward):* Entrenamiento inicial 2000–2014; prueba ciega en 2015–2024.
  2. *El satélite degrada el pronóstico:* Modelo de Tendencia (MAE 4.79 qq/ha) vs Solo NDVI (MAE **5.32 qq/ha**). Añadir satélite saturado aumentó el error.
  3. *Fusión multimodal:* La combinación de clima en floración con tendencia redujo el error a **4.51 qq/ha**.
- **Frase-clave (H3):** *"Un modelo honesto muestra dónde falla: la validación temporal sin trampas revela que ningún algoritmo anticipa una plaga sin datos de campo."*
- **Visual:** Chart.js interactivo con la predicción retrospectiva de los 4 modelos sobre las últimas 10 campañas reales.
- **Guion del orador:** "En esta demo probamos 4 modelos año por año entrenando solo con el pasado. Agregar solo satélite empeora el error de 4.79 a 5.32 qq/ha. La fusión de clima de floración con tendencia histórica logra el mejor resultado con 4.51 qq/ha."

---

## ACTO 5: DECIDIR (~5.5 min)

### Diapositiva 18: 5 lecciones innegociables
- **Insignia:** `TEORÍA` | **Tiempo sugerido:** 2.0 min
- **Tesis:** Principios metodológicos destilados de 2,557 días de meteorología amazónica y 24 campañas cafetaleras reales auditadas.
- **Puntos clave:**
  1. *Respeta la flecha del tiempo:* Jamás apliques k-fold aleatorio en series temporales.
  2. *Baseline parsimonioso primero:* ExtraTrees y ARIMA empataron con modelos de 200M en 0.11s de cómputo.
  3. *Bandas probabilísticas obligatorias:* Reportar un punto esconde el riesgo.
  4. *La física manda antes que el código:* Conoce las limitaciones biofísicas de tus sensores (saturación NDVI).
  5. *Complejidad justificada por escala:* Redes profundas brillan con millones de series, no en sensores locales individuales.
- **Frase-clave:** *"El rigor metodológico vale más que cualquier arquitectura neuronal."*
- **Visual:** 5 tarjetas estructuradas con enlaces conceptuales a los experimentos empíricos presentados.
- **Guion del orador:** "Cinco lecciones para su carrera: valida respetando la flecha del tiempo, empieza con un baseline simple, comunica bandas de incertidumbre, revisa la física del sensor antes de afinar modelos, y usa redes profundas solo cuando tengas volumen masivo."

---

### Diapositiva 19: ¿Qué modelo uso? Árbol de decisión
- **Insignia:** `TEORÍA` | **Tiempo sugerido:** 2.0 min
- **Tesis:** Una guía algorítmica para seleccionar la arquitectura adecuada según el volumen de datos, las covariables y el objetivo del problema.
- **Puntos clave:**
  1. *1 serie local corta (<3,000 registros):* Modelos clásicos (ARIMA/ETS) o ExtraTrees con rezagos.
  2. *Riesgo de récords térmicos fuera de rango:* Modela primeras diferencias (\(\Delta y\)), jamás niveles directos en árboles.
  3. *Covariables climáticas y biofísicas:* Fusión tabular tras auditar la correlación en la ventana fenológica sensible.
  4. *Miles de series heterogéneas sin reentreno:* Foundation Models Zero-Shot (TimesFM).
- **Frase-clave:** *"La complejidad se gana con evidencia, no se asume por defecto."*
- **Visual:** Flujo interactivo de bifurcación de preguntas que conduce a la arquitectura recomendada.
- **Guion del orador:** "¿Qué modelo uso mañana en mi tesis o proyecto? Si es una sola serie corta, ARIMA o árboles. Si hay récords térmicos, modela diferencias. Si tienes miles de series, usa Foundation Models."

---

### Diapositiva 20: Cierre y recursos abiertos
- **Insignia:** `TEORÍA` | **Tiempo sugerido:** 1.5 min
- **Tesis:** Volvemos al cono inicial: la inteligencia artificial no elimina la incertidumbre del mundo, pero nos ofrece la disciplina matemática para decidir mejor.
- **Puntos clave:**
  1. *Código y datos 100% abiertos:* Repositorio con notebooks ejecutables y datos auditados.
  2. *49 Referencias académicas:* Nature, Science, ICML, TMLR y compendios del INEI/MIDAGRI.
  3. *Reproducibilidad completa:* Cuadernos listos para correr y auditar.
- **Frase-clave final:** *"¿Puede la IA predecir el futuro? No. Puede ayudarnos a decidir mejor sin conocerlo."*
- **Visual:** Cierre en espejo con el cono estocástico transformado en decisiones operativas y código QR al repositorio.
- **Guion del orador:** "¿Puede la IA predecir el futuro? No. Pero si la usamos con honestidad metodológica y cuantificando la incertidumbre, nos ayuda a tomar mejores decisiones en un mundo incierto. Todo el código y los datos están en el repositorio abierto. ¡Muchas gracias!"
