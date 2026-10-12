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
    df_bm = df_bm.sort_values("rmse_1d", ascending=True).reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    colors = ["#10b981" if p > 0.05 else "#f59e0b" if p == 1.0 else "#ef4444" for p in df_bm["p_valor_vs_mejor"]]
    bars = ax.barh(df_bm["modelo"], df_bm["rmse_1d"], color=colors, height=0.6, edgecolor="#334155")

    for bar, val, p in zip(bars, df_bm["rmse_1d"], df_bm["p_valor_vs_mejor"]):
        tag = " (Líder)" if p == 1.0 else " (Empate p>0.05)" if p > 0.05 else " (p<0.05 inf.)"
        ax.text(val + 0.02, bar.get_y() + bar.get_height() / 2, f"{val:.2f}°C{tag}", va="center", fontsize=9, fontweight="bold")

    ax.set_xlabel("RMSE a 1 Día (°C) en Holdout Ciego de 90 Días", fontsize=11, fontweight="bold")
    ax.set_title("Benchmark de 8 Modelos — Regla de Parsimonia y Significancia Diebold-Mariano", fontsize=13, fontweight="bold", pad=12)
    ax.set_xlim(0, max(df_bm["rmse_1d"]) * 1.25)
    ax.grid(axis="x", linestyle="--", alpha=0.5)

    fig.tight_layout()
    out_path = OUTPUT_DIR / "benchmark_modelos.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Generado: {out_path}")

def plot_forecast_7d_cono():
    df_fc = pd.read_csv(DATA_DIR / "senamhi_forecast_7d.csv")
    x = range(1, len(df_fc) + 1)

    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    ax.fill_between(x, df_fc["ci_lower_p10"], df_fc["ci_upper_p90"], color="#38bdf8", alpha=0.25, label="Banda P10–P90 (ExtraTrees)")
    ax.plot(x, df_fc["pred_extratrees"], "o-", color="#0284c7", linewidth=2.5, label="Pronóstico ExtraTrees (P50)")
    ax.plot(x, df_fc["pred_timesfm"], "s--", color="#8b5cf6", linewidth=2, label="TimesFM 2.5 Zero-Shot")
    ax.plot(x, df_fc["tmax_observada"], "*-", color="#111827", linewidth=2.5, label="Observado Real (SENAMHI)")

    ax.set_xticks(x)
    ax.set_xticklabels([f"D+{i}\n{f}" for i, f in zip(x, df_fc["fecha"])], fontsize=9)
    ax.set_ylabel("Temperatura Máxima (°C)", fontsize=11, fontweight="bold")
    ax.set_title("Caso 1: Pronóstico Operativo a 7 Días y Cono de Incertidumbre", fontsize=13, fontweight="bold", pad=12)
    ax.legend(loc="upper right", frameon=True)
    ax.grid(True, linestyle="--", alpha=0.5)

    fig.tight_layout()
    out_path = OUTPUT_DIR / "forecast_7d_cono.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Generado: {out_path}")

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"=== Generando visualizaciones del Caso 1 en {OUTPUT_DIR} ===")
    plot_serie_punchana()
    plot_benchmark_modelos()
    plot_forecast_7d_cono()
    print("=== Visualizaciones del Caso 1 completadas con éxito ===")

if __name__ == "__main__":
    main()
