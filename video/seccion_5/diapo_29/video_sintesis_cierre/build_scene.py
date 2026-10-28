#!/usr/bin/env python3
"""Genera scene.html: cierre ejecutivo de 25 s para la Diapo 29 (Sección 5), 'Dos casos, tres axiomas, una disciplina'."""

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
DURATION_MS = 25000

fc = pd.read_csv(ROOT / "data/caso_1/senamhi_forecast_7d.csv")
di = pd.read_csv(ROOT / "data/caso_1/senamhi_diario.csv", parse_dates=["fecha"]).set_index("fecha")
df = pd.read_csv(ROOT / "data/caso_2/cafe_jaen_campanias.csv")
hip = json.loads((ROOT / "data/caso_2/cafe_jaen_hipotesis.json").read_text(encoding="utf-8"))

s = di["tmax"].astype(float)
T = s.rolling(365, center=True, min_periods=180).mean()
S = s.groupby(s.index.month).transform("mean") - s.mean()
C = s.rolling(30, center=True, min_periods=15).mean() - T
E = s - T - S - C

qhat = float(((fc["ci_upper_p90"] - fc["ci_lower_p10"]) / 2).mean())
r2014 = float(df.loc[df["campania"] == 2014, "rendimiento_qq_ha"].iloc[0])

MES = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
days = ["%02d·%s" % (int(d[8:10]), MES[int(d[5:7]) - 1]) for d in fc["fecha"].astype(str)]

data = {
    "days": days,
    "obs": [round(float(v), 1) for v in fc["tmax_observada"]],
    "et": [round(float(v), 2) for v in fc["pred_extratrees"]],
    "lo": [round(float(v), 2) for v in fc["ci_lower_p10"]],
    "hi": [round(float(v), 2) for v in fc["ci_upper_p90"]],
    "qhat": round(qhat, 2),
    "n": len(s),
    "sigma": round(float(E.std()), 2),
    "record": round(float(s.max()), 1),
    "years": [int(v) for v in df["campania"]],
    "ndvi": [None if pd.isna(v) else round(float(v), 4) for v in df["ndvi_anual"]],
    "rend": [None if pd.isna(v) else round(float(v), 2) for v in df["rendimiento_qq_ha"]],
    "i2014": int(df.index[df["campania"] == 2014][0]),
    "rend2014": round(r2014, 1),
    "caidaPct": float(hip["H4_roya_invisibilidad"]["caida_rendimiento_pct"]),
    "varNdviPct": float(hip["H4_roya_invisibilidad"]["variacion_ndvi_pct"]),
    "rDeficit": float(hip["H2_fenologia"]["r_deficit_hidrico"]),
    "rLluvia": float(hip["H2_fenologia"]["r_lluvia_flor"]),
    "rmse": 1.88,
    "cpu": 0.25,
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
print(
    f"scene.html escrito: {len(html):,} bytes · n={data['n']} · σ={data['sigma']} · récord={data['record']} · "
    f"N={len(data['years'])} · 2014 rend={data['rend2014']} ({data['caidaPct']}%) · banda {min(data['lo'])}–{max(data['hi'])} · q̂={data['qhat']}"
)
