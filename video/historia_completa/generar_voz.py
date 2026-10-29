"""Genera la narración con Chatterbox (local, MIT) a partir de guion.json y arma narracion.wav + timeline.json.

Uso: _voz/.venv/Scripts/python.exe generar_voz.py   (ver README del pipeline; el venv vive en _voz/, ignorado por git)
"""
import json
import re
import wave

import difflib
import unicodedata

import numpy as np
import torch
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
from faster_whisper import WhisperModel

EXAGERACION, CFG = 0.7, 0.4          # más exageración = más altibajos y exclamaciones
LEAD, GAP, TAIL = 1.0, 0.7, 2.0      # silencios (s) al inicio, entre tramos y al final
PAUSA_FRASE, PAUSA_SUSPENSO = 0.22, 0.45
# Solo para la voz: grafía fonética de nombres propios (el subtítulo usa el texto real).
FONETICA = {"Verhulst": "Ferjulst", "Jenkins": "Yénkins"}
INTENTOS, UMBRAL = 6, 0.85            # el modelo a veces inventa palabras: se transcribe y se reintenta
NUMEROS = set("y uno dos tres cuatro cinco seis siete ocho nueve diez doce veinte veinticuatro veintitres "
              "veintiuno treinta cincuenta setenta mil cien ciento ochocientos novecientos millones".split())


def normalizar(texto: str) -> list[str]:
    """Palabras sin tildes, signos ni números (Whisper escribe 1950 donde el guion dice mil novecientos...)."""
    t = unicodedata.normalize("NFKD", texto.lower()).encode("ascii", "ignore").decode()
    return [w for w in re.findall(r"[a-z]+", t) if w not in NUMEROS]


def parecido(esperado: str, oido: str) -> float:
    return difflib.SequenceMatcher(None, normalizar(esperado), normalizar(oido)).ratio()


def frases(texto: str) -> list[str]:
    """Corta en frases para que el modelo no derive en tramos largos."""
    return [f.strip() for f in re.split(r"(?<=[.!?…])\s+", texto) if f.strip()]


def _a16k(audio: np.ndarray, sr: int) -> np.ndarray:
    import librosa
    return librosa.resample(audio, orig_sr=sr, target_sr=16000)


def main() -> None:
    guion = json.load(open("guion.json", encoding="utf-8"))
    torch.manual_seed(7)
    modelo = ChatterboxMultilingualTTS.from_pretrained(device="cuda" if torch.cuda.is_available() else "cpu")
    sr = modelo.sr
    oido = WhisperModel("small", device="cpu", compute_type="int8")

    def sintetizar(frase: str) -> np.ndarray:
        """Genera la frase hasta que Whisper la reconozca (o devuelve el mejor intento)."""
        mejor, mejor_r = None, -1.0
        for intento in range(INTENTOS):
            torch.manual_seed(7 + intento)
            wav = modelo.generate(frase, language_id="es", exaggeration=EXAGERACION, cfg_weight=CFG)
            audio = wav.squeeze(0).cpu().numpy().astype(np.float32)
            texto = " ".join(x.text for x in oido.transcribe(audio if sr == 16000 else _a16k(audio, sr),
                                                              language="es")[0])
            r = parecido(frase, texto)
            if r > mejor_r:
                mejor, mejor_r = audio, r
            if r >= UMBRAL:
                break
        print(f"   {mejor_r:.2f} x{intento + 1}  {frase[:60]}", flush=True)
        return mejor
    silencio = lambda s: np.zeros(int(sr * s), dtype=np.float32)
    pistas, t, timeline = [silencio(LEAD)], LEAD, []
    for i, seg in enumerate(guion):
        texto = seg["say"]
        for real, fon in FONETICA.items():
            texto = texto.replace(real, fon)
        partes = []
        for f in frases(texto):
            partes += [sintetizar(f), silencio(PAUSA_SUSPENSO if f.endswith("...") else PAUSA_FRASE)]
        audio = np.concatenate(partes[:-1])
        dur = len(audio) / sr
        timeline.append({"id": seg["id"], "show": seg["show"], "say": seg["say"], "t": round(t, 3), "dur": round(dur, 3)})
        print(f"{seg['id']:16s} {dur:5.1f}s", flush=True)
        pistas += [audio, silencio(GAP if i < len(guion) - 1 else TAIL)]
        t += dur + GAP
    total = np.concatenate(pistas)
    pcm = (np.clip(total / max(1.0, np.abs(total).max()) * 0.95, -1, 1) * 32767).astype("<i2")
    with wave.open("narracion.wav", "wb") as w:
        w.setnchannels(1), w.setsampwidth(2), w.setframerate(sr), w.writeframes(pcm.tobytes())
    json.dump({"dur_s": round(len(total) / sr, 3), "segments": timeline},
              open("timeline.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("total", round(len(total) / sr, 1), "s")


if __name__ == "__main__":
    main()
