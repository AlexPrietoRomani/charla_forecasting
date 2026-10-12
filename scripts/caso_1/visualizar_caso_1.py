"""
Generador de visualizaciones y análisis gráfico para Caso 1 (Clima Punchana - SENAMHI).
Genera figuras estáticas de alta resolución (300 DPI) en images/caso_1/ para informes,
publicaciones o respaldo offline de la charla.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

OUTPUT_DIR = Path("docs/images/caso_1")
DATA_DIR = Path("data/caso_1")

def plot_serie_punchana():
    df = pd.read_csv(DATA_DIR / "senamhi_diario.csv", parse_dates=["fecha"])
    recent = df.tail(365).copy()

    fig, ax1 = plt.subplots(figsize=(12, 5), dpi=300)
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    ax1.plot(recent["fecha"], recent["tmax"], color="#ef4444", label="Tmax Diaria (°C)", linewidth=1.2, alpha=0.9)
    ax1.plot(recent["fecha"], recent["tmax"].rolling(14).mean(), color="#991b1b", label="Media Móvil 14d", linewidth=2.0)
    ax1.set_ylabel("Temperatura Máxima (°C)", color="#ef4444", fontsize=11, fontweight="bold")
    ax1.set_title("Estación SENAMHI Punchana (Iquitos) — Serie Diaria Reciente y Dinámica Térmica", fontsize=13, fontweight="bold", pad=12)
    ax1.grid(True, linestyle="--", alpha=0.5)

    ax2 = ax1.twinx()
    ax2.bar(recent["fecha"], recent["precip"], color="#3b82f6", alpha=0.35, width=1.0, label="Precipitación (mm)")
    ax2.set_ylabel("Lluvia Diaria (mm)", color="#3b82f6", fontsize=11, fontweight="bold")
    ax2.grid(False)

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right", frameon=True)

    fig.tight_layout()
    out_path = OUTPUT_DIR / "serie_punchana.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Generado: {out_path}")

def plot_benchmark_modelos():
    df_bm = pd.read_csv(DATA_DIR / "benchmark_punchana.csv")
    df_bm = df_bm.sort_values("rmse_1d", ascending=False).reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(11, 7.5), dpi=300)
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    colors = []
    for _, row in df_bm.iterrows():
        fam = row["familia"]
        p = row["p_valor_vs_mejor"]
        if "Física Global" in fam:
            colors.append("#8b5cf6")  # Púrpura para ECMWF y GFS
        elif p == 1.0:
            colors.append("#059669")  # Esmeralda para el líder
        elif p > 0.05:
            colors.append("#10b981")  # Verde para empates estadísticos
        elif "Baseline" in fam:
            colors.append("#ef4444")  # Rojo para baselines
        else:
            colors.append("#f59e0b")  # Ámbar para estadísticamente inferiores

    bars = ax.barh(df_bm["modelo"], df_bm["rmse_1d"], color=colors, height=0.65, edgecolor="#1e293b", linewidth=0.8)

    for bar, val, p, fam in zip(bars, df_bm["rmse_1d"], df_bm["p_valor_vs_mejor"], df_bm["familia"]):
        if p == 1.0:
            tag = " (Líder)"
        elif "Física Global" in fam:
            tag = f" [Física Global, p={p:.3f}]"
        elif p > 0.05:
            tag = f" [Empate p={p:.2f}]"
        else:
            tag = f" [p={p:.3f} inf.]"
        ax.text(val + 0.03, bar.get_y() + bar.get_height() / 2, f"{val:.2f}°C{tag}", va="center", fontsize=8.5, fontweight="bold", color="#1e293b")

    ax.set_xlabel("RMSE a 1 Día (°C) en Holdout Ciego de 90 Días (Menor es mejor)", fontsize=11, fontweight="bold")
    ax.set_title("Benchmark de 14 Modelos en Punchana (Iquitos) — Físicos Globales vs Estadísticos vs ML vs Zero-Shot", fontsize=12.5, fontweight="bold", pad=12)
    ax.set_xlim(0, max(df_bm["rmse_1d"]) * 1.35)
    ax.grid(axis="x", linestyle="--", alpha=0.5)

    # Leyenda personalizada
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#059669", edgecolor="#1e293b", label="Líder Empírico"),
        Patch(facecolor="#10b981", edgecolor="#1e293b", label="Empate Estadístico Diebold-Mariano (p > 0.05)"),
        Patch(facecolor="#8b5cf6", edgecolor="#1e293b", label="Física Global Supercómputo (ECMWF / NOAA)"),
        Patch(facecolor="#f59e0b", edgecolor="#1e293b", label="Estadísticamente Inferior (p < 0.05)"),
        Patch(facecolor="#ef4444", edgecolor="#1e293b", label="Baseline Clásico"),
    ]
    ax.legend(handles=legend_elements, loc="lower right", frameon=True, fontsize=8.5)

    fig.tight_layout()
    out_path = OUTPUT_DIR / "benchmark_modelos.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Generado: {out_path}")

def plot_forecast_7d_cono():
    df_fc = pd.read_csv(DATA_DIR / "senamhi_forecast_7d.csv")
    x = range(1, len(df_fc) + 1)

    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    # Banda de incertidumbre
    ax.fill_between(x, df_fc["ci_lower_p10"], df_fc["ci_upper_p90"], color="#38bdf8", alpha=0.22, label="Banda P10–P90 (Incertidumbre ExtraTrees)")
    
    # Observado Real
    ax.plot(x, df_fc["tmax_observada"], "*-", color="#0f172a", linewidth=2.8, markersize=10, label="Observado Real (SENAMHI Punchana)")
    
    # Modelos locales y Zero-shot
    ax.plot(x, df_fc["pred_extratrees"], "o-", color="#0284c7", linewidth=2.2, label="ExtraTrees Local (P50)")
    ax.plot(x, df_fc["pred_timesfm"], "s--", color="#6366f1", linewidth=1.8, label="TimesFM 2.5 Zero-Shot")
    
    # Modelos de Física Global
    if "pred_ecmwf" in df_fc.columns:
        ax.plot(x, df_fc["pred_ecmwf"], "^-.", color="#8b5cf6", linewidth=1.8, label="ECMWF IFS (Europa 9km)")
    if "pred_noaa_gfs" in df_fc.columns:
        ax.plot(x, df_fc["pred_noaa_gfs"], "d:", color="#f97316", linewidth=1.8, label="NOAA GFS (EE.UU. 28km)")

    ax.set_xticks(x)
    ax.set_xticklabels([f"D+{i}\n{f}" for i, f in zip(x, df_fc["fecha"])], fontsize=9)
    ax.set_ylabel("Temperatura Máxima (°C)", fontsize=11, fontweight="bold")
    ax.set_title("Caso 1: Pronóstico Operativo a 7 Días — Sensores SENAMHI vs Física Global vs ML Local", fontsize=12.5, fontweight="bold", pad=12)
    ax.legend(loc="lower left", frameon=True, fontsize=8.5, ncol=2)
    ax.grid(True, linestyle="--", alpha=0.5)

    fig.tight_layout()
    out_path = OUTPUT_DIR / "forecast_7d_cono.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Generado: {out_path}")

def plot_fisica_vs_senamhi():
    p_global = DATA_DIR / "noaa_ecmwf_forecast.csv"
    p_senamhi = DATA_DIR / "senamhi_diario.csv"
    if not p_global.exists() or not p_senamhi.exists():
        print(f"[WARN] No se encontró {p_global} o {p_senamhi}, omitiendo gráfico físico vs senamhi.")
        return

    df_g = pd.read_csv(p_global, parse_dates=["fecha"])
    df_s = pd.read_csv(p_senamhi, parse_dates=["fecha"])
    df_merged = pd.merge(df_g, df_s[["fecha", "tmax"]], on="fecha", how="inner").rename(columns={"tmax": "tmax_senamhi"})

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7), dpi=300, sharex=True)
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    # Subplot 1: Series temporales del holdout
    ax1.plot(df_merged["fecha"], df_merged["tmax_senamhi"], color="#0f172a", label="SENAMHI Punchana (Observado en Tierra)", linewidth=1.8)
    ax1.plot(df_merged["fecha"], df_merged["tmax_ecmwf"], color="#8b5cf6", linestyle="--", label="ECMWF IFS (~9 km Europa)", linewidth=1.4, alpha=0.9)
    ax1.plot(df_merged["fecha"], df_merged["tmax_noaa_gfs"], color="#f97316", linestyle=":", label="NOAA GFS (~28 km EE.UU.)", linewidth=1.4, alpha=0.9)
    ax1.set_ylabel("Tmax Diaria (°C)", fontsize=10, fontweight="bold")
    ax1.set_title("Confrontación de la Física Global de Supercómputo vs Sensores SENAMHI en Punchana (Holdout 92 días)", fontsize=11.5, fontweight="bold")
    ax1.legend(loc="upper right", frameon=True, fontsize=8.5)
    ax1.grid(True, linestyle="--", alpha=0.5)

    # Subplot 2: Error diario (Física - Observado)
    err_ecmwf = df_merged["tmax_ecmwf"] - df_merged["tmax_senamhi"]
    err_gfs = df_merged["tmax_noaa_gfs"] - df_merged["tmax_senamhi"]
    ax2.axhline(0, color="#64748b", linestyle="-", linewidth=1.0)
    ax2.plot(df_merged["fecha"], err_ecmwf, color="#8b5cf6", label=f"Sesgo ECMWF IFS (MAE = {err_ecmwf.abs().mean():.2f}°C, RMSE = {np.sqrt((err_ecmwf**2).mean()):.2f}°C)", linewidth=1.3)
    ax2.plot(df_merged["fecha"], err_gfs, color="#f97316", label=f"Sesgo NOAA GFS (MAE = {err_gfs.abs().mean():.2f}°C, RMSE = {np.sqrt((err_gfs**2).mean()):.2f}°C)", linewidth=1.3)
    ax2.fill_between(df_merged["fecha"], err_ecmwf, 0, color="#8b5cf6", alpha=0.1)
    ax2.set_ylabel("Error Residual (°C)", fontsize=10, fontweight="bold")
    ax2.set_xlabel("Fecha", fontsize=10, fontweight="bold")
    ax2.legend(loc="upper right", frameon=True, fontsize=8.5)
    ax2.grid(True, linestyle="--", alpha=0.5)

    fig.tight_layout()
    out_path = OUTPUT_DIR / "fisica_global_vs_senamhi.png"
    plt.savefig(out_path, dpi=300)
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
