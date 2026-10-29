#!/usr/bin/env python3
"""Genera scene.html y narration.vtt del video 'Historia de las series temporales' (~190 s, narrado)."""

import base64
import json
import pathlib
import re
import sys

import pandas as pd

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parents[1]
sys.path.insert(0, str(SRC.parent / "_pipeline"))
from subtitles import write_vtt  # noqa: E402

MAX_WORDS = 12


def chunk_say(say: str) -> list[str]:
    """Divide el texto en frases cortas (<= 12 palabras) cortando en puntuación."""
    parts = [p.strip() for p in re.split(r"(?<=[.,:;?!])\s+", say) if p.strip()]
    out: list[str] = []
    for part in parts:
        words = part.split()
        n = -(-len(words) // MAX_WORDS)
        size = -(-len(words) // n)
        out += [" ".join(words[i : i + size]) for i in range(0, len(words), size)]
    return out


def build_beats(timeline: dict) -> list[dict]:
    """Reparte cada segmento en beats proporcionales a la longitud de cada frase."""
    beats = []
    for seg in timeline["segments"]:
        chunks = chunk_say(seg["say"])
        total = sum(len(c) for c in chunks)
        cum = 0
        for c in chunks:
            t0 = seg["t"] + seg["dur"] * cum / total
            cum += len(c)
            t1 = seg["t"] + seg["dur"] * cum / total
            beats.append({"t": round(t0, 3), "dur": round(t1 - t0 - 0.05, 3), "text": c})
    return beats


def build_data() -> dict:
    """Series reales de Iquitos (SENAMHI) para la apertura y la descomposición."""
    df = pd.read_csv(ROOT / "data/caso_1/senamhi_diario.csv", parse_dates=["fecha"]).set_index("fecha")
    s = df["tmax"].asfreq("D").interpolate(limit_direction="both")
    hist = s["2025-07-01":"2025-12-31"]
    fut = s["2025-01-01":"2025-03-01"].rolling(5, min_periods=1, center=True).mean()
    fut = fut + (hist.iloc[-7:].mean() - fut.iloc[:7].mean())
    w = s.resample("W").mean()
    trend = w.rolling(52, center=True, min_periods=10).mean().bfill().ffill()
    det = w - trend
    seas = det.groupby(w.index.isocalendar().week.values).transform("mean")
    res = det - seas
    cyc = res.rolling(13, center=True, min_periods=3).mean().bfill().ffill()
    noise = res - cyc
    r = lambda a: [round(float(v), 3) for v in a]  # noqa: E731
    return {
        "hist": r(hist), "fut": r(fut),
        "wk": {"comb": r(w), "trend": r(trend), "seas": r(seas), "cyc": r(cyc), "noise": r(noise)},
    }


def main() -> None:
    timeline = json.loads((SRC / "timeline.json").read_text(encoding="utf-8"))
    beats = build_beats(timeline)
    fonts_css = ""
    for family, fname, weight in [
        ("Space Grotesk", "SpaceGrotesk-500.woff2", "300 800"),
        ("IBM Plex Sans", "IBMPlexSans-400.woff2", "100 700"),
        ("IBM Plex Mono", "IBMPlexMono-400.woff2", "400"),
        ("IBM Plex Mono", "IBMPlexMono-600.woff2", "600"),
    ]:
        b64 = base64.b64encode((SRC / "fonts" / fname).read_bytes()).decode("ascii")
        fonts_css += (
            "@font-face{font-family:'%s';font-style:normal;font-weight:%s;"
            "src:url(data:font/woff2;base64,%s) format('woff2');}\n" % (family, weight, b64)
        )
    cfg = json.loads((SRC / "video.json").read_text(encoding="utf-8"))
    dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))  # noqa: E731
    html = (
        (SRC / "scene_template.html").read_text(encoding="utf-8")
        .replace("__FONTS_CSS__", fonts_css)
        .replace("__TIMELINE_JSON__", dump(timeline))
        .replace("__DATA_JSON__", dump(build_data()))
        .replace("__DURATION_MS__", str(cfg["dur_ms"]))
        .replace("__BEATS_JSON__", dump(beats))
    )
    (SRC / "scene.html").write_text(html, encoding="utf-8")
    write_vtt(beats, cfg["start_ms"], cfg["time_scale"], SRC / "narration.vtt")
    print(f"scene.html: {len(html):,} bytes · {len(beats)} subtítulos")


if __name__ == "__main__":
    main()
