import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import * as k from "/home/aprietor/.gemini/antigravity-cli/skills/anatomy/kit/iso-kit.mjs";

const WIDTH = 840;
const HEIGHT = 560;

// Escena: Tierra vs Supercómputo (Caso 1 SENAMHI Punchana)
// Lado Izquierdo: Estación Meteorológica SENAMHI Punchana (Tierra, microclima tropical a 2m)
//   - Torre reticulada de 3 patas de acero galvanizado con celosías en X
//   - Garita Stevenson reglamentaria OMM con lamas de ventilación y sensor termohigrométrico PT100 interno
//   - Pluviómetro de balancín en pedestal calibrado (200 cm²)
//   - Datalogger industrial IP66 con panel solar y tubería conduit apantallada
//   - Cruceta superior con anemómetro de 3 cazoletas, veleta direccional y piranómetro solar
//
// Lado Derecho: Supercomputador HPC Cluster / Rack de Centro de Datos (ECMWF IFS / NOAA GFS)
//   - Gabinete rack estándar 42U de centro de datos con zócalo, puertas biseladas y pies niveladores
//   - Bahías de servidores blade modulares extraíbles con manijas y orejetas de montaje en rack
//   - Ranuras/rejillas de ventilación horizontal de flujo forzado
//   - Matriz de LEDs indicadores de estado (verde/azul de cómputo paralelo activo)
//   - Panel de control y consola frontal iluminada con pantalla OLED: "ECMWF IFS · RESOLUCIÓN 9km · SESGO +2.46°C"
//   - Bandeja de cableado estructurado de fibra óptica y ducto de refrigeración líquida

const BASE = { x: -150, y: -110, w: 300, d: 220, r: 8 };
const BASE_H = 12;
const FOOT_H = 6;

// Mástil y estación meteorológica (SENAMHI Punchana, izquierda)
const TOWER = [ -75, 15 ];
const TOWER_H = 145;

// Rack de Supercómputo HPC (Centro de datos ECMWF / NOAA, derecha)
const RACK = { x: 35, y: -70, w: 85, d: 115, r: 4 };
const RACK_BASE_Z = 0;
const RACK_H = 150;

const P = k.fitProjection(
  [
    ...k.boxCorners(BASE, -BASE_H - FOOT_H, 0),
    [TOWER[0] - 28, TOWER[1] - 25, TOWER_H + 30],
    [TOWER[0] + 28, TOWER[1] + 25, TOWER_H + 30],
    [RACK.x - 10, RACK.y - 10, RACK_H + 15],
    [RACK.x + RACK.w + 10, RACK.y + RACK.d + 10, RACK_H + 15]
  ],
  WIDTH,
  HEIGHT,
  { pad: 32, azimuth: 44, elevation: 32 }
);

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const byDepth = (points) => [...points].sort((a, b) => k.depthOf([a[0], a[1], 0], P) - k.depthOf([b[0], b[1], 0], P));

function buildFigure() {
  const parts = [];

  // 1. Halo base y patas
  parts.push(`<path class="iso-halo" d="${k.haloOf(BASE, -BASE_H - FOOT_H, BASE_H, P)}"/>`);

  for (const [x, y] of byDepth(k.corners(BASE, 20))) {
    parts.push(S(k.cylinder(x, y, 9, -BASE_H - FOOT_H, 2, P, 28), { tone: "lo" }));
    parts.push(S(k.cylinder(x, y, 7, -BASE_H - FOOT_H + 2, FOOT_H - 2, P, 28), { tone: "mid" }));
  }

  // Plataforma metálica
  parts.push(S(k.slabOf(BASE, -BASE_H, BASE_H, P, 8, 1.8), { tone: "mid" }));
  parts.push(L(k.planOutline(k.insetPlan(BASE, 6), 0, P), { tone: "lo" }));

  // Tornillería en esquinas
  const screws = k.corners(BASE, 12);
  parts.push(L(screws.map(([x, y]) => k.ring(x, y, 2.5, 0, P, 16)).join(""), { tone: "lo" }));
  parts.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 0.5 }));

  // Regla métrica grabada de calibración (estándar OMM / WMO)
  const rulerStrip = { x: -130, y: BASE.y + BASE.d - 18, w: 260, d: 8, r: 1 };
  parts.push(S(k.slabOf(rulerStrip, 0, 0.8, P, 3), { tone: "lo", crease: "none" }));
  const ticks = k.topTicks(rulerStrip.x + 6, rulerStrip.x + rulerStrip.w - 6, 5, 5, rulerStrip.y + 1, 0.8, [2, 4], P);
  parts.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));

  // 2. Estación SENAMHI Punchana (Sector Izquierdo)
  // Zapata de anclaje de la torre
  const towerBase = { x: TOWER[0] - 22, y: TOWER[1] - 22, w: 44, d: 44, r: 4 };
  parts.push(S(k.slabOf(towerBase, 0, 5, P, 4, 0.8), { tone: "lo" }));
  parts.push(L(k.planOutline(k.insetPlan(towerBase, 3), 5, P), { tone: "faint" }));

  // Pernos de anclaje a tierra (4 esquinas de la zapata)
  const anchorBolts = k.corners(towerBase, 6);
  parts.push(L(anchorBolts.map(([x, y]) => k.ring(x, y, 1.8, 5, P, 12)).join(""), { tone: "lo" }));
  parts.push(D(anchorBolts.map(([x, y]) => at([x, y, 5])), { size: 0.45 }));

  // Torre reticulada (3 patas triangulares de acero galvanizado con celosías en X)
  const legOffset = 14;
  const leg1 = [TOWER[0], TOWER[1] - legOffset];
  const leg2 = [TOWER[0] - legOffset * 0.86, TOWER[1] + legOffset * 0.5];
  const leg3 = [TOWER[0] + legOffset * 0.86, TOWER[1] + legOffset * 0.5];

  for (const leg of [leg1, leg2, leg3]) {
    parts.push(S(k.cylinder(leg[0], leg[1], 2.2, 5, TOWER_H - 15, P, 16), { tone: "mid" }));
  }

  // Riostras diagonales en X a lo largo de la torre (celosía estructural)
  for (let z = 15; z < TOWER_H - 25; z += 20) {
    parts.push(L(k.segment([leg1[0], leg1[1], z], [leg2[0], leg2[1], z + 20], P), { tone: "lo" }));
    parts.push(L(k.segment([leg2[0], leg2[1], z], [leg1[0], leg1[1], z + 20], P), { tone: "lo" }));
    parts.push(L(k.segment([leg2[0], leg2[1], z], [leg3[0], leg3[1], z + 20], P), { tone: "lo" }));
    parts.push(L(k.segment([leg3[0], leg3[1], z], [leg2[0], leg2[1], z + 20], P), { tone: "lo" }));
    parts.push(L(k.segment([leg1[0], leg1[1], z + 20], [leg2[0], leg2[1], z + 20], P), { tone: "mid" }));
    parts.push(L(k.segment([leg2[0], leg2[1], z + 20], [leg3[0], leg3[1], z + 20], P), { tone: "mid" }));
    parts.push(L(k.segment([leg3[0], leg3[1], z + 20], [leg1[0], leg1[1], z + 20], P), { tone: "mid" }));
  }

  // Garita meteorológica de radiación (Stevenson Screen a 2.0m reglamentarios OMM)
  const louverZ = 65;
  parts.push(S(k.slabOf({ x: TOWER[0] - 25, y: TOWER[1] - 4, w: 18, d: 8, r: 1.5 }, louverZ + 8, 3, P, 2), { tone: "lo" }));

  // Caja de láminas (Louvered shield)
  const screenBox = { x: TOWER[0] - 45, y: TOWER[1] - 14, w: 24, d: 24, r: 2.5 };
  parts.push(S(k.slabOf(screenBox, louverZ, 26, P, 4, 1.0), { tone: "hi", lit: true }));
  for (let lz = louverZ + 3; lz < louverZ + 24; lz += 3.5) {
    parts.push(L(k.segment([screenBox.x, screenBox.y + screenBox.d, lz], [screenBox.x + screenBox.w, screenBox.y + screenBox.d, lz], P), { tone: "lo" }));
  }
  parts.push(S(k.cylinder(screenBox.x + 12, screenBox.y + 12, 2.5, louverZ + 4, 16, P, 16), { tone: "hi", lit: true }));

  // Gabinete Datalogger industrial IP66
  const dlBox = { x: TOWER[0] + 10, y: TOWER[1] - 10, w: 20, d: 14, r: 2 };
  parts.push(S(k.slabOf(dlBox, 35, 24, P, 3, 0.8), { tone: "hi" }));
  parts.push(L(k.planOutline(k.insetPlan(dlBox, 1.5), 35 + 24, P), { tone: "faint" }));
  parts.push(D([at([dlBox.x + 3, dlBox.y + dlBox.d - 3, 35 + 12])], { size: 0.5, tone: "lo" }));

  // Panel solar fotovoltaico de 30W
  const pvPanel = { x: TOWER[0] + 8, y: TOWER[1] - 25, w: 22, d: 18, r: 1 };
  parts.push(S(k.slabOf(pvPanel, 70, 2, P, 2), { tone: "mid" }));
  parts.push(L(k.segment([pvPanel.x + 11, pvPanel.y, 72], [pvPanel.x + 11, pvPanel.y + pvPanel.d, 72], P), { tone: "blue" }));

  // Pluviómetro de balancín en pedestal propio
  const rainX = TOWER[0] - 25;
  const rainY = TOWER[1] + 35;
  parts.push(S(k.cylinder(rainX, rainY, 11, 0, 32, P, 28), { tone: "mid" }));
  parts.push(S(k.cylinder(rainX, rainY, 13, 32, 5, P, 28), { tone: "hi" }));
  parts.push(L(k.ring(rainX, rainY, 12, 37, P, 28), { tone: "lit" }));
  parts.push(L(k.ring(rainX, rainY, 8, 34, P, 20), { tone: "faint" }));

  // Coronación de la torre (z = TOWER_H): Anemómetro, veleta y piranómetro
  const topCrossZ = TOWER_H - 12;
  const crossArm = { x: TOWER[0] - 32, y: TOWER[1] - 4, w: 64, d: 8, r: 2 };
  parts.push(S(k.slabOf(crossArm, topCrossZ, 5, P, 4, 0.6), { tone: "hi" }));

  // Anemómetro sónico/cazoletas
  const cupAx = TOWER[0] - 26;
  parts.push(S(k.cylinder(cupAx, TOWER[1], 2, topCrossZ + 5, 18, P, 16), { tone: "mid" }));
  parts.push(S(k.cylinder(cupAx, TOWER[1], 8, topCrossZ + 18, 4, P, 24), { tone: "hi", lit: true }));
  for (const cdeg of [0, 120, 240]) {
    const crad = cdeg * (Math.PI / 180);
    const cx = cupAx + 10 * Math.cos(crad);
    const cy = TOWER[1] + 10 * Math.sin(crad);
    parts.push(L(k.segment([cupAx, TOWER[1], topCrossZ + 20], [cx, cy, topCrossZ + 20], P), { tone: "lo" }));
    parts.push(S(k.cylinder(cx, cy, 3, topCrossZ + 18, 4, P, 16), { tone: "hi" }));
  }

  // Veleta aerodinámica
  const vaneAx = TOWER[0] + 26;
  parts.push(S(k.cylinder(vaneAx, TOWER[1], 2, topCrossZ + 5, 20, P, 16), { tone: "mid" }));
  const vaneTail = { x: vaneAx - 1.5, y: TOWER[1] - 12, w: 3, d: 24, r: 0.8 };
  parts.push(S(k.slabOf(vaneTail, topCrossZ + 20, 8, P, 2), { tone: "hi", lit: true }));
  parts.push(S(k.cylinder(vaneAx, TOWER[1] + 12, 3.5, topCrossZ + 22, 5, P, 16), { tone: "lo" }));

  // Piranómetro solar central
  parts.push(S(k.cylinder(TOWER[0], TOWER[1], 4.5, topCrossZ + 5, 8, P, 20), { tone: "hi" }));
  parts.push(S(k.cylinder(TOWER[0], TOWER[1], 3, topCrossZ + 13, 3, P, 20), { tone: "hi", lit: true }));

  // Conduit de cables
  const conduitPts = [
    [TOWER[0] + 2, TOWER[1], topCrossZ],
    [TOWER[0] + 2, TOWER[1] + 5, 60],
    [dlBox.x + 10, dlBox.y + 7, 59]
  ];
  for (let i = 0; i < conduitPts.length - 1; i++) {
    parts.push(L(k.segment(conduitPts[i], conduitPts[i + 1], P), { tone: "faint" }));
  }

  // 3. Supercomputador HPC Cluster (Gabinete Rack de Centro de Datos, Derecha)
  // Zócalo base del rack con pies antivibración
  parts.push(S(k.slabOf(k.insetPlan(RACK, -4), 0, 6, P, 3, 0.8), { tone: "lo" }));
  const rackFeet = k.corners(RACK, -2);
  for (const [fx, fy] of rackFeet) {
    parts.push(S(k.cylinder(fx, fy, 4, 0, 4, P, 16), { tone: "mid" }));
  }

  // Chasis principal del Rack (Cuerpo monolítico de acero con esquinas biseladas)
  parts.push(S(k.slabOf(RACK, 6, RACK_H, P, 4, 1.2), { tone: "mid" }));
  parts.push(L(k.planOutline(k.insetPlan(RACK, 3), 6 + RACK_H, P), { tone: "hi" }));

  // Techo del rack: rejilla de extracción de ventiladores (Fans de enfriamiento)
  const fanZ = 6 + RACK_H;
  for (const foffset of [-20, 0, 20]) {
    const fcx = RACK.x + RACK.w / 2;
    const fcy = RACK.y + RACK.d / 2 + foffset;
    parts.push(S(k.cylinder(fcx, fcy, 10, fanZ, 2.5, P, 24), { tone: "lo" }));
    parts.push(L(k.ring(fcx, fcy, 9.5, fanZ + 2.5, P, 24), { tone: "faint" }));
  }

  // Frontal del Rack (y = RACK.y + RACK.d): Bahías de Servidores Blade (42U)
  const frontY = RACK.y + RACK.d;
  const numUnits = 7; // 7 servidores blade de alta densidad
  const unitH = (RACK_H - 30) / numUnits;

  for (let u = 0; u < numUnits; u++) {
    const uz = 12 + u * unitH;
    // Marco exterior de la unidad blade
    const unitPlan = { x: RACK.x + 6, y: frontY - 1.5, w: RACK.w - 12, d: 3, r: 1 };
    parts.push(S(k.slabOf(unitPlan, uz, unitH - 2.5, P, 2, 0.4), { tone: u === 3 ? "hi" : "mid", lit: u === 3 }));

    // Manijas metálicas a los costados del servidor blade
    parts.push(L(k.segment([RACK.x + 9, frontY + 2.5, uz + 2], [RACK.x + 9, frontY + 2.5, uz + unitH - 4.5], P), { tone: "hi" }));
    parts.push(L(k.segment([RACK.x + RACK.w - 9, frontY + 2.5, uz + 2], [RACK.x + RACK.w - 9, frontY + 2.5, uz + unitH - 4.5], P), { tone: "hi" }));

    // Ranuras horizontales de ventilación forzada en la cara frontal del servidor
    for (let slotZ = uz + 3; slotZ < uz + unitH - 5; slotZ += 3.2) {
      parts.push(L(k.segment([RACK.x + 16, frontY + 1.6, slotZ], [RACK.x + RACK.w - 24, frontY + 1.6, slotZ], P), { tone: "lo" }));
    }

    // LEDs de actividad de CPU / Cómputo (Verde / Cyan en los paneles frontales)
    const ledPt1 = at([RACK.x + RACK.w - 15, frontY + 1.8, uz + unitH / 2]);
    const ledPt2 = at([RACK.x + RACK.w - 19, frontY + 1.8, uz + unitH / 2]);
    parts.push(`<circle cx="${ledPt1[0]}" cy="${ledPt1[1]}" r="1.4" fill="var(--anatomy-green)"/>`);
    parts.push(`<circle cx="${ledPt2[0]}" cy="${ledPt2[1]}" r="1.4" fill="var(--anatomy-blue)"/>`);
  }

  // Pantalla / Consola de Diagnóstico Operacional en la unidad central (u = 3)
  const oledZ = 12 + 3 * unitH + 3;
  const oledBox = { x: RACK.x + 18, y: frontY - 0.5, w: 45, d: 2, r: 1 };
  parts.push(S(k.slabOf(oledBox, oledZ, unitH - 8, P, 2), { tone: "hi", lit: true }));
  // Líneas de telemetría en la pantalla del rack
  parts.push(L(k.segment([oledBox.x + 4, frontY + 1.8, oledZ + 3], [oledBox.x + 40, frontY + 1.8, oledZ + 3], P), { tone: "cyan" }));
  parts.push(L(k.segment([oledBox.x + 4, frontY + 1.8, oledZ + 6], [oledBox.x + 28, frontY + 1.8, oledZ + 6], P), { tone: "cyan" }));

  // Ducto aéreo de fibra óptica y refrigeración líquida que sale del rack hacia el exterior
  const pipePts = [
    [RACK.x + 20, RACK.y + 20, RACK_H + 6],
    [RACK.x + 20, RACK.y - 15, RACK_H + 25],
    [RACK.x + 70, RACK.y - 25, RACK_H + 25]
  ];
  for (let i = 0; i < pipePts.length - 1; i++) {
    parts.push(L(k.segment(pipePts[i], pipePts[i + 1], P), { tone: "blue" }));
  }

  // 4. Placas grabadas y etiquetas técnicas ubicadas en espacios limpios
  const tagStation = at([TOWER[0] - 25, TOWER[1] + 55, 0]);
  const tagHpc = at([RACK.x + RACK.w / 2, frontY + 36, 0]);

  const bodyContent = `
  ${parts.join("\n  ")}
  <g class="iso-face-text" data-tone="hi">
    <text x="${tagStation[0]}" y="${tagStation[1]}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.08em">SENAMHI PUNCHANA · MEDICIÓN LOCAL (2m)</text>
    <text x="${tagStation[0]}" y="${tagStation[1] + 13}" font-size="9" fill="var(--fest-cyan)" text-anchor="middle">MAE MODELOS ML: 1.88 °C · RESIDUOS CALIBRADOS</text>
  </g>
  <g class="iso-face-text" data-tone="hi">
    <text x="${tagHpc[0]}" y="${tagHpc[1]}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.08em">SUPERCOMPUTADOR NUMÉRICO (HPC RACK)</text>
    <text x="${tagHpc[0]}" y="${tagHpc[1] + 13}" font-size="9" fill="var(--anatomy-red)" text-anchor="middle">ECMWF IFS (9 km) / NOAA GFS (28 km) · SESGO: +2.58 °C</text>
  </g>`;

  return k.figureSvg({ body: bodyContent, standalone: "dark", width: WIDTH, height: HEIGHT });
}

const svgOut = buildFigure();
writeFileSync(join(process.cwd(), "front/components/anatomy/anatomy_estacion_vs_malla.svg"), svgOut);
console.log("Generado con éxito con HPC Supercomputer Rack: front/components/anatomy/anatomy_estacion_vs_malla.svg");
