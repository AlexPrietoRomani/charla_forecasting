### Informe Técnico y Narrativo: Anatomía, Evolución y Fronteras del Forecasting en el Mundo Real

##### 1\. LA ANATOMÍA FUNDAMENTAL: ¿QUÉ ES UNA SERIE TEMPORAL Y POR QUÉ ES TAN DIFÍCIL?

###### *1.1. Descomposición Ontológica y la Metáfora Físico-Biológica*

Comprender la estructura interna subyacente de una serie temporal antes de seleccionar o entrenar cualquier algoritmo constituye un imperativo estratégico irrenunciable. En entornos de producción industrial, energética y financiera, precipitarse a aplicar modelos de alta complejidad sin descomponer previamente la señal conduce de manera inevitable a errores conceptuales severos, falsos diagnósticos de rendimiento y fallas catastróficas en la toma de decisiones. La descomposición matemática actúa como la herramienta ontológica fundamental para aislar las fuerzas deterministas de la fluctuación estocástica, previniendo que la arquitectura intente aprender variaciones aleatorias como si fuesen leyes causales.Desde el punto de vista analítico, una serie temporal observable en tiempo continuo  \$Y(t)\$  se desglosa ontológicamente mediante la ecuación de componentes:\$\$Y(t) \= T(t) \+ S(t) \+ C(t) \+ \\varepsilon(t)\$\$En formulaciones aditivas discretas como el algoritmo  **STL**  ( *Seasonal-Trend Decomposition based on Loess* ), la notación se expresa convencionalmente como:\$\$Y\_t \= T\_t \+ S\_t \+ R\_t\$\$Donde cada componente representa una dimensión física o estructural del sistema:

* **Tendencia**  **\$T(t)**\$  **(**  **\$T\_t**\$  **):**  Refleja la inercia estructural de bajo comportamiento y largo plazo del sistema. Representa la dirección subyacente sobre la cual se desplaza la serie, desprovista de variaciones estacionales o de alta frecuencia.  
* **Estacionalidad**  **\$S(t)**\$  **(**  **\$S\_t**\$  **):**  Captura las oscilaciones periódicas y armónicas que se repiten a intervalos fijos debido a ciclos astronómicos, calendáricos o de actividad humana (como patrones de 24 horas, 7 días o 12 meses).  
* **Ciclo**  **\$C(t)**\$  **:**  Modula expansiones y contracciones no periódicas de mediano a largo plazo, a menudo vinculadas a dinámicas macroeconómicas o cambios de régimen del entorno.  
* **Residuo o Componente Remanente**  **\$\\varepsilon(t)**\$  **(**  **\$R\_t**\$  **):**  Representa el componente estocástico no explicado por las dinámicas estructurales; es la perturbación aleatoria pura del sistema.Para interiorizar esta relación, considere la  **metáfora físico-biológica del cauce y flujo de un río**  o el desarrollo de un cultivo agrícola. El cauce geomorfológico del río y su cuenca representan la  *tendencia*   \$T(t)\$  a largo plazo (la inercia física que define la capacidad y dirección general); el ciclo de las mareas y el régimen de derretimiento primaveral de nieves representan la  *estacionalidad periódica*   \$S(t)\$  astronómica; las variaciones de sequías e inundaciones interanuales constituyen la  *dinámica cíclica*   \$C(t)\$ ; mientras que las turbulencias locales, ráfagas de viento puntuales y desprendimientos imprevistos representan el  *ruido estocástico*   \$\\varepsilon(t)\$ .

###### *El Método STL y la Sincronización Subgráfica*

El método STL (Cleveland, Cleveland, McRae & Terpenning, 1990\) institucionalizó la separación rígida pero flexible de estos componentes utilizando suavizado local regresivo ( *Loess* ). STL opera mediante subgráficos sincronizados horizontalmente que permiten descomponer la serie original ruidosa ( \$Y\_t\$ ) en una tendencia Loess suavizada ( \$T\_t\$ ), una estacionalidad armónica oscilante ( \$S\_t\$ ) y un residuo estocástico ( \$R\_t\$ ) que enciende alertas analíticas cuando sus valores superan umbrales anómalos (por ejemplo,  \$\\pm 2.5\\sigma\$ ). Esta descomposición en tiempo real permite a operadores del sistema eléctrico de potencia como el  **COES**  en el Perú y  **RTE**  en Francia desglosar la demanda horaria de megavatios para programar el despacho óptimo de centrales hidroeléctricas y de ciclo combinado, aislando el choque estacional diario del incremento estructural del consumo.Esta descomposición estructural pone de manifiesto que el comportamiento de cualquier serie temporal se debate continuamente entre el determinismo físico del sistema y la aleatoriedad estocástica irreducible.

###### *1.2. Física y Causalidad Subyacente vs. Ruido Estocástico: La Trampa del Mapeo en Producción*

Confundir la señal causal subyacente con el ruido blanco representa uno de los mayores riesgos financieros y operacionales en sistemas industriales de misión crítica. En la práctica, los datos históricos observados son simplemente una realización discreta de un proceso estocástico subyacente, donde las variaciones de alta frecuencia suelen ser el producto de micro-interacciones impredecibles que no se repetirán en el futuro.La distinción operativa se fundamenta en la naturaleza del proceso:

* **Física / Causalidad Subyacente:**  Representa la dinámica estructural del sistema (mecanismos termodinámicos, restricciones físicas de la red, comportamiento del consumidor impulsado por factores socioeconómicos).  
* **Ruido Estocástico**  **\$\\varepsilon(t)**\$  **:**  Representa la variación aleatoria indecodificable que no contiene información predictiva útil sobre el futuro.Al entrenar arquitecturas de alta capacidad descriptiva (como redes profundas o árboles de decisión no podados), existe un riesgo inminente denominado la  **"Trampa de la Memorización"**  ( *Overfitting* ). Si se fuerza a un modelo complejo a minimizar el error de entrenamiento forzando al regresor  \$\\hat{f}\$  a aprender y reconstruir las fluctuaciones exactas de  \$\\varepsilon(t)\$ , el modelo no está aprendiendo la ley física subyacente, sino memorizando el ruido histórico.Al desplegar este modelo memorizador en un entorno de producción real, el término de error impredecible adopta nuevos valores no vistos, lo que resulta en fallas catastróficas de pronóstico, pérdida de estabilidad en los sistemas de control y decisiones de inversión erróneas.Los pilares clave que explican este colapso operacional en producción son:  
* **Degradación del Error In-Sample vs. Out-of-Sample:**  La optimización matemática agresiva sobre los residuos de entrenamiento incrementa drásticamente la varianza del modelo en datos no observados, destruyendo la capacidad de generalización.  
* **Violación de la Estabilidad Causal:**  Las correlaciones espurias aprendidas a partir del ruido estocástico cambian de fase o desaparecen por completo fuera del conjunto de entrenamiento.  
* **Incapacidad de Reacción ante Variaciones de Régimen:**  Un modelo que memorizó el residuo carece de la flexibilidad estructural requerida para adaptarse cuando la verdadera tendencia o estacionalidad experimenta un cambio estructural.La necesidad imperiosa de modelar la señal causal pura aislando la perturbación estocástica fue, precisamente, el motor matemático que impulsó la creación de las primeras herramientas analíticas clásicas.

##### 2\. LA GRAN SAGA EVOLUTIVA DEL FORECASTING (ERAS, FORTALEZAS Y QUIEBRES)

\====================================================================================================  
                        LA SAGA EVOLUTIVA DEL FORECASTING INDUSTRIAL  
\====================================================================================================

 ERA 1: CLÁSICOS ANALÍTICOS            ERA 2: PUENTE TABULAR                 ERA 3: DEEP LEARNING  
 (Verhulst, Holt-Winters, ARIMA)       (Lags \+ GBDT: LightGBM)               (RNN, LSTM, PatchTST)  
  ┌───────────────────────────┐         ┌───────────────────────────┐         ┌───────────────────────────┐  
  │ • Parsimonia matemática.  │         │ • Matrices supervisadas.  │         │ • Representaciones auto.  │  
  │ • Inferencia CPU (µs).    │ ──────\> │ • Domina M5 Competition.  │ ──────\> │ • Parches temporales.     │  
  │ • Fallo: No-linealidad.   │         │ • Fallo: Extrapolación    │         │ • Fallo: Costo cuadrático │  
  └───────────────────────────┘         │   (Mesetas estáticas).    │         │   en Transformers.    │  
                                        └───────────────────────────┘         └───────────────────────────┘  
                                                                                            │  
                                                                                            ▼  
                                                                             ERA 4: FOUNDATION MODELS  
                                                                             (TimesFM, Chronos, Moirai)  
                                                                              ┌───────────────────────────┐  
                                                                              │ • Inferencia Zero-Shot.   │  
                                                                              │ • Billones de datos.      │  
                                                                              │ • Ventana Contexto/Cal.   │  
                                                                              └───────────────────────────┘  
\====================================================================================================

###### *2.1. Era 1: Los Clásicos Analíticos (Verhulst, Holt-Winters, ARIMA / SARIMA)*

La era analítica sentó las bases del pronóstico cuantitativo moderno apoyándose en la parsimonia matemática, la elegancia de las soluciones en forma cerrada y la sólida teoría de los procesos estocásticos estacionarios.**Contexto y analogía intuitiva:**  Esta era concibe a las series temporales mediante analogías con la física de resortes y la dinámica biológica de crecimiento acotado. Un ejemplo representativo es la curva logística de Verhulst (1838), diseñada para modelar el crecimiento de poblaciones sujetas a la resistencia del medio ambiente mediante una ecuación sigmoidea en tiempo discreto o continuo:\$\$y\_t \= \\frac{L}{1 \+ e^{-k(t-t\_0)}}\$\$Donde  \$L\$  representa la capacidad de carga máxima del entorno,  \$k\$  la tasa de crecimiento intrínseco y  \$t\_0\$  el punto de inflexión temporal donde la velocidad de crecimiento  \$\\left.\\frac{dy}{dt}\\right|\_{t\_0} \= \\frac{kL}{4}\$  alcanza su pico absoluto antes de desacelerarse por la saturación del medio.**Fortalezas y superpoderes:**  Los modelos analíticos destacan por su extrema parsimonia matemática, requiriendo una cantidad mínima de parámetros para ser ajustados. Esto permite ejecutar inferencias en microsegundos sobre hardware CPU modesto y garantiza una interpretabilidad matemática absoluta, donde cada parámetro posee un significado analítico o físico directo (por ejemplo, los coeficientes de suavizado  \$\\alpha, \\beta, \\gamma\$  en Holt-Winters controlan explícitamente la tasa de actualización del nivel, la tendencia y la estacionalidad).**Momento de quiebre en producción:**  Estos modelos colapsan cuando se enfrentan a relaciones no lineales altamente complejas o cuando se intenta escalar la solución a miles de series interconectadas con covariables cruzadas. Un caso histórico documentado por el Instituto Nacional de Salud ( **INS/MINSA** ) del Perú durante el brote de Dengue en la región de Loreto evidencia esta limitación: mientras que los modelos polinomiales no acotados predecían teóricamente una cantidad infinita e incontrolable de infectados conforme avanzaban las semanas, el modelo logístico acotado de Verhulst proyectó con precisión el límite biológico del pico de capacidad hospitalaria ( \$L\$ ), previniendo una sobreasignación errónea de recursos. Sin embargo, ante variaciones climáticas multivariadas impredecibles, estos modelos lineales rígidos se mostraron incapaces de reajustar sus supuestos.**El salto necesario:**  La incapacidad de los marcos analíticos para incorporar características transversales masivas e interacciones no lineales sin asunciones previas motivó la transición hacia el aprendizaje automático tabular.

###### *2.2. Era 2: El Puente Tabular (El Truco de los Lags: Random Forest, LightGBM, XGBoost)*

El surgimiento del aprendizaje automático tabular transformó radicalmente la industria del  *retail*  y la gestión de cadenas de suministro al estructurar el tiempo no como una secuencia continua, sino como una matriz de datos supervisada.**Contexto y analogía intuitiva:**  El núcleo de este enfoque reside en el  **"truco de los lags"** : la reestructuración de la serie temporal mediante ventanas deslizantes. Una secuencia unidimensional  \$y\_1, y\_2, \\dots, y\_t\$  se convierte en una tabla de entrenamiento supervisado donde los regresores son valores pasados ( \$y\_{t-1}, y\_{t-2}, \\dots, y\_{t-n}\$ ) junto con estadísticas móviles ( *rolling mean* ,  *rolling std* ) y variables calendáricas, proyectando un objetivo futuro  \$y\_{t+h}\$ . El algoritmo ignora la naturaleza secuencial del tiempo; simplemente mapea un vector de características estático a una variable escalar.**Fortalezas y superpoderes:**  Los modelos basados en  *Gradient Boosted Decision Trees*  (GBDT), como  **LightGBM** ,  **XGBoost**  y  **CatBoost** , dominaron de forma contundente la célebre competencia  **Walmart M5 Forecasting Competition**  (Makridakis et al., 2022), la cual abarcó 30,490 SKUs. Su poder radicaba en la capacidad masiva de ingerir miles de covariables exógenas (precios, promociones, categorías) y capturar interacciones complejas no lineales sin requerir la infraestructura computacional pesada de las GPUs.**Quiebre ("La trampa de los árboles"):**  A pesar de su éxito, los modelos basados en árboles de decisión poseen una limitación matemática insuperable: dividen el espacio de características mediante particiones hiperrectangulares ortogonales ( \$X\_{\\min}, X\_{\\max}\$ ). Como resultado,  **los modelos GBDT son matemáticamente incapaces de extrapolar valores fuera del rango histórico de entrenamiento** . Al enfrentar un valor de entrada superior al máximo observado en la fase de ajuste, el árbol asigna el dato a su hoja extrema, generando una  **meseta plana estática**  ( \$y \= \\text{constante}\$ ).  
  VALOR OBSERVADO  
        ▲  
        │                                  ┌───────────────────────── (Demanda Real: \+20 GW)  
        │                                 ╱  
        │                             ╱  
        │  DATOS HISTÓRICOS       ╱  
        │   (Entrenamiento)   ╱  
        │  ┌───────────────┐  ╱  
        │  │               │ ╱  
        │  │               │╱  
        │  └───────────────┴─────────────────────────────────────── (Predicción GBDT: Meseta Plana)  
        └─────────────────────────────────────────────────────────► TIEMPO  
                                     ↑ Evento Récord  
                                  (Tormenta Uri: \-18 °C)

El impacto operacional devastador de esta falencia se evidenció durante el  **colapso del sistema eléctrico de ERCOT en Texas (febrero de 2021\)** . La tormenta invernal Uri llevó la temperatura ambiente a \-18 °C, un evento sin precedentes en 50 años. Los modelos tabulares operacionales, entrenados con datos históricos donde tales temperaturas no existían, proyectaron un techo plano estático en la demanda de energía. La demanda real superó en  **20 GW**  las previsiones de las mesetas tabulares, provocando un apagón masivo de 4 días que afectó a millones de personas y causó pérdidas económicas estimadas en \$195 mil millones de dólares.**El salto necesario:**  La inflexibilidad de los árboles ante valores extremos y eventos récord abrió la puerta al desarrollo del aprendizaje profundo secuencial.

###### *2.3. Era 3: El Deep Learning Secuencial y de Parches (RNN, LSTM, N-BEATS, TFT y PatchTST)*

La necesidad de modelar representaciones temporales jerárquicas sin ingeniería manual de variables impulsó el desarrollo de redes neuronales profundas diseñadas específicamente para extraer dinámicas secuenciales continuas.**Contexto y analogía intuitiva:**  Esta era interpreta la serie de tiempo como un flujo continuo de información donde la memoria interna del sistema evoluciona mediante vectores latentes, capturando patrones dinámicos tanto a corto como a largo plazo.**Fortalezas y superpoderes:**  Arquitecturas como las  **LSTM**  ( *Long Short-Term Memory* ),  **N-BEATS**  y el  **Temporal Fusion Transformer (TFT)**  (Lim et al., 2021\) demostraron un rendimiento notable al integrar covariables estáticas y dinámicas, aislando patrones espaciotemporales sin necesidad de crear variables de  *lag*  a mano.**Quiebre:**  Las redes recurrentes exhiben cuellos de botella severos: sus compuertas de olvido ( \$f\_t\$ ), entrada ( \$i\_t\$ ) y salida ( \$o\_t\$ ) sufren de desvanecimiento de gradiente en secuencias largas y son intrínsecamente secuenciales, lo que impide su paralelización masiva en GPUs. Por otro lado, la aplicación directa de  *Transformers*  punto a punto presenta una complejidad computacional cuadrática  \$\\mathcal{O}(L^2)\$  respecto a la longitud de la secuencia  \$L\$ , volviendo prohibitivo el procesamiento de horizontes extensos.**El salto necesario:**  La arquitectura  **PatchTST**  (Nie et al., ICLR 2023\) resolvió este costo cuadrático replanteando el problema desde la teoría del procesamiento de señales. A diferencia del lenguaje natural (NLP), donde las palabras individuales poseen significado semántico aislado, un punto numérico único en una serie temporal carece de semántica. PatchTST divide la serie continua en bloques o "parches" de pasos temporales (por ejemplo, de 16 o 64 pasos) que capturan la forma local de la señal (tendencia local y micro-estacionalidad). Al agrupar  \$P\$  pasos en un solo parche, la longitud de la secuencia se reduce a  \$L/P\$ , transformando la complejidad cuadrática  \$\\mathcal{O}(L^2)\$  en  \$\\mathcal{O}((L/P)^2)\$ . Aplicando autoatención ( *Self-Attention* ) multi-cabeza sobre estos parches, se extraen dependencias complejas a largo plazo. Empresas de energía renovable como  **CAISO**  en California y  **Enel Green Power**  adoptaron este enfoque para pronosticar la generación de cientos de parques eólicos y solares sin acumular error recursivo.La capacidad de procesar parches temporales con Transformers preparó el terreno para la llegada de los modelos preentrenados a gran escala.

###### *2.4. Era 4: La Revolución Zero-Shot y Modelos Fundacionales (TimesFM, Chronos, Lag-Llama, Moirai, TimeGPT)*

Los modelos fundacionales de series temporales ( **TSFMs** , por sus siglas en inglés) representan un cambio de paradigma: pasar del diseño de modelos específicos entrenados localmente hacia el aprendizaje de representaciones universales preentrenadas sobre billones de puntos de datos (como el conjunto  **LOTSA** , que cuenta con 27 mil millones de observaciones).**Contexto y analogía intuitiva:**  Estos modelos tratan las series temporales de forma análoga a como los Grandes Modelos de Lenguaje (LLMs) procesan el texto. Cuantizan los valores numéricos en  *tokens*  discretos o proyectan parches numéricos en espacios latentes profundos, lo que les permite realizar inferencias en modo  **Zero-Shot**  (predecir series jamás vistas durante el entrenamiento sin ajustar un solo parámetro local).**Fortalezas y superpoderes:**  Proporcionan capacidades predictivas inmediatas  *out-of-the-box* , reduciendo drásticamente los costos de infraestructura al eliminar la necesidad de ciclos continuos de reentrenamiento local. Las arquitecturas más destacadas de esta era se desglosan a continuación:| Modelo | Parámetros | Arquitectura Base | Objetivo de Pérdida | Mecanismo de Salida || \------ | \------ | \------ | \------ | \------ || **TimesFM** | 200M / 500M | Decoder-Only (Google) | MSE por bloques de parches | Mapeo puntual directo || **Chronos** | 46M / 48M | T5 Encoder-Decoder (Amazon) | Cross-Entropy sobre 4096 tokens | Muestreo probabilístico de tokens || **Lag-Llama** | 2.5M | LLaMA Backbone | Neg Log-Likelihood | Distribución Student-t || **Moirai** | Variado (Small/Base/Large) | Encoder-Only (Salesforce) | Mixture Log-Likelihood (4 distribuciones) | Intervalos/Parámetros de distribución || **TimeGPT-1** | Propietario | Transformer (Nixtla) | Optimizado vía API | Punto / Intervalos nativos |

* **TimesFM**  (Google Research, Das et al., 2024): Modelo  *decoder-only*  de 200M y 500M de parámetros que optimiza la pérdida MSE directamente sobre bloques de parches futuros en una sola pasada forward.  
* **Chronos**  (Amazon, Ansari et al., 2024): Cuantiza series temporales mediante escalado y discretización a un vocabulario de 4,096  *tokens* , reutilizando arquitecturas T5 (versiones como Chronos-t5-small de 46M y Chronos-Bolt de 48M) y entrenando con entropía cruzada.  
* **Lag-Llama**  (Rasul et al., 2024): Modelo compacto de 2.5M de parámetros basado en la arquitectura LLaMA que construye  *lags*  explícitos y variables calendáricas, emitiendo una distribución probabilística Student-t.  
* **Moirai**  (Salesforce, Woo et al., 2024): Arquitectura  *encoder-only*  preentrenada sobre el dataset  **LOTSA (27 mil millones de puntos)**  que optimiza una pérdida de verosimilitud sobre una mezcla de 4 distribuciones (Student-t, Normal, Binomial Negativa y Log-Normal).  
* **TimeGPT-1**  (Nixtla, Garza et al., 2024): Ofrece una infraestructura basada en API optimizada para inferencia distribuida.*Incertidumbre Nativa vs. Garantías Conformes:*  Es crucial precisar que aunque modelos como Chronos (vía muestreo de tokens) o Lag-Llama (vía parámetros Student-t) generan salidas probabilísticas nativas,  **sus intervalos intrínsecos carecen de garantías matemáticas de cobertura en muestras finitas**  cuando los datos sufren cambios de distribución o violan la supuesta familia paramétrica. Por ello, la aplicación de Predicción Conforme sobre sus predicciones (o medianas) es lo que otorga garantías rigurosas de cobertura ( \$MCR \\ge 1-\\alpha\$ ).**Momento de quiebre / Limitaciones:**  A pesar de su potencia, los TSFMs presentan restricciones operacionales severas:  
1. *Alta latencia y costo computacional:*  Desplegar modelos de 500M de parámetros en entornos de inferencia estricta o dispositivos  *edge*  resulta costoso e inviable.  
2. *Opacidad de negocio ("Black Box"):*  Dificultad para auditar y justificar pronósticos ante organismos reguladores.  
3. *Gestión de Covariables Exógenas Futuras:*  Existe una disparidad operativa crítica en la industria (OTexts Ch. 15.4). Mientras arquitecturas como  **Moirai**  (vía su diseño  *encoder-only* ) y  **TimeGPT**  (vía una matriz explícita X\_df) pueden ingerir covariables exógenas dinámicas futuras (como pronósticos de temperatura o viento), los modelos univariados puros como el  **Chronos**  base o  **Lag-Llama**  son incapaces de incorporar impulsores exógenos futuros directamente sin modificaciones profundas.**El salto necesario:**  Para transformar estas predicciones puntuales o intervalos no calibrados en herramientas de ingeniería confiables, se requiere cuantificar la incertidumbre operacional mediante Predicción Conforme.

##### 3\. LA ILUSIÓN DE LA CERTEZA Y EL CONO DE INCERTIDUMBRE (CONFORMAL PREDICTION)

###### *3.1. Horizonte de Predictibilidad y Límite de Lyapunov*

La búsqueda de una predicción puntual única y perfecta ( \$\\hat{y}\_t\$ ) para horizontes lejanos es una trampa metodológica. En sistemas dinámicos complejos y no lineales (desde la demanda de la red eléctrica hasta la logística transoceánica), los pequeños errores en las condiciones iniciales se amplifican de forma exponencial a lo largo del tiempo.Este fenómeno se rige por el  **Límite de Lyapunov** , el cual define el horizonte temporal máximo más allá del cual el sistema pierde su correlación con el estado inicial y se vuelve inherentemente impredecible en términos puntuales.  
                                  EL CONO DE INCERTIDUMBRE  
                                    
    Valor Real (y)  
          ▲                                             Bandas Empíricas (P90)  
          │                                          ┌───────────────────────  
          │                                   ┌──────┘  
          │                            ┌──────┘  \\  Error (\$\\varepsilon\$)  
          │     Punto Fijo     ┌┘                  \\  Exponencial  
          ├────────────────────┼────────────────────X──────────────────►  
          │                    └┐                  /  Límite de  
          │                     └──────┐          /   Lyapunov  
          │                            └──────┐  /  
          │                                   └──────┐  
          │                                          └───────────────────────  
          └───────────────────────────────────────────────────────────► Horizontes (h)

Exigir un punto fijo para planificar decisiones operativas críticas presenta tres fallas estructurales:

1. **Omisión de la Asimetría del Riesgo:**  En la operación de redes eléctricas o el reabastecimiento de inventario en  *retail* , el costo de subestimar la demanda (apagones sistémicos, penalizaciones regulatorias, ventas perdidas) es inmensamente superior al costo de sobreestimarla (costo de reserva giratoria, almacenamiento excesivo). Un punto fijo ignora este desequilibrio, haciendo imprescindible el uso de intervalos conformes ajustados por cuantiles asimétricos o funciones de pérdida  *pinball* .  
2. **Falsa Sensación de Control:**  Un pronóstico puntual enmascara la varianza inherente del proceso estocástico, induciendo a los comités ejecutivos a asumir niveles de exposición al riesgo inaceptables.  
3. **Deterioro Exponencial del Horizonte:**  La precisión puntual se degrada a un ritmo exponencial a medida que el horizonte  \$h\$  se desplaza más allá del límite de estabilidad del sistema.La crítica al punto fijo conduce de manera natural hacia la solución matemática de cuantificación de incertidumbre no paramétrica.

###### *3.2. Del Punto Fijo ( \$\\hat{y}\_t\$ ) a las Bandas Empíricas P10–P90 y Predicción Conforme (SCP)*

Para superar la ilusión de la certeza, la ciencia de datos moderna migra desde la estimación puntual hacia la cuantificación no paramétrica de incertidumbre mediante  **Predicción Conforme**  ( *Split Conformal Prediction*  \- SCP, Lei et al., 2017). A diferencia de los métodos bayesianos o de las asunciones gaussianas tradicionales, SCP proporciona  **garantías matemáticas de cobertura empírica válidas en muestras finitas** , sin asumir distribuciones predefinidas.

###### *Algoritmo Matemático de Split Conformal Prediction (SCP)*

Dado un nivel de error tolerado  \$\\alpha \\in 0, 1\$  (por ejemplo,  \$\\alpha \= 0.10\$  para una cobertura del 90%) y un conjunto de  \$N\$  observaciones  \$(x\_i, y\_i)\$ , SCP sigue 5 pasos rigurosos:

1. **División (**  ***Splitting***  **):**  Se separa el historial disponible en dos conjuntos disjuntos: entrenamiento  \$Tr \= \\{(x\_i, y\_i) \\mid i \= 1, \\dots, N\_s\\}\$  y calibración  \$Cal \= \\{(x\_i, y\_i) \\mid i \= N\_s \+ 1, \\dots, N\\}\$ .  
2. **Entrenamiento (**  ***Training***  **):**  Se entrena un modelo regresor  \$\\hat{f}\$  exclusivamente sobre el conjunto de entrenamiento  \$Tr\$ .  
3. **Puntaje de Conformidad (**  ***Conformity Score***  **):**  Se evalúa  \$\\hat{f}\$  sobre el conjunto  \$Cal\$  y se calcula el residuo absoluto para cada punto:  \$\$S\_i \= |\\hat{f}(x\_i) \- y\_i|, \\quad \\forall i \\in Cal\$\$  
4. **Umbral de Incertidumbre (**  **\$\\hat{q}**\$  **):**  Se calcula el umbral  \$\\hat{q}\$  como el cuantil  \$1-\\hat{\\alpha}\$  de la distribución empírica de los puntajes  \$S\_{Cal}\$ :  \$\$\\hat{q} \= q\_{1-\\hat{\\alpha}}(S\_{Cal}) \\quad \\text{con} \\quad 1-\\hat{\\alpha} \= \\frac{\\lceil(|Cal|+1)(1-\\alpha)\\rceil}{|Cal|}\$\$  
5. **Intervalo de Predicción (**  ***Prediction Interval***  **):**  Para una nueva observación  \$x\_{N+k}\$ , el intervalo conforme garantizado al  \$(1-\\alpha)\\%\$  es:  \$\$I(x\_{N+k}) \= \\left\\hat{f}(x\_{N+k}) \- \\hat{q}, \\;\\; \\hat{f}(x\_{N+k}) \+ \\hat{q}\\right\$\$

###### *Cuantiles Globales vs. Cuantiles Locales en Series Multivariadas*

En conjuntos con  \$M\$  series temporales (como NN5 o M3), existen dos formulaciones matemáticas para calcular el umbral conforme (Achour et al., 2025):

* **Cuantil Global (**  ***Global Quantile***  **):**  Unifica los puntajes de conformidad de las  \$M\$  series en un único conjunto agrupado:  \$\$\\hat{q}*{\\text{global}} \= q*{1-\\hat{\\alpha}}\\left( \\bigcup\_{j=1}^M S\_{Cal, j} \\right)\$\$  
* **Cuantil Local (**  ***Local Quantile***  **):**  Calcula un umbral independiente para cada serie  \$j \\in \\{1, \\dots, M\\}\$ :  \$\$\\hat{q}*j \= q*{1-\\hat{\\alpha}}\\left( S\_{Cal, j} \\right) \\quad \\forall j \\in \\{1, \\dots, M\\}\$\$*Criterio de Selección:*  El  **Cuantil Local**  es técnicamente superior cuando las series individuales poseen escalas o varianzas drásticamente heterogéneas, evitando que las series de alta volatilidad ensanchen artificialmente las bandas de las series estables. Por el contrario, el  **Cuantil Global**  se utiliza cuando la longitud de calibración por serie  \$|Cal\_j|\$  es extremadamente corta, permitiendo agrupar datos entre series para estabilizar el cálculo del cuantil.

###### *Hallazgos Empíricos Clave (Estudio Achour et al., 2025\)*

El análisis empírico de Achour et al. (2025) sobre conjuntos de datos reales (ERCOT, NN5, M3) demuestra la superioridad operacional de los TSFMs combinados con SCP en escenarios de escasez de datos:  
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐  
│              DESEMPEÑO DE MODELOS BAJO ESCASEZ DE DATOS Y CONFORMAL PREDICTION                   │  
├──────────────────────┬────────────────────────┬─────────────────────────┬────────────────────────┤  
│ Modelo               │ Asignación de Datos    │ Ancho Intervalo (MSIW)  │ Precisión (MASE)       │  
├──────────────────────┼────────────────────────┼─────────────────────────┼────────────────────────┤  
│ GBDT (LightGBM)      │ Req. 80% Entrenam.     │ Ancho / Inestable       │ Severamente Degradado  │  
│                      │ Queda \<20% Calibración │                         │ por destrucción Lags   │  
├──────────────────────┼────────────────────────┼─────────────────────────┼────────────────────────┤  
│ TSFM Zero-Shot       │ 0% Entrenamiento Local │ Estrecho / Calibrado    │ Altamente Preciso      │  
│ (ChronosBolt/TimesFM)│ 80%-90% Calibración    │ (MSIW reducido)         │ (MASE superior)        │  
└──────────────────────┴────────────────────────┴─────────────────────────┴────────────────────────┤

* **Sinergia entre Zero-Shot y Calibración:**  Dado que los TSFMs no requieren entrenamiento local (solo una ventana corta de contexto  \$C\$ ), en muestras pequeñas (como ERCOT 2232 puntos o series semanales/mensuales de NN5 y M3),  **es posible destinar entre el 80% y el 90% de los datos históricos exclusivamente al conjunto de calibración (**  **\$Cal**\$  **)** . Esto maximiza la cardinalidad  \$|Cal|\$ , estabilizando  \$\\hat{q}\$  y produciendo intervalos significativamente más estrechos ( **MSIW** ) sin perder cobertura ( **MCR**   \$\\ge 90\\%\$ ).  
* **Evidencia Numérica en ERCOT 2232 (Horizonte Corto S):**  
* **ChronosBolt:**  Logró un  **MASE de 0.362** , un  **MSIW de 0.312**  y una tasa de cobertura  **MCR del 91.3%** .  
* **LightGBM (80% Train / 20% Cal):**  Alcanzó un  **MASE de 0.659**  y un  **MSIW de 0.428**  con  **MCR del 89.0%** .  
* **LightGBM (20% Train / 80% Cal):**  Se colapsó por completo, registrando un  **MASE de 1.195**  y  **MSIW de 0.724** .  
* **La Razón Matemática del Colapso de LightGBM:**  Al reducir el entrenamiento de LightGBM al 20% en series cortas, la creación de variables de  *lag*  (necesarias para construir la matriz supervisada) genera valores nulos ( *NaNs* ) que deben ser eliminados. Esto destruye las primeras filas de datos, dejando una muestra de entrenamiento insuficiente para aprender los patrones estacionales, degradando masivamente tanto el pronóstico puntual como la calibración posterior.La combinación de precisión puntual e incertidumbre conforme permite construir una matriz de evaluación objetiva para la toma de decisiones directivas.

##### 4\. MATRIZ COMPARATIVA EJECUTIVA

###### *4.1. Evaluación Multidimensional de Familias de Modelos*

Un marco de evaluación holístico para la toma de decisiones ejecutivas no debe limitar su análisis al error absoluto de validación; debe ponderar de manera integral los requisitos de datos, la factibilidad computacional, el riesgo de colapso en producción y la aptitud del modelo según la naturaleza del negocio.| Familia de Modelo | Requisito de Datos | Costo de Cómputo (CPU vs GPU) | Capacidad de Extrapolación | Riesgo Típico en Producción | Caso de Uso Ideal || \------ | \------ | \------ | \------ | \------ | \------ || **Clásicos Analíticos**  (ARIMA, Holt-Winters, Verhulst) | Mínimo ( \$N \< 500\$  puntos). Exige estacionalidad clara y serie continua. | Insignificante (CPU en microsegundos). | Nula fuera de curvas paramétricas o tendencias lineales estricta. | Subajuste ( *underfitting* ) severo ante no-linealidades complejas o covariables cruzadas. | Dispositivos edge, micro-retail, epidemiología de brotes acotados (INS/MINSA). || **Puente Tabular**  (LightGBM, XGBoost, CatBoost) | Medio ( \$10^3 \- 10^5\$  puntos). Exige construcción manual de lags y rolling stats. | Bajo y eficiente (CPU multihilo en milisegundos). | Nula matemáticamente (partición hiperrectangular genera mesetas planas). | Fallo catastrófico en eventos récord fuera de rango histórico (ej. crisis ERCOT 2021). | Retail masivo con covariables estables y miles de SKUs interconectados (Walmart M5). || **Deep Learning Secuencial / Parches**  (PatchTST, TFT, LSTM) | Alto ( \$\> 10^5\$  puntos) para evitar sobreajuste y memorización. | Alto (GPU intensiva en entrenamiento; inferencia moderada). | Moderada a alta mediante representaciones latentes profundas continuas. | Costos desbordados de infraestructura y degradación por desvanecimiento de gradiente. | Pronóstico eólico y solar multivariable a escala de red eléctrica (CAISO, COES, Enel). || **Foundation Models Zero-Shot**  (TimesFM 2.0, Chronos-Bolt, Lag-Llama, Moirai) | Cero datos de entrenamiento local (solo ventana de contexto  \$C\$  de 32 a 512 puntos). | Inferencia optimizada en GPU/TPU (muy rápida en variantes como Chronos-Bolt). | Alta (preentrenamiento sobre billones de puntos en diversos dominios). | Opacidad de caja negra, alto consumo de memoria y falta de soporte exógeno en variantes univariadas. | Catálogos fríos ( *cold-start* ), e-commerce de alta rotación y calibración conforme bajo escasez de datos. |

###### *4.2. Trade-offs Operacionales: Latencia, Cómputo y Restricciones de Datos*

La selección de la arquitectura idónea exige equilibrar el triángulo de compromiso entre la granularidad de los datos, la latencia exigida y la capacidad de procesar covariables.

###### *Granularidad Temporal e Impacto en la Calibración Conforme*

En frecuencias de alta velocidad como las horarias ( **ERCOT** ), los patrones intra-diarios dominan la señal, permitiendo que arquitecturas profundas y TSFMs capturen dinámicas de largo alcance. Sin embargo, en frecuencias bajas (diaria/semanal en  **NN5**  o mensual en  **M3** ), la escasez intrínseca de puntos limita drásticamente a los modelos tabulares: la creación de  *lags*  remueve observaciones críticas, impidiendo reservar una muestra suficiente para el conjunto de calibración  \$Cal\$ . En estos escenarios, los TSFMs Zero-Shot destacan al asignar casi la totalidad del historial disponible a la calibración conforme.

###### *Gestión de Covariables Exógenas Futuras*

Un compromiso operativo clave reside en la capacidad del modelo para ingerir factores exógenos programados (promociones, pronósticos meteorológicos de radiación o viento). Mientras que los modelos tabulares y arquitecturas como  **Moirai**  o  **TimeGPT-1**  integran de forma nativa variables exógenas dinámicas futuras, modelos fundacionales univariados puros como  **Chronos**  base o  **Lag-Llama**  no pueden procesar directamente estos impulsores, limitando su utilidad en sectores como la generación eléctrica o la planificación de demanda impulsada por promociones.

###### *Ley de Escala en Modelos Fundacionales ( Scaling Law )*

Los datos empíricos confirman que la ley de escala se mantiene vigente en el dominio temporal:\$\$\\text{Rendimiento (MASE / MSIW)} \\propto \\text{Escala del Modelo (\\\# Parámetros)}\$\$  
  MASE / MSIW (Menor es Mejor)  
        ▲  
  0.90  │   ● Lag-Llama (2.5M)  
        │  
  0.60  │          ● Chronos Small (46M)  
        │  
  0.35  │                 ● Chronos-Bolt (48M) / TimesFM 1.0 (200M)  
        │                                ● TimesFM 2.0 (500M)  
  0.00  └──────────────────────────────────────────────────────────► TAMAÑO DEL MODELO

Modelos de mayor escala como  **TimesFM 2.0 (500M de parámetros)**  y  **Chronos-Bolt (48M)**  superan de forma consistente a modelos pequeños como  **Lag-Llama (2.5M)**  en métricas de precisión (MASE) y estrechez de intervalo (MSIW). Esto demuestra que los TSFMs aún no han alcanzado la meseta de saturación de rendimiento ( *performance plateau* ), convirtiendo el escalado de parámetros y datos de preentrenamiento en la vía primaria para elevar la precisión.Las restricciones operacionales y los trade-offs de cómputo conducen directamente a las reglas finales de decisión directiva.

##### 5\. CONCLUSIÓN Y LECCIONES DE CAMPO

###### *5.1. Axiomas Operacionales para Tomadores de Decisiones*

Para guiar la adopción tecnológica sin sucumbir a modas transitorias, todo Líder Técnico (CTO, Chief Data Officer) debe regir su arquitectura bajo  **3 Axiomas Clave de Campo** :

1. **Axioma de Parsimonia vs. Preentrenamiento:**   *No despliegue un Foundation Model de 500M de parámetros si un modelo lineal o tabular en diferencias satisface la latencia sobre un volumen de datos conocido.*  Reserve los TSFMs para escenarios  *Zero-Shot* , catálogos fríos ( *cold-start* ) o situaciones de escasez severa de datos donde la calibración conforme necesite asignar la casi totalidad del historial al conjunto  \$Cal\$ .  
2. **Axioma de Extrapolación y Frontera Física:**   *Jamás confíe la gestión de un riesgo de cola o la predicción de un evento récord a modelos tabulares basados en árboles de decisión (GBDT).*  La imposibilidad matemática de los árboles para extrapolar fuera del  *convex hull*  de entrenamiento generará mesetas planas engañosas que inducirán el colapso operativo del sistema ante eventos extremos (como la crisis de ERCOT en 2021).  
3. **Axioma de la Certidumbre Probabilística:**   *Un pronóstico puntual aislado (*  *\$\\hat{y}\_t*\$  *) no es una herramienta de ingeniería, sino una apuesta irresponsable.*  Todo valor puntual debe ir acompañado de sus correspondientes intervalos de incertidumbre calibrados no paramétricamente mediante Predicción Conforme (SCP), garantizando la tasa de cobertura requerida para la gestión del riesgo de negocio.

###### *5.2. Árbol de Decisión Práctico de Arquitectura por Sector*

Para seleccionar la arquitectura idónea según las restricciones de su proyecto, aplique la siguiente guía metodológica basada en 3 preguntas secuenciales de filtro:

* **¿Cuál es el volumen de datos disponible por serie (**  **\$N**\$  **)?**  
* Si  \$N \< 500\$  observaciones o es un producto nuevo sin historial ( *cold-start* )  \$\\to\$  Evalúe la disponibilidad de infraestructura. Para cómputo ligero use  **Vía 1** ; para alta precisión use  **Vía 4** .  
* Si  \$10^3 \\le N \\le 10^5\$  observaciones en series tabulares conocidas  \$\\to\$  Use  **Vía 2** .  
* Si  \$N \> 10^5\$  observaciones en sistemas complejos interconectados  \$\\to\$  Use  **Vía 3** .  
* **¿Cuál es la exigencia de latencia y costo de cómputo?**  
* Inferencia en microsegundos sobre CPU o dispositivos  *edge*   \$\\to\$   **Vía 1** .  
* Procesamiento  *batch*  de alto rendimiento en CPU multihilo  \$\\to\$   **Vía 2** .  
* Inferencia acelerada en GPU/TPU  \$\\to\$   **Vía 3**  o  **Vía 4** .  
* **¿Cuál es el impacto operacional de un evento extremo fuera del rango histórico?**  
* Si el costo de un fallo de extrapolación es crítico o asimétrico  \$\\to\$   **Evite Vía 2** ; adopte  **Vía 3**  o  **Vía 4 integradas con Predicción Conforme (SCP)** .

\====================================================================================================  
                        RUTAS METODOLÓGICAS DE ARQUITECTURA SECTORIAL  
\====================================================================================================

  \[INICIO: EVALUACIÓN DE PROYECTO\]  
     │  
     ├─► VÍA 1: MODELOS ANALÍTICOS Y SUAVIZADO (ARIMA, Holt-Winters, Verhulst)  
     │    • Condición: N \< 500, estacionalidad clara, inferencia en CPU de microsegundos.  
     │    • Sectores: Epidemiología de brotes (INS/MINSA), inventario en micro-retail.  
     │  
     ├─► VÍA 2: ML TABULAR CON LAGS (LightGBM, XGBoost, CatBoost)  
     │    • Condición: 10³ a 10⁵ observaciones, covariables estables, datos dentro del rango histórico.  
     │    • Sectores: Demanda de retail masivo con covariables (Walmart M5), ventas recurrentes.  
     │  
     ├─► VÍA 3: DEEP LEARNING DE PARCHES (PatchTST, TFT)  
     │    • Condición: \> 10⁵ series cruzadas multivariadas, interdependencias complejas, GPU disponible.  
     │    • Sectores: Redes eléctricas y parques renovables (CAISO, COES, Enel), tráfico masivo.  
     │  
     └─► VÍA 4: FOUNDATION MODELS ZERO-SHOT \+ SCP (TimesFM, Chronos-Bolt, Moirai)  
          • Condición: Cold-start, escasez de datos locales, necesidad de bandas P10-P90 garantizadas.  
          • Sectores: E-commerce con rotación continua, alertas climáticas, riesgo financiero.  
\====================================================================================================

El futuro del pronóstico de series temporales no consiste en la ilusión de adivinar el punto exacto del mañana, sino en dominar la arquitectura matemática de la incertidumbre.  
