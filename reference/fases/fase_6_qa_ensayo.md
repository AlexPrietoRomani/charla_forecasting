# Fase 6: QA Visual, Auditoría Multi-Resolución, Ensayo y Bitácora

> **Documento de Fase:** `reference/fases/fase_6_qa_ensayo.md`  
> **Plan Relacionado:** [plan_detallado_diapositivas.md](../plan_detallado_diapositivas.md) (Sección 6)  
> **Estado:** `[ ] Pendiente de Ejecución` (Requiere aprobación explícita del usuario)

---

## 1. Objetivo de la Fase
Garantizar la perfección visual, técnica y operativa de la presentación final:
1. Auditar en resoluciones de proyector (1920×1080, 1366×768, 1600×900) para asegurar cero desbordes verticales y legibilidad a distancia.
2. Comprobar contraste WCAG AA tanto en tema oscuro como en tema claro.
3. Realizar un ensayo cronometrado del guion (ajuste estricto a 30–40 minutos).
4. Documentar en la bitácora (`docs/logs/log.md`) el incidente de los datos sintéticos y la solución adoptada.
5. Actualizar las fuentes en NotebookLM para que el asistente cuente con la versión 100% depurada.

---

## 2. Entregables
1. Capturas o reporte de verificación visual en el servidor local (`http://localhost:8000/presentacion.html`).
2. Entrada formal en `docs/logs/log.md` (Incidente: Reemplazo de datos sintéticos por datos oficiales y reales).
3. `docs/presentacion_slides_texto.md` actualizado y reimportado en NotebookLM.

---

## 3. Subfases y Tareas

### SF6.1 Auditoría Visual y de Responsividad
- [X] **T6.1.1** Verificar las 20 diapositivas a resolución 1920×1080: comprobar que ningún panel genere scrollbar involuntario.
- [X] **T6.1.2** Verificar a resolución 1366×768 (típica de laptops de auditorio): comprobar que los textos no se monten sobre los SVGs.
- [X] **T6.1.3** Probar alternancia de temas (claro y oscuro): verificar que todos los textos, ejes de gráficos y líneas mantengan contraste adecuado.
- [X] **T6.1.4** Verificar navegación por teclado completa: `←` / `→` (anterior/siguiente), `F` (pantalla completa), `Home` / `End`, `N` (notas), `D` (modo oscuro).

### SF6.2 Ensayo Cronometrado del Ponente
- [X] **T6.2.1** Realizar una lectura completa del guion acumulando los tiempos por acto:
  - Acto 1 (Diapos 01–03): ~5 min
  - Acto 2 (Diapos 04–11): ~13 min
  - Acto 3 (Diapos 12–14): ~6 min
  - Acto 4 (Diapos 15–17): ~6 min
  - Acto 5 (Diapos 18–20): ~5 min
  - Total proyectado: ~35 minutos (encaja exactamente en la ventana de 30 a 40 minutos).
- [X] **T6.2.2** Ajustar extensiones en notas de orador si alguna diapositiva sobrepasa los 2 minutos de explicación.

### SF6.3 Bitácora y Ecosistema de Investigación
- [X] **T6.3.1** Redactar entrada forense en `docs/logs/log.md` con la estructura: Síntoma (datos sintéticos no declarados) $\to$ Causa Raíz (script generador con fórmulas de simulación) $\to$ Resolución (migración a MIDAGRI y Planetary Computer) $\to$ Lecciones aprendidas.
- [X] **T6.3.2** Actualizar `docs/presentacion_slides_texto.md` reflejando fielmente las 20 diapositivas finales.
- [X] **T6.3.3** Sincronizar el notebook de NotebookLM con el texto actualizado para futuras consultas.

---

## 4. Criterios de Aceptación (DoD Fase 6)
- [X] Las 20 diapositivas se visualizan sin errores de renderizado en Chrome/Brave/Firefox.
- [X] La bitácora documenta de manera transparente todo el proceso de auditoría y corrección.
- [X] El deck está listo para ser presentado en vivo por el usuario.
