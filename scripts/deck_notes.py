def get_speaker_notes():
    return {
        1: """<strong>Objetivo:</strong> Desarmar la fantasía del pronóstico puntual desde el segundo 1.<br><br>
          <strong>Guion sugerido:</strong> "Buenas tardes. Cuando abren cualquier app del clima y les dice 'mañana lloverá a las 3:00 PM con 28 °C', les están mintiendo piadosamente. El futuro no es una línea determinista; es un cono de posibilidades que se ensancha segundo a segundo debido a la entropía física del sistema (σ ∝ √h). Hoy vamos a responder con datos reales y rigor científico si la IA puede predecir el futuro o si solo estamos reproduciendo correlaciones pasadas." """,

        2: """<strong>Objetivo:</strong> Revelar la descomposición ontológica de cualquier señal física real (NotebookLM AI & Infografía 3).<br><br>
          <strong>Guion sugerido:</strong> "Miren esta ecuación fundamental: Y(t) = T(t) + S(t) + C(t) + ε(t). Toda serie temporal en la naturaleza tiene cuatro componentes físicos: una tendencia secular de calentamiento global (+0.20 °C/década), un ciclo solar anual invariable de 365 días, un macro-ciclo acoplado océano-atmósfera como El Niño cada 3 a 7 años, y ruido estocástico residual. Y presten atención a esta nota diagnóstica crítica: si fuerzan a una red neuronal profunda de 50 capas a memorizar el ruido residual ε, garantizarán un sobreajuste catastrófico en producción. El verdadero forecasting predice la física subyacente, jamás el ruido blanco." """,

        3: """<strong>Objetivo:</strong> Ubicar a la audiencia en la línea de tiempo evolutiva de 60 años de forecasting.<br><br>
          <strong>Guion sugerido:</strong> "No caigamos en la trampa de creer que el forecasting nació con ChatGPT. Tenemos cuatro eras metodológicas: la estadística clásica de 1960 (ARIMA, ETS) que sigue dominando en series cortas; el Machine Learning tabular de los 2000 (Random Forest, LightGBM) que ganó la competencia M5 de Walmart; el Deep Learning de 2017 (LSTM, PatchTST); y los Foundation Models Zero-Shot de este año (TimesFM, Chronos). La Ley de Parsimonia manda: más parámetros no garantizan mejor pronóstico." """,

        4: """<strong>Objetivo:</strong> Demostrar que los modelos matemáticos respetan límites físicos y biológicos.<br><br>
          <strong>Guion:</strong> "Miren este control interactivo. Si aumento alfa, el modelo sufre de amnesia inmediata: solo le importa lo que pasó ayer. Si lo bajo, promedia meses de historia. Y en biología ocurre lo mismo: ningún cultivo ni epidemia crece hasta el infinito; la curva logística impone un techo biológico infranqueable." """,

        5: """<strong>Objetivo:</strong> Mostrar el fallo garrafal de Random Forest ante eventos récord (Caso ERCOT Texas y Punchana).<br><br>
          <strong>Guion:</strong> "Muchos usan Random Forest sin entender su arquitectura: un árbol promedia hojas en cajas espaciales. Si viene un récord histórico fuera de distribución, flatlinea en una meseta constante. En la tormenta invernal Uri de Texas (Feb 2021), los árboles de la red predijeron meseta y la demanda superó el tope por 20 GW, provocando un colapso de 4 días. En nuestro experimento con datos SENAMHI en Punchana ocurrió exactamente lo mismo: el árbol falló por 5.5 °C. Para solucionarlo, hay que modelar primeras diferencias (Δy)." """,

        6: """<strong>Objetivo:</strong> Explicar el salto de LSTM a PatchTST sin jerga oscura.<br><br>
          <strong>Guion:</strong> "Las redes recurrentes procesaban día por día, como deletrear una palabra letra por letra, asfixiando a la GPU con cuellos de botella secuenciales. PatchTST agrupa los días en parches de 16 pasos, reduciendo la memoria en un 87.5% y permitiendo paralelizar auto-atención global. Operadores como CAISO y Enel usan PatchTST para monitorear 1,000 turbinas eólicas simultáneamente sin acumulación de error recursivo." """,

        7: """<strong>Objetivo:</strong> Presentar el concepto Zero-Shot en series temporales (TimesFM y Chronos).<br><br>
          <strong>Guion:</strong> "Así como los LLMs leen todo internet, TimesFM de Google y Chronos de AWS se pre-entrenaron con 100 mil millones de puntos temporales. Chronos discretiza los números en 4,096 tokens, tratándolos exactamente como palabras. Pueden pronosticar series que jamás vieron sin actualizar un solo gradiente. ¿Podrán competir contra modelos locales en la Amazonía peruana?" """,

        8: """<strong>Objetivo:</strong> Exponer la histología foliar y la trampa biofísica de la saturación del NDVI.<br><br>
          <strong>Guion:</strong> "Todos aman los mapas satelitales verdes. Pero hay una trampa biofísica elemental: la clorofila en el mesófilo en empalizada absorbe el 90% de luz roja (665 nm) y refleja el infrarrojo cercano (842 nm). Cuando el dosel arbóreo se cierra y el índice de área foliar supera 3 (LAI > 3), el NDVI choca contra una asíntota en 0.80 y queda completamente ciego. Por eso Copersucar y AgroVision migraron a NDRE y EVI para detectar estrés antes de que el cultivo muera." """,

        9: """<strong>Objetivo:</strong> Demostrar que el reloj fenológico manda sobre el acumulado anual de lluvia.<br><br>
          <strong>Guion:</strong> "En agricultura tropical, no importa cuánta lluvia cae en el año, sino en qué semana cae. En floración (agosto-octubre), si la precipitación no supera el umbral crítico de 140 mm, ocurre aborto floral irreversible. En la sequía de 2024, un modelo satelital ingenuo pronosticó 24.8 qq/ha porque las hojas estaban verdes; el modelo fenológico detectó el aborto y congeló la proyección en 18.46 qq/ha (la realidad fue 18.2 qq/ha, error de apenas 0.26)." """,

        10: """<strong>Objetivo:</strong> Mostrar que los supercomputadores de fluidos atmosféricos también discrepan.<br><br>
          <strong>Guion:</strong> "No solo la IA tiene incertidumbre. Aquí comparamos dos supercomputadores resolviendo las ecuaciones de Navier-Stokes con 4D-Var: NOAA GFS de Estados Unidos y ECMWF IFS de Europa discrepan en más de 6 °C sobre la misma coordenada de Iquitos para el mismo día. La incertidumbre está en la física caótica de la atmósfera." """,

        11: """<strong>Objetivo:</strong> Presentar el hito de GraphCast de DeepMind sobre mallas icosaédricas.<br><br>
          <strong>Guion:</strong> "En 2023, DeepMind publicó en Science que una Graph Neural Network sobre una esfera icosaédrica con 40,962 vértices calcula en 60 segundos en un solo TPU lo que al supercomputador de ECMWF le toma dos horas en miles de núcleos. GraphCast predijo la intensificación récord del Huracán Otis de Categoría 1 a 5 en menos de 24 horas, donde los modelos físicos tradicionales fallaron." """,

        12: """<strong>Objetivo:</strong> Presentar la estación Punchana de SENAMHI y la mugre de los datos de campo.<br><br>
          <strong>Guion:</strong> "Bienvenidos a Punchana, en la confluencia de los ríos Nanay y Amazonas. Aquí no hay laboratorios limpios: hay 85% de humedad, sensores con 9.7% de huecos y friajes antárticos que desploman la temperatura a 19 °C. Quien hace machine learning en el mundo real tiene que limpiar datos con rigor temporal estricto antes de tirar código." """,

        13: """<strong>Objetivo:</strong> Revelar el resultado del benchmark de 8 modelos en Punchana.<br><br>
          <strong>Guion:</strong> "Evaluamos 8 modelos sobre 90 días ciegos en Punchana. El ganador operativo fue ExtraTrees (1.880 °C de RMSE), corriendo en 0.11 segundos en un CPU modesto. Empató estadísticamente con TimesFM de 200 millones de parámetros (1.965 °C, p=0.27). Gastar 70 veces más cómputo en un solo sensor aislado no compró mayor precisión." """,

        14: """<strong>Objetivo:</strong> Demostrar el pronóstico probabilístico operativo a 7 días con bandas P10–P90.<br><br>
          <strong>Guion:</strong> "Aquí ven la demo operativa en vivo. La banda verde no es adorno: es el cono de cuantiles P10 a P90 que capturó el 85.7% de la realidad. Si van a tomar una decisión de gestión de desastres o logística fluvial en el río Amazonas, no miren la línea puntual: miren el ancho de la banda. El valor está en la incertidumbre." """,

        15: """<strong>Objetivo:</strong> Introducir el Caso B en Jaén y la telemetría Edge-AI de CENFROCAFE.<br><br>
          <strong>Guion:</strong> "Auditamos 24 años oficiales del Ministerio de Agricultura en Jaén, Cajamarca. Pero miren arriba esta telemetría real: la cooperativa CENFROCAFE vuela drones con visión artificial a 14.8 metros de altitud, contando 1,420 cerezas maduras y cuantificando la roya al 14.2% para predecir la cosecha 90 días antes. A 700 km de altitud, el satélite es ciego; a 14 metros, el dron cuenta granos reales." """,

        16: """<strong>Objetivo:</strong> Exponer la prueba forense de la ceguera satelital durante la crisis de la roya 2014.<br><br>
          <strong>Guion:</strong> "Este es el gráfico forense más contundente de la charla: la correlación entre NDVI anual y rendimiento fue de apenas 0.154. En 2014, el rendimiento de café colapsó un 56% (de 22.7 a 10.0 qq/ha), pero el satélite MODIS reportó que Jaén estaba 1.4% más verde. El hongo mató el grano bajo las ramas sin tirar el dosel. Confiar ciegamente en el satélite costó S/. 228 millones sin alerta." """,

        17: """<strong>Objetivo:</strong> Demostrar la superioridad de la fusión multimodal con validación Walk-Forward.<br><br>
          <strong>Guion:</strong> "Si meten satélite crudo al modelo, el error empeora a 5.32 quintales por hectárea debido al ruido del dosel. Pero si fusionan la precipitación en la ventana fenológica de floración con la tendencia agronómica, el error baja a 4.51 qq/ha. La biología y la física salvan al algoritmo." """,

        18: """<strong>Objetivo:</strong> Sintetizar las 5 leyes empíricas innegociables del forecasting real.<br><br>
          <strong>Guion:</strong> "Llévense estas 5 lecciones a sus proyectos: 1. Validación temporal Walk-Forward pura, jamás cross-validation aleatorio; 2. Comiencen por un baseline simple; 3. Reporten bandas de cuantiles P10-P90; 4. La física manda antes que el código; y 5. La complejidad profunda solo se justifica ante miles de series simultáneas." """,

        19: """<strong>Objetivo:</strong> Entregar el árbol de decisión metodológico para elegir el modelo correcto.<br><br>
          <strong>Guion:</strong> "Este árbol resume la decisión en ingeniería: si tienen una sola serie local, usen ARIMA o árboles con rezagos; si hay riesgo de récords inéditos, modelen diferencias Δy; si tienen variables biológicas, apliquen filtros fenológicos; y si gestionan miles de series sin GPU para reentrenar, acudan a Foundation Models Zero-Shot." """,

        20: """<strong>Objetivo:</strong> Cierre de alto impacto y entrega del repositorio 100% reproducible.<br><br>
          <strong>Guion:</strong> "Cerramos con la pregunta del título: ¿puede la IA predecir el futuro? La respuesta honesta y científica es no: el futuro posee entropía irreductible. Pero lo que la IA y la estadística rigurosa sí logran es darnos el marco matemático para decidir bajo riesgo controlado. Todos los cuadernos de Google Colab, datos de SENAMHI y compendios del MIDAGRI están abiertos en este QR con licencia MIT. Muchas gracias." """
    }
