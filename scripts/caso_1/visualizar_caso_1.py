"""
Generador de visualizaciones y análisis gráfico para Caso 1 (Clima Punchana - SENAMHI).
Genera figuras estáticas de alta resolución (300 DPI) en docs/images/caso_1/ con diseño
editorial profesional sin superposiciones, leyendas desacopladas y takeaways visuales claros.
"""

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import pandas as pd
import numpy as np

OUTPUT_DIR = Path("docs/images/caso_1")
DATA_DIR = Path("data/caso_1")

plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Helvetica", "Arial"]
plt.rcParams["axes.edgecolor"] = "#cbd5e1"
plt.rcParams["axes.linewidth"] = 0.8

def plot_serie_punchana():
    df = pd.read_csv(DATA_DIR / "senamhi_diario.csv", parse_dates=["fecha"])
    recent = df.tail(365).copy()

    # Limpiar valores centinela de precipitación (-999.0 en datos brutos SENAMHI)
    recent.loc[recent["precip"] < 0, "precip"] = np.nan
    recent["precip_clean"] = recent["precip"].fillna(0)

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(12, 6.8), dpi=300, sharex=True,
        gridspec_kw={"height_ratios": [2.2, 1.0], "hspace": 0.12}
    )
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    # Subplot 1: Dinámica Térmica
    ax1.plot(recent["fecha"], recent["tmax"], color="#f87171", label="Tmax Diaria (°C)", linewidth=1.1, alpha=0.75)
    ax1.plot(recent["fecha"], recent["tmax"].rolling(14, min_periods=3).mean(), color="#dc2626", label="Media Móvil Tmax 14d", linewidth=2.2)
    if "tmin" in recent.columns:
        ax1.plot(recent["fecha"], recent["tmin"].rolling(14, min_periods=3).mean(), color="#0284c7", linestyle="--", label="Media Móvil Tmin 14d", linewidth=1.6)

    # Identificar y anotar evento de friaje extremo (mínimo histórico reciente en Tmax)
    friaje_idx = recent["tmax"].idxmin()
    friaje_row = recent.loc[friaje_idx]
    ax1.annotate(
        f"Evento de Friaje Polar Amazónico\nTmax cae a {friaje_row['tmax']:.1f}°C ({friaje_row['fecha'].strftime('%d-%b-%Y')})",
        xy=(friaje_row["fecha"], friaje_row["tmax"]),
        xytext=(friaje_row["fecha"] + pd.Timedelta(days=22), friaje_row["tmax"] + 3.2),
        arrowprops=dict(arrowstyle="->", color="#991b1b", lw=1.8),
        fontsize=9, fontweight="bold", color="#7f1d1d",
        bbox=dict(boxstyle="round,pad=0.35", fc="#fee2e2", ec="#ef4444", alpha=0.95)
    )

    ax1.set_ylabel("Temperatura (°C)", fontsize=10.5, fontweight="bold")
    ax1.set_ylim(19.0, 38.5)
    ax1.set_title(
        "Estación SENAMHI Punchana (Iquitos) — Serie Diaria Reciente y Dinámica Térmica\n"
        "Comportamiento de alta variabilidad convectiva y caída de hasta 12 °C durante incursiones de aire frío (friajes)",
        fontsize=11.5, fontweight="bold", pad=12
    )
    ax1.legend(loc="upper right", frameon=True, fontsize=8.5, framealpha=0.95)
    ax1.grid(True, linestyle="--", alpha=0.5)

    # Subplot 2: Precipitación Diaria Limpia
    ax2.bar(recent["fecha"], recent["precip_clean"], color="#3b82f6", width=1.1, alpha=0.7, label="Lluvia Diaria (mm)")
    ax2.set_ylabel("Precipitación (mm)", fontsize=10.5, fontweight="bold", color="#1d4ed8")
    ax2.set_xlabel("Fecha", fontsize=10.5, fontweight="bold")
    ax2.set_ylim(0, max(recent["precip_clean"].max() * 1.25, 60))
    ax2.legend(loc="upper right", frameon=True, fontsize=8.5, framealpha=0.95)
    ax2.grid(True, linestyle="--", alpha=0.5)

    out_path = OUTPUT_DIR / "serie_punchana.png"
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[OK] Generado: {out_path}")

def plot_benchmark_modelos():
    df_bm = pd.read_csv(DATA_DIR / "benchmark_punchana.csv")
    df_bm = df_bm.sort_values("rmse_1d", ascending=False).reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(12, 8.8), dpi=300)
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    colors = []
    for _, row in df_bm.iterrows():
        fam = row["familia"]
        p = row["p_valor_vs_mejor"]
        if "Física Global" in fam:
            colors.append("#8b5cf6")  # Púrpura para ECMWF y GFS
        elif p == 1.0:
            colors.append("#059669")  # Esmeralda para el líder
        elif p >= 0.05:
            colors.append("#10b981")  # Verde para empates estadísticos
        elif "Baseline" in fam:
            colors.append("#ef4444")  # Rojo para baselines
        else:
            colors.append("#f59e0b")  # Ámbar para estadísticamente inferiores

    bars = ax.barh(df_bm["modelo"], df_bm["rmse_1d"], color=colors, height=0.64, edgecolor="#1e293b", linewidth=0.8)

    max_val = max(df_bm["rmse_1d"])
    for bar, val, p, fam in zip(bars, df_bm["rmse_1d"], df_bm["p_valor_vs_mejor"], df_bm["familia"]):
        if p == 1.0:
            tag = " (Líder Ref. DM)"
        elif "Física Global" in fam:
            tag = f" [Supercómputo, p={p:.3f}]"
        elif p >= 0.05:
            tag = f" [Empate est., p={p:.2f}]"
        else:
            tag = f" [p={p:.3f} inf.]"
        ax.text(val + 0.04, bar.get_y() + bar.get_height() / 2, f"{val:.2f}°C{tag}", va="center", fontsize=8.8, fontweight="bold", color="#0f172a")

    # Línea vertical punteada en el benchmark del ganador
    ax.axvline(1.88, color="#059669", linestyle="--", linewidth=1.4, alpha=0.85)

    ax.set_xlabel("RMSE a 1 Día (°C) en Holdout Ciego de 90 Días — Menor es mejor", fontsize=11, fontweight="bold", labelpad=8)
    ax.set_title(
        "Caso 1: Benchmark de 14 Modelos en Estación SENAMHI Punchana (Iquitos)\n"
        "ExtraTrees y TimesFM lideran (1.88 °C); ECMWF (~9km) y NOAA (~28km) degradan a 2.46 °C y 2.58 °C",
        fontsize=12, fontweight="bold", pad=12
    )
    ax.set_xlim(0, 4.3)
    ax.grid(axis="x", linestyle="--", alpha=0.5)

    # LEYENDA EN ESPACIO VACÍO SUPERIOR DERECHO (CERO SUPERPOSICIÓN)
    legend_elements = [
        Patch(facecolor="#059669", edgecolor="#1e293b", label="Líder Empírico (ExtraTrees)"),
        Patch(facecolor="#10b981", edgecolor="#1e293b", label="Empate Estadístico DM (p ≥ 0.05)"),
        Patch(facecolor="#8b5cf6", edgecolor="#1e293b", label="Física Global (ECMWF 9km / NOAA 28km)"),
        Patch(facecolor="#f59e0b", edgecolor="#1e293b", label="Estadísticamente Inferior (p < 0.05)"),
        Patch(facecolor="#ef4444", edgecolor="#1e293b", label="Baseline Univariado Clásico"),
    ]
    ax.legend(handles=legend_elements, loc="upper right", bbox_to_anchor=(0.98, 0.88), frameon=True, fontsize=8.8, framealpha=0.95)

    out_path = OUTPUT_DIR / "benchmark_modelos.png"
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[OK] Generado: {out_path}")

def plot_forecast_7d_cono():
    df_fc = pd.read_csv(DATA_DIR / "senamhi_forecast_7d.csv")
    x = list(range(1, len(df_fc) + 1))

    fig, ax = plt.subplots(figsize=(11.5, 6.4), dpi=300)
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    # Banda de incertidumbre empírica P10-P90
    ax.fill_between(x, df_fc["ci_lower_p10"], df_fc["ci_upper_p90"], color="#38bdf8", alpha=0.22, label="Banda P10–P90 (Incertidumbre ExtraTrees)")

    # Observado Real
    ax.plot(x, df_fc["tmax_observada"], "*-", color="#0f172a", linewidth=3.2, markersize=12, label="Observado Real (SENAMHI Punchana)")

    # Modelos locales y Zero-shot
    ax.plot(x, df_fc["pred_extratrees"], "o-", color="#0284c7", linewidth=2.4, markersize=7, label="ExtraTrees Local P50 (Ganador)")
    ax.plot(x, df_fc["pred_timesfm"], "s--", color="#6366f1", linewidth=2.0, markersize=6, label="TimesFM 2.5 Zero-Shot (Google)")

    # Modelos de Física Global
    if "pred_ecmwf" in df_fc.columns:
        ax.plot(x, df_fc["pred_ecmwf"], "^-.", color="#8b5cf6", linewidth=1.8, markersize=6, label="ECMWF IFS (Europa ~9 km)")
    if "pred_noaa_gfs" in df_fc.columns:
        ax.plot(x, df_fc["pred_noaa_gfs"], "d:", color="#f97316", linewidth=1.8, markersize=6, label="NOAA GFS (EE.UU. ~28 km)")

    # Anotaciones descriptivas de takeaways clave
    ax.annotate(
        "Falsa alarma de friaje en física global\nECMWF cae a 24.8°C y NOAA a 22.8°C (no ocurrida)",
        xy=(5, 22.8), xytext=(3.3, 23.5),
        arrowprops=dict(arrowstyle="->", color="#c2410c", lw=1.6),
        fontsize=8.5, fontweight="bold", color="#9a3412",
        bbox=dict(boxstyle="round,pad=0.3", fc="#ffedd5", ec="#f97316", alpha=0.95)
    )

    ax.annotate(
        "Divergencia entre modelos\nalcanza 6.2°C en D+7",
        xy=(7, 34.7), xytext=(5.7, 37.2),
        arrowprops=dict(arrowstyle="->", color="#4338ca", lw=1.6),
        fontsize=8.5, fontweight="bold", color="#3730a3",
        bbox=dict(boxstyle="round,pad=0.3", fc="#e0e7ff", ec="#6366f1", alpha=0.95)
    )

    ax.set_xticks(x)
    ax.set_xticklabels([f"D+{i}\n{f}" for i, f in zip(x, df_fc["fecha"])], fontsize=9.5, fontweight="bold")
    ax.set_ylabel("Temperatura Máxima (°C)", fontsize=11, fontweight="bold")
    ax.set_ylim(21.5, 39.5)
    ax.set_title(
        "Caso 1: Pronóstico Operativo Multi-Modelo a 7 Días y Cono de Incertidumbre\n"
        "Banda P10–P90 cubre 5 de 7 días (71.4%); los friajes del 28 y 30 dic caen fuera; divergencia inter-agencias de hasta 7.2 °C",
        fontsize=12, fontweight="bold", pad=12
    )

    # Leyenda exterior inferior
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), frameon=True, fontsize=9, ncol=3, framealpha=0.95)
    ax.grid(True, linestyle="--", alpha=0.5)

    out_path = OUTPUT_DIR / "forecast_7d_cono.png"
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[OK] Generado: {out_path}")

def plot_fisica_vs_senamhi():
    p_global = DATA_DIR / "noaa_ecmwf_forecast.csv"
    p_senamhi = DATA_DIR / "senamhi_diario.csv"
    if not p_global.exists() or not p_senamhi.exists():
        print(f"[WARN] No se encontró {p_global} o {p_senamhi}, omitiendo.")
        return

    df_g = pd.read_csv(p_global, parse_dates=["fecha"])
    df_s = pd.read_csv(p_senamhi, parse_dates=["fecha"])
    df_merged = pd.merge(df_g, df_s[["fecha", "tmax"]], on="fecha", how="inner").rename(columns={"tmax": "tmax_senamhi"})

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(11.5, 7.8), dpi=300, sharex=True,
        gridspec_kw={"height_ratios": [1.4, 1.0], "hspace": 0.12}
    )
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    # Subplot 1: Series temporales
    ax1.plot(df_merged["fecha"], df_merged["tmax_senamhi"], color="#0f172a", label="SENAMHI Punchana (Sensores de Superficie)", linewidth=2.0)
    ax1.plot(df_merged["fecha"], df_merged["tmax_ecmwf"], color="#8b5cf6", linestyle="--", label="ECMWF IFS (~9 km Europa)", linewidth=1.5, alpha=0.9)
    ax1.plot(df_merged["fecha"], df_merged["tmax_noaa_gfs"], color="#f97316", linestyle=":", label="NOAA GFS (~28 km EE.UU.)", linewidth=1.5, alpha=0.9)
    ax1.set_ylabel("Tmax (°C)", fontsize=10.5, fontweight="bold")
    ax1.set_title(
        "Supercómputo Global de Pronóstico Numérico (NWP) vs Observación Real en Tierra (Holdout 92 días)\n"
        "Discrepancia promedio entre NOAA y ECMWF: 2.58 °C (máximo de 7.20 °C en la misma estación)",
        fontsize=11.5, fontweight="bold", pad=12
    )
    ax1.legend(loc="upper right", frameon=True, fontsize=8.5, framealpha=0.95)
    ax1.grid(True, linestyle="--", alpha=0.5)

    # Subplot 2: Residuales
    err_ecmwf = df_merged["tmax_ecmwf"] - df_merged["tmax_senamhi"]
    err_gfs = df_merged["tmax_noaa_gfs"] - df_merged["tmax_senamhi"]
    mae_ecmwf = err_ecmwf.abs().mean()
    rmse_ecmwf = np.sqrt((err_ecmwf**2).mean())
    mae_gfs = err_gfs.abs().mean()
    rmse_gfs = np.sqrt((err_gfs**2).mean())

    ax2.axhline(0, color="#475569", linestyle="-", linewidth=1.2)
    ax2.plot(df_merged["fecha"], err_ecmwf, color="#8b5cf6", label=f"Sesgo ECMWF IFS (MAE = {mae_ecmwf:.2f}°C, RMSE = {rmse_ecmwf:.2f}°C)", linewidth=1.4)
    ax2.plot(df_merged["fecha"], err_gfs, color="#f97316", label=f"Sesgo NOAA GFS (MAE = {mae_gfs:.2f}°C, RMSE = {rmse_gfs:.2f}°C)", linewidth=1.4)
    ax2.fill_between(df_merged["fecha"], err_ecmwf, 0, color="#8b5cf6", alpha=0.10)
    ax2.set_ylabel("Error Residual (°C)", fontsize=10.5, fontweight="bold")
    ax2.set_xlabel("Fecha", fontsize=10.5, fontweight="bold")
    ax2.legend(loc="upper right", frameon=True, fontsize=8.5, framealpha=0.95)
    ax2.grid(True, linestyle="--", alpha=0.5)

    out_path = OUTPUT_DIR / "fisica_global_vs_senamhi.png"
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[OK] Generado: {out_path}")

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"=== Generando visualizaciones del Caso 1 en {OUTPUT_DIR} ===")
    plot_serie_punchana()
    plot_benchmark_modelos()
    plot_forecast_7d_cono()
    plot_fisica_vs_senamhi()
    print("=== Visualizaciones del Caso 1 completadas con éxito ===")

if __name__ == "__main__":
    main()
