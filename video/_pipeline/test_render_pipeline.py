"""Verifica la estructura del pipeline de video: configuraciones, capturador único y ffmpeg resoluble."""

import json
from pathlib import Path

import pytest
import render

REPO_ROOT = Path(__file__).resolve().parents[2]
VIDEO_ROOT = REPO_ROOT / "video"
SKIPPED_DIRS = {".git", ".venv", "node_modules"}


def _find_files(file_name: str) -> list[Path]:
    """Devuelve los archivos del repo con el nombre indicado, sin entrar en carpetas de entorno."""
    return [
        path
        for path in REPO_ROOT.rglob(file_name)
        if not SKIPPED_DIRS.intersection(path.relative_to(REPO_ROOT).parts)
    ]


def test_each_video_folder_has_valid_config():
    """Comprueba que las 9 carpetas de video tienen video.json con las claves requeridas."""
    configs = sorted(VIDEO_ROOT.glob("seccion_*/diapo_*/video_*/video.json"))
    assert len(configs) == 9
    for config_path in configs:
        config = json.loads(config_path.read_text(encoding="utf-8"))
        assert set(render.REQUIRED_KEYS) <= set(config), config_path
        assert config["fps"] == 30, config_path
        assert len(config["bg"]) == 6, config_path


def test_single_capture_script_in_repo():
    """Comprueba que solo existe el capturador compartido en video/_pipeline."""
    captures = _find_files("capture.mjs")
    assert captures == [render.CAPTURE_SCRIPT]


def test_no_render_sh_left():
    """Comprueba que no quedan scripts render.sh en el repo."""
    assert _find_files("render.sh") == []


def test_resolve_ffmpeg_returns_existing_binary():
    """Comprueba que render.py obtiene una ruta de ffmpeg existente."""
    assert Path(render.resolve_ffmpeg()).is_file()


def test_out_override_required_with_frames_only():
    """Comprueba que --frames-only exige --out-override para no reemplazar el MP4 vigente."""
    with pytest.raises(SystemExit) as error:
        render.main([str(VIDEO_ROOT), "--frames-only", "3"])
    assert error.value.code == 2
