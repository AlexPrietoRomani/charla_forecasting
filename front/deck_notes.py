def get_speaker_notes():
    return {
        1: """<strong>Objetivo:</strong> Apertura de alto impacto y presentación del tema oficial en el Aula Magna UNAP.<br><br>
          <strong>Guion sugerido:</strong> "Buenas tardes con todos. Es un honor estar en el Iquitos Data Fest 2026. Cuando abren cualquier app meteorológica y les promete lluvia puntual a las 3:00 PM con 28 °C, les están mintiendo piadosamente. El futuro no es un punto determinista; es un cono estocástico que se ensancha inevitablemente con el tiempo. Hoy responderemos con datos reales de la Amazonía y rigor científico si la IA puede predecir el futuro o si solo estamos reproduciendo correlaciones del pasado." """,

        2: """<strong>Objetivo:</strong> Presentación personal y conexión con la audiencia (Ingeniero Agrónomo & Data Scientist).<br><br>
          <strong>Guion sugerido:</strong> "Para quienes no me conocen, soy Alex Prieto Romani, Ingeniero Agrónomo y Agriculture Data Scientist con maestría en Big Data & Data Science. Mi trabajo se centra en la intersección entre la física biológica del campo y la analítica avanzada: agricultura de precisión, teledetección satelital, visión artificial y modelos predictivos aplicados a series temporales complejas como el clima y el rendimiento agrícola." """,

        3: """<strong>Objetivo:</strong> Exponer la hoja de ruta clara de la sesión con los 5 bloques temáticos.<br><br>
          <strong>Guion sugerido:</strong> "Esta tarde estructuramos nuestra conferencia en cinco secciones fundamentales: primero, la historia y fundamentos matemáticos de los modelos de series temporales; segundo, el Caso 1 en Iquitos con 2,557 días de SENAMHI y la trampa de los árboles; tercero, cómo se aplican las series temporales en el agro desde la biología y la fenología; cuarto, el Caso 2 con la predicción de rendimiento de café en Jaén y la trampa del NDVI; y quinto, nuestras conclusiones y reglas empíricas innegociables para llevar modelos a producción." """,

        4: """<strong>Objetivo:</strong> Introducir la Sección 01 y ubicar el marco conceptual de la evolución histórica.<br><br>
          <strong>Guion sugerido:</strong> "Iniciamos el viaje preguntándonos cómo la ciencia ha intentado modelar el tiempo. No se trata de una historia donde lo nuevo reemplaza a lo viejo, sino de cuatro escuelas metodológicas que conviven hoy y resuelven problemas a escalas muy diferentes: desde un agricultor en Jaén hasta el operador del sistema eléctrico interconectado nacional." """,

        5: """<strong>Objetivo:</strong> Explicar la descomposición ontológica de cualquier señal física real.<br><br>
          <strong>Guion sugerido:</strong> "Miren esta ecuación fundamental: Y(t) = T(t) + S(t) + C(t) + ε(t). Toda serie temporal física combina cuatro dinámicas superpuestas: la tendencia secular, los ciclos astronómicos rígidos de 365 días del sol, macrociclos como El Niño y el ruido térmico residual. Quédense con esta regla: si no desestacionalizan su señal, su red neuronal más profunda no habrá aprendido ninguna relación causal: solo habrá memorizado qué mes del año es." """,

        6: """<strong>Objetivo:</strong> Recorrer las cuatro eras metodológicas del forecasting y sus casos de industria.<br><br>
          <strong>Guion sugerido:</strong> "La evolución del forecasting pasó por cuatro grandes saltos conceptuales. Primero, las fórmulas matemáticas cerradas de Verhulst y Holt-Winters: pocos parámetros, convergencia en microsegundos y mucha física. En los 2010s rompimos la flecha del tiempo para meter rezagos en Random Forest y LightGBM; dominaron Walmart M5 con 30 mil productos, pero tienen una patología: particionan el espacio en hiperrectángulos y jamás pueden extrapolar un récord histórico fuera de rango. Luego vinieron las LSTMs y PatchTST, que entendieron que el tiempo se procesa mejor en bloques o parches como palabras en un texto, reduciendo el cómputo 8 veces. Y hoy estamos en la era de los Foundation Models: modelos como TimesFM y Chronos que aprendieron patrones sobre cientos de miles de millones de puntos y hacen pronóstico Zero-Shot instantáneo sin reentrenar gradientes locales." """,

        7: """<strong>Objetivo:</strong> Demostrar la dispersión temporal y la inevitabilidad del cono de incertidumbre.<br><br>
          <strong>Guion sugerido:</strong> "Cuando le pedimos a ChatGPT o a una red neuronal un número para mañana, responde con aplomo instantáneo. Pero el futuro no es un punto determinista; es un cono estocástico que se ensancha inevitablemente. En la atmósfera amazónica o en el mercado de café, la entropía se acumula rápidamente: σ_h ∝ √h. La IA no sabe lo que no sabe. En horizontes más allá de 7 días, un pronóstico puntual oculta el riesgo operacional: debemos tomar decisiones sobre bandas empíricas P10–P90, nunca sobre un escalar aislado." """,

        8: """<strong>Objetivo:</strong> Introducir la Sección 02 con datos climatológicos reales de Iquitos.<br><br>
          <strong>Guion sugerido:</strong> "Pasamos a la Sección 2: la predicción de temperatura máxima en la estación SENAMHI Punchana, aquí en Iquitos. 2,557 días continuos de mediciones en pleno régimen ecuatorial hiperhúmedo. Vamos a poner a prueba los algoritmos ante el clima tropical real." """,

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

        14: """<strong>Objetivo:</strong> Introducir la Sección 03: Cómo se aplican las series temporales en el agro.<br><br>
          <strong>Guion sugerido:</strong> "Entramos a la Sección 3: el mundo agrícola. Predecir cultivos no es predecir cotizaciones de bolsa ni clics en una web. En el agro la biología vegetal impone leyes implacables: dinámicas de ultrabaja frecuencia, retardos fenológicos de meses entre el estímulo y la cosecha, y efectos umbral fisiológicos donde un grado de calor más puede esterilizar una flor." """,

        15: """<strong>Objetivo:</strong> Explicar los tres retos biológicos fundamentales que rigen las series agrícolas.<br><br>
          <strong>Guion sugerido:</strong> "Tres leyes gobiernan las series agronómicas: primero, los retrasos fenológicos biológicos: la cosecha de hoy se determinó en la floración de hace 6 a 8 meses; segundo, los efectos umbral no lineales de grados día (GDD) y déficit de vapor (VPD); y tercero, las series de ultrabaja frecuencia: en agricultura solo tenemos 1 dato al año (24 datos en 24 años). En regímenes de tan pocos datos, el sobreajuste es letal: la física del dominio vale más que cualquier arquitectura profunda." """,

        16: """<strong>Objetivo:</strong> Detallar las 3 ventanas fenológicas críticas del cultivo y su asimetría física.<br><br>
          <strong>Guion sugerido:</strong> "Miren este calendario fenológico: en el café de Jaén, la campaña se juega en tres ventanas. La floración entre agosto y octubre es hipercrítica: si hay estrés hídrico de solo dos semanas, la flor aborta y el rendimiento colapsa. El llenado entre noviembre y febrero define el calibre del grano. Y la cosecha entre marzo y julio exige calor seco para recolectar y secar. La misma temperatura de 34 °C que ayuda al secado en cosecha, destruye la producción completa si ocurre en plena floración. El tiempo biológico no es lineal." """,

        17: """<strong>Objetivo:</strong> Introducir la Sección 04: Caso 2: Predicción de rendimiento usando NDVI.<br><br>
          <strong>Guion sugerido:</strong> "Con ese marco biológico claro, pasamos a la Sección 4: el Caso 2. Auditamos 24 campañas oficiales de café en Jaén (Cajamarca), cruzadas con 576 compuestos satelitales MODIS de la NASA y reanálisis climático ERA5. Vamos a descubrir por qué el satélite óptico más popular de la agricultura falló catastróficamente ante una plaga real." """,

        18: """<strong>Objetivo:</strong> Resaltar los 3 datos auditados clave de las 24 campañas en Jaén.<br><br>
          <strong>Guion sugerido:</strong> "Tres métricas resumen este caso: 24 campañas agrícolas continuas del Ministerio de Agricultura (SIEA/MIDAGRI); una caída histórica de -56% en el rendimiento durante la epidemia de roya amarilla en 2013; y un MAE mínimo de 4.51 quintales por hectárea alcanzado por nuestro modelo de fusión fenológica." """,

        19: """<strong>Objetivo:</strong> Demostrar con evidencia forense la trampa de saturación del satélite NDVI.<br><br>
          <strong>Guion sugerido:</strong> "Este es el hallazgo más contundente de nuestra investigación: el satélite MODIS NDVI tuvo una correlación prácticamente nula con el rendimiento real (r = 0.154, p = 0.600). En la epidemia de roya de 2013, el rendimiento oficial cayó -56%, pero el NDVI subió +1.4% porque las malezas y la sombra mantuvieron verde el dosel superior. El satélite fue ciego a la pérdida de S/. 228 millones. En cambio, el estrés hídrico en floración explicó el 56% de la varianza real (r = 0.751)." """,

        20: """<strong>Objetivo:</strong> Demostrar la validación Walk-Forward expansiva y la superioridad del modelo de fusión.<br><br>
          <strong>Guion sugerido:</strong> "Evaluamos año por año con validación Walk-Forward sin fuga temporal, entrenando solo con campañas del pasado. El modelo alimentado únicamente con satélite NDVI (M3) tuvo un error de 6.18 qq/ha, siendo peor que una tendencia simple (4.79 qq/ha). Pero cuando fusionamos la anomalía de lluvia en floración con la tendencia agronómica, el error se redujo a 4.51 qq/ha. La biología rescató al algoritmo." """,

        21: """<strong>Objetivo:</strong> Introducir la Sección 05: Conclusiones y lecciones aprendidas.<br><br>
          <strong>Guion sugerido:</strong> "Llegamos a la Sección 5: el momento de destilar los aprendizajes de estos dos casos empíricos. Lo que hemos visto en la meteorología de Iquitos y en los cafetales de Jaén nos deja tres principios metodológicos innegociables para cualquiera que aplique IA a datos del mundo real." """,

        22: """<strong>Objetivo:</strong> Sintetizar los 3 pilares maestros de la conferencia.<br><br>
          <strong>Guion sugerido:</strong> "Llévense tres verdades a sus proyectos y tesis: 1. Respeten la causalidad del tiempo: jamás usen cross-validation aleatorio en series temporales; entrenen en el pasado y evalúen en el futuro. 2. El valor está en la banda, no en el punto: un escalar aislado oculta el riesgo operacional; comuniquen siempre conos P10–P90 calibrados. Y 3. La física y el dominio mandan antes que el algoritmo: conozcan los límites de sus sensores y la fisiología antes de optimizar hiperparámetros." """,

        23: """<strong>Objetivo:</strong> Cierre memorable, agradecimientos y apertura del debate con QR.<br><br>
          <strong>Guion sugerido:</strong> "Volvemos a la pregunta que dio título a esta charla: ¿puede la IA predecir el futuro? La respuesta honesta y científica es no: el futuro contiene entropía física irreductible. Pero lo que la IA y el modelado probabilístico sí pueden hacer es darnos las herramientas para tomar mejores decisiones en un mundo incierto. Todo el código, los datasets auditados y las diapositivas interactivas están disponibles escaneando este código QR que los lleva directo a mi sitio web. ¡Muchas gracias, Iquitos!" """
    }
