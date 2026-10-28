#!/usr/bin/env python3
"""Genera scene.html: entrada de 30 s para la Diapo 7 (Sección 1), 'El truco de los lags y árboles'. Serie real de Punchana + experimento de extrapolación (2023)."""

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

df = pd.read_csv(ROOT / "data/caso_1/senamhi_diario.csv", parse_dates=["fecha"]).set_index("fecha")
s = df["tmax"].astype(float)

start = pd.Timestamp("2023-08-15")
end = pd.Timestamp("2023-10-15")
seg = s.loc[start:end]
curve = [None if pd.isna(v) else round(float(v), 1) for v in seg]
dates = [d.strftime("%Y-%m-%d") for d in seg.index]
idx = {d: i for i, d in enumerate(dates)}


def tmax(day):
    return round(float(s.loc[pd.Timestamp(day)]), 1)


def media7(day):
    d = pd.Timestamp(day)
    return round(float(s.loc[d - pd.Timedelta(days=6):d].mean()), 1)


t_win = "2023-10-06"
rows = []
for day in ["2023-10-05", "2023-10-06", "2023-10-07"]:
    d = pd.Timestamp(day)
    rows.append({
        "y1": f"{tmax(d - pd.Timedelta(days=1)):.1f}",
        "y7": f"{tmax(d - pd.Timedelta(days=7)):.1f}",
        "m7": f"{media7(d):.1f}",
        "promo": str(1 if day == "2023-10-05" else 0),
        "clima": f"{tmax(day):.1f}",
        "th": f"{tmax(d + pd.Timedelta(days=1)):.1f}",
    })

exp = pd.read_csv(ROOT / "data/caso_1/experimento_extrapolacion.csv")
exp_labels = [pd.Timestamp(v).strftime("%d·%m") for v in exp["fecha"]]

data = {
    "curve": curve,
    "curveStart": "15 Ago",
    "curveTicks": [{"i": idx["2023-08-15"], "label": "15·08"},
                   {"i": idx["2023-09-15"], "label": "15·09"},
                   {"i": idx["2023-10-01"], "label": "01·10"},
                   {"i": idx["2023-10-15"], "label": "15·10"}],
    "win": {
        "i7": idx["2023-09-29"], "im": idx["2023-10-02"], "i1": idx["2023-10-05"],
        "start": idx["2023-09-29"], "end": idx["2023-10-06"],
    },
    "rows": rows,
    "star": 1,
    "y1v": round(float(s.loc[pd.Timestamp("2023-10-05")]), 1),
    "y7v": round(float(s.loc[pd.Timestamp("2023-09-29")]), 1),
    "mv": round(float(s.loc[pd.Timestamp("2023-10-02")]), 1),
    "exp": {
        "labels": exp_labels,
        "real": [round(float(v), 1) for v in exp["tmax_real"]],
        "niv": [round(float(v), 2) for v in exp["pred_arbol_niveles"]],
        "dif": [round(float(v), 2) for v in exp["pred_arbol_diferencias"]],
        "tope": 34.0,
        "iRec": int(exp["tmax_real"].values.argmax()),
        "rec": round(float(exp["tmax_real"].max()), 1),
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
print(f"scene.html escrito: {len(html):,} bytes · curva {len(curve)} días · récord {data['exp']['rec']} °C en i={data['exp']['iRec']} · fila récord yₜ₊ₕ={rows[1]['th']} °C")
