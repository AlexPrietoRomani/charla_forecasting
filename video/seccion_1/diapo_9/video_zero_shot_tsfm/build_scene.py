#!/usr/bin/env python3
"""Genera scene.html: entrada de 30 s para la Diapo 9 (Sección 1), 'Modelos que predicen sin entrenar (TSFM)'. Datos reales de Punchana y benchmark de modelos."""

import base64
import json
import pathlib
import sys

import pandas as pd

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "_pipeline"))
from subtitles import load_beats, write_vtt  # noqa: E402

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parents[3]

FPS = 30
DURATION_MS = 30000

df = pd.read_csv(ROOT / "data/caso_1/senamhi_diario.csv")
bm = pd.read_csv(ROOT / "data/caso_1/benchmark_punchana.csv")

ctx = df[df["fecha"] <= "2025-12-24"].tail(60).copy()
dates = [str(v) for v in ctx["fecha"]]
vals = [round(float(v), 1) for v in ctx["tmax"]]
short = ["%02d·%s" % (int(d[8:10]), ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"][int(d[5:7]) - 1]) for d in dates]

def row(prefix):
    r = bm[bm["modelo"].astype(str).str.startswith(prefix)].iloc[0]
    return {
        "rmse": round(float(r["rmse_1d"]), 3),
        "mae": round(float(r["mae_1d"]), 3),
        "p": float(r["p_valor_vs_mejor"]),
        "t": float(r["tiempo_s"]),
    }

data = {
    "dates": short,
    "vals": vals,
    "n": len(df),
    "bench": {
        "extra": row("ExtraTrees"),
        "tfm": row("TimesFM"),
        "chr": row("Chronos"),
    },
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

video_cfg = json.loads((SRC / "video.json").read_text(encoding="utf-8"))
beats = load_beats(SRC / "beats.json")
template = (SRC / "scene_template.html").read_text(encoding="utf-8")
html = (
    template.replace("__FONTS_CSS__", fonts_css)
    .replace("__DATA_JSON__", json.dumps(data, separators=(",", ":")))
    .replace("__DURATION_MS__", str(DURATION_MS))
    .replace("__BEATS_JSON__", json.dumps(beats, ensure_ascii=False, separators=(",", ":")))
)
(SRC / "scene.html").write_text(html, encoding="utf-8")
write_vtt(beats, video_cfg["start_ms"], video_cfg["time_scale"], SRC / "narration.vtt")
b = data["bench"]
print(
    f"scene.html escrito: {len(html):,} bytes · contexto {len(vals)} días ({short[0]}→{short[-1]}) · n={data['n']} · "
    f"TimesFM {b['tfm']['rmse']} · Chronos {b['chr']['rmse']} · ExtraTrees {b['extra']['rmse']}"
)
