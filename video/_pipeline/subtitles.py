"""Genera la pista de subtítulos WebVTT de un video a partir de sus beats."""

import json
from pathlib import Path

MS_PER_SECOND = 1000
MS_PER_MINUTE = 60 * MS_PER_SECOND
MS_PER_HOUR = 60 * MS_PER_MINUTE


def load_beats(path: Path) -> list[dict]:
    """Lee beats.json y devuelve la lista de beats."""
    return json.loads(Path(path).read_text(encoding="utf-8"))


def format_timestamp(milliseconds: float) -> str:
    """Formatea milisegundos como HH:MM:SS.mmm."""
    hours, rest = divmod(max(0, round(milliseconds)), MS_PER_HOUR)
    minutes, rest = divmod(rest, MS_PER_MINUTE)
    seconds, millis = divmod(rest, MS_PER_SECOND)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{millis:03d}"


def beats_to_vtt(beats: list[dict], start_ms: float = 0, time_scale: float = 1) -> str:
    """Convierte beats (tiempos de escena) a texto WebVTT en tiempos del MP4 final.

    El MP4 reproduce el tramo de escena que empieza en start_ms reproducido a time_scale veces el ritmo de escena,
    así que t_video = (t_escena - start_ms) * time_scale. Los beats fuera del tramo se descartan.
    """
    lines = ["WEBVTT", ""]
    cue = 0
    for beat in beats:
        begin = (beat["t"] * MS_PER_SECOND - start_ms) * time_scale
        end = ((beat["t"] + beat["dur"]) * MS_PER_SECOND - start_ms) * time_scale
        if end <= 0:
            continue
        cue += 1
        lines += [str(cue), f"{format_timestamp(begin)} --> {format_timestamp(end)}", beat["text"], ""]
    return "\n".join(lines)


def write_vtt(beats: list[dict], start_ms: float, time_scale: float, out_path: Path) -> Path:
    """Escribe narration.vtt con los beats ajustados al tramo y velocidad del MP4."""
    out_path = Path(out_path)
    out_path.write_text(beats_to_vtt(beats, start_ms, time_scale), encoding="utf-8")
    return out_path
