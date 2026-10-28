# Pipeline de video

Renderiza los MP4 de las entradas cinemáticas de cada diapositiva a partir de su escena HTML.
Un solo capturador (`capture.mjs`) y un solo script de render (`render.py`) sirven a las 9 carpetas.

## Requisitos

- Python 3.13 con `pip install -r requirements.txt` (incluye `playwright` e `imageio-ffmpeg`).
- Node.js 22 o superior en el PATH (`node`).
- Un navegador Chromium, en este orden de preferencia:
  1. Variable `CHROME_BIN` con la ruta del ejecutable.
  2. Chromium de Playwright (`python -m playwright install chromium`).
  3. Microsoft Edge en `Program Files` o `Program Files (x86)`.
  4. `chromium` o `google-chrome` en el PATH.
- ffmpeg: el del PATH o, si no existe, el de `imageio-ffmpeg`.

## Uso

```bash
python video/_pipeline/render.py video/seccion_1/diapo_10/video_cono_incertidumbre
```

Opciones:

- `--skip-build`: no regenera `scene.html`.
- `--frames-only N --out-override RUTA.mp4`: captura solo N frames para una prueba rápida.
  Exige `--out-override` para no reemplazar el MP4 vigente.
- `--out-override RUTA.mp4`: escribe el MP4 en otra ruta.

## Cómo añadir un video nuevo

1. Crea la carpeta `video/seccion_N/diapo_M/video_<slug>/` con `build_scene.py`, `scene_template.html` y `fonts/`.
   `build_scene.py` debe escribir `scene.html` en su propia carpeta y exponer `window.__ready` y `window.__setTime(ms)`.
2. Añade `video.json` con las claves `fps`, `dur_ms`, `start_ms`, `time_scale`, `dpr`, `bg` (hex sin `#`) y `out` (nombre del MP4).
3. Ejecuta `python video/_pipeline/render.py <carpeta>`.
4. Corre `python -m pytest video/_pipeline -q`: valida que el `video.json` nuevo tiene las claves requeridas.

Cada carpeta conserva solo sus fuentes y su MP4 vigente. El capturador y el render no se copian.
