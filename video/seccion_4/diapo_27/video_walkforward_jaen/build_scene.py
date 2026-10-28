#!/usr/bin/env python3
"""Genera scene.html: entrada de 30 s para la Diapo 27 (Sección 4), 'Validación Walk-Forward y el Ganador'. Datos reales del café de Jaén."""

import base64
import json
import pathlib

import pandas as pd

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parents[3]

FPS = 30
DURATION_MS = 30000

bench = pd.read_csv(ROOT / "data/caso_2/benchmark_cafe.csv")
preds = pd.read_csv(ROOT / "data/caso_2/cafe_jaen_predicciones_modelos.csv")

SHORT = {
    "M12": "Random Forest (d=2)",
    "M08": "Solo Déficit Hídrico",
    "M16": "Zero-Shot Heurístico",
    "M07": "Solo Lluvia Floración",
    "M11": "ElasticNet Multimodal",
    "M01": "Persistencia Naive",
    "M06": "Solo EVI Floración",
    "M10": "Lasso Multimodal",
    "M13": "ExtraTrees (d=2)",
    "M15": "Gaussian Process",
    "M04": "Holt Lineal",
    "M02": "Media Histórica",
    "M09": "Ridge Multimodal",
    "M05": "Solo NDVI Anual",
    "M03": "Tendencia OLS",
    "M14": "Bayes Ridge",
}

models = []
for _, row in bench.iterrows():
    code = str(row["modelo"]).split(":")[0].strip()
    models.append(
        {
            "code": code,
            "short": SHORT[code],
            "mae": round(float(row["mae_walkforward"]), 3),
            "rmse": round(float(row["rmse_walkforward"]), 3),
            "mape": round(float(row["mape_walkforward"]), 2),
            "err2020": round(float(row["error_abs_2020"]), 2),
            "ms": round(float(row["tiempo_ms"]), 2),
        }
    )

years = [int(v) for v in preds["campania"]]
cols = {str(c).split(":")[0].strip(): c for c in preds.columns if ":" in str(c)}

series = {
    "real": [round(float(v), 2) for v in preds["rendimiento_real"]],
    "M12": [round(float(v), 2) for v in preds[cols["M12"]]],
    "M08": [round(float(v), 2) for v in preds[cols["M08"]]],
    "M05": [round(float(v), 2) for v in preds[cols["M05"]]],
}

best = models[0]
m05 = next(m for m in models if m["code"] == "M05")
delta_m05 = round((m05["mae"] / best["mae"] - 1) * 100, 1)

data = {
    "models": models,
    "years": years,
    "series": series,
    "i2020": years.index(2020),
    "err2020M05": m05["err2020"],
    "deltaM05": delta_m05,
    "nModels": len(models),
    "nTests": len(years),
    "best": best,
}

fonts_css = ""
font_files = [
    ("Space Grotesk", "SpaceGrotesk-500.woff2", "300 800"),
    ("IBM Plex Sans", "IBMPlexSans-400.woff2", "100 700"),
    ("IBM Plex Mono", "IBMPlexMono-400.woff2", "400"),
    ("IBM Plex Mono", "IBMPlexMono-600.woff2", "600"),
]
for family, fname, weight in font_files:
    b64 = base64.b64encode((SRC / "fonts" / fname).read_bytes()).decode("ascii")
    fonts_css += (
        "@font-face{font-family:'%s';font-style:normal;font-weight:%s;"
        "src:url(data:font/woff2;base64,%s) format('woff2');}\n" % (family, weight, b64)
    )

template = (SRC / "scene_template.html").read_text(encoding="utf-8")
html = (
    template.replace("__FONTS_CSS__", fonts_css)
    .replace("__DATA_JSON__", json.dumps(data, separators=(",", ":")))
    .replace("__DURATION_MS__", str(DURATION_MS))
)
(SRC / "scene.html").write_text(html, encoding="utf-8")
print(
    f"scene.html escrito: {len(html):,} bytes · {data['nModels']} modelos · {data['nTests']} tests "
    f"({years[0]}, {years[1]}–{years[-1]}) · ganador {best['code']} MAE {best['mae']} · "
    f"M05 MAE {m05['mae']} (+{delta_m05}%) · error 2020 M05 = {m05['err2020']}"
)
