def get_speaker_notes():
    return {
        1: """<strong>Objetivo:</strong> Apertura de alto impacto y presentación del tema oficial en el Aula Magna UNAP.<br><br>
          <strong>Guion sugerido:</strong> "Buenas tardes con todos. Es un honor estar en el Iquitos Data Fest 2026. Cuando abren cualquier app meteorológica y les promete lluvia puntual a las 3:00 PM con 28 °C, les están mintiendo piadosamente. El futuro no es un punto determinista; es un cono estocástico que se ensancha inevitablemente con el tiempo. Hoy responderemos con datos reales de la Amazonía y rigor científico si la IA puede predecir el futuro o si solo estamos reproduciendo correlaciones del pasado." """,

        2: """<strong>Objetivo:</strong> Presentación personal y conexión con la audiencia (Ingeniero Agrónomo & Data Scientist).<br><br>
          <strong>Guion sugerido:</strong> "Para quienes no me conocen, soy Alex Prieto Romani, Ingeniero Agrónomo y Agriculture Data Scientist con maestría en Big Data & Data Science. Mi trabajo se centra en la intersección entre la física biológica del campo y la analítica avanzada: agricultura de precisión, teledetección satelital, visión artificial y modelos predictivos aplicados a series temporales complejas como el clima y el rendimiento agrícola." """,

        3: """<strong>Objetivo:</strong> Exponer la hoja de ruta clara de la sesión con los 4 bloques temáticos.<br><br>
          <strong>Guion sugerido:</strong> "Esta tarde abordaremos cuatro actos fundamentales: primero, la historia y fundamentos matemáticos de las series temporales; segundo, el Caso 1 en Iquitos con 2,557 días de SENAMHI y la trampa de los árboles; tercero, cómo se aplican las series en el agro y el Caso 2 con 24 campañas de café en Jaén; y cuarto, las conclusiones y reglas empíricas para llevar modelos a producción." """,

        4: """<strong>Objetivo:</strong> Introducir el Acto 1 y ubicar el marco conceptual.<br><br>
          <strong>Guion sugerido:</strong> "Iniciamos con el primer bloque: la evolución de los modelos de series temporales. Durante décadas hemos intentado descifrar el futuro. Vamos a entender cómo pasamos de las fórmulas lineales estadísticas de Box-Jenkins a los grandes modelos de grafos y transformers, y por qué la física nunca pasa de moda." """,

        5: """<strong>Objetivo:</strong> Explicar la descomposición ontológica de cualquier señal física real.<br><br>
          <strong>Guion sugerido:</strong> "Miren esta ecuación fundamental: Y(t) = T(t) + S(t) + C(t) + ε(t). Toda serie temporal en la naturaleza es la superposición de leyes termodinámicas, ciclos astronómicos de 365 días, macrociclos oceánicos como El Niño y ruido caótico residual. El secreto de la ingeniería no es forzar a una red profunda a memorizar el ruido, sino modelar la señal física real." """,

        6: """<strong>Objetivo:</strong> Recorrer las cuatro eras metodológicas del forecasting.<br><br>
          <strong>Guion sugerido:</strong> "El forecasting no nació con los LLMs. Tenemos cuatro grandes eras: la estadística clásica (ARIMA, Holt-Winters); el Machine Learning tabular (Random Forest, XGBoost); el Deep Learning temporal (LSTM, TFT); y los Foundation Models Zero-Shot de hoy (Chronos, GraphCast). Cada era tiene su lugar, pero la ley de parsimonia manda: mayor complejidad no garantiza mejor precisión." """,

        7: """<strong>Objetivo:</strong> Demostrar la dispersión temporal y la inevitabilidad del cono de incertidumbre.<br><br>
          <strong>Guion sugerido:</strong> "Miren este cono de incertidumbre estocástica. Debido a la teoría del caos y la entropía de Lorenz, la dispersión crece con σ ∝ √h. Un pronóstico puntual es una ilusión que oculta el riesgo operativo. En horizontes más allá de 7 días, cualquier decisión logística en la cuenca amazónica debe tomarse sobre bandas P10–P90, jamás sobre un escalar." """,

        8: """<strong>Objetivo:</strong> Introducir el Caso 1 con datos climatológicos reales de Iquitos.<br><br>
          <strong>Guion sugerido:</strong> "Pasamos a nuestro primer caso real: la predicción de temperatura máxima en la estación SENAMHI Punchana, aquí en Iquitos. 2,557 días continuos de mediciones en pleno régimen ecuatorial hiperhúmedo. Vamos a poner a prueba los algoritmos ante el clima tropical real." """,

        9: """<strong>Objetivo:</strong> Destacar las 3 métricas críticas del dataset de Punchana.<br><br>
          <strong>Guion sugerido:</strong> "Tres cifras definen este desafío: 2,557 días de registro ininterrumpido; una media tropical constante de 31.8 °C; y un horizonte de 7 días donde el error del modelo iguala a la varianza histórica del clima, marcando la frontera de predictibilidad meteorológica." """,

        10: """<strong>Objetivo:</strong> Demostrar el fallo de los árboles de decisión ante olas de calor récord.<br><br>
          <strong>Guion sugerido:</strong> "Aquí está una de las trampas más peligrosas en la práctica: Random Forest particiona el espacio en cajas ortogonales. Si en Iquitos ocurre una ola de calor histórica de 37.4 °C y el modelo se entrenó con un tope de 34.0 °C, el árbol colapsa en una meseta constante de 31.5 °C. La solución no es una red más grande, sino modelar primeras diferencias (Δy)." """,

        11: """<strong>Objetivo:</strong> Revelar los resultados del benchmark ciego entre 6 familias de modelos.<br><br>
          <strong>Guion sugerido:</strong> "Evaluamos 6 modelos sobre un conjunto de prueba ciego de 365 días en Punchana. El ganador indiscutible fue ExtraTrees con un MAE de 1.15 °C entrenando en 0.11 segundos en CPU. Empató con redes profundas consumiendo 70 veces menos recursos. La navaja de Ockham demostrada empíricamente." """,

        12: """<strong>Objetivo:</strong> Mostrar la ejecución en vivo del pronóstico multi-step con intervalos.<br><br>
          <strong>Guion sugerido:</strong> "Aquí observan la proyección operativa a 7 días. Noten cómo las bandas P10–P90 capturan 6 de los 7 días reales (85.7% de cobertura empírica). El séptimo día la incertidumbre se ensancha, alertando a los tomadores de decisiones sobre el riesgo físico real." """,

        13: """<strong>Objetivo:</strong> Explicar el código de ingeniería que hace posible el modelo parsimonioso.<br><br>
          <strong>Guion sugerido:</strong> "En apenas 15 líneas de código resolvemos el problema: transformamos a diferencias finitas, inyectamos retardos temporales de 1, 2, 3, 7 y 14 días para capturar la memoria inercial de la atmósfera, y reconstruimos el nivel estocástico de forma acumulativa en milisegundos." """,

        14: """<strong>Objetivo:</strong> Introducir el Bloque 3: Series temporales en la agricultura y el Caso 2 en Jaén.<br><br>
          <strong>Guion sugerido:</strong> "Entramos al tercer bloque: la agricultura. Predecir cultivos no es predecir acciones de bolsa ni tráfico web. En el agro la biología impone retardos fenológicos de meses. Vamos a auditar 24 campañas oficiales de café en Jaén y poner a prueba los satélites de la NASA." """,

        15: """<strong>Objetivo:</strong> Explicar los fundamentos biológicos que rigen las series agrícolas.<br><br>
          <strong>Guion sugerido:</strong> "En agricultura tropical, lo que ocurre en la cosecha de junio se definió en la floración de octubre del año anterior. Además, en series agrícolas no tenemos millones de filas: tenemos apenas 24 datos en 24 años. Si aplican redes neuronales masivas sin respetar la fenología, el sobreajuste destruirá cualquier predicción." """,

        16: """<strong>Objetivo:</strong> Demostrar con evidencia forense la saturación óptica del satélite NDVI.<br><br>
          <strong>Guion sugerido:</strong> "Este gráfico es contundente: el satélite MODIS NDVI mostró un R² de apenas 0.08 frente al rendimiento real. En la crisis de la roya amarilla de 2013, el rendimiento cayó un 56%, pero el satélite decía que el campo estaba verde porque el dosel arbóreo satura. En cambio, el estrés hídrico en floración explicó el 56% de la varianza real." """,

        17: """<strong>Objetivo:</strong> Resaltar los 3 datos clave de las 24 campañas de café en Jaén.<br><br>
          <strong>Guion sugerido:</strong> "24 campañas continuas del MIDAGRI; una caída del 56% por plaga biológica que el satélite no vio; y un MAE mínimo de 4.51 quintales por hectárea alcanzado únicamente cuando combinamos la física climática con la tendencia agronómica." """,

        18: """<strong>Objetivo:</strong> Demostrar la validación Walk-Forward expansiva y la superioridad del modelo de fusión.<br><br>
          <strong>Guion sugerido:</strong> "Evaluamos año por año con validación Walk-Forward sin fuga temporal. El modelo que solo usó satélite falló con MAE de 6.18 qq/ha. Pero nuestro modelo de Fusión Fenológica (clima en floración + tendencia) logró el menor error del benchmark (4.51 qq/ha). La biología rescató al algoritmo." """,

        19: """<strong>Objetivo:</strong> Sintetizar las 3 conclusiones maestras de la conferencia.<br><br>
          <strong>Guion sugerido:</strong> "Llévense tres verdades innegociables: 1. Respeten la causalidad del tiempo: jamás usen cross-validation aleatorio; 2. El valor está en la banda de incertidumbre, no en la predicción puntual; y 3. Entiendan el dominio físico antes de elegir el algoritmo. La física manda sobre el código." """,

        20: """<strong>Objetivo:</strong> Cierre memorable, agradecimientos y apertura del debate con QR.<br><br>
          <strong>Guion sugerido:</strong> "Volvemos a la pregunta inicial: ¿puede la IA predecir el futuro? La respuesta rigurosa es no: el futuro tiene entropía irreductible. Pero lo que la IA sí puede hacer es darnos las herramientas para tomar decisiones óptimas sin conocer el futuro. Todo el código, notebooks de Google Colab y datos de SENAMHI están disponibles escaneando este código QR. ¡Muchas gracias, Iquitos!" """
    }
