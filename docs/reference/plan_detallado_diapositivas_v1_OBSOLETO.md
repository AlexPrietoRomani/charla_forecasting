# Plan Maestro y Guion Visual Diapositiva por Diapositiva (25 Slides)
## Charla: "¿Puede la IA predecir el futuro? Lecciones de forecasting desde el mundo real"

---

## 0. Diagnóstico Visual del Estado Actual (Auditoría con Playwright / Headless Browser)

Tras renderizar y capturar las diapositivas a resolución 1600×900 y 1920×1080, se identificaron los siguientes problemas estructurales:
1. **Huecos y Vacíos Excesivos (Dead Space):** Al pasar a ancho completo (`calc(100vw - 56px)` y `100vh`), las tarjetas con 4 líneas de texto o SVGs pequeños dejan entre 50% y 85% del lienzo en blanco (evidente en Diapos 2, 4, 6, 7, 9, 13, 14).
2. **Animaciones que no cuentan historia:** Algunas animaciones solo muestran líneas trazadas sin etapas pedagógicas explicadas paso a paso.
3. **Fórmulas matemáticas rotas:** Caracteres LaTeX sin renderizar o con símbolos Unicode corruptos (`\u0000lpha` en Holt-Winters).
4. **Desconexión entre el gráfico y el texto:** En Diapo 14 (Open-Meteo), el gráfico ocupa arriba y deja todo el tercio inferior desierto sin explicar *por qué* discrepan NOAA y ECMWF ni qué significa para el tomador de decisiones.

A continuación se detalla la **reingeniería pedagógica y visual de cada una de las 25 diapositivas**.

---

## Bloque 1: Introducción y Fundamentos Ontológicos (Slides 1 a 3)

### Slide 01 — Portada & Gancho Provocador
* **Propósito:** Captar la atención inmediata desmitificando la "bola de cristal" de la IA.
* **Ilación:** Punto de partida cero. Abre la pregunta central: ¿la IA predice o calcula probabilidades?
* **Guion para público profano (Speaker Script):**
  > "Cuando escuchamos 'Inteligencia Artificial para predecir el futuro', solemos imaginar una bola de cristal o una máquina que sabe qué va a pasar mañana con certeza matemática. Hoy vamos a desmontar ese mito. La IA no sabe el futuro. Lo que hace la estadística y el aprendizaje automático es **cuantificar la incertidumbre** para que los humanos podamos tomar decisiones de millones de dólares o salvar cosechas enteras bajo riesgo controlado. Veremos cómo predecimos el clima en la Amazonía peruana y la cosecha de café en Jaén con satélites espaciales."
* **¿Lleva Animación?:** **Sí**.
  * **Qué cuenta la animación:** Un pulso temporal tipo radar/sonar que barre una serie ruidosa y revela una banda de incertidumbre cónica que se ensancha hacia el horizonte futuro, simbolizando que el futuro nunca es una línea fija, sino un cono de probabilidades.
* **Layout y Elementos para llenar armónicamente el espacio:**
  * **Columna Izquierda (55%):** Título de gran impacto tipográfico, subtítulo con badges contextuales (SENAMHI, Sentinel-2, NOAA, Open-Meteo), autoría y llamada a la acción.
  * **Columna Derecha (45%):** Canvas visual del pulso radar + 3 tarjetas métricas resumen de lo que verán en la charla: `7 Años de Clima Diario`, `6 Campañas Satelitales`, `±1.65σ Incertidumbre`.

---

### Slide 02 — Anatomía de una Serie Temporal desde Cero
* **Propósito:** Explicar los 4 componentes ontológicos de cualquier serie temporal a una persona que jamás ha visto matemáticas.
* **Ilación:** Conecta con la portada: antes de predecir, tenemos que desarmar el reloj para ver qué engranajes lo mueven.
* **Guion para público profano (Speaker Script):**
  > "Imaginemos que medimos la temperatura todos los días. Esa curva que parece un electrocardiograma caótico en realidad es la suma de 4 fuerzas: 
  > 1) La **Tendencia**: la dirección a largo plazo (el calentamiento global o el envejecimiento de una planta). 
  > 2) La **Estacionalidad**: el ritmo fijo del calendario (hace más calor al mediodía que a medianoche, o en verano que en invierno).
  > 3) El **Ciclo**: mareas irregulares de varios años, como el Fenómeno de El Niño.
  > 4) El **Ruido**: una ráfaga de viento o una nube que tapó el sol hoy a las 3 PM. 
  > Predecir consiste en modelar los primeros tres y no dejarse engañar por el cuarto."
* **¿Lleva Animación?:** **Sí (Interactiva / Paso a Paso)**.
  * **Qué cuenta la animación:** Una descomposición visual acumulativa en 4 pasos:
    - *Paso 1:* Se dibuja la línea de tendencia base suave.
    - *Paso 2:* Se le monta encima la onda estacional senoidal que sube y baja regularmente.
    - *Paso 3:* Se suma la fluctuación cíclica plurianual de El Niño.
    - *Paso 4:* Se inyecta el ruido gaussiano final, revelando la serie real caótica. El usuario puede ver cómo cada componente se suma.
* **Layout y Elementos para llenar armónicamente el espacio:**
  * **Panel Superior / Izquierdo (55%):** El gráfico dinámico interactivo con selector de componentes (Tendencia / Estacionalidad / Ciclo / Ruido).
  * **Panel Derecho (45%):** 4 tarjetas explicativas con ejemplos de la vida real (Agricultura, Tráfico, Temperatura, Ventas de retail), fórmula matemática tipografiada limpiamente ($Y_t = T_t + S_t + C_t + \epsilon_t$), y nota clave: *"El error fatal del principiante es intentar predecir el ruido estocástico"*.

---

### Slide 03 — El Gran Mapa de los 4 Paradigmas
* **Propósito:** Mostrar el mapa de ruta conceptual de toda la charla para que la audiencia nunca se pierda.
* **Ilación:** Una vez entendido qué es una serie, ¿con qué herramientas la atacamos?
* **Guion para público profano (Speaker Script):**
  > "Para atacar una serie no hay una sola IA, hay 4 escuelas de pensamiento completamente diferentes:
  > Primero, los **Métodos Paramétricos y Clásicos**, que usan fórmulas matemáticas elegantes como curvas de crecimiento y ARIMA.
  > Segundo, el **Machine Learning Tabular y Deep Learning**, que convierten el tiempo en filas y columnas o usan redes recurrentes.
  > Tercero, la **Biofísica Satelital**, donde los datos no vienen de un termómetro, sino del reflejo de la luz infrarroja en las hojas de los cultivos a 786 km de altura.
  > Y cuarto, los **Modelos Físicos Globales y Zero-Shot**, supercomputadores de agencias espaciales y modelos gigantes que predicen sin reentrenar. Vamos a explorar cada uno."
* **¿Lleva Animación?:** **No (Estructura de cuadrantes navegable)**.
  * **Por qué no:** Es un mapa mental de alto nivel; la claridad estática con badges de colores, íconos y contraste nítido es superior para no saturar cognitivamente.
* **Layout y Elementos:**
  * Grid de 4 tarjetas grandes (2x2) que llenan toda la pantalla.
  * Cada tarjeta tiene: Ícono, Nombre del Paradigma, Pregunta que responde, Modelos representativos, Nivel de datos requerido y Ventaja competitiva principal.

---

## Bloque 2: Explicación Profunda de Familias y Mecanismos (Slides 4 a 15)

### Slide 04 — Paradigma 1: Curvas Paramétricas y Crecimiento Físico
* **Propósito:** Explicar cómo la naturaleza y los negocios siguen leyes matemáticas de crecimiento (exponencial vs saturación logística) y cómo Holt-Winters captura la inercia.
* **Ilación:** Arrancamos por lo más intuitivo y fundamentado: cuando conocemos la física del problema.
* **Guion para público profano (Speaker Script):**
  > "Si lanzamos un producto o una planta germina, al principio crece exponencialmente: cada día se duplica. Pero en el mundo real los recursos son finitos: el campo tiene un límite de espacio, el mercado tiene un límite de clientes. Por eso, el crecimiento exponencial se dobla y se convierte en una **curva logística o sigmoide** con una asíntota o techo máximo. Si usamos una IA compleja sin saber esto, pronosticará que los árboles crecerán hasta la luna. Holt-Winters, por su parte, pondera el pasado reciente: lo que pasó ayer pesa más que lo que pasó hace un año."
* **¿Lleva Animación?:** **Sí (Simulador de Parámetros de Curva)**.
  * **Qué cuenta la animación:** La curva logística generándose en vivo mostrando cómo al variar la capacidad de carga ($L$) o la tasa de crecimiento ($k$), la curva cambia de pendiente y choca contra el techo biológico. A su lado, Holt-Winters mostrando cómo los pesos decaen exponencialmente hacia el pasado ($\alpha(1-\alpha)^k$).
* **Layout:**
  * **Izquierda (50%):** Gráfico interactivo con las 3 curvas (Exponencial roja disparándose al infinito vs Logística verde saturándose en el límite $L$ vs Lineal gris de referencia) + etiquetas dinámicas sin superposición.
  * **Derecha (50%):** 3 bloques explicativos: 1) Cuándo aplicar curva logística (cultivos, epidemias, adopción tecnológica), 2) Suavizado Holt-Winters desglosado (Nivel, Tendencia, Estacionalidad), 3) Advertencia práctica: *"No uses regresión lineal cuando la biología impone un techo"*.

---

### Slide 05 — Paradigma 1: Descomposición Estadística (ARIMA, SARIMAX, Prophet)
* **Propósito:** Explicar cómo funcionan los modelos clásicos sin asustar con ecuaciones incomprensibles.
* **Ilación:** Si la serie no es solo una curva suave, sino que rebota día a día, ¿cómo modelamos ese rebote?
* **Guion para público profano (Speaker Script):**
  > "ARIMA hace algo muy simple e intuitivo: mira cómo el dato de hoy depende de los datos de los días anteriores (Autorregresión, AR) y cómo los errores de cálculo recientes ayudan a corregir el rumbo (Media Móvil, MA). Prophet, creado por Meta, hace lo contrario: divide la serie en piezas de lego (tendencia + día de la semana + fiestas patrias + feriados). Son los reyes indiscutibles para pronósticos de 1 a 7 días cuando tenemos datos limpios de una sola estación."
* **¿Lleva Animación?:** **No (Diagrama de Flujo Arquitectónico Limpio)**.
* **Layout:**
  * **Izquierda (50%):** Anatomía visual de ARIMA (Ecuación desglosada con colores: término autoregresivo $p$, diferenciación $d$, término de choque $q$) y cuándo es imbatible.
  * **Derecha (50%):** Prophet descompuesto en piezas de lego visuales (Línea de tendencia + barras de día de la semana + picos de feriados). Tabla comparativa inferior: ARIMA vs Prophet (Ventajas, desventajas, interpretabilidad).

---

### Slide 06 — Paradigma 2: El Puente Tabular (Lags y Rolling Stats)
* **Propósito:** Revelar el truco fundamental que permite usar Random Forest o XGBoost en series de tiempo.
* **Ilación:** Los modelos de árboles son los más usados en la industria, pero ¿cómo "entiende" el tiempo un árbol que solo sabe tabular?
* **Guion para público profano (Speaker Script):**
  > "Un árbol de decisión no sabe qué es el martes ni qué significa 'ayer'. Solo sabe leer tablas de Excel con filas independientes. Para enseñarle a pronosticar, construimos un **puente temporal**: convertimos la serie en una ventana deslizante. La columna objetivo es la temperatura de hoy; las columnas predictoras son: ¿cuánto midió ayer? (Lag 1), ¿hace 7 días? (Lag 7), ¿cuál fue el promedio de la última semana? (Rolling Mean). Así, transformamos una película continua en una sucesión de fotos para que el bosque aprenda patrones."
* **¿Lleva Animación?:** **Sí (Ventana Deslizante Paso a Paso)**.
  * **Qué cuenta la animación:** La matriz de datos llenándose: una serie temporal horizontal donde un marco selector rectangular avanza día por día, y en cada paso "empuja" los valores hacia las columnas de una tabla supervisada ($X_1, X_2, X_7, \text{Target}$).
* **Layout:**
  * **Izquierda (55%):** Animación de la ventana deslizante interactiva con datos reales de SENAMHI.
  * **Derecha (45%):** Tabla de feature engineering con los 3 tipos de features temporales: Lags puros, Estadísticas rodantes (Rolling Mean/Std) y Variables cíclicas ($\sin(2\pi d/365)$ y $\cos(2\pi d/365)$) para que el modelo entienda que el 31 de diciembre está pegado al 1 de enero.

---

### Slide 07 — Paradigma 2: La Patología de No-Extrapolación de los Árboles
* **Propósito:** Mostrar la limitación fatal más importante del Machine Learning tabular (concepto crítico para evitar catástrofes en producción).
* **Ilación:** Random Forest parece perfecto, pero tiene una falla de diseño congénita que todo ingeniero debe conocer.
* **Guion para público profano (Speaker Script):**
  > "Presten mucha atención a esto: **los árboles de decisión no pueden extrapolar**. Un árbol solo sabe cortar el espacio conocido en cajitas cuadradas y promediar los datos de entrenamiento. Si en el entrenamiento la temperatura máxima histórica fue de 35 °C, y el cambio climático trae una ola de calor de 39 °C, el Random Forest predecirá exactamente 35 °C: una línea plana horizontal. Jamás predecirá un valor mayor al máximo histórico que vio. Si tu problema tiene tendencia creciente (inflación, ventas de una startup en expansión), un árbol puro te llevará al desastre si no diferencias la serie antes."
* **¿Lleva Animación?:** **Sí (Contraste Visual Extrapolación vs Meseta)**.
  * **Qué cuenta la animación:** Una serie que rompe hacia arriba un récord histórico. La regresión lineal sigue subiendo; el Random Forest se aplana en una línea horizontal punteada roja demostrando visualmente la meseta.
* **Layout:**
  * **Izquierda (55%):** Gráfico interactivo: Curva real superando el umbral histórico vs Predicción de Árbol (meseta plana) vs Modelo con Diferenciación.
  * **Derecha (45%):** 3 tarjetas de impacto: 1) La Causa Matemática (cortes ortogonales invariantes a orden), 2) Los Casos Fatales (inflación récord, pandemias, calor extremo), 3) La Solución Obligatoria (modelar $\Delta Y_t$ o desestacionalizar antes de entrenar).

---

### Slide 08 — Paradigma 2: Deep Learning Secuencial (LSTM vs PatchTST)
* **Propósito:** Explicar cómo las redes neuronales procesan secuencias y cómo la arquitectura moderna cambió de recurrencia a parches de atención.
* **Ilación:** Si los árboles no tienen memoria temporal nativa, ¿qué pasa con las redes creadas específicamente para secuencias?
* **Guion para público profano (Speaker Script):**
  > "Durante décadas usamos LSTMs: redes con 'compuertas' de memoria que deciden qué olvidar de hace 10 días y qué recordar hoy. Pero procesar dato por dato es lento y olvida secuencias muy largas. En 2023 la arquitectura cambió radicalmente con **PatchTST**: en lugar de mirar punto por punto diario, corta la serie en 'parches' de 16 días (como si fueran palabras en una frase) y aplica Transformer con auto-atención para relacionar el parche de este verano con el parche del verano pasado."
* **¿Lleva Animación?:** **Sí (Circuito de Compuertas LSTM vs Parches PatchTST)**.
  * **Qué cuenta la animación:** 
    - Lado A: Una bolita de información pasando secuencialmente por las 3 compuertas de la LSTM (olvido, entrada, salida).
    - Lado B: La serie cortándose en bloques de colores (parches) y flechas de atención conectando parches distantes en paralelo.
* **Layout:**
  * **Mitad Izquierda (50%):** Circuito visual interactivo LSTM con compuertas explicadas ($f_t, i_t, \tilde{C}_t, o_t$).
  * **Mitad Derecha (50%):** Mecanismo de parches de PatchTST con tokens temporales y proyección de atención cruzada.

---

### Slide 09 — Paradigma 2: Análisis Crítico de Redes (Mito de la Serie Única)
* **Propósito:** Vacunar a la audiencia contra la trampa del *hype* de Deep Learning aplicado a ciegas.
* **Ilación:** Si PatchTST y LSTM son tan avanzados, ¿debemos usarlos para todo? No.
* **Guion para público profano (Speaker Script):**
  > "Aquí viene la lección más dura del mundo real: **entrenar una red neuronal profunda sobre una sola estación meteorológica o un solo producto suele ser un desperdicio colosal de tiempo y dinero**. En una sola serie, un Random Forest o un ARIMA entrenan en 2 segundos en tu laptop y suelen tener menor error que una red de millones de parámetros que tarda 2 horas y sobreajusta el ruido. ¿Cuándo sí gana Deep Learning? Cuando tienes 100,000 series simultáneas (todas las tiendas de un supermercado) y usas modelos multivariados como DeepAR o Temporal Fusion Transformers (TFT)."
* **¿Lleva Animación?:** **No (Matriz de Realidad de Costo / Beneficio)**.
* **Layout:**
  * **Panel Izquierdo (50%):** Gráfico de Dispersión / Trade-off: Volumen de datos ($X$) vs Complejidad del Modelo ($Y$) mostrando la "Zona de Desastre de DL" (poco dato + mucha red = sobreajuste masivo).
  * **Panel Derecho (50%):** Tabla de auditoría empírica: Tiempo de entrenamiento, consumo energético, interpretabilidad y RMSE comparativo. Tarjeta destacada con la regla de oro: *"Si puedes resolverlo con ExtraTrees en 1 segundo, no uses un Transformer"*.

---

### Slide 10 — Paradigma 3: Visión por Computador en el Agro
* **Propósito:** Mostrar cómo la IA de visión extrae datos que alimentan los pronósticos agrícolas antes de mirar los satélites.
* **Ilación:** Pasamos del termómetro a los ojos de la IA en el campo.
* **Guion para público profano (Speaker Script):**
  > "Para predecir cuántos quintales de café cosecharemos, antes contábamos a mano en unas pocas ramas. Hoy la visión artificial lo hace a escala: con drones y teléfonos, **YOLOv12** cuenta granos de café maduros en milisegundos con mecanismos de atención de área; **SAM 2.1** de Meta segmenta automáticamente la copa de cada cafeto individual aislando el suelo; y **DINOv2** genera representaciones visuales del estado de salud de la hoja sin supervisión humana previa."
* **¿Lleva Animación?:** **Sí (Detección de Drones y Bounding Boxes)**.
  * **Qué cuenta la animación:** Una imagen de cafetal donde un dron pasa: se proyectan *bounding boxes* verdes sobre cerezas maduras con conteo en tiempo real ($N = 1,420$ granos/planta) y polígonos de segmentación de copa.
* **Layout:**
  * **Izquierda (55%):** Visualizador de visión por computador (YOLOv12 detection + SAM mask).
  * **Derecha (45%):** 3 tarjetas técnicas: 1) YOLOv12 (inferencia en 1.6 ms y atención por área A2), 2) SAM 2.1 (máscaras de biomasa de dosel), 3) De la imagen al número: cómo las detecciones se convierten en features de densidad para el modelo de rendimiento.

---

### Slide 11 — Paradigma 3: Biofísica Satelital & Saturación Espectral
* **Propósito:** Explicar la física del sensor orbital Sentinel-2 y el fenómeno de la saturación del NDVI (piedra angular de la charla).
* **Ilación:** Si el dron cubre hectáreas, el satélite cubre valles enteros desde el espacio. Pero los satélites tienen trampas físicas.
* **Guion para público profano (Speaker Script):**
  > "Sentinel-2 orbita a 786 km de altura midiendo la luz que refleja la Tierra en 13 bandas. La clorofila de una planta sana absorbe con avidez la luz Roja para hacer fotosíntesis, pero sus células esponjosas rebotan casi toda la luz Infrarroja Cercana (NIR) para no sobrecalentarse. El NDVI mide esa diferencia. Pero aquí está la trampa: cuando el cafetal es muy denso (Índice de Área Foliar > 3), el NDVI se satura: da 0.85 tanto si la planta está llena de frutos como si está sufriendo estrés interno. Por eso usamos EVI y NDRE (borde rojo), que penetran el dosel sin saturarse."
* **¿Lleva Animación?:** **Sí (Curva Espectral y Saturación Foliar)**.
  * **Qué cuenta la animación:**
    - Superior: Un haz de luz solar cayendo sobre una hoja; el Rojo entra y se absorbe (flecha corta), el NIR rebota con fuerza (flecha larga).
    - Inferior: Curva asintótica de saturación: el NDVI sube rápido y se aplana en 0.80 a pesar de que la biomasa sigue creciendo, mientras que el EVI sigue subiendo de forma lineal y sensible.
* **Layout:**
  * **Izquierda (55%):** Diagrama óptico interactivo de la hoja + Gráfico de saturación (Biomasa vs NDVI vs EVI vs NDRE).
  * **Derecha (45%):** Fórmulas exactas de AgroVisión tipografiadas con significado físico:
    - $\text{NDVI} = \frac{\text{B08} - \text{B04}}{\text{B08} + \text{B04}}$
    - $\text{EVI} = 2.5 \times \frac{\text{B08} - \text{B04}}{\text{B08} + 6\,\text{B04} - 7.5\,\text{B02} + 1}$
    - $\text{NDRE} = \frac{\text{B08} - \text{B05}}{\text{B08} + \text{B05}}$ (el centinela del nitrógeno).

---

### Slide 12 — Paradigma 3: Fusión Multimodal Biofísica
* **Propósito:** Mostrar cómo se acopla la teledetección espacial con la fenología botánica del cultivo y el clima.
* **Ilación:** Un índice satelital solo no predice la cosecha; tiene que estar amarrado al reloj biológico del café.
* **Guion para público profano (Speaker Script):**
  > "El café no crece todo el año al mismo ritmo. En Jaén tiene 3 fases sagradas: 1) **Floración** (agosto-octubre): donde la lluvia define cuántas flores brotan. 2) **Llenado de grano** (noviembre-febrero): donde la planta necesita máxima energía solar y agua equilibrada. 3) **Cosecha** (marzo-julio): donde el exceso de lluvia pudre el grano. La verdadera IA no mete un promedio anual ciego: integra la integral de EVI y el balance hídrico en cada una de esas tres ventanas específicas."
* **¿Lleva Animación?:** **Sí (Línea de Tiempo Fenológica Sincronizada)**.
  * **Qué cuenta la animación:** Una barra temporal anual donde un selector resalta sucesivamente las 3 fases (Floración en amarillo, Llenado en verde, Cosecha en rojo) mientras abajo se sincronizan las curvas de lluvia y vigor satelital.
* **Layout:**
  * **Izquierda (55%):** Calendario fenológico dinámico con gráficos de área de precipitación y EVI acumulado por fase.
  * **Derecha (45%):** Arquitectura del vector de características de fusión: 3 ventanas × 3 sensores = 9 predictores agronómicos de alta densidad explicativa.

---

### Slide 13 — Paradigma 4: Modelos Físicos Globales y Supercómputo
* **Propósito:** Explicar cómo pronostican el clima las superpotencias mundiales (física computacional masiva).
* **Ilación:** Si queremos predecir el clima antes de que impacte los cultivos, ¿de dónde vienen los pronósticos que vemos en el celular?
* **Guion para público profano (Speaker Script):**
  > "¿De dónde sale el pronóstico del tiempo? No sale de una simple regresión. Agencias como la NOAA de Estados Unidos o el ECMWF de Europa operan supercomputadores que dividen la atmósfera del planeta en millones de cubos tridimensionales y resuelven las ecuaciones de la termodinámica y fluidos de Navier-Stokes. El modelo europeo IFS corre a 9 km de resolución con asimilación 4D-Var. Es el pináculo de la física computacional humana."
* **¿Lleva Animación?:** **Sí (Malla Atmosférica 3D del Planeta)**.
  * **Qué cuenta la animación:** Un globo terráqueo estilizado dividido en cuadrículas 3D donde columnas de presión, viento y humedad se calculan capa por capa.
* **Layout:**
  * **Izquierda (50%):** Esquema visual de discretización atmosférica (cubos tridimensionales Navier-Stokes + asimilación de satélites).
  * **Derecha (50%):** Comparativa técnica de las 3 grandes agencias:
    - **NOAA GFS (EE.UU.):** 13 km resolución, libre, optimista en calor continental.
    - **ECMWF IFS (Europa):** 9 km resolución, el estándar de oro de precisión global.
    - **DWD ICON (Alemania):** Malla icosaédrica triangular no-hidrostática.

---

### Slide 14 — Paradigma 4: La Disparidad en Vivo (NOAA vs ECMWF para Iquitos)
* **Propósito:** Mostrar datos reales actuales de Open-Meteo para las coordenadas exactas de Iquitos y demostrar que incluso los mejores supercomputadores del mundo discrepan radicalmente.
* **Ilación:** Si la física es perfecta, ¿por qué discrepan los modelos? Esta es la prueba empírica.
* **Guion para público profano (Speaker Script):**
  > "Miren este gráfico en pantalla. Son los datos descargados en vivo para Iquitos para los próximos 7 días consultando directamente los supercomputadores de NOAA, ECMWF y Alemania. Para el mismo día, NOAA GFS pronostica una ola de calor asfixiante de **36.9 °C**, mientras que el modelo europeo ECMWF proyecta **29.3 °C**. ¡Una diferencia de casi 8 grados Celsius para la misma coordenada geográfica! ¿Quién tiene la razón? Ninguno por sí solo. Por eso el pronóstico moderno no es un número único: es un ensamble probabilístico."
* **¿Lleva Animación?:** **No (Gráfico Interactivo de Alta Fidelidad + Panel Explicativo)**.
* **Layout para eliminar el espacio vacío observado en la captura:**
  * **Panel Superior/Izquierdo (60%):** Gráfico Chart.js interactivo con las 3 curvas (NOAA azul fuerte, ECMWF verde esmeralda, DWD naranja punteado) con tooltips enriquecidos y delta de discrepancia sombreado en gris translúcido.
  * **Panel Lateral/Inferior (40%):**
    - Tarjeta KPI gigante: `Δ 7.6 °C` (Discrepancia máxima entre agencias).
    - Tarjeta de Causa Física: Por qué discrepan (parametrización convectiva en selva tropical húmeda vs nubosidad de dosel amazónico).
    - Conclusión operativa: *"Nunca tomes decisiones de siembra o logística con un solo proveedor climático; usa ensambles multimodelo"*.

---

### Slide 15 — Paradigma 4: La Revolución AI Weather & Zero-Shot
* **Propósito:** Presentar la frontera absoluta de la IA en 2024–2026: GraphCast de DeepMind y Foundation Models (TimesFM, Chronos).
* **Ilación:** ¿Cómo responde la IA moderna a los supercomputadores físicos? Reduciendo semanas de cómputo a segundos.
* **Guion para público profano (Speaker Script):**
  > "En 2023 Google DeepMind publicó **GraphCast** en la revista *Science*. En lugar de resolver ecuaciones diferenciales durante 3 horas en un supercomputador de 10 millones de dólares, entrenaron una Red Neuronal de Grafos sobre 40 años de clima. Resultado: genera un pronóstico global a 10 días en **60 segundos sobre una sola GPU**, batiendo al modelo europeo en el 90% de variables. Y en series temporales puras, Google lanzó **TimesFM** y Amazon **Chronos**: modelos fundacionales zero-shot entrenados con miles de millones de puntos que pronostican cualquier serie desconocida sin necesidad de calibración previa."
* **¿Lleva Animación?:** **Sí (Malla Icosaédrica de GraphCast & Tokenización Zero-Shot)**.
  * **Qué cuenta la animación:** La Tierra cubierta por una malla icosaédrica de múltiples niveles de resolución donde los mensajes de la GNN fluyen por los nodos en un barrido de 60 segundos. Al lado, una serie fragmentándose en parches de tokens numéricos que entran a un Transformer.
* **Layout:**
  * **Izquierda (50%):** Arquitectura GraphCast (GNN icosaédrica + benchmark Science 2023: 90% de variables ganadas a ECMWF en 60s).
  * **Derecha (50%):** Modelos Zero-Shot (TimesFM de Google y Chronos de Amazon): Arquitectura de cuantización, pronóstico en frío (*cold-start*) y cuándo utilizarlos en producción.

---

## Bloque 3: Casos Reales en Perú con Mapas y Demos en Vivo (Slides 16 a 21)

### Slide 16 — Caso A: Ubicación y Microclima (SENAMHI Iquitos)
* **Propósito:** Situar geográficamente el problema del pronóstico amazónico con un mapa satelital de alta resolución.
* **Ilación:** Pasamos de la teoría global a la práctica peruana: nuestra primera estación de prueba.
* **Guion para público profano (Speaker Script):**
  > "Aterricemos en Perú. Nos vamos a Loreto, a la estación Punchana de SENAMHI (código 103015), en plena selva baja a 91 metros sobre el nivel del mar, junto a la confluencia de los ríos Nanay y Amazonas. Aquí el clima es extremo: humedad constante superior al 85%, calor sofocante y tormentas convectivas que se forman en menos de 40 minutos. Descargamos 7 años completos de datos diarios limpios (2019 al 2025, 2,557 días) con la librería Garúa para poner a prueba nuestros algoritmos."
* **¿Lleva Animación?:** **No (Mapa Satelital Leaflet Interactivo a Pantalla Partida)**.
* **Layout:**
  * **Izquierda (55%):** Mapa satelital interactivo Leaflet (Esri World Imagery) con marcador personalizado sobre la estación Punchana y radio de microclima amazónico de 5 km sombreado en cian translúcido.
  * **Derecha (45%):** Ficha técnica de la estación: Coordenadas (-3.6903°, -73.2556°), Período descargado (2,557 días), Variables auditadas (T° máx, T° mín, Precipitación), y porcentaje de huecos curado tras limpieza.

---

### Slide 17 — Caso A: Benchmark Empírico de 7 Años
* **Propósito:** Mostrar la tabla de resultados rigurosa sin trampas (validación temporal estricta de 90 días).
* **Ilación:** ¿Qué modelo ganó la batalla en los datos reales de SENAMHI?
* **Guion para público profano (Speaker Script):**
  > "Evaluamos 5 niveles de modelos compitiendo en igualdad de condiciones sobre un período de prueba ciego de 90 días. El modelo Naive (decir que mañana hará la misma temperatura que hoy) tiene un error de 2.31 °C. ARIMA logró bajar a 2.12 °C. ExtraTrees logró 2.16 °C en 0.2 segundos. Y la red LSTM profunda logró 2.09 °C. ¿Vale la pena una red neuronal compleja para ganar apenas 0.07 °C frente a un árbol que corre en milisegundos? En la mayoría de aplicaciones operativas, la respuesta es NO."
* **¿Lleva Animación?:** **No (Tabla de Rendimiento de Alto Impacto con Barras de Error Horizontales)**.
* **Layout:**
  * **Izquierda (55%):** Tabla de benchmarking completa con semáforo de colores (Modelo, Paradigma, RMSE °C, MAE °C, Tiempo de Entrenamiento, Veredicto).
  * **Derecha (45%):** Gráfico de barras horizontales comparativo de RMSE + 2 tarjetas de análisis: 1) El umbral de costo-beneficio, 2) Por qué ExtraTrees superó a Random Forest (aleatoriedad pura que filtra el ruido amazónico).

---

### Slide 18 — Caso A: DEMO 1 EN VIVO (Pronóstico 7 Días con Incertidumbre)
* **Propósito:** Demostración interactiva en vivo del pronóstico a 7 días con bandas de confianza.
* **Ilación:** Ver los modelos funcionando en vivo sobre los datos reales.
* **Guion para público profano (Speaker Script):**
  > "Aquí tienen la demo en vivo. Pueden prender y apagar cada modelo con los botones superiores. Pero fíjense en la franja sombreada: es nuestra banda de incertidumbre al 90% (±1.645 sigma). Noten cómo a medida que avanzamos del día 1 al día 7, la banda se ensancha: la física nos dice que el error se acumula. Nunca entreguen a un gerente o a un agricultor una sola línea; entreguen el rango de riesgo."
* **¿Lleva Animación?:** **Gráfico Interactivo Chart.js con Selector Dinámico**.
* **Layout:**
  * **Izquierda (65%):** Gráfico Chart.js interactivo leyendo `senamhi_forecast_7d.csv` con cono de incertidumbre sombreado y selector interactivo de modelos (Naive, ARIMA, ExtraTrees, LSTM, Observado).
  * **Derecha (35%):** Panel de control en vivo: Métricas del pronóstico activo, valor esperado a 48h, probabilidad de superar 34 °C y recomendación operativa.

---

### Slide 19 — Caso B: Finca Cafetalera en Jaén & Visor de Heatmaps
* **Propósito:** Mostrar la parcela de café y permitir al usuario alternar entre capas satelitales (RGB, NDVI, EVI, NDRE).
* **Ilación:** Dejamos el clima puro y nos vamos al segundo caso real: café en los Andes del norte de Perú.
* **Guion para público profano (Speaker Script):**
  > "Nos trasladamos a Jaén, Cajamarca, a 1,100 metros sobre el nivel del mar, una de las capitales del café especial de Perú. En pantalla tienen la parcela de 12 hectáreas observada por Sentinel-2. Pero miren los botones de la derecha: podemos cambiar de capa espectral. En RGB vemos la foto satelital convencional. Al pulsar 'Heatmap NDVI', todo se ve verde uniforme saturado. Pero al pulsar 'Heatmap EVI' o 'NDRE', la IA revela las zonas con deficiencia de nitrógeno y pérdida de vigor que el ojo humano y el NDVI no podían ver."
* **¿Lleva Animación?:** **Visor de Capas Leaflet Interactivo (Heatmap Switcher)**.
* **Layout:**
  * **Izquierda (65%):** Mapa satelital interactivo Leaflet centrado en Jaén (-5.6766°, -78.7742°) con polígono de la finca y capas vectoriales/raster intercambiables en tiempo real.
  * **Derecha (35%):** Selector de capas interactivo (RGB Satélite, NDVI Saturado, EVI Biomasa Dinámica, NDRE Clorofila Borde Rojo) + leyenda espectral interpretativa del estado del cafetal.

---

### Slide 20 — Caso B: La Evidencia de Campo (Prueba de las 6 Campañas)
* **Propósito:** Demostrar empíricamente con datos de 6 años por qué el modelo simple de solo NDVI falló y la fusión fenológica acertó.
* **Ilación:** La prueba irrefutable de que la biofísica importa más que la complejidad del algoritmo.
* **Guion para público profano (Speaker Script):**
  > "Analizamos 6 campañas consecutivas de café (2020 a 2025). Miren la campaña 2024: hubo una sequía severa durante la floración seguida de un golpe de calor. El NDVI promedio anual marcó 0.788, exactamente igual que en 2023 (0.789). Si usabas solo NDVI, predecías una cosecha abundante de 24 quintales por hectárea. La cosecha real se desplomó a 18.2 quintales. El modelo simple falló catastróficamente. En cambio, nuestro modelo de Fusión Multimodal, que leyó el estrés hídrico en la ventana de floración y la caída de EVI, predijo 18.46 quintales: un error de solo 0.26 quintales."
* **¿Lleva Animación?:** **No (Tabla Forense de Evidencia de Campañas con Resaltado)**.
* **Layout:**
  * **Izquierda (55%):** Tabla detallada campaña por campaña: Año, Rendimiento Real (qq/ha), NDVI anual (plano), Predicción Solo NDVI (error grave), Predicción Fusión EVI+Clima (acierto milimétrico).
  * **Derecha (45%):** Diagnóstico forense visual de la campaña 2024 con tarjeta de alerta roja ("Por qué falló el NDVI tradicional") y tarjeta verde ("Cómo la fenología salvó el pronóstico").

---

### Slide 21 — Caso B: DEMO 2 EN VIVO (Validación Cruzada LOYO)
* **Propósito:** Gráfico interactivo que demuestra la superioridad del modelo de fusión en validación Leave-One-Year-Out.
* **Ilación:** Validación matemática formal para que no quede duda estadística.
* **Guion para público profano (Speaker Script):**
  > "Para evitar autoengañarnos, usamos validación Leave-One-Year-Out: entrenamos con 5 años y predecimos el año restante, rotando cada campaña. El modelo de Fusión Multimodal logra un MAPE de 4.4% frente al 5.4% del modelo estancado. Pero más allá del número global, miren las barras: en los años de crisis climática, la fusión rastrea la caída con fidelidad, permitiendo a la cooperativa cafetalera comprar seguros agrícolas o negociar contratos a futuro con certidumbre."
* **¿Lleva Animación?:** **Gráfico Interactivo Chart.js con Selector de Series**.
* **Layout:**
  * **Izquierda (65%):** Gráfico interactivo de barras y líneas leyendo `cafe_ndvi_rendimiento.csv`: Cosecha Observada vs Modelo Fusión vs Modelo Solo NDVI.
  * **Derecha (35%):** Métricas de validación: MAPE (4.4% vs 5.4%), $R^2$ ajustado, y tarjeta de impacto financiero: valor del error por contenedor de exportación de café (evitar pérdidas de \$15,000 USD por sobrestimación).

---

## Bloque 4: Síntesis Operativa, Decisiones y Cierre (Slides 22 a 25)

### Slide 22 — 5 Lecciones desde las Trincheras
* **Propósito:** Destilar los 5 aprendizajes más valiosos y no obvios de la práctica real.
* **Ilación:** Resumen ejecutivo de todo lo aprendido en los dos casos peruanos.
* **Guion para público profano (Speaker Script):**
  > "Si mañana tienen que implementar un sistema de pronóstico en su empresa o tesis, llévense estas 5 lecciones grabadas en piedra:
  > 1. **Validación temporal obligatoria**: jamás hagan shuffle en series de tiempo; predecir el pasado con el futuro es autoengaño.
  > 2. **Árboles antes que redes**: arranca siempre con ExtraTrees o LightGBM como baseline sólido.
  > 3. **Asimetría del error**: no cuesta lo mismo que sobre café en el almacén a que te falte para cumplir un contrato internacional.
  > 4. **Respeta la física del sensor**: ningún modelo de Deep Learning arregla un índice que está físicamente saturado.
  > 5. **Interpretabilidad**: un pronóstico que los agrónomos o meteorólogos no entienden jamás será adoptado."
* **¿Lleva Animación?:** **No (Tarjetas de Principios de Alta Legibilidad)**.
* **Layout:**
  * 5 tarjetas horizontales numeradas con íconos, títulos en negrita y resumen de impacto que cubren la pantalla de forma ordenada y balanceada.

---

### Slide 23 — Árbol de Decisión Práctico de Modelado
* **Propósito:** Una guía paso a paso para que cualquier asistente elija el modelo correcto para su problema.
* **Ilación:** La herramienta práctica de referencia para aplicar lo aprendido el lunes por la mañana.
* **Guion para público profano (Speaker Script):**
  > "¿Cómo eligen qué modelo usar? Sigan este flujograma: Si tienen menos de 100 datos: modelos paramétricos o ARIMA. Si tienen entre 100 y 100,000 filas tabulares con estacionalidad: Random Forest o ExtraTrees con lags. Si tienen cientos de miles de series simultáneas de retail: Deep Learning (TFT / DeepAR). Y si no tienen datos históricos y necesitan pronosticar en frío: Foundation Models Zero-Shot como TimesFM o Chronos."
* **¿Lleva Animación?:** **No (Árbol de Decisión Visual / Diagrama de Flujo)**.
* **Layout:**
  * Flujograma SVG nítido con nodos condicionales (Volumen de datos, Frecuencia, Exógenas) que desembocan en cajas de recomendación de modelos.

---

### Slide 24 — Cierre Filosófico: La IA no predice, cuantifica
* **Propósito:** El mensaje final que el público recordará al salir de la sala.
* **Ilación:** El cierre conceptual que da respuesta a la pregunta del título.
* **Guion para público profano (Speaker Script):**
  > "Volvemos a la pregunta inicial: ¿Puede la IA predecir el futuro? La respuesta honesta y científica es: **NO**. El futuro no está escrito en ningún archivo CSV. El clima es caótico y el mercado es voluble. Lo que la IA sí puede hacer —y lo hace mejor que cualquier otra herramienta creada por la humanidad— es **cuantificar la incertidumbre**, desarmar el ruido y mostrarnos el abanico de futuros probables para que tomemos decisiones más inteligentes, justas y resilientes hoy. Muchas gracias."
* **¿Lleva Animación?:** **Sí (Cono de Incertidumbre y Decisión)**.
  * **Qué cuenta la animación:** Un haz de luz que se abre desde el presente hacia múltiples ramas de probabilidades, convergiendo en un nodo verde de "Decisión Informada".
* **Layout:**
  * Frase de cierre monumental tipografiada al centro-izquierda con el cono interactivo a la derecha, enmarcada con elegancia minimalista.

---

### Slide 25 — Referencias, Ecosistema y Código Abierto
* **Propósito:** Brindar acceso a todo el código, datos, papers BibTeX y notebooks reproducibles.
* **Ilación:** Transparencia y reproducibilidad académica e ingenieril total.
* **Guion para público profano (Speaker Script):**
  > "Todo lo que han visto hoy es 100% reproducible. En el repositorio de GitHub encontrarán los notebooks de Python, los datos limpios de SENAMHI, las fórmulas de AgroVisión, los papers citados y el código de esta misma presentación. Escaneen el código QR o descarguen el repositorio para explorar los modelos en su propia máquina."
* **¿Lleva Animación?:** **No (Hub de Recursos y Código QR)**.
* **Layout:**
  * **Izquierda (50%):** Enlaces directos a los notebooks (`01_clima_senamhi.ipynb`, `02_cafe_ndvi.ipynb`), scripts de descarga (`garua`, Open-Meteo) y bibliografía destacada (`refs.bib`: Ramos 2020, Barbosa 2021, Huete 2002, Nie 2023).
  * **Derecha (50%):** Tarjeta con Código QR de acceso al repositorio, comandos de clonación git y créditos de código abierto.

---

## 5. Reglas de Implementación en el Generador (`scripts/build_deck.py`)

Para erradicar definitivamente los problemas de maquetación y espacios vacíos observados en el navegador:
1. **Regla de Ocupación Visual (No Dead Space):** Cada diapositiva de pantalla completa debe usar una estructura simétrica de rejilla: o bien un *split 60/40* o un *grid de cuadrantes* donde el panel complementario contenga tarjetas de contexto, KPIs numéricos destacados o tablas forenses, evitando dejar franjas de más del 20% de vacío.
2. **Corrección de Matemáticas:** Sustituir los strings crudos de LaTeX (`\alpha`, `\beta`, `\Delta`) por entidades tipográficas HTML limpias (`&alpha;`, `&beta;`, `&Delta;`, `x&#772;`, `&sigma;`) o renderizado KaTeX verificado, para que no aparezcan símbolos corruptos `\u0000lpha`.
3. **Escala y Posición de SVGs:** Todos los SVGs animados deben tener `viewBox="0 0 W H"` con `width="100%"` y `preserveAspectRatio="xMidYMid meet"`, con textos y etiquetas ubicados en coordenadas no superpuestas con las curvas.
4. **Enriquecimiento del Slide 14 (Disparidad NOAA vs ECMWF):** El gráfico ocupará el 60% superior/izquierdo y el espacio restante se llenará con un panel analítico que desglosa la discrepancia de 7.6 °C, explicando la diferencia de modelado convectivo tropical de cada agencia y su impacto práctico.
5. **Selector de Capas / Heatmaps en Slide 19 (Jaén):** Conectar los botones del visor satelital con capas Leaflet reales (capa de polígono y capas ráster simuladas por gradiente de color para NDVI, EVI y NDRE) para que la interacción sea inmediata y pedagógica.
