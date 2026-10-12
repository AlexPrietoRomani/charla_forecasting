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

    fig, ax1 = plt.subplots(figsize=(11, 5.5), dpi=300)
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    color_rend = "#0d9488"
    line1 = ax1.plot(con_rend["campania"], con_rend["rendimiento_qq_ha"], "o-", color=color_rend, linewidth=2.8, markersize=8, label="Rendimiento Oficial (qq/ha)")
    ax1.set_xlabel("Campaña Agrícola", fontsize=11, fontweight="bold", labelpad=8)
    ax1.set_ylabel("Rendimiento (qq pergamino / ha)", color=color_rend, fontsize=11, fontweight="bold")
    ax1.set_ylim(5, 40)
    ax1.grid(True, linestyle="--", alpha=0.5)

    ax2 = ax1.twinx()
    color_prod = "#64748b"
    line2 = ax2.bar(con_rend["campania"] + 0.15, con_rend["produccion_t"] / 1000, width=0.3, color=color_prod, alpha=0.28, label="Producción Total (miles t)")
    ax2.set_ylabel("Producción Total (miles t)", color=color_prod, fontsize=11, fontweight="bold")
    ax2.set_ylim(0, 32)
    ax2.grid(False)

    # Marcador de la Crisis de la Roya 2012-2014 con anotación
    ax1.axvspan(2012, 2014, color="#ef4444", alpha=0.15, label="Crisis de Roya Amarilla (2012-2014)")
    ax1.annotate("Epidemia de Roya (2012–2014)\nColapso -56% en cosecha", xy=(2014, 10.0), xytext=(2014.3, 14.5),
                 arrowprops=dict(arrowstyle="->", color="#dc2626", lw=1.8),
                 fontsize=9.5, fontweight="bold", color="#991b1b",
                 bbox=dict(boxstyle="round,pad=0.3", fc="#fee2e2", ec="#ef4444", alpha=0.95))

    ax1.set_title("Caso 2: Evolución Oficial de Café en Jaén (INEI / MIDAGRI-SIEA 2010–2024)\nQuiebre biológico por plaga (-56% en 2014) y posterior recuperación agronómica", fontsize=12, fontweight="bold", pad=12)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", frameon=True, fontsize=9, framealpha=0.95)

    fig.tight_layout()
    out_path = OUTPUT_DIR / "rendimiento_historico.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Generado: {out_path}")

def plot_saturacion_ndvi():
    df = pd.read_csv(DATA_DIR / "cafe_jaen_campanias.csv")
    con_rend = df.dropna(subset=["rendimiento_kg_ha"]).copy()

    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    sc = ax.scatter(con_rend["ndvi_anual"], con_rend["rendimiento_qq_ha"], s=110, c=con_rend["campania"], cmap="viridis", edgecolor="#1e293b", linewidth=1.5, zorder=3)
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label("Campaña Agrícola", fontsize=10, fontweight="bold")

    # Ajuste lineal mostrando la falta de relación (saturación del dosel)
    m, b = np.polyfit(con_rend["ndvi_anual"], con_rend["rendimiento_qq_ha"], 1)
    x_vals = np.linspace(con_rend["ndvi_anual"].min() * 0.98, con_rend["ndvi_anual"].max() * 1.02, 100)
    ax.plot(x_vals, m * x_vals + b, "--", color="#ef4444", linewidth=2.2, label=f"Ajuste OLS (r = 0.154, p = 0.600 — Pendiente Prácticamente Plana)")

    # Anotación sobre el año de la roya
    roya_row = con_rend[con_rend["campania"] == 2014].iloc[0]
    ax.annotate("Campaña 2014: Epidemia de Roya\nCosecha colapsa a 10.0 qq/ha\nNDVI se mantiene verde en 0.748",
                xy=(roya_row["ndvi_anual"], roya_row["rendimiento_qq_ha"]), xytext=(roya_row["ndvi_anual"] - 0.038, roya_row["rendimiento_qq_ha"] + 5.5),
                arrowprops=dict(arrowstyle="->", color="#dc2626", lw=1.8),
                fontsize=9.5, fontweight="bold", color="#991b1b",
                bbox=dict(boxstyle="round,pad=0.35", fc="#fee2e2", ec="#dc2626", alpha=0.95))

    ax.set_xlabel("MODIS NDVI Promedio Anual (250m)", fontsize=11, fontweight="bold", labelpad=8)
    ax.set_ylabel("Rendimiento Oficial (qq/ha)", fontsize=11, fontweight="bold")
    ax.set_title("La Trampa Biofísica del NDVI: Saturación Espectral Asintótica en Dosel Cerrado de Café\nEl verdor foliar satura en ~0.74 (CV = 2.3%) independientemente de la carga fructífera o ataques de roya", fontsize=12, fontweight="bold", pad=12)
    ax.legend(loc="upper left", frameon=True, fontsize=9, framealpha=0.95)
    ax.grid(True, linestyle="--", alpha=0.5)

    fig.tight_layout()
    out_path = OUTPUT_DIR / "saturacion_ndvi.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Generado: {out_path}")

def plot_comparativa_modelos_cafe():
    p_bm = DATA_DIR / "benchmark_cafe.csv"
    if not p_bm.exists():
        print(f"[WARN] No se encontró {p_bm}")
        return

    df_bm = pd.read_csv(p_bm)
    df_bm = df_bm.sort_values("mae_walkforward", ascending=False).reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(12, 9.0), dpi=300)
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    colors = []
    for _, row in df_bm.iterrows():
        fam = row["familia"]
        p = row["p_valor_vs_mejor"]
        if p == 1.0:
            colors.append("#059669")  # Líder
        elif "Sensoramiento" in fam:
            colors.append("#ef4444")  # Rojo para satélite aislado
        elif "Clima" in fam:
            colors.append("#0284c7")  # Azul cielo para clima fenológico
        elif "Multimodal" in fam or "Árboles" in fam:
            colors.append("#10b981")  # Verde para multimodal / árboles
        elif "Baseline" in fam:
            colors.append("#94a3b8")  # Gris para baselines
        else:
            colors.append("#f59e0b")  # Ámbar para otros

    bars = ax.barh(df_bm["modelo"], df_bm["mae_walkforward"], color=colors, height=0.65, edgecolor="#1e293b", linewidth=0.8)

    max_val = max(df_bm["mae_walkforward"])
    for bar, val, p, fam in zip(bars, df_bm["mae_walkforward"], df_bm["p_valor_vs_mejor"], df_bm["familia"]):
        tag = " (Líder Ref. DM)" if p == 1.0 else f" [p={p:.2f}]"
        ax.text(val + 0.05, bar.get_y() + bar.get_height() / 2, f"{val:.2f} qq/ha{tag}", va="center", fontsize=8.8, fontweight="bold", color="#0f172a")

    ax.set_xlabel("MAE en Validación Walk-Forward Expansiva (qq/ha) — Menor es mejor", fontsize=11, fontweight="bold", labelpad=8)
    ax.set_title("Caso 2: Benchmark de 16 Modelos en Café Jaén (Test Ciego 2016–2024)\nRandom Forest (3.72 qq/ha) y Déficit Hídrico (3.90 qq/ha) superan al Satélite Óptico (5.45 qq/ha) por más de 30%", fontsize=12, fontweight="bold", pad=14)
    ax.set_xlim(0, max_val * 1.48)
    ax.grid(axis="x", linestyle="--", alpha=0.5)

    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#059669", edgecolor="#1e293b", label="Líder Empírico (Random Forest d=2)"),
        Patch(facecolor="#0284c7", edgecolor="#1e293b", label="Clima Fenológico Puro (Floración Ago–Oct)"),
        Patch(facecolor="#10b981", edgecolor="#1e293b", label="ML Multimodal Regularizado / Árboles"),
        Patch(facecolor="#94a3b8", edgecolor="#1e293b", label="Baseline Univariado"),
        Patch(facecolor="#ef4444", edgecolor="#1e293b", label="Satélite Óptico Aislado (Trampa de Saturación)"),
    ]
    ax.legend(handles=legend_elements, loc="lower right", frameon=True, fontsize=9, framealpha=0.95)

    fig.tight_layout()
    out_path = OUTPUT_DIR / "comparativa_modelos_cafe.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Generado: {out_path}")

def plot_trayectoria_walkforward():
    p_preds = DATA_DIR / "cafe_jaen_predicciones_modelos.csv"
    if not p_preds.exists():
        print(f"[WARN] No se encontró {p_preds}")
        return

    df_p = pd.read_csv(p_preds)
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=300)
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    # Observado Real
    ax.plot(df_p["campania"], df_p["rendimiento_real"], "*-", color="#0f172a", linewidth=3.2, markersize=11, label="Observado Oficial SIEA (Cosecha Real)")

    # Modelo Ganador: Random Forest
    if "M12: Random Forest Parsimonioso (d=2)" in df_p.columns:
        ax.plot(df_p["campania"], df_p["M12: Random Forest Parsimonioso (d=2)"], "o-", color="#059669", linewidth=2.4, label="M12: Random Forest (Ganador MAE 3.72)")

    # Clima Fenológico: Solo Déficit Hídrico
    if "M08: Solo Déficit Hídrico Floración" in df_p.columns:
        ax.plot(df_p["campania"], df_p["M08: Solo Déficit Hídrico Floración"], "s--", color="#0284c7", linewidth=2.0, label="M08: Solo Déficit Hídrico Floración (MAE 3.90)")

    # Multimodal ElasticNet
    if "M11: ElasticNet Multimodal (L1+L2)" in df_p.columns:
        ax.plot(df_p["campania"], df_p["M11: ElasticNet Multimodal (L1+L2)"], "^-.", color="#8b5cf6", linewidth=1.8, label="M11: ElasticNet Multimodal (MAE 4.33)")

    # Falla del Satélite Óptico: Solo NDVI
    if "M05: Solo NDVI Anual (Saturado)" in df_p.columns:
        ax.plot(df_p["campania"], df_p["M05: Solo NDVI Anual (Saturado)"], "d:", color="#ef4444", linewidth=2.4, label="M05: Solo NDVI Anual (Falla por Saturación MAE 5.45)")

    # Media Histórica
    if "M02: Media Histórica Acumulada" in df_p.columns:
        ax.plot(df_p["campania"], df_p["M02: Media Histórica Acumulada"], "--", color="#94a3b8", linewidth=1.5, label="M02: Media Histórica Baseline (MAE 4.79)")

    ax.set_xticks(df_p["campania"])
    ax.set_xticklabels([str(int(c)) for c in df_p["campania"]], fontsize=10, fontweight="bold")
    ax.set_ylabel("Rendimiento (qq pergamino / ha)", fontsize=11, fontweight="bold")
    ax.set_xlabel("Campaña Agrícola (Test Walk-Forward)", fontsize=11, fontweight="bold")
    ax.set_ylim(12.0, 39.0)
    ax.set_title("Caso 2: Validación Walk-Forward en Jaén (2016–2024) — Trayectorias de Pronóstico Out-of-Sample\nModelos fenológicos captan el récord de 2020 (35.38 qq/ha); Solo NDVI falla por 18.25 qq/ha", fontsize=12, fontweight="bold", pad=12)
    
    # Leyenda exterior inferior
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), frameon=True, fontsize=8.8, ncol=3, framealpha=0.95)
    ax.grid(True, linestyle="--", alpha=0.5)

    fig.tight_layout()
    out_path = OUTPUT_DIR / "prediccion_walkforward_cono.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Generado: {out_path}")

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"=== Generando visualizaciones del Caso 2 en {OUTPUT_DIR} ===")
    plot_rendimiento_historico()
    plot_saturacion_ndvi()
    plot_comparativa_modelos_cafe()
    plot_trayectoria_walkforward()
    print("=== Visualizaciones del Caso 2 completadas con éxito ===")

if __name__ == "__main__":
    main()
