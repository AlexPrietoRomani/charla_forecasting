"""Renderiza el MP4 de una carpeta de video: escena, captura de frames por CDP y codificación con ffmpeg."""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PIPELINE_DIR = Path(__file__).resolve().parent
CAPTURE_SCRIPT = PIPELINE_DIR / "capture.mjs"
REQUIRED_KEYS = ("fps", "dur_ms", "start_ms", "time_scale", "dpr", "bg", "out")
# Duración del fade-in desde el color de fondo, en segundos.
FADE_SECONDS = 0.35


def load_config(video_dir: Path) -> dict:
    """Lee y valida el video.json de la carpeta indicada."""
    config = json.loads((video_dir / "video.json").read_text(encoding="utf-8"))
    missing = [key for key in REQUIRED_KEYS if key not in config]
    if missing:
        raise SystemExit(f"video.json sin claves requeridas: {missing}")
    return config


def resolve_ffmpeg() -> str:
    """Devuelve la ruta de ffmpeg del PATH o la del paquete imageio-ffmpeg."""
    found = shutil.which("ffmpeg")
    if found:
        return found
    try:
        import imageio_ffmpeg
    except ImportError:
        # Dependencia de render, no del análisis: se instala al primer uso sin ffmpeg.
        subprocess.run([sys.executable, "-m", "pip", "install", "imageio-ffmpeg"], check=True)
        import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def capture_frames(video_dir: Path, frames_dir: Path, config: dict, frames_only: int | None) -> None:
    """Captura los PNG de la escena con capture.mjs usando el navegador resuelto."""
    fps = config["fps"]
    dur_ms = config["dur_ms"] if frames_only is None else round(frames_only * 1000 / fps)
    # capture.mjs usa PYTHON_BIN para consultar el chromium de playwright del mismo intérprete.
    env = {**os.environ, "PYTHON_BIN": sys.executable}
    command = [
        "node", str(CAPTURE_SCRIPT), "scene.html", str(frames_dir),
        str(fps), str(dur_ms), str(config["start_ms"]), str(config["time_scale"]), str(config["dpr"]),
    ]
    expected = round(dur_ms / 1000 * fps)
    for attempt in (1, 2):
        subprocess.run(command, cwd=video_dir, env=env, check=False)
        produced = len(list(frames_dir.glob("f*.png")))
        # En Windows la limpieza del perfil de Chrome puede fallar (EPERM/EBUSY) tras capturar todo:
        # si están todos los frames, el exit distinto de 0 no es un error real.
        if produced == expected:
            return
        print(f"captura incompleta ({produced}/{expected}), intento {attempt}/2", file=sys.stderr)
    raise SystemExit(f"captura fallida: {produced}/{expected} frames")


def encode(ffmpeg: str, frames_dir: Path, config: dict, out_path: Path) -> None:
    """Codifica los frames a H.264 con fade-in desde el color de fondo."""
    fade = f"fade=t=in:st=0:d={FADE_SECONDS}:color=0x{config['bg']}"
    command = [
        ffmpeg, "-y", "-loglevel", "error",
        "-framerate", str(config["fps"]), "-i", str(frames_dir / "f%05d.png"),
        "-vf", fade,
        "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", str(out_path),
    ]
    subprocess.run(command, check=True)


def main(argv: list[str] | None = None) -> int:
    """Ejecuta el render completo o parcial según los argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(description="Renderiza el video de una carpeta de diapositiva.")
    parser.add_argument("video_dir", type=Path, help="carpeta con video.json y build_scene.py")
    parser.add_argument("--skip-build", action="store_true", help="no regenera scene.html")
    parser.add_argument("--frames-only", type=int, metavar="N", help="captura solo N frames (smoke test)")
    parser.add_argument("--out-override", type=Path, help="ruta alternativa del MP4")
    args = parser.parse_args(argv)

    if args.frames_only is not None and args.out_override is None:
        parser.error("--frames-only requiere --out-override para no reemplazar el MP4 vigente")

    video_dir = args.video_dir.resolve()
    config = load_config(video_dir)
    if not args.skip_build:
        # PYTHONUTF8 evita el fallo cp1252 de Windows al imprimir caracteres como σ.
        build_env = {**os.environ, "PYTHONUTF8": "1"}
        subprocess.run([sys.executable, "build_scene.py"], cwd=video_dir, env=build_env, check=True)

    out_path = args.out_override.resolve() if args.out_override else video_dir / config["out"]
    ffmpeg = resolve_ffmpeg()
    with tempfile.TemporaryDirectory() as tmp:
        frames_dir = Path(tmp)
        capture_frames(video_dir, frames_dir, config, args.frames_only)
        encode(ffmpeg, frames_dir, config, out_path)

    size_mb = out_path.stat().st_size / 1_000_000
    print(f"OK: {out_path} ({size_mb:.2f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
