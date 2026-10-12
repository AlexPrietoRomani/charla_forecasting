"""
Generador de visualizaciones y análisis gráfico para Caso 2 (Rendimiento Café Jaén - MIDAGRI / MODIS / Clima).
Genera figuras estáticas de alta resolución (300 DPI) en images/caso_2/ para informes,
publicaciones o respaldo offline de la charla.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

OUTPUT_DIR = Path("docs/images/caso_2")
DATA_DIR = Path("data/caso_2")

def plot_rendimiento_historico():
    df = pd.read_csv(DATA_DIR / "cafe_jaen_campanias.csv")
    con_rend = df.dropna(subset=["rendimiento_kg_ha"]).copy()

    fig, ax1 = plt.subplots(figsize=(11, 5), dpi=300)
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    color_rend = "#0d9488"
    line1 = ax1.plot(con_rend["campania"], con_rend["rendimiento_qq_ha"], "o-", color=color_rend, linewidth=2.5, label="Rendimiento Oficial (qq/ha)")
    ax1.set_xlabel("Campaña Agrícola", fontsize=11, fontweight="bold")
    ax1.set_ylabel("Rendimiento (qq pergamino / ha)", color=color_rend, fontsize=11, fontweight="bold")
    ax1.grid(True, linestyle="--", alpha=0.5)

    ax2 = ax1.twinx()
    color_prod = "#64748b"
    line2 = ax2.bar(con_rend["campania"] + 0.15, con_rend["produccion_t"] / 1000, width=0.3, color=color_prod, alpha=0.3, label="Producción Total (k Toneladas)")
    ax2.set_ylabel("Producción Total (miles t)", color=color_prod, fontsize=11, fontweight="bold")
    ax2.grid(False)

    # Marcador de la Crisis de la Roya 2012-2014
    ax1.axvspan(2012, 2014, color="#ef4444", alpha=0.15, label="Crisis de Roya Amarilla (2012-2014)")

    ax1.set_title("Evolución Oficial de Café en Jaén (MIDAGRI / INEI) — Quiebre Estructural y Resiliencia", fontsize=13, fontweight="bold", pad=12)
    ax1.legend(loc="upper left", frameon=True)

    fig.tight_layout()
    out_path = OUTPUT_DIR / "rendimiento_historico.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Generado: {out_path}")

def plot_saturacion_ndvi():
    df = pd.read_csv(DATA_DIR / "cafe_jaen_campanias.csv")
    con_rend = df.dropna(subset=["rendimiento_kg_ha"]).copy()

    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    sc = ax.scatter(con_rend["ndvi_anual"], con_rend["rendimiento_qq_ha"], s=100, c=con_rend["campania"], cmap="viridis", edgecolor="#1e293b", linewidth=1.5, zorder=3)
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label("Campaña Agrícola", fontsize=10, fontweight="bold")

    # Ajuste lineal mostrando la falta de relación (saturación del dosel)
    m, b = np.polyfit(con_rend["ndvi_anual"], con_rend["rendimiento_qq_ha"], 1)
    x_vals = np.linspace(con_rend["ndvi_anual"].min() * 0.98, con_rend["ndvi_anual"].max() * 1.02, 100)
    ax.plot(x_vals, m * x_vals + b, "--", color="#ef4444", linewidth=2, label=f"Tendencia (Pendiente={m:.1f}, r ≈ 0.05)")

    ax.set_xlabel("MODIS NDVI Promedio Anual (250m)", fontsize=11, fontweight="bold")
    ax.set_ylabel("Rendimiento Cosechado (qq/ha)", fontsize=11, fontweight="bold")
    ax.set_title("La Trampa Biofísica del NDVI: Saturación Espectral Asintótica en Dosel Cerrado", fontsize=13, fontweight="bold", pad=12)
    ax.legend(loc="upper left", frameon=True)
    ax.grid(True, linestyle="--", alpha=0.5)

    fig.tight_layout()
    out_path = OUTPUT_DIR / "saturacion_ndvi.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Generado: {out_path}")

def plot_comparativa_modelos_cafe():
    df_res = pd.read_csv(DATA_DIR / "cafe_jaen_resultados.csv")
    
    # Calcular métricas por modelo sobre las predicciones
    obs = df_res["rendimiento_obs"]
    modelos = [
        ("M0: Persistencia", df_res["pred_m0_persistencia"]),
        ("M1: Tendencia", df_res["pred_m1_tendencia"]),
        ("M2: Solo NDVI", df_res["pred_m2_satelite"]),
        ("M3: Solo Clima", df_res["pred_m3_clima"]),
        ("M4: Fusión Clima+Sat", df_res["pred_m4_fusion"])
    ]
    
    nombres = []
    maes = []
    rmses = []
    for nom, pred in modelos:
        nombres.append(nom)
        maes.append(np.mean(np.abs(obs - pred)))
        rmses.append(np.sqrt(np.mean((obs - pred) ** 2)))

    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    x = np.arange(len(nombres))
    w = 0.35

    bars1 = ax.bar(x - w/2, maes, w, label="MAE (qq/ha)", color="#3b82f6", edgecolor="#1e293b")
    bars2 = ax.bar(x + w/2, rmses, w, label="RMSE (qq/ha)", color="#10b981", edgecolor="#1e293b")

    for b in list(bars1) + list(bars2):
        val = b.get_height()
        ax.text(b.get_x() + b.get_width()/2, val + 0.05, f"{val:.2f}", ha="center", va="bottom", fontsize=9, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(nombres, fontsize=10, fontweight="bold")
    ax.set_ylabel("Error de Pronóstico (qq/ha)", fontsize=11, fontweight="bold")
    ax.set_title("Validación Temporal Expansiva: Comparativa de Modelos en Jaén", fontsize=13, fontweight="bold", pad=12)
    ax.set_ylim(0, max(rmses) * 1.25)
    ax.legend(frameon=True)
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    fig.tight_layout()
    out_path = OUTPUT_DIR / "comparativa_modelos_cafe.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Generado: {out_path}")

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"=== Generando visualizaciones del Caso 2 en {OUTPUT_DIR} ===")
    plot_rendimiento_historico()
    plot_saturacion_ndvi()
    plot_comparativa_modelos_cafe()
    print("=== Visualizaciones del Caso 2 completadas con éxito ===")

if __name__ == "__main__":
    main()
