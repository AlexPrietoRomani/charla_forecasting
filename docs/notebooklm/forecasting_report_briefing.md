# Comprehensive Briefing Document: Advanced Forecasting Paradigms, High-Fidelity Visualizations, and Foundation Models

## Executive Summary

This briefing document synthesizes key insights, architectural specifications, and empirical benchmarks from recent advancements in time series forecasting and advanced presentation engineering. The core objective of these developments is twofold: first, upgrading presentation decks (specifically `scripts/build_deck.py` generating `presentacion.html`) from elementary SVG primitives to **high-fidelity, mathematically and physically accurate interactive schemas**; second, evaluating modern machine learning paradigms—ranging from parametric curves and tree-based ensembles to sequential deep learning and large-scale zero-shot foundation models like **Chronos** and **GraphCast**.

By grounding mathematical mechanisms in real-world, traceable sectorial cases across **Energy & Power Grids, Retail & Supply Chain, Agro-export & Remote Sensing, Epidemiology & Public Health, and Meteorology & Maritime Logistics**, these frameworks bridge theoretical modeling and operational decision-making. Notably, the empirical findings demonstrate that tabular models (e.g., LightGBM) excel in bounded historical regimes but fail catastrophically during out-of-bounds extreme events (e.g., the Texas ERCOT crisis). Concurrently, foundation models trained via cross-entropy over discretized time-series tokens (e.g., Amazon's **Chronos**) achieve state-of-the-art in-domain and zero-shot accuracy, rivaling or exceeding task-specific deep learning models.

---

## Key Themes & Architectural Paradigms

```
                  ┌────────────────────────────────────────────────────────┐
                  │          TIME SERIES FORECASTING PARADIGMS             │
                  └───────────────────────────┬────────────────────────────┘
                                              │
    ┌──────────────────────┬──────────────────┴──────────────────┬──────────────────────┐
    │                      │                                     │                      │
┌───▼──────────────────┐ ┌─▼───────────────────────────┐ ┌───────▼──────────────────┐ ┌──▼──────────────────┐
│ 1. Parametric / STL  │ │ 2. Tabular ML (MLP/Trees)   │ │ 3. Sequential DL     │ │ 4. Foundation / NWP │
│    Smoothing         │ │    Lags & Rolling Window    │ │    (LSTM, PatchTST)   │ │    (Chronos, GraphCast)│
└───┬──────────────────┘ └─┬───────────────────────────┘ └───────┬──────────────────┘ └──┬───────────────────┘
    │                      │                                     │                         │
    ├─ Verhulst Sigmoid    ├─ Feature Engineering (Lags 1-14)    ├─ Long Short-Term Memory ├─ Discretization / Bins
    ├─ Holt-Winters        ├─ Orthogonal Partitions             ├─ Multi-Head Attention   ├─ Language Model (T5/GPT)
    └─ Loess Decomp. ($Y_t$)└─ Fails on Out-of-Bounds Extremes  └─ Patch Tokenization     └─ 4D-Var / GNN Mashing
```

### 1. Parametric Curves, Holt-Winters, and STL Decomposition
Classical smoothing techniques and biological growth models remain vital for bounded systems and structural decomposition. Curvature constraints (e.g., carrying capacity $L$) prevent runaway exponential estimates in epidemiological and population models. Seasonal-Trend Decomposition using Loess (STL) isolates low-frequency trends ($T_t$), strict harmonic seasonalities ($S_t$), and stochastic residuals ($R_t$) to provide additive signal clarity ($Y_t = T_t + S_t + R_t$).

### 2. Tabular Feature Engineering vs. Spatial Tree Failure
Bridging continuous time series into supervised tabular matrices ($X_1, \dots, X_{14} \to Y_{\text{target}}$) via sliding windows enables gradient-boosted trees (e.g., LightGBM) to dominate standard benchmark competitions like Kaggle's M5. However, tree-based models rely on orthogonal space partitioning bounded within $[X_{\min}, X_{\max}]$. Consequently, they are inherently incapable of extrapolation, predicting flat horizontal plateaus during unprecedented record events.

### 3. Sequential Deep Learning and Spatial-Temporal Attention
Architectures designed for sequential dynamics evolved from recurrent architectures with memory gating (LSTM) to patch-based multi-head self-attention mechanisms (PatchTST). Segmenting time series into discrete 16-step patches captures long-range spatiotemporal dependencies without suffering from recursive error accumulation.

### 4. Language Modeling Paradigms and Zero-Shot Foundation Models
Formulating univariate time series forecasting as a sequence modeling task—analogous to natural language processing—allows standard Transformer architectures (T5, GPT-2) to perform regression via classification. By scaling and quantizing real values into discrete token vocabularies, pretrained models (e.g., Chronos) leverage synthetic Gaussian Process data (KernelSynth) and Mixup augmentations (TSMixup) to deliver high zero-shot performance across diverse unseen domains.

---

## Detailed Technical Analysis of Enriched Visualizations & Traceable Case Studies

The presentation deck update transforms 10 critical slides into high-fidelity technical schematics with infinite CSS keyframe animations. Below is the comprehensive specification of each redesigned slide, including the exact mathematical formulations, visual mechanisms, traceable industry cases, and academic references.

### Slide 4: Paradigma 1 — Curvas Paramétricas & Suavizado Exponencial

*   **Mathematical Formulations:**
    *   *Logistic Sigmoid Curve:* $y_t = \frac{L}{1 + e^{-k(t-t_0)}}$ with upper horizontal asymptote of biological carrying capacity $L = 100\%$.
    *   *Inflection Point:* Located at $t_0$ with height $L/2$ and maximum velocity tangent $\left.\frac{dy}{dt}\right|_{t_0} = \frac{kL}{4}$.
    *   *Unconstrained Exponential:* $y_0 e^{rt}$ projecting to infinity.
    *   *Holt-Winters Weight Decay:* $w_k = \alpha(1-\alpha)^{k-1}$ for lags $t-1$ to $t-14$ (e.g., $w_1 = 0.30$ vs. $w_{14} \approx 0.002$).
*   **Visual Mechanisms:**
    *   Left Panel: Dual plot contrasting the bounded sigmoid curve (featuring a decelerating cyclic animated tracer) against a dashed red runaway exponential curve.
    *   Right Panel: Real-time weighted bar chart animating exponential decay across 14 historical lags.
*   **Traceable Industry Case Study:**
    *   *Epidemiology:* Dengue outbreak modeling in Iquitos/Loreto by the National Institute of Health (INS/MINSA Peru). Unconstrained polynomial models projected infinite infections; the logistic curve bounded peak ICU bed requirements accurately.
    *   *Retail:* Holt-Winters exponential smoothing processing 50,000 SKUs per second for supermarket inventory replenishment.
*   **Academic References:** Verhulst (1838); Murray (*Mathematical Biology*, 2002); Hyndman et al. (2002).

### Slide 5: Paradigma 1 — Descomposición Estadística STL

*   **Mathematical Formulations:**
    *   *Additive Decomposition:* $Y_t = T_t + S_t + R_t$.
    *   *Anomaly Threshold:* Stochastic residual $R_t = Y_t - T_t - S_t$ pulsing red when exceeding $\pm 2.5\sigma$.
*   **Visual Mechanisms:**
    *   Four vertically stacked, horizontally synchronized subplots representing $Y_t$ (noisy demand/temperature), $T_t$ (smoothed Loess trend), $S_t$ (strict 24h/7d harmonic cycle), and $R_t$ (residual spikes).
    *   A continuous vertical sweep bar crosses all four signals simultaneously to demonstrate additivity.
*   **Traceable Industry Case Study:**
    *   *Energy & Power Grids:* System operators COES (Peru) and RTE (France) decomposing hourly power demand to schedule hydroelectric dispatch and combined-cycle thermal generation.
*   **Academic References:** Cleveland, Cleveland, McRae, & Terpenning (1990) *STL: A Seasonal-Trend Decomposition Procedure Based on Loess*.

### Slide 6: Paradigma 2 — El Puente Tabular (De Tiempo a Matriz Supervisada)

*   **Mathematical Formulations:**
    *   *Sliding Window Map:* $[y_{t-14}, \dots, y_{t-1}, y_t] \to (X_1, X_2, \dots, X_{14} \to Y_{\text{target}})$.
*   **Visual Mechanisms:**
    *   Top: Continuous horizontal flow of a raw time series sequence.
    *   Center: Moving cyan sliding window stepping rightward, dropping particle/arrow projections that freeze ordered values into rows of a supervised tabular matrix.
    *   Visual proof that decision trees consume static memory rows without intrinsic awareness of time's arrow.
*   **Traceable Industry Case Study:**
    *   *Retail & Supply Chain:* Kaggle / Walmart M5 Forecasting Competition (30,490 SKUs). Winning teams proved LightGBM utilizing lags $1\dots 28$ and rolling statistics (*rolling mean/std*) outperformed complex deep learning architectures on individual series.
*   **Academic References:** Makridakis, Spiliotis, & Assimakopoulos (*Int. J. Forecast.*, 2022); Ke et al. (*LightGBM, NeurIPS*, 2017).

### Slide 7: Paradigma 2 — Patología de los Árboles (No Extrapolan)

*   **Mathematical Formulations:**
    *   *Orthogonal Bounded Hull:* Decision space $(X_1, X_2)$ partitioned into hyper-rectangles within training limits $[X_{\min}, X_{\max}]$. Out-of-bounds query $X_{\text{new}} > X_{\max}$ forces prediction to $y = \text{constant}$.
*   **Visual Mechanisms:**
    *   Left Panel: 2D orthogonal decision partition grid containing historical training points inside a bounding box.
    *   Right Panel: Time series plot showing a query point exceeding the historical threshold, causing the model to output a flat horizontal plateau.
*   **Traceable Industry Case Study:**
    *   *Energy Crisis:* Texas ERCOT Winter Storm Uri (February 2021). Dallas temperatures dropped to -18 °C (a 50-year record). Tabular models trained on 10 years of data predicted a flat peak; actual power demand exceeded predictions by 20 GW, triggering a 4-day grid failure and $195 billion in economic losses.
*   **Academic References:** Grinsztajn, Oyallon, & Varoquaux (*NeurIPS*, 2022); Breiman (2001).

### Slide 8: Paradigma 2 — Deep Learning Secuencial (LSTM vs. PatchTST)

*   **Mathematical Formulations:**
    *   *LSTM Forget Gate:* $f_t = \sigma(W_f [h_{t-1}, x_t] + b_f)$.
    *   *Cell State Update:* $C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$.
    *   *PatchTST Tokenization:* Segmentation into 16-step patches followed by multi-head self-attention projection.
*   **Visual Mechanisms:**
    *   Left Panel: Animated LSTM cell showing cell state highway ($C_{t-1} \to C_t$), opening/closing gate graphics ($f_t, i_t, o_t$), and output hidden state $h_t$.
    *   Right Panel: Continuous time series divided into 16-step blocks mapped into a dynamic multi-head self-attention heat map.
*   **Traceable Industry Case Study:**
    *   *Renewable Energy:* California ISO (CAISO) and Enel Green Power processing 1,000 wind turbines simultaneously via PatchTST to capture spatial-temporal correlations without recursive error accumulation.
*   **Academic References:** Hochreiter & Schmidhuber (1997); Nie, Nguyen, Sinthong, & Kalagnanam (*ICLR*, 2023); Lim et al. (*TFT*, 2021).

### Slide 10: Paradigma 3 — Visión Artificial Local (Drones & Robótica en Cafetales)

*   **Visual Mechanisms:**
    *   Precision Agriculture Drone Heads-Up Display (HUD):
        *   Telemetry Overlay: Altitude: 14.8 m | Ground Speed: 2.1 m/s | Battery: 84% | Coordinates: Jaén -5.6766°.
        *   YOLOv12 Real-Time Bounding Boxes: Red (`[ID: 104] Ripe Cherry: 96.8%`, count: 1,420 fruits/plant), Light Green (`[ID: 105] Unripe Cherry: 89.1%`), Purple (`[ID: 106] Coffee Rust / Hemileia vastatrix: 14.2%`).
        *   SAM 2.1 Polygon Mask: Semitransparent canopy segmentation isolating foliage from soil/shadows (`Canopy Cover: 94.2%`).
*   **Traceable Industry Case Study:**
    *   *Agro-export:* CENFROCAFE Cooperative (Jaén, Cajamarca) and ECOM Agroindustrial deploying multispectral drone flights to estimate yield (quintales per hectare) and physical quality 90 days prior to harvest.
*   **Academic References:** Kirillov et al. (*Meta AI, SAM 2*, 2024); Ramos et al. (*Comput. Electron. Agric.*, 2020).

### Slide 11: Paradigma 3 — Biofísica Satelital & Saturación de Índices

*   **Mathematical & Biophysical Principles:**
    *   *Red Band (665 nm, Sentinel-2 Band 4):* 95% absorbed by chlorophyll $a$ and $b$ for photosynthesis.
    *   *Near-Infrared NIR (842 nm, Sentinel-2 Band 8):* 85% reflected by mesophyll cell-air interfaces to prevent thermal damage.
    *   *Red Edge (690–730 nm, Sentinel-2 Band 5):* Steepest spectral slope.
    *   *Index Saturation:* Normalized Difference Vegetation Index ($\text{NDVI} = \frac{\text{NIR} - \text{Red}}{\text{NIR} + \text{Red}}$) saturates at an asymptote of 0.80 when Leaf Area Index ($\text{LAI}$) exceeds 3. Enhanced Vegetation Index (EVI) and Normalized Difference Red Edge (NDRE) maintain linear response to biomass/nitrogen.
*   **Visual Mechanisms:**
    *   Left Panel: Microscopic leaf histological cross-section (waxy cuticle, palisade parenchyma with chloroplasts, spongy mesophyll).
    *   Right Panel: Spectral reflectance curve (400–2500 nm) showing Red Edge cliff, alongside a plot proving NDVI saturation vs. NDRE/EVI linearity at $\text{LAI} > 3$.
*   **Traceable Industry Case Study:**
    *   *Agricultural Commodities:* Copersucar / Raízen (Brazil, sugarcane) and AgroVisión (Peru, blueberries and coffee). Switching from NDVI to NDRE detected nitrogen deficiencies previously hidden beneath dense mature canopies.
*   **Academic References:** Gates et al. (1965); Huete et al. (*Remote Sens. Environ.*, 2002); Barnes et al. (2000).

### Slide 12: Paradigma 3 — Fusión Multimodal Fenológica (El Reloj Botánico)

*   **Mathematical & Environmental Variables:**
    *   *Three Phenological Stages:* Window 1 Flowering (Aug–Oct) $\to$ Window 2 Grain Filling (Nov–Feb) $\to$ Window 3 Ripening/Harvest (Mar–Jul).
    *   *Meteorological Inputs:* CHIRPS precipitation, Vapor Pressure Deficit (VPD).
    *   *Satellite Inputs:* Sentinel-2 EVI (10m resolution) and NDWI (foliar moisture).
*   **Visual Mechanisms:**
    *   Tri-modular synchronized year-long alignment.
    *   Dynamic Crisis Marker: Precipitation drops below the critical $140\text{ mm}$ threshold during Flowering (vs. $290\text{ mm}$ historical norm), triggering an **Irreversible Floral Abortion** alert. The model freezes yield loss at 18.2 qq/ha despite subsequent heavy rainfall in January.
*   **Traceable Industry Case Study:**
    *   *Coffee Campaign 2024 (Jaén, Cajamarca):* Flowering drought caused a real 24% yield loss. A naive NDVI-only model predicted 24.0 qq/ha (an error of 5.8 qq/ha); the AgroVisión phenological fusion model predicted 18.2 qq/ha against an actual yield of 18.46 qq/ha (an error of only 0.26 qq/ha).
*   **Academic References:** Ramos et al. (2020); Barbosa et al. (*Agronomy*, 2021); Bernardi et al. (*Remote Sens.*, 2023).

### Slide 13: Paradigma 4 — Modelos Físicos Globales & Supercómputo NWP

*   **Mathematical & Physical Dynamics:**
    *   *Fluid Dynamics Equations:* Zonal/meridional advection $(u,v)$, Coriolis force $-2\vec{\Omega} \times \vec{v}$, pressure gradient $-\frac{1}{\rho}\nabla p$, convective moisture plumes $w$.
    *   *Atmospheric Discretization:* 1000 hPa (Surface), 850 hPa (Planetary Boundary Layer / Amazon moisture transport), 500 hPa (Mid-Troposphere / geostrophic vorticity), 250 hPa (Tropopause / Jet Stream).
    *   *4D-Var Data Assimilation:* Ingesting polar-orbiting satellite feeds (MetOp, NOAA-20) and radiosondes every 6 hours.
*   **Visual Mechanisms:**
    *   3D atmospheric pressure grid displaying fluid vector fields and pulsing 4D-Var assimilation cycles.
*   **Traceable Industry Case Study:**
    *   *Maritime Logistics & Aviation:* Maersk and Air France utilizing ECMWF IFS wind field forecasts to route vessels and aircraft along optimal atmospheric currents, cutting CO2 emissions and saving up to 15% in fuel.
*   **Academic References:** Bauer, Thorpe, & Brunet (*Nature*, 2015) *The quiet revolution of numerical weather prediction*.

### Slide 15: Paradigma 4 — GraphCast & Foundation Models Zero-Shot

*   **Architectural & Computational Metrics:**
    *   *Google DeepMind GraphCast:* Icosahedral multi-scale mesh ($M_0$ to $M_6$, 40,962 interconnected vertices). Graph Neural Network (GNN) Encoder $\to$ Processor (16 message-passing blocks) $\to$ Decoder architecture.
    *   *Hardware/Latency Efficiency:* ECMWF IFS running on a European supercomputer (thousands of x86 CPU nodes, 2-hour runtime) vs. GraphCast running on 1 Cloud TPU v4 (complete global inference in 60 seconds, superior on 90% of weather variables).
    *   *Zero-Shot Series Tokenizers:* Google TimesFM and Amazon Chronos (T5 architecture) discretizing continuous sequence values into semantic tokens for zero-shot forecasting.
*   **Visual Mechanisms:**
    *   Left Panel: Interactive globe wrapped in an icosahedral mesh with pulsing GNN message-passing lines and hardware comparison table.
    *   Right Panel: Patch tokenization stream feeding into zero-shot predictive heads.
*   **Traceable Industry Case Study:**
    *   *Early Warning Systems:* Rapid cyclone track forecasting (Hurricane Otis, Acapulco 2023) and Google Flood Hub monitoring riverine basins across 80 countries.
*   **Academic References:** Lam et al. (*Science*, 2023) *GraphCast*; Das et al. (*Google*, 2024) *TimesFM*; Ansari et al. (*Amazon*, 2024) *Chronos*.

### Slide 23: Síntesis — Árbol de Decisión Práctico de Modelado por Sector

```
                         ┌────────────────────────────────────────┐
                         │   1. What is the dataset volume (N)?   │
                         └───────────────────┬────────────────────┘
                                             │
      ┌──────────────────────┬───────────────┴───────────────┬──────────────────────┐
      │ N < 500              │ 10³ ≤ N ≤ 10⁵                 │ N > 10⁵              │ Catalog / Global
┌─────▼───────────────┐ ┌────▼──────────────────┐ ┌──────────▼───────────────┐ ┌────▼──────────────────┐
│ VIA 1: ANALYTICAL   │ │ VIA 2: TABULAR ML     │ │ VIA 3: DEEP LEARNING     │ │ VIA 4: FOUNDATION     │
│ & SMOOTHING         │ │ WITH LAGS             │ │ MULTIVARIABLE            │ │ MODELS (ZERO-SHOT)    │
├─────────────────────┤ ├───────────────────────┤ ├──────────────────────────┤ ├───────────────────────┤
│ • Holt-Winters      │ │ • LightGBM / ExtraTree│ │ • PatchTST / TFT / DeepAR│ │ • Chronos / TimesFM   │
│ • ARIMA / Logistic  │ │ • Lags 1-14 + Rolling │ │ • Cross-series deps.     │ │ • GraphCast           │
├─────────────────────┤ ├───────────────────────┤ ├──────────────────────────┤ ├───────────────────────┤
│ INS Dengue, Small   │ │ Regional Harvest,     │ │ CAISO/COES Power Grids,  │ │ E-commerce Catalogs,  │
│ Retail Restock      │ │ Station Temps         │ │ Wind Turbine Farms       │ │ Global Climate Alerts │
└─────────────────────┘ └───────────────────────┘ └──────────────────────────┘ └───────────────────────┘
```

*   **Academic References:** Makridakis et al. (M4/M5 Competitions); Hyndman (2021); Lim et al. (2021).

---

## Foundation Models in Time Series: Chronos Methodology & Performance Analysis

Amazon's **Chronos** (Ansari et al., 2024) adapts language model architectures directly to probabilistic time series forecasting with minimal structural modifications.

```
┌──────────────────┐    Mean Scaling     ┌──────────────────┐    Uniform Quant.    ┌──────────────────┐
│  Raw Time Series │ ──────────────────> │ Scaled Values    │ ───────────────────> │ Discrete Tokens  │
│  x₁, x₂, ..., x_C│   s = (1/C)∑|x_i|   │ x̃_i = x_i / s    │   q(x̃) ∈ {1..B}    │ z₁, z₂, ..., z_C │
└──────────────────┘                     └──────────────────┘                      └────────┬─────────┘
                                                                                            │
┌──────────────────┐   Dequant. & Unscale ┌──────────────────┐  Cross-Entropy Loss  ┌───────▼──────────┐
│ Probabilistic    │ <────────────────── │ Sampled Tokens   │ <─────────────────── │ T5 / GPT Language│
│ Forecast Paths   │   x_pred = d(z)*s   │ z_{C+1}...z_{C+H}│  p_θ(z_{t+1}|z_{1:t})│ Model Backbone   │
└──────────────────┘                     └──────────────────┘                      └──────────────────┘
```

### 1. Tokenization and Objective Function
*   **Mean Scaling:** Each univariate context window $x_{1:C}$ is scaled by the mean of its absolute values:
    $$s = \frac{1}{C}\sum_{i=1}^C |x_i|, \quad \tilde{x}_i = \frac{x_i}{s}$$
    This scaling preserves exact zero entries (critical for retail sales or night solar generation).
*   **Uniform Quantization:** Continuous real space is mapped into $B$ discrete bins bounded within $[c_1 = -15, c_B = +15]$ with edges $b_i = \frac{c_i + c_{i+1}}{2}$:
    $$q(\tilde{x}) = j \quad \text{if } b_{j-1} \le \tilde{x} < b_j$$
    Special tokens `PAD` and `EOS` are included, yielding a total vocabulary size $|V_{ts}| = 4096$. Time and frequency features (e.g., day-of-week) are intentionally omitted; the time series is treated strictly as an abstract sequence.
*   **Categorical Objective Function:** Chronos performs **regression via classification** by minimizing cross-entropy over discrete tokens:
    $$\ell(\theta) = -\sum_{h=1}^{H+1} \sum_{i=1}^{|V_{ts}|} \mathbf{1}(z_{C+h+1} = i) \log p_\theta(z_{C+h+1} = i \mid z_{1:C+h})$$
*   **Probabilistic Inferences:** Forecast trajectories are generated by autoregressively sampling discrete tokens from $p_\theta$ and applying the dequantization function $d(j) = c_j$ multiplied by scale $s$.

### 2. Synthetic Data Augmentation Strategies
To overcome the scarcity of high-quality time series pretraining data compared to text, Chronos utilizes two augmentation mechanisms:
*   **TSMixup:** Generates convex combinations of $k \sim U\{1, K\}$ ($K=3$) scaled real time series sampled across different training datasets:
    $$\tilde{x}^{\text{TSMixup}}_{1:l} = \sum_{i=1}^k \lambda_i \tilde{x}^{(i)}_{1:l}, \quad [\lambda_1, \dots, \lambda_k] \sim \text{Dir}(\alpha)$$
*   **KernelSynth:** Generates pure synthetic series using Gaussian Processes ($GP(m(t)=0, \tilde{\kappa}(t, t'))$). Kernels are sampled from a bank (Linear, RBF, Periodic) and combined via random binary operators ($+$ or $\times$).

### 3. Empirical Benchmark Results

Chronos models were pretrained on **28 datasets** (~890,000 univariate series, ~84 billion tokens) using 10M TSMixup augmentations and 1M KernelSynth series in a 9:1 ratio for 200,000 steps (AdamW, linear lr decay $0.001 \to 0$).

Evaluation was conducted using:
*   **Weighted Quantile Loss (WQL):** Assessing 9 quantile levels $\{0.1, \dots, 0.9\}$.
*   **Mean Absolute Scaled Error (MASE):** Assessing point forecast accuracy relative to Seasonal Naive.
*   **Aggregation Method:** Geometric mean of relative scores against Seasonal Naive (ensuring baseline independence).

#### Comprehensive Benchmark Metrics Summary Table

| Model | Model Class | Parameters | Benchmark I (In-Domain) Rel. WQL | Benchmark I (In-Domain) Rel. MASE | Benchmark II (Zero-Shot) Rel. WQL | Benchmark II (Zero-Shot) Rel. MASE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Seasonal Naive** | Baseline | 0 | 1.000 | 1.000 | 1.000 | 1.000 |
| **AutoARIMA** | Local Statistical | 0 | 0.876 | 0.864 | 0.838 | 0.895 |
| **AutoETS** | Local Statistical | 0 | 1.083 | 0.871 | 1.000 | 0.951 |
| **SCUM (Ensemble)** | Local Statistical | 0 | 1.076 | 0.861 | 0.757 | 0.843 |
| **DeepAR** | Task-Specific DL | Variable | 0.656 | 0.727 | 0.757 | 0.847 |
| **TFT** | Task-Specific DL | Variable | 0.697 | 0.806 | 0.639 | 0.894 |
| **PatchTST** | Task-Specific DL | Variable | 0.601 | 0.706 | 0.681 | **0.810** |
| **GPT4TS** | Task-Specific DL | ~117M | N/A | 0.857 | N/A | 0.895 |
| **ForecastPFN** | Pretrained (Synthetic) | ~10M | N/A | N/A | N/A | ~1.188 |
| **Lag-Llama** | Pretrained | 2.4M | 1.060 | 1.141 | 1.152 | 1.291 |
| **Moirai-1.0-R (Base)**| Pretrained | 14M | 0.689 | 0.854 | 0.733 | 0.951 |
| **Moirai-1.0-R (Large)**| Pretrained | 311M | 0.603 | 0.741 | 0.684 | 0.852 |
| **Chronos-GPT2** | Pretrained (Decoder) | 90M | 0.664 | 0.740 | 0.687 | 0.850 |
| **Chronos-T5 (Mini)** | Pretrained | 20M | 0.623 | 0.732 | 0.678 | 0.852 |
| **Chronos-T5 (Small)**| Pretrained | 46M | 0.598 | 0.695 | 0.672 | 0.841 |
| **Chronos-T5 (Base)** | Pretrained | 200M | 0.580 | 0.706 | 0.662 | 0.835 |
| **Chronos-T5 (Large)**| Pretrained | 710M | **0.564** | **0.695** | **0.645** | 0.830 |
| **Chronos-T5 (Small) Fine-Tuned** | Fine-Tuned (Task) | 46M | N/A | N/A | **0.597** | **0.760** |

#### Hyperparameter & Architectural Insights
1.  **Model Scaling:** Performance improves monotonically with model capacity (Mini 20M $\to$ Large 710M).
2.  **Language Model Initialization vs. Random Initialization:** Initializing Chronos with pretrained C4 language model weights offers **no significant advantage** over random initialization. Randomly initialized models achieve equal or lower training loss and equal downstream accuracy.
3.  **Synthetic Data Proportion:** A **10% KernelSynth proportion** combined with 90% TSMixup yields optimal zero-shot generalization. Training purely on synthetic data (100%) achieves respectable baseline accuracy (outperforming ForecastPFN), but degrades relative to real data incorporation.
4.  **Trend Handling Limitations:** Chronos accurately models linear trends and complex seasonalities, but **struggles with exponential trends** unless log-scaling is applied prior to tokenization. Furthermore, short context lengths cause Chronos to underpredict steep trends, whereas longer contexts resolve the trend slope accurately.

---

## Important Quotes & Contextual Analysis

### 1. On Visual Fidelity and Industry Traceability
> *"Las animaciones previas del mazo de diapositivas utilizaban primitivas SVG elementales... no reflejaban el mecanismo físico, biológico ni matemático real. Además, la audiencia requiere ver casos de uso de la industria reales, con números, nombres de instituciones y papers científicos trazables."*
> — **Especificación de Diseño (Slide Deck Redesign)**

*   **Contextual Analysis:** This diagnosis highlights a common deficiency in technical presentations: relying on abstract visual placeholders rather than accurate mechanics. In high-stakes enterprise domain discussions, executive and technical audiences demand traceable metrics (e.g., Texas ERCOT losses, CENFROCAFE yield predictions) to ground theoretical concepts in operational reality.

### 2. On the Extrapolation Failure of Tabular Tree Models
> *"Al salir [del convex hull acotado], el algoritmo lo asigna forzosamente a la hoja extrema, proyectando una meseta horizontal plana en la serie temporal ($y = \text{constante}$)... Tormenta invernal Uri llevó la temperatura a -18 °C en Dallas... Modelos tabulares entrenados con 10 años de datos predijeron un tope de demanda plano; la demanda real superó en 20 GW la previsión, provocando un colapso de la red de 4 días y pérdidas de $195 mil millones."*
> — **Especificación de Diseño (Slide 7 Analysis)**

*   **Contextual Analysis:** This quote articulates the structural risk of applying decision trees (e.g., XGBoost, LightGBM) to time series subject to regime shifts. Because tree algorithms split space orthogonally, any query outside historical boundaries is assigned to the nearest leaf node, creating a constant prediction plateau. In critical infrastructure (e.g., ERCOT grid management), this mathematical limitation can result in severe real-world failures.

### 3. On Formulating Time Series as Sequence Language Modeling
> *"In this work, we take a step back and ask: what are the fundamental differences between a language model that predicts the next token, and a time series forecasting model that predicts the next values? ... Shouldn't good language models 'just work' on time series? ... Chronos tokenizes time series into discrete bins through simple scaling and quantization of real values... performing regression via classification."*
> — **Ansari et al. (Chronos Paper, Section 1 & 2)**

*   **Contextual Analysis:** Ansari et al. challenge the assumption that time series require specialized architectural modifications (like continuous distribution heads, lag features, or frequency embeddings). By discretizing scalar values into a fixed token vocabulary, off-the-shelf Transformer architectures can leverage standard cross-entropy loss functions, enabling zero-shot forecasting across diverse domains.

---

## Actionable Insights & Practical Decision Framework

### 1. Production Model Selection Matrix

To select the appropriate forecasting architecture, engineers and technical leads should apply a decision pipeline based on dataset volume, computational constraints, and extrapolation requirements:

*   **Scenario A: Low Data ($N < 500$ series) or High Regulatory Interpretability Requirements**
    *   *Recommended Model:* Parametric Curves (Verhulst Sigmoid) or Classical Smoothing (Holt-Winters, AutoARIMA).
    *   *Primary Rationale:* Bounded mathematical structures prevent overfitting and unconstrained growth estimates (e.g., INS Dengue bed capacity planning).
*   **Scenario B: Medium Tabular Data ($10^3 \le N \le 10^5$ series) within Bounded Historical Regimes**
    *   *Recommended Model:* LightGBM / ExtraTrees with Lag Features ($1\dots 14, 1\dots 28$) and Rolling Window Statistics.
    *   *Primary Rationale:* Offers high tabular accuracy and low training latency (e.g., M5 Retail competition benchmarks).
    *   *Critical Warning:* **Do not deploy** standalone tree models if the target system is subject to unprecedented extreme events (e.g., climate anomalies, price spikes) without hybrid trend-decoupling mechanisms.
*   **Scenario C: High-Volume Complex Multivariable Systems ($N > 10^5$ series)**
    *   *Recommended Model:* PatchTST or Temporal Fusion Transformer (TFT).
    *   *Primary Rationale:* Multi-head self-attention across 16-step patches captures complex spatiotemporal interdependencies across thousands of sensors (e.g., CAISO wind farms) without recursive error accumulation.
*   **Scenario D: Cold-Start / Zero-Shot / Large E-Commerce Catalogs**
    *   *Recommended Model:* Pretrained Foundation Models (**Chronos-T5 Large** or **TimesFM**).
    *   *Primary Rationale:* Delivers top-tier zero-shot probabilistic forecasts out of the box without requiring dataset-specific retraining.
    *   *Optimization Step:* Fine-tuning a small Chronos variant (e.g., Chronos-T5 Small) for just 1,000 steps on domain data yields superior performance compared to training complex task-specific models from scratch.

### 2. Implementation & Deployment Guidelines

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        FOUNDATION MODEL FORECASTING PIPELINE                           │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
     ┌──────────────────────────────────────┼──────────────────────────────────────┐
     │                                      │                                      │
┌────▼─────────────────────────────┐ ┌──────▼──────────────────────────────┐ ┌─────▼──────────────────────────────┐
│  PRE-PROCESSING                  │ │  INFERENCE                          │ │  POST-PROCESSING                    │
├──────────────────────────────────┤ ├─────────────────────────────────────┤ ├─────────────────────────────────────┤
│ 1. Apply log-transforms to       │ │ 1. Use context lengths ≥ 512 tokens │ │ 1. Sample 20+ autoregressive paths  │
│    exponentially growing series. │ │    to capture long-range trends.    │ │    to reconstruct quantiles.          │
│ 2. Apply mean scaling to preserve│ │ 2. Deploy Chronos-T5 Base/Large for │ │ 2. Dequantize ($d(j)=c_j$) and      │
│    exact zero-value semantics.   │ │    zero-shot baseline forecasts.    │ │    unscale by factor $s$.             │
│ 3. Quantize continuous values    │ │ 3. Fine-tune Chronos-T5 Small (~46M)│ │ 3. Verify residual variance against │
│    into uniform bins ($B=4096$). │ │    for 1k steps to minimize latency.│ │    physical system limits ($\pm 2.5\sigma$).│
└──────────────────────────────────┘ └─────────────────────────────────────┘ └─────────────────────────────────────┘
```

1.  **Pre-processing Data Transformations:**
    *   Always apply logarithmic scaling ($y \to \log(y)$) prior to tokenization if the input time series exhibits exponential growth dynamics.
    *   Utilize **mean scaling** ($s = \frac{1}{C}\sum |x_i|$) rather than standard min-max scaling to preserve exact zero-value semantics.
2.  **Context Window Allocation:**
    *   Maintain context lengths of **at least 512 tokens** during foundation model inference. Short context windows degrade slope/trend estimations in sequence models like Chronos.
3.  **Foundation Model Training & Fine-Tuning Strategy:**
    *   When pretraining time-series language models from scratch, **avoid initializing with pretrained NLP text weights**; random initialization converges faster and yields equivalent or better downstream accuracy.
    *   Incorporate a **10% synthetic Gaussian Process dataset** (generated via composed linear, periodic, and smooth kernels) alongside real-data Mixup augmentations to optimize zero-shot generalization across unseen domains.