import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import * as k from "/home/aprietor/.gemini/antigravity-cli/skills/anatomy/kit/iso-kit.mjs";

const WIDTH = 760;
const HEIGHT = 520;

// Escena: Microclima Local SENAMHI Punchana vs Celda Global NWP (ECMWF ~9km / NOAA GFS ~28km)
// 1. Plataforma instrumental con base de acero, patas antivibración, canaletas de cables
// 2. Garita meteorológica (Stevenson screen) con lamas de ventilación, termohigrómetro digital PT100 interno
// 3. Torre reticulada metálica (mástil con crucetas, escalerilla y pernos)
// 4. Estación de sensores: anemómetro ultrasónico de 3 ejes, veleta direccional, piranómetro solar
// 5. Pluviómetro de balancín en pedestal con aro receptor calibrado (200 cm²)
// 6. Datalogger / gabinete industrial IP66 con panel solar y cableado conduit blindado
// 7. Envolvente volumétrica de Supercómputo NWP: celda ortogonal masiva, vórtices de fluido, gradiente térmico
const BASE = { x: -150, y: -110, w: 300, d: 220, r: 8 };
const BASE_H = 12;
const FOOT_H = 6;

// Mástil y estación meteorológica (SENAMHI Punchana, izquierda)
const TOWER = [ -70, 15 ];
const TOWER_H = 140;

// Cubo de volumen global (NWP ECMWF / GFS, derecha)
const CUBE = { x: 25, y: -90, w: 110, d: 110, r: 0 };
const CUBE_Z0 = 25;
const CUBE_H = 105;

const P = k.fitProjection(
  [
    ...k.boxCorners(BASE, -BASE_H - FOOT_H, 0),
    [TOWER[0] - 25, TOWER[1] - 25, TOWER_H + 30],
    [TOWER[0] + 25, TOWER[1] + 25, TOWER_H + 30],
    ...k.boxCorners(CUBE, CUBE_Z0, CUBE_Z0 + CUBE_H + 15)
  ],
  WIDTH,
  HEIGHT,
  { pad: 28, azimuth: 44, elevation: 31 }
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

  for (const [x, y] of byDepth(k.corners(BASE, 22))) {
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

  // Columnas verticales de la torre
  for (const leg of [leg1, leg2, leg3]) {
    parts.push(S(k.cylinder(leg[0], leg[1], 2.2, 5, TOWER_H - 15, P, 16), { tone: "mid" }));
  }

  // Riostras diagonales en X a lo largo de la torre (celosía estructural)
  for (let z = 15; z < TOWER_H - 25; z += 20) {
    parts.push(L(k.segment([leg1[0], leg1[1], z], [leg2[0], leg2[1], z + 20], P), { tone: "lo" }));
    parts.push(L(k.segment([leg2[0], leg2[1], z], [leg1[0], leg1[1], z + 20], P), { tone: "lo" }));
    parts.push(L(k.segment([leg2[0], leg2[1], z], [leg3[0], leg3[1], z + 20], P), { tone: "lo" }));
    parts.push(L(k.segment([leg3[0], leg3[1], z], [leg2[0], leg2[1], z + 20], P), { tone: "lo" }));
    // Anillo horizontal de rigidización
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

  // Pluviómetro de balancín
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

  // 3. Celda de Volumen Global NWP (Supercómputo, Derecha)
  parts.push(S(k.slabOf(k.insetPlan(CUBE, -6), 0, 5, P, 3), { tone: "lo" }));

  for (let step = 1; step <= 4; step++) {
    const gx = CUBE.x + (CUBE.w / 5) * step;
    parts.push(L(k.segment([gx, CUBE.y, 5.2], [gx, CUBE.y + CUBE.d, 5.2], P), { tone: "lo" }));
    const gy = CUBE.y + (CUBE.d / 5) * step;
    parts.push(L(k.segment([CUBE.x, gy, 5.2], [CUBE.x + CUBE.w, gy, 5.2], P), { tone: "lo" }));
  }

  const c000 = [CUBE.x, CUBE.y, CUBE_Z0];
  const c100 = [CUBE.x + CUBE.w, CUBE.y, CUBE_Z0];
  const c010 = [CUBE.x, CUBE.y + CUBE.d, CUBE_Z0];
  const c110 = [CUBE.x + CUBE.w, CUBE.y + CUBE.d, CUBE_Z0];

  const c001 = [CUBE.x, CUBE.y, CUBE_Z0 + CUBE_H];
  const c101 = [CUBE.x + CUBE.w, CUBE.y, CUBE_Z0 + CUBE_H];
  const c011 = [CUBE.x, CUBE.y + CUBE.d, CUBE_Z0 + CUBE_H];
  const c111 = [CUBE.x + CUBE.w, CUBE.y + CUBE.d, CUBE_Z0 + CUBE_H];

  parts.push(L(k.segment(c000, c001, P), { tone: "mid" }));
  parts.push(L(k.segment(c100, c101, P), { tone: "mid" }));
  parts.push(L(k.segment(c010, c011, P), { tone: "mid" }));
  parts.push(L(k.segment(c110, c111, P), { tone: "hi" }));

  parts.push(L(k.segment(c001, c101, P), { tone: "hi" }));
  parts.push(L(k.segment(c101, c111, P), { tone: "hi" }));
  parts.push(L(k.segment(c111, c011, P), { tone: "hi" }));
  parts.push(L(k.segment(c011, c001, P), { tone: "hi" }));

  for (const lz of [CUBE_Z0 + 35, CUBE_Z0 + 70]) {
    parts.push(L(k.segment([CUBE.x, CUBE.y, lz], [CUBE.x + CUBE.w, CUBE.y, lz], P), { tone: "faint" }));
    parts.push(L(k.segment([CUBE.x + CUBE.w, CUBE.y, lz], [CUBE.x + CUBE.w, CUBE.y + CUBE.d, lz], P), { tone: "faint" }));
    parts.push(L(k.segment([CUBE.x + CUBE.w, CUBE.y + CUBE.d, lz], [CUBE.x, CUBE.y + CUBE.d, lz], P), { tone: "faint" }));
    parts.push(L(k.segment([CUBE.x, CUBE.y + CUBE.d, lz], [CUBE.x, CUBE.y, lz], P), { tone: "faint" }));
  }

  for (let step = 1; step <= 4; step++) {
    const gx = CUBE.x + (CUBE.w / 5) * step;
    parts.push(L(k.segment([gx, CUBE.y, CUBE_Z0 + CUBE_H], [gx, CUBE.y + CUBE.d, CUBE_Z0 + CUBE_H], P), { tone: "faint" }));
    const gy = CUBE.y + (CUBE.d / 5) * step;
    parts.push(L(k.segment([CUBE.x, gy, CUBE_Z0 + CUBE_H], [CUBE.x + CUBE.w, gy, CUBE_Z0 + CUBE_H], P), { tone: "faint" }));
  }

  const gridNodes = [
    c001, c101, c011, c111,
    [CUBE.x + CUBE.w / 2, CUBE.y + CUBE.d / 2, CUBE_Z0 + CUBE_H],
    [CUBE.x + CUBE.w / 2, CUBE.y + CUBE.d / 2, CUBE_Z0 + 50]
  ];
  for (const node of gridNodes) {
    parts.push(S(k.cylinder(node[0], node[1], 3.2, node[2] - 1.5, 3.5, P, 16), { tone: "hi", lit: true }));
    parts.push(D([at([node[0], node[1], node[2] + 2])], { size: 0.65, tone: "hi" }));
  }

  const biasVec1 = [CUBE.x + 10, CUBE.y - 12, CUBE_Z0 + 50];
  const biasVec2 = [CUBE.x + CUBE.w - 10, CUBE.y + CUBE.d + 12, CUBE_Z0 + 50];
  parts.push(L(k.segment(biasVec1, biasVec2, P), { tone: "red" }));
  parts.push(L(k.segment(biasVec2, [biasVec2[0] - 8, biasVec2[1] - 4, biasVec2[2] + 4], P), { tone: "red" }));
  parts.push(L(k.segment(biasVec2, [biasVec2[0] - 8, biasVec2[1] - 4, biasVec2[2] - 4], P), { tone: "red" }));

  // 4. Placas grabadas y lecturas ubicadas en zonas despejadas
  const tagStation = at([TOWER[0] - 30, TOWER[1] + 55, 0]);
  const tagGrid = at([CUBE.x + 15, CUBE.y + CUBE.d + 34, 0]);

  const bodyContent = `
  ${parts.join("\n  ")}
  <g class="iso-face-text" data-tone="hi">
    <text x="${tagStation[0]}" y="${tagStation[1]}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.08em">SENAMHI PUNCHANA · MEDICIÓN LOCAL (2m)</text>
    <text x="${tagStation[0]}" y="${tagStation[1] + 13}" font-size="9" fill="var(--anatomy-blue)" text-anchor="middle">MAE MODELOS ML: 1.88 °C · RESIDUOS CALIBRADOS</text>
  </g>
  <g class="iso-face-text" data-tone="hi">
    <text x="${tagGrid[0]}" y="${tagGrid[1]}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.08em">CELDA NWP (ECMWF ~9km / NOAA GFS ~28km)</text>
    <text x="${tagGrid[0]}" y="${tagGrid[1] + 13}" font-size="9" fill="var(--anatomy-red)" text-anchor="middle">SESGO SISTEMÁTICO: +2.58 °C (SIN DOWNSCALING)</text>
  </g>`;

  return k.figureSvg({ body: bodyContent, standalone: "dark", width: WIDTH, height: HEIGHT });
}

const svgOut = buildFigure();
writeFileSync(join(process.cwd(), "front/components/anatomy/anatomy_estacion_vs_malla.svg"), svgOut);
console.log("Generado con éxito con standalone:dark: front/components/anatomy/anatomy_estacion_vs_malla.svg");
