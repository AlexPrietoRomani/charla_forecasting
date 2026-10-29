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

## Subtítulos (beats)

Los videos son mudos: cada carpeta lleva `beats.json` con 3 a 5 beats `{"t": seg, "dur": seg, "text": "..."}`
(tiempos de la escena, máximo 10 palabras por beat, lenguaje llano, sin solapes).

- `build_scene.py` inyecta los beats en `__BEATS_JSON__` y la escena dibuja la banda `<div id="subs">` como función
  pura del tiempo (fade de 0.25 s), de modo que el MP4 lleva el subtítulo quemado y el render sigue siendo determinista.
- `build_scene.py` también escribe `narration.vtt` con `subtitles.write_vtt(beats, start_ms, time_scale, ruta)`.
  Los tiempos del VTT son los del MP4 final: `t_video = (t_escena - start_ms) * time_scale` (p. ej. `anatomia_senal`
  usa el tramo [4 s, 27 s] reproducido a 1.3043x).
- Decisión de accesibilidad: el deck se abre por `file://` y Chrome bloquea `<track src="narration.vtt">` por CORS.
  Por eso el compilador del deck incrusta el VTT como `data:text/vtt;base64,...` en un `<track kind="subtitles"
  srclang="es">` sin `default` y con `mode="hidden"`. Con el subtítulo quemado ya visible, el track queda disponible
  para lectores de pantalla y para activarlo a mano sin duplicar el texto.

## Windows: limpieza del perfil de Chrome

`capture.mjs` borra el perfil temporal de Chrome con `rmSync(..., {maxRetries: 5, retryDelay: 200})` dentro de
`try/catch`: un `EPERM`/`EBUSY` al limpiar ya no es un error. `render.py` acepta la salida del capturador si el
directorio tiene todos los PNG esperados; si faltan, reintenta una vez. Renderiza como máximo 2 videos en paralelo.

No hay cambios de variables de entorno ni de dependencias.

## Video narrado (`video/historia_completa/`)

Video de ~4 min con voz: historia de las series temporales (Parte 1) y origen del pronóstico en el agro (Parte 2).

1. Edita el texto en `guion.json` (`say` = lo que se dice, `show` = titular en pantalla).
2. Genera la voz con Chatterbox (modelo local, licencia MIT) en un entorno aparte, porque fija `torch==2.6.0`:
   `uv venv video/historia_completa/_voz/.venv --python 3.11` y luego
   `uv pip install --python video/historia_completa/_voz/.venv/Scripts/python.exe chatterbox-tts faster-whisper "setuptools<81"`
   (en GPU NVIDIA, reinstala `torch==2.6.0 torchaudio==2.6.0` desde `https://download.pytorch.org/whl/cu124`).
3. Desde `video/historia_completa/`: `_voz/.venv/Scripts/python.exe generar_voz.py`. Escribe `narracion.wav` y
   `timeline.json`; cada frase se transcribe con Whisper y se regenera si el modelo inventó palabras.
4. Actualiza `dur_ms` de `video.json` con `timeline.json → dur_s`, corre `python video/_pipeline/render.py video/historia_completa`
   y une audio y video: `ffmpeg -i historia_series_temporales_mudo.mp4 -i narracion.wav -c:v copy -c:a aac -b:a 160k historia_series_temporales.mp4`.
