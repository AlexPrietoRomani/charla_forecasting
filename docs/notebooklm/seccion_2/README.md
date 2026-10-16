# Sección 2 — Caso 1 Clima SENAMHI (Iquitos) · Prompts para NotebookLM

> ⚠️ **NotebookLM NO ve los datos.** Todos los prompts de este README ya llevan
> los datos reales incrustados (estación, CSVs resumidos, cifras). Pégalos tal cual.
> Los 6 prototipos HTML de referencia están en `prototipos/` (mismo sistema visual
> oscuro que secciones 1 y 3, 16:9, canvas interactivo, sin dependencias).

**Prototipos:** `12_Caso_1_Auditoria_Iquitos.html` · `13_Datos_SENAMHI_Punchana.html` ·
`14_Trampa_Arboles_Meseta_vs_Diferencias.html` ·
`15_Benchmark_14_Modelos_Tierra_vs_Supercomputo.html` ·
`16_Pronostico_7_Dias_Cono_P10_P90.html` ·
`17_Pipeline_Codigo_Diferencias_ExtraTrees.html`

## Datos reales incrustados (fuente: `data/caso_1/`)

- **Estación:** Punchana, Loreto (SENAMHI `103015`), −3.6903°, −73.2556°, 91 msnm.
- **Periodo:** 2019-01-01 → 2025-12-31, **N=2,557 días**, tmax media **31.79 °C**, máx **38.0 °C**
  (2023-10-07 y 2024-10-18), mín **19.2 °C**.
- **Medias anuales (media, máx):** 2019: 31.61/36.0 · 2020: 31.70/36.0 · 2021: 31.19/35.4 ·
  2022: 31.57/37.0 · 2023: 32.18/38.0 · 2024: 32.75/38.0 · 2025: 31.50/36.2.
- **Medias mensuales ENE–DIC:** 32.05, 31.77, 31.41, 31.35, 30.50, 30.41, 30.67, 32.00,
  33.12, 33.01, 33.08, 32.08 (fresco MAY–JUL ≈30.5, pico SEP–NOV ≈33.1).
- **Histograma tmax (bins 19–38 °C, paso 1):** [2,2,0,4,5,4,18,51,81,97,183,346,472,453,351,297,113,65,13].
- **Benchmark (RMSE 1d, MAE 1d, tiempo, p DM vs mejor):**
  ExtraTrees 1.880/1.466/0.25s CPU/p=1.0 · TimesFM-ZS 1.883/1.457/7.87s GPU/p=0.7095 ·
  RandomForest 1.888/1.471/0.6s/p=0.8759 · Chronos-ZS 1.903/1.418/3.13s/p=0.6523 ·
  LightGBM 1.926/1.466/0.06s/p=0.4136 · ARIMA(2,0,1) 1.964/1.506/p=0.151 ·
  Ridge 2.017/p=0.0331 · SARIMA 2.026/p=0.0799 · LSTM 2.053/17.03s/p=0.033 ·
  Holt-Winters 2.065/p=0.0426 · Naive-1d 2.334/p=0.0054 · ECMWF IFS 9km 2.458/2.043/p=0.0271 ·
  NOAA GFS 28km 2.583/2.013/p=0.0085 · Naive-7d 2.874/p=0.0001.
  Protocolo: 2,467 train + 90 holdout ciego Q4-2025, Diebold-Mariano + HLN (1997).
- **Ola SEP–OCT 2023 (32 días, tope train 34.0 °C, récord 38.0 °C el 2023-10-07):**
   RF en niveles → meseta ~31.5 °C (MAE en ola ≈4.1 °C recalculado en vivo); RF en
  diferencias → hasta 37.46 °C (MAE en ola ≈1.4 °C recalculado en vivo). Ver `experimento_extrapolacion.csv`.
- **Pronóstico 7d 25–31 dic 2025 (obs / ExtraTrees / P10 / P90):**
  33.6/34.33/31.24/37.42 · 33.2/32.89/29.80/35.99 · 32.4/33.05/29.95/36.14 ·
  27.2/32.77/29.68/35.86 · 30.4/32.64/29.55/35.73 · 27.8/32.73/29.64/35.82 ·
  31.0/32.76/29.66/35.85. ARIMA plano en 30.38 toda la semana.
- **Auditoría resuelta (deck corregido y regenerado):** cobertura real **5/7 (71.4%)**; fuera
  28 y 30 dic (friajes) — el deck decía 6/7 (85.7%, hardcodeado) y ya fue corregido. El 0.11s
  del slide 17 era de una corrida vieja del benchmark; la canónica da **0.25s CPU** y el MAE
  canónico es **1.466 °C** (el "1.15" era typo) — deck corregido a 0.25s/1.466.

---

## PROMPT 1 — Informe técnico y narrativo Sección 2

```text
Actúa como panel de 3 expertos: (1) climatólogo tropical amazónico (SENAMHI),
(2) estadístico de forecasting (tests Diebold-Mariano, conformal),
(3) ingeniero ML de campo (CPU edge, sin GPU).
Audiencia: Iquitos Data Fest 2026, mitad sin formación estadística. Tono: auditoría
empírica con storytelling ("la selva contra los algoritmos"), cero humo, toda cifra
trazable a los DATOS DE ARRIBA (no inventes ninguna).

Genera el "Informe Técnico y Narrativo – Sección 2: Caso 1 Clima SENAMHI Iquitos,
2,557 días de termómetro contra 14 modelos", estructura obligatoria:

### 1. EL LABORATORIO: Punchana como banco de pruebas
Estación 103015, coordenadas, periodo, variables (tmax/tmin/precip/humedad),
media 31.79, récord 38.0 (doble fecha), ciclo estacional (fresco MAY–JUL vs pico
SEP–NOV), histograma (moda 31–32 °C con 925 días, cola derecha de olas). Tesis:
régimen hiperhúmedo de baja varianza con shocks de calor récord = el peor caso
para modelos en niveles.

### 2. LA TRAMPA: meseta de los árboles en la ola SEP–OCT 2023
Explica hiperrectángulos cerrados y convex hull con analogía ("el loro que solo
repite lo oído"). Con los 32 días: RF-niveles meseta ~31.5 °C vs récord 38.0 °C;
cuantifica el MAE en ola de cada variante. Remedio: Δy = y_t − y_{t−1} + lags
1,2,3,7,14 → RF-diferencias llega a 37.46 °C. Conecta con Era 2 de la Sección 1.

### 3. EL DUELO: benchmark 14 modelos, Tierra vs Supercómputo
Tabla completa con RMSE/MAE/tiempo/p-valor. Lee el test DM: líderes empatados
(ExtraTrees, TimesFM p=0.71, RF p=0.88, Chronos p=0.65, LightGBM p=0.41);
física global pierde (ECMWF p=0.027, GFS p=0.0085) por falta de downscaling en
microclima; LSTM pierde y cuesta 17s. Regla de parsimonia: ExtraTrees CPU 0.25s
empata con TimesFM GPU 7.87s. Costo-beneficio explícito por modelo.

### 4. EL CONO: pronóstico 7d 25–31 dic 2025 con bandas P10–P90
Tabla día a día con obs vs 4 modelos + cono. Detecta los friajes (27.2 y 27.8 °C)
como rupturas. Usa la cobertura corregida 5/7 (71.4%): 28 y 30 dic caen fuera por friajes.
Moraleja: el punto fijo miente en h=7 (ancho 6.18 °C); el cono avisa.

### 5. EL PIPELINE + 3 AXIOMAS DEL CASO + PUENTE AL AGRO
Código comentado de 8 líneas (diff → lags → ExtraTrees → cumsum + cono).
3 axiomas estilo Sección 1 (ej. "Jamás pidas a un árbol un valor que nunca vio").
Puente al Acto 3: del clima-diario (N=2,557) a la cosecha-anual (N=24): qué cambia
cuando la frecuencia colapsa. 1500–2000 palabras, LaTeX para fórmulas, tablas Markdown.
```

## PROMPT 2 — Diapositivas Sección 2 (6 slides, espejo del deck 12–17)

```text
Eres diseñador instruccional. Genera el contenido EXACTO de las 6 diapositivas del
Acto 2 "Caso 1: Clima SENAMHI Iquitos" para presentacion.html, sistema visual de la
Sección 1 (título display, eyebrow mono cian, 3 bullets con <strong>, fuente pequeña,
guion 30s que empiece con "Miren..."). Usa SOLO las cifras de DATOS REALES de arriba.
Para CADA slide: (a) eyebrow, (b) título, (c) 3 bullets ≤25 palabras con cifra trazable,
(d) descripción del gráfico oscuro (cian/ámbar/rojo/verde), (e) fuente, (f) guion 30s.
Slides: 12 PORTADA (2557 días, Punchana, 3 preguntas) · 13 DATOS (media 31.79, récord
38.0 doble fecha, histograma moda 31–32, ciclo SEP–NOV vs MAY–JUL) · 14 TRAMPA (tope
34.0, meseta 31.5, récord 38.0, Δy hasta 37.46) · 15 BENCHMARK (tabla 14, líderes
p>0.05, ExtraTrees 1.88/0.25s empata TimesFM 7.87s p=0.71, ECMWF 2.46/GFS 2.58 pierden)
· 16 CONO 7D (tabla día a día, friajes, cobertura 5/7 = 71.4%) ·
17 PIPELINE (código 8 líneas diff→lags→ExtraTrees→cono, 0.25s CPU). Cierra 17 con
gancho al Acto 3 (de N=2,557 diario a N=24 anual).
```

## PROMPTS 3–8 — Una infografía por diapositiva (estilo claro PPTX S3: fondo marfil #F5F2EB, slate #3A4754, terracota #C96F4A, verde #4A7C59, 16:9, español, sin watermark)

```text
[12] Portada hero 16:9 fondo marfil: título "2,557 DÍAS DE TERMÓMETRO CONTRA 14 MODELOS",
sub "Caso 1 · Punchana, Iquitos (SENAMHI 103015)". Izquierda 3 KPIs (2,557 días
2019–2025 · media 31.79 °C · récord 38.0 °C oct-2023/2024). Centro: strip estacional
con pico SEP–NOV sombreado ámbar y puntos rojos en récords. Derecha cita: "Miren,
siete años de termómetro en la selva. Vamos a auditar a catorce modelos con estos
datos." Footer: SENAMHI Punchana −3.6903°, −73.2556°, 91 msnm.
```

```text
[13] Dashboard 16:9: izquierda histograma tmax bins 1 °C con valores
[2,2,0,4,5,4,18,51,81,97,183,346,472,453,351,297,113,65,13], moda 31–32 °C (472+453)
en cian, cola ≥36 °C (65+13) en rojo; derecha barras mensuales medias
[32.05,31.77,31.41,31.35,30.50,30.41,30.67,32.00,33.12,33.01,33.08,32.08] con MAY–JUL
verde fresco y SEP–NOV ámbar pico. Título "PUNCHANA 2019–2025: POCA VARIANZA, SHOCKS
RÉCORD". Footer: N=2,557 · mín 19.2 °C (friajes).
```

```text
[14] Duelo 16:9: eje X 32 días 15-sep→16-oct-2023, eje Y 26–39 °C; línea real cian
con pico 38.0 el 07-oct; línea roja punteada plana ~31.5 "RF en niveles: meseta
(limitada por tope 34.0 °C)"; línea verde punteada que sigue los picos hasta 37.46
"RF en diferencias Δy"; banda roja sombreada bajo 34.0 "rango visto en train".
Tarjetas MAE en ola recalculado en vivo: niveles ≈4.1 °C vs diferencias ≈1.4 °C. Título "LA TRAMPA:
EL ÁRBOL NO IMAGINA LO QUE NUNCA VIO". Cita: "Miren, el árbol es un loro sabio:
repite perfecto lo oído, pero no inventa palabras."
```

```text
[15] Podio 16:9: barras horizontales RMSE 1d ordenadas de los 14 modelos con valores
exactos de la tabla (1.880, 1.883, 1.888, 1.903, 1.926, 1.964, 2.017, 2.026, 2.053,
2.065, 2.334, 2.458, 2.583, 2.874); verde p>0.05 (5 líderes), ámbar clásicos/ML,
rojo ECMWF/GFS; insignias "0.25s CPU" vs "7.87s GPU"; sello "p=0.71 EMPATE".
Título "TIERRA (CPU) VS SUPERCÓMPUTO: GANA LA MEMORIA LOCAL". Footer: DM+HLN 1997,
holdout 90 días Q4-2025.
```

```text
[16] Cono 16:9: eje X 25→31 dic 2025; puntos obs [33.6,33.2,32.4,27.2,30.4,27.8,31.0];
línea ExtraTrees; cono verde P10–P90 ensanchándose (ancho h=1 ≈6.18 °C → h=7 duplica);
ARIMA gris plano en 30.38; días 28 y 30 marcados "FRIAJE ❌ fuera del cono".
Contador "5/7 dentro (71.4%)" con nota "coincide con el deck corregido".
Título "A 7 DÍAS EL PUNTO FIJO MIENTE, EL CONO AVISA".
```

```text
[17] Receta 16:9 estilo pizarra: 4 tarjetas → "1. Δy = y_t − y_{t−1} (estacionariza)" →
"2. lags 1·2·3·7·14 (memoria inercial)" → "3. ExtraTrees(100) CPU 0.25s" →
"4. cumsum + residuos = cono P10–P90"; bloque código 8 líneas; badges "RMSE 1.88 °C ·
0.25s CPU · sin GPU · p=1.0"; flecha "siguiente: del clima diario (N=2,557) a la
cosecha anual (N=24) → Acto 3". Nota al pie: cifras canónicas 0.25s CPU · RMSE 1.88 °C ·
MAE 1.466 °C (deck corregido).
```
