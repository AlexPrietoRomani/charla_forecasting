# Fase 5: Refactorización de la Presentación Interactiva (20 Diapositivas)

> **Documento de Fase:** `reference/fases/fase_5_deck_20_slides.md`  
> **Plan Relacionado:** [plan_detallado_diapositivas.md](../plan_detallado_diapositivas.md) (Sección 2, 4 y 5)  
> **Estado:** `[ ] Pendiente de Ejecución` (Requiere aprobación explícita del usuario)

---

## 1. Objetivo de la Fase
Reescribir el generador `scripts/build_deck.py` para compilar el archivo único `presentacion.html` con la nueva estructura de 20 diapositivas ajustada para una audiencia universitaria (30 a 40 minutos), diseño Split-Screen sin huecos blancos, consumo dinámico de datos desde los nuevos CSVs reales, y notas de orador en panel oculto.

---

## 2. Entregables
1. `scripts/build_deck.py` (Script refactorizado y modular).
2. `presentacion.html` (Presentación single-file autocontenida de 20 diapositivas).
3. Hojas de estilo y scripts JS embebidos con soporte de tecla `N` (Speaker Notes) y accesibilidad `prefers-reduced-motion`.

---

## 3. Subfases y Tareas

### SF5.1 Arquitectura Visual y Layout 40/60 Split-Screen
- [X] **T5.1.1** Ajustar el layout del deck a 20 diapositivas exactas, eliminando las diapositivas redundantes de la versión anterior (dron no respaldado, descomposiciones duplicadas).
- [X] **T5.1.2** Implementar el grid Split-Screen:
  - Panel Izquierdo (~38% ancho): Título de la diapositiva, insignia semántica fija, tesis en una sola frase, máximo 3 viñetas breves y la **Frase-clave** destacada en tarjeta de alto contraste.
  - Panel Derecho (~62% ancho): Visual animado interactivo a altura completa sin márgenes vacíos ("Zero-White-Space").
- [X] **T5.1.3** Normalizar las 5 insignias visuales con su paleta de color estricta:
  - `TEORÍA` (Violeta `--badge-teoria`)
  - `MECANISMO` (Cian `--badge-mecanismo`)
  - `EVIDENCIA` (Ámbar `--badge-evidencia`)
  - `CASO REAL` (Esmeralda `--badge-caso_real`)
  - `DEMO` (Rojo `--badge-demo`)

### SF5.2 Drawer de Notas del Ponente (`Speaker Notes`) y Glosario
- [X] **T5.2.1** Crear drawer deslizante inferior/lateral que se activa con la tecla `N` o botón discreto, conteniendo el guion conversacional completo y el temporizador sugerido por diapositiva.
- [X] **T5.2.2** Evitar que el texto largo del guion sature la pantalla principal (la audiencia debe mirar al ponente y al gráfico, no leer un párrafo).
- [X] **T5.2.3** Implementar tooltip emergente ("Glosario") para términos estadísticos básicos (*lag*, *overfitting*, *zero-shot*, *cuantiles*, *NDVI*) que se active al pasar el cursor sobre palabras subrayadas con puntos.

### SF5.3 Animaciones Cíclicas y Accesibilidad
- [X] **T5.3.1** Programar animaciones en bucle infinito suave (`@keyframes`) con propósitos físicos concretos (haz de probabilidad, ventana deslizante, decaimiento exponencial, atención en parches, absorción foliar).
- [X] **T5.3.2** Configurar loops intensos únicamente en las diapositivas clave donde el movimiento es el argumento principal; loops calmos y sutiles en el resto.
- [X] **T5.3.3** Incorporar media query `@media (prefers-reduced-motion: reduce)` para pausar las animaciones si el sistema del usuario lo requiere.

### SF5.4 Conexión de Demos Interactivas a CSVs Reales
- [X] **T5.4.1** Actualizar Demo 1 (Diapositiva 14): Gráfico interactivo con Chart.js conectado a `data/senamhi_forecast_7d.csv`, mostrando la predicción del modelo ganador de Iquitos, bandas de incertidumbre y conmutadores para NOAA GFS / ECMWF IFS / TimesFM.
- [X] **T5.4.2** Actualizar Demo 2 (Diapositiva 17): Gráfico interactivo conectado a `data/cafe_jaen_campanias.csv` y `data/cafe_jaen_resultados.csv`, permitiendo explorar la validación temporal expansiva año a año.
- [X] **T5.4.3** Garantizar que ninguna cifra de la presentación esté escrita a mano en el código HTML/JS: todas se inyectan dinámicamente desde los CSVs de `data/`.

---

## 4. Criterios de Aceptación (DoD Fase 5)
- [X] `presentacion.html` contiene exactamente 20 elementos `<section class="slide">`.
- [X] No existen números huérfanos o sintéticos antiguos (`grep` limpio de 29.98, 0.788, etc.).
- [X] Tecla `N` abre y cierra limpiamente las notas del ponente.
- [X] El archivo compila y corre de forma 100% offline con doble clic en el navegador.
