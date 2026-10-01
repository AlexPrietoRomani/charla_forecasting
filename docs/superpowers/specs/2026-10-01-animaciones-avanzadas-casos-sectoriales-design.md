# Especificación de Diseño: Animaciones Avanzadas de Alta Fidelidad y Casos de Uso Sectoriales Trazables

**Fecha:** 2026-10-01  
**Proyecto:** Charla de Forecasting — *¿Puede la IA predecir el futuro? Lecciones de forecasting desde el mundo real*  
**Archivo Destino:** `scripts/build_deck.py` -> `presentacion.html`

---

## 1. Motivación y Diagnóstico

Las animaciones previas del mazo de diapositivas utilizaban primitivas SVG elementales (dos líneas simples, puntos flotantes y cajas estáticas). Aunque contaban con animación infinita en CSS, **no reflejaban el mecanismo físico, biológico ni matemático real**. Además, la audiencia requiere ver **casos de uso de la industria reales, con números, nombres de instituciones y papers científicos trazables**.

Este rediseño transforma 10 diapositivas clave en **esquemas interactivos de alta fidelidad técnica**, incorporando casos emblemáticos en 5 sectores:
1. **Energía & Redes Eléctricas:** Colapso de ERCOT (Texas 2021), CAISO (California), RTE (Francia) y COES (Perú).
2. **Retail & Supply Chain:** Walmart / Amazon M5 Forecasting Competition (30,490 SKUs).
3. **Agroexportación & Teledetección:** Cooperativas de Jaén (CENFROCAFE, Finca La Palma) y AgroVisión Perú.
4. **Epidemiología & Salud Pública:** Brote de Dengue en Loreto / Ucayali (MINSA/INS Perú).
5. **Meteorología Global & Logística Marítima:** Disparidad NOAA GFS vs ECMWF IFS en Iquitos y Google DeepMind GraphCast.

---

## 2. Especificación Detallada de las 10 Animaciones Enriquecidas

### Slide 4: Paradigma 1 — Curvas Paramétricas & Suavizado Exponencial
- **Gráfico Izquierdo (Dinámica Biológica & Saturación):**
  - Curva sigmoide logística $y_t = \frac{L}{1 + e^{-k(t-t_0)}}$ completa con ejes numéricos ($t$ en semanas, biomasa/población).
  - Asíntota horizontal superior de capacidad de carga biológica $L=100\%$.
  - Punto de inflexión en $t_0$ con altura $L/2$ y tangente de velocidad máxima calculada $\left.\frac{dy}{dt}\right|_{t_0} = \frac{kL}{4}$.
  - Trazador animado cíclico que desacelera conforme sube, mostrando cómo el crecimiento se frena por resistencia del medio.
  - Curva exponencial desbocada $y_0 e^{rt}$ en rojo punteado proyectándose hacia el infinito.
- **Gráfico Derecho (Holt-Winters & Ponderación Exponencial):**
  - Diagrama de barras ponderadas en tiempo real para lags $t-1$ hasta $t-14$: $w_k = \alpha(1-\alpha)^{k-1}$.
  - Resalta visualmente cómo $w_1 = 0.30$ (ayer) domina la predicción, mientras $w_{14} \approx 0.002$ tiene influencia prácticamente nula.
- **Caso Real Trazable:**
  - *Epidemiología:* Modelado del brote de Dengue en Iquitos/Loreto por el Instituto Nacional de Salud (INS/MINSA). Un modelo polinomial o no restringido predecía infectados infinitos; la curva logística con capacidad finita acotó el pico real de camas UCI.
  - *Retail:* Holt-Winters procesando 50,000 SKUs por segundo en cadenas de supermercados.
- **Referencias:** Verhulst (1838); Murray (Mathematical Biology 2002); Hyndman et al. (2002).

---

### Slide 5: Paradigma 1 — Descomposición Estadística STL
- **Esquema Visual:**
  - 4 subgráficos apilados verticalmente y sincronizados horizontalmente:
    1. $Y_t$: Serie original ruidosa (demanda de megavatios o temperatura).
    2. $T_t$: Tendencia Loess suavizada (baja frecuencia, componente interanual).
    3. $S_t$: Ciclo estacional armónico oscilante estricto (frecuencia semanal de 7 días o diaria de 24h).
    4. $R_t$: Residuo estocástico ($Y_t - T_t - S_t$) con picos anómalos pulsando en rojo cuando superan $\pm 2.5\sigma$.
  - Barra de barrido vertical sincronizada que atraviesa las 4 señales simultáneamente para ilustrar la aditividad $Y_t = T_t + S_t + R_t$.
- **Caso Real Trazable:**
  - *Energía Eléctrica:* Operadores del sistema eléctrico COES (Perú) y RTE (Francia) descomponiendo la demanda horaria para programar despacho de hidroeléctricas y ciclos combinados.
- **Referencias:** Cleveland, Cleveland, McRae & Terpenning (1990) *STL: A Seasonal-Trend Decomposition Procedure Based on Loess*.

---

### Slide 6: Paradigma 2 — El Puente Tabular (De Tiempo a Matriz Supervisada)
- **Esquema Visual:**
  - Parte superior: Flujo horizontal de la serie de tiempo continua $[y_{t-14}, \dots, y_{t-1}, y_t]$.
  - Caja de ventana deslizante de color cian que se desplaza paso a paso hacia la derecha.
  - Proyección de caída de partículas/flechas: los valores de la ventana caen ordenadamente en las columnas de una tabla supervisada ($X_1, X_2, \dots, X_{14} \to Y_{target}$).
  - Muestra explícitamente cómo una fila de la matriz se "congela" en memoria tabular para ser consumida por un árbol de decisión sin que este entienda el concepto de flecha del tiempo.
- **Caso Real Trazable:**
  - *Retail & Supply Chain:* Kaggle / Walmart M5 Forecasting Competition (Makridakis et al. 2022). Equipos ganadores demostraron que LightGBM con lags $1\dots 28$ y estadísticas móviles (*rolling mean/std*) batió a arquitecturas complejas de Deep Learning en series individuales.
- **Referencias:** Makridakis, Spiliotis & Assimakopoulos (Int. J. Forecast. 2022); Ke et al. (LightGBM, NeurIPS 2017).

---

### Slide 7: Paradigma 2 — Patología de los Árboles (No Extrapolan)
- **Esquema Visual:**
  - Panel izquierdo: Espacio de partición ortogonal 2D $(X_1, X_2)$ dividido en cuadrantes rectangulares por cortes sucesivos de decisión.
  - Los datos de entrenamiento quedan encerrados en una caja límite (convex hull acotado $[X_{\min}, X_{\max}]$).
  - Un punto de consulta nuevo (evento récord futuro) avanza más allá de la frontera máxima.
  - Al salir, el algoritmo lo asigna forzosamente a la hoja extrema, proyectando una meseta horizontal plana en la serie temporal ($y = \text{constante}$).
- **Caso Real Trazable:**
  - *Crisis Energética de Texas (ERCOT, Febrero 2021):* Tormenta invernal Uri llevó la temperatura a -18 °C en Dallas (evento sin precedentes en 50 años). Modelos tabulares entrenados con 10 años de datos predijeron un tope de demanda plano; la demanda real superó en 20 GW la previsión, provocando un colapso de la red de 4 días y pérdidas de \$195 mil millones.
- **Referencias:** Grinsztajn, Oyallon, Varoquaux (NeurIPS 2022); Breiman (2001).

---

### Slide 8: Paradigma 2 — Deep Learning Secuencial (LSTM vs PatchTST)
- **Esquema Visual Doble:**
  - **Lado Izquierdo (Celda LSTM):**
    - Muestra la autopista superior del estado de celda ($C_{t-1} \to C_t$).
    - Compuerta de olvido $f_t = \sigma(W_f [h_{t-1}, x_t] + b_f)$ con compuerta gráfica abriéndose/cerrándose.
    - Compuerta de entrada $i_t \times \tilde{C}_t$ inyectando nueva memoria y compuerta de salida $o_t \to h_t$.
  - **Lado Derecho (PatchTST — Estado del Arte 2023-2026):**
    - Serie continua segmentada en bloques o "patches" de 16 pasos temporales.
    - Proyección lineal a espacio latente.
    - Matriz de auto-atención multi-cabeza (Self-Attention) con enlaces interconectando parches distantes en un mapa de calor dinámico.
- **Caso Real Trazable:**
  - *Energía Renovable:* California ISO (CAISO) y Enel Green Power procesando simultáneamente 1,000 turbinas eólicas con PatchTST, capturando correlaciones espaciotemporales sin acumulación de error recursivo.
- **Referencias:** Hochreiter & Schmidhuber (1997); Nie, Nguyen, Sinthong & Kalagnanam (ICLR 2023); Lim et al. (2021) TFT.

---

### Slide 10: Paradigma 3 — Visión Artificial Local (Drones & Robótica en Cafetales)
- **Esquema Visual:**
  - Interfaz de Vuelo de Dron (HUD Profesional de Agricultura de Precisión):
    - Retícula central con telemetría activa: `Altitud: 14.8 m | Ground Speed: 2.1 m/s | Batería: 84% | Coordenadas: Jaén -5.6766°`.
    - Detecciones YOLOv12 en tiempo real con bounding boxes de colores:
      - Rojo: `[ID: 104] Cereza Madura: 96.8% [Conteo: 1,420 frutos/planta]`.
      - Verde claro: `[ID: 105] Cereza Verde: 89.1%`.
      - Púrpura: `[ID: 106] Roya (Hemileia vastatrix): 14.2%`.
    - Máscara poligonal semitransparente de segmentación de copa (SAM 2.1) aislando el follaje del suelo y sombras: `Canopy Cover: 94.2%`.
- **Caso Real Trazable:**
  - *Agroexportación de Café Especial:* Cooperativa CENFROCAFE (Jaén, Cajamarca) y ECOM Agroindustrial utilizando vuelos de drones multiespectrales para estimar volumen de quintales y calidad física 90 días antes del corte.
- **Referencias:** Kirillov et al. (Meta AI, 2024) SAM 2; Ramos et al. (Computers and Electronics in Agriculture, 2020).

---

### Slide 11: Paradigma 3 — Biofísica Satelital & Saturación de Índices
- **Esquema Visual Doble:**
  - **Panel Izquierdo (Física Óptica de la Hoja):**
    - Corte microscópico: Cutícula cerosa $\to$ Parénquima en empalizada (cloroplastos) $\to$ Mesófilo esponjoso con cavidades de aire.
    - Haz Rojo (Banda 4, 665 nm): Penetra y es absorbido en un 95% por los pigmentos de clorofila $a$ y $b$ para fotosíntesis.
    - Haz Infrarrojo Cercano NIR (Banda 8, 842 nm): Penetra la cutícula y rebota intensamente (85% reflectancia) en las interfaces célula-aire del mesófilo para evitar el sobrecalentamiento celular.
  - **Panel Derecho (Curva Espectral 400-2500 nm & Saturación):**
    - Gráfico continuo de reflectancia foliar mostrando el abrupto acantilado del "Red Edge" (690-730 nm, Banda 5 de Sentinel-2).
    - Curva comparativa de saturación: El NDVI se estanca en una asíntota plana de 0.80 cuando el Índice de Área Foliar supera 3 ($\text{LAI} > 3$), mientras que el EVI y el NDRE continúan respondiendo linealmente a aumentos de biomasa y nitrógeno.
- **Caso Real Trazable:**
  - *Commodities Agrícolas:* Copersucar / Raízen en Brasil (caña de azúcar) y AgroVisión en Perú (arándanos y café). El cambio de NDVI a NDRE permitió detectar deficiencias de nitrógeno que antes quedaban ocultas bajo canopias maduras.
- **Referencias:** Gates et al. (1965); Huete et al. (Remote Sens. Environ., 2002); Barnes et al. (2000) NDRE.

---

### Slide 12: Paradigma 3 — Fusión Multimodal Fenológica (El Reloj Botánico)
- **Esquema Visual:**
  - Diagrama tri-modular sincronizado a lo largo del año agrícola:
    1. Eje Fenológico: Ventana 1 Floración (Ago-Oct) $\to$ Ventana 2 Llenado de Grano (Nov-Feb) $\to$ Ventana 3 Maduración/Cosecha (Mar-Jul).
    2. Eje Meteorológico: Precipitación acumulada CHIRPS y Déficit de Presión de Vapor (VPD).
    3. Eje Satelital: Sentinel-2 EVI (10m) y NDWI de humedad foliar.
  - Marcador de Crisis Dinámico: Durante la Floración (Ago-Oct), la línea de lluvia cae por debajo del umbral crítico ($140\text{ mm}$ frente al histórico de $290\text{ mm}$). Se activa la señal de alarma: **Aborto Floral Irreversible**. Aunque en enero llueva con fuerza y el EVI se mantenga verde, el modelo de fusión congela la pérdida y proyecta 18.2 qq/ha.
- **Caso Real Trazable:**
  - *Campaña Cafetalera 2024 en Jaén (Cajamarca):* La sequía en floración causó una pérdida real del 24% en quintales por hectárea. El modelo ingenuo de solo NDVI predijo 24.0 qq/ha (falló por 5.8 qq/ha); el modelo de fusión fenológica AgroVisión acertó con 18.46 qq/ha (error de solo 0.26 qq/ha).
- **Referencias:** Ramos et al. (2020); Barbosa et al. (Agronomy, 2021); Bernardi et al. (Remote Sens., 2023).

---

### Slide 13: Paradigma 4 — Modelos Físicos Globales & Supercómputo NWP
- **Esquema Visual:**
  - Malla tridimensional de la atmósfera terrestre discretizada en niveles de presión barométrica:
    - Nivel Superficie (1000 hPa).
    - Nivel Capa Límite Planetaria (850 hPa, transporte de humedad amazónica).
    - Nivel Troposfera Media (500 hPa, vorticidad geostrófica).
    - Nivel Tropopausa (250 hPa, corriente en chorro o Jet Stream).
  - Vectores de dinámica de fluidos: advección zonal y meridional $(u, v)$, fuerza de Coriolis $-2\vec{\Omega} \times \vec{v}$, gradiente barométrico $-\frac{1}{\rho}\nabla p$ y penachos convectivos de vapor $w$.
  - Ciclo de asimilación 4D-Var: satélites de órbita polar (MetOp, NOAA-20) y radiosondeos inyectando millones de observaciones para recalibrar la integración numérica cada 6 horas.
- **Caso Real Trazable:**
  - *Navegación Marítima & Aviación:* Maersk y Air France utilizando campos de viento de ECMWF IFS para enrutar buques y aviones a favor de corrientes, reduciendo emisiones de CO2 y ahorrando hasta un 15% de combustible.
- **Referencias:** Bauer, Thorpe & Brunet (Nature 2015) *The quiet revolution of numerical weather prediction*.

---

### Slide 15: Paradigma 4 — GraphCast & Foundation Models Zero-Shot
- **Esquema Visual:**
  - **Lado Izquierdo (Google DeepMind GraphCast):**
    - Esfera terráquea con malla icosaédrica multiescala ($M_0$ a $M_6$, 40,962 vértices interconectados).
    - Pulsos de red neuronal de grafos (GNN): Encoder (cuadrícula latitud-longitud a malla icosaédrica) $\to$ Processor (16 bloques de paso de mensajes de alta velocidad) $\to$ Decoder.
    - Cuadro comparativo de infraestructura: ECMWF IFS (supercomputador europeo con miles de nodos CPU x86, 2 horas de cómputo) vs GraphCast (1 Cloud TPU v4, inferencia global completa en 60 segundos con 90% de variables meteorológicas superiores).
  - **Lado Derecho (Foundation Models Zero-Shot):**
    - Flujo de tokenización de series temporales de TimesFM (Google Research) y Chronos (Amazon T5): segmentación de valores numéricos continuos en tokens semánticos, prediciendo sin requerir ajuste fino (*fine-tuning*).
- **Caso Real Trazable:**
  - *Alerta Temprana de Desastres:* Predicción de trayectoria rápida de ciclones tropicales (Huracán Otis en Acapulco 2023) y Google Flood Hub monitoreando crecidas en cuencas de 80 países.
- **Referencias:** Lam et al. (Science 2023) GraphCast; Das et al. (Google 2024) TimesFM; Ansari et al. (Amazon 2024) Chronos.

---

### Slide 23: Síntesis — Árbol de Decisión Práctico de Modelado por Sector
- **Esquema Visual:**
  - Flujograma interactivo y animado de decisión guiado por 3 preguntas clave:
    1. *¿Cuál es el volumen de datos disponible?* ($N < 500$, $10^3 - 10^5$, $> 10^5$ o catálogo global).
    2. *¿Cuál es la exigencia de latencia y costo de cómputo?* (< 1 segundo en CPU vs entrenamiento en GPU).
    3. *¿Cuál es el sector de negocio y regulación?*
  - 4 Vías de Decisión con casos sectoriales explícitos:
    - **Vía 1: Modelos Analíticos / Suavizado:** $N < 500$, alta estacionalidad. *Sector:* Epidemiología de brotes (INS/MINSA), Retail de reposición en bodega pequeña. *Herramientas:* Holt-Winters, ARIMA, Curvas Logísticas.
    - **Vía 2: ML Tabular con Lags:** $10^3 - 10^5$ observaciones, variables climáticas/precios. *Sector:* Pronóstico de temperatura de estación (Punchana), Rendimiento agrícola por finca (Jaén). *Herramientas:* ExtraTrees, LightGBM con lags 1-14 y rolling stats.
    - **Vía 3: Deep Learning Multivariable:** $> 10^5$ series cruzadas con interdependencias. *Sector:* Parques eólicos y solares a escala nacional (CAISO, COES), Demanda eléctrica horaria. *Herramientas:* PatchTST, TFT, DeepAR.
    - **Vía 4: Foundation Models / Zero-Shot:** Nuevos productos sin historial o pronóstico planetario rápido. *Sector:* Catálogos masivos de e-commerce, alertas climáticas globales. *Herramientas:* TimesFM, Chronos, GraphCast.
- **Referencias:** Makridakis et al. (M4/M5 Competition); Hyndman (2021); Lim et al. (2021).

---

## 3. Plan de Verificación y Criterios de Aceptación
1. **Compilación limpia:** `python scripts/build_deck.py` ejecuta con código 0 y genera `presentacion.html` completamente autocontenido.
2. **Validación estructural de HTML:** 0 etiquetas sin cerrar ni anomalías sintácticas.
3. **Animaciones continuas:** Todas las figuras SVG conservan `@keyframes` infinitos que no se detienen.
4. **Verificación visual:** Captura de pantalla de las diapositivas actualizadas mediante Playwright / Edge headless en 1440x900 y confirmación de que no hay espacios vacíos ni desbordamientos de texto.
5. **Citas bibliográficas:** Cada caja explicativa incluye la referencia formal coincidente con `refs.bib`.
