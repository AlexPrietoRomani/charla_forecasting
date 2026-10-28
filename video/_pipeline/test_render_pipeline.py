"""Verifica la estructura del pipeline de video: configuraciones, capturador único y ffmpeg resoluble."""

import json
import re
from pathlib import Path

import pytest
import render
import subtitles

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


MAX_BEAT_WORDS = 10
MIN_BEATS, MAX_BEATS = 3, 5


def _video_dirs() -> list[Path]:
    """Devuelve las 9 carpetas de video."""
    return sorted(path.parent for path in VIDEO_ROOT.glob("seccion_*/diapo_*/video_*/video.json"))


def test_each_video_has_valid_beats():
    """Comprueba beats.json: 3-5 beats, texto de máximo 10 palabras y sin solapes."""
    for video_dir in _video_dirs():
        beats = json.loads((video_dir / "beats.json").read_text(encoding="utf-8"))
        assert MIN_BEATS <= len(beats) <= MAX_BEATS, video_dir
        previous_end = 0.0
        for beat in beats:
            assert 0 < len(beat["text"].split()) <= MAX_BEAT_WORDS, (video_dir, beat)
            assert beat["dur"] > 0 and beat["t"] >= previous_end, (video_dir, beat)
            previous_end = beat["t"] + beat["dur"]


def test_each_video_has_parseable_vtt():
    """Comprueba que narration.vtt empieza con WEBVTT y sus tiempos son crecientes y válidos."""
    pattern = re.compile(r"^(\d{2}):(\d{2}):(\d{2})\.(\d{3}) --> (\d{2}):(\d{2}):(\d{2})\.(\d{3})$")
    for video_dir in _video_dirs():
        lines = (video_dir / "narration.vtt").read_text(encoding="utf-8").splitlines()
        assert lines[0] == "WEBVTT", video_dir
        cues = [pattern.match(line) for line in lines if "-->" in line]
        assert cues and all(cues), video_dir
        for match in cues:
            values = [int(group) for group in match.groups()]
            begin = values[0] * 3_600_000 + values[1] * 60_000 + values[2] * 1000 + values[3]
            end = values[4] * 3_600_000 + values[5] * 60_000 + values[6] * 1000 + values[7]
            assert 0 <= begin < end, video_dir


def test_write_vtt_applies_start_and_time_scale(tmp_path):
    """Comprueba que write_vtt convierte tiempos de escena a tiempos del MP4 final."""
    beats = [{"t": 4.0, "dur": 2.0, "text": "uno"}, {"t": 10.0, "dur": 3.0, "text": "dos"}]
    out_path = subtitles.write_vtt(beats, 4000, 1.3043, tmp_path / "narration.vtt")
    content = out_path.read_text(encoding="utf-8")
    assert "00:00:00.000 --> 00:00:02.609" in content
    assert "00:00:07.826 --> 00:00:11.739" in content
    identity = subtitles.beats_to_vtt(beats, 0, 1)
    assert "00:00:04.000 --> 00:00:06.000" in identity


def test_capture_script_tolerates_profile_cleanup_failure():
    """Comprueba que capture.mjs reintenta y silencia el fallo de limpieza del perfil en Windows."""
    script = render.CAPTURE_SCRIPT.read_text(encoding="utf-8")
    assert "maxRetries" in script and "removeProfile" in script
