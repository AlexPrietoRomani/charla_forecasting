import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "/home/aprietor/.gemini/antigravity-cli/skills/anatomy/kit/iso-kit.mjs";

const WIDTH = 680;
const HEIGHT = 460;

// Escena: Estación micrometeorológica SENAMHI sobre base instrumental (tierra local)
// vs Cubo gigante de malla atmosférica (NWP: GFS ~28km / ECMWF ~9km)
const BASE = { x: -140, y: -100, w: 280, d: 200, r: 8 };
const BASE_H = 12;
const FOOT_H = 6;

// Mástil y estación meteorológica (SENAMHI Punchana)
const TOWER = [ -60, 20 ];
const TOWER_H = 120;
const SENSOR_Z = TOWER_H - 10;

// Cubo de malla global (NWP GFS / ECMWF) suspendido como rejilla de volumen
const CUBE = { x: 20, y: -80, w: 100, d: 100, r: 0 };
const CUBE_Z0 = 30;
const CUBE_H = 90;

const P = k.fitProjection(
  [
    ...k.boxCorners(BASE, -BASE_H - FOOT_H, 0),
    [TOWER[0], TOWER[1], TOWER_H + 25],
    ...k.boxCorners(CUBE, CUBE_Z0, CUBE_Z0 + CUBE_H)
  ],
  WIDTH,
  HEIGHT,
  { pad: 26, azimuth: 44, elevation: 32 }
);

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const byDepth = (points) => [...points].sort((a, b) => k.depthOf([a[0], a[1], 0], P) - k.depthOf([b[0], b[1], 0], P));

function buildFigure() {
  const parts = [];

  // 1. Sombra / Halo base
  parts.push(`<path class="iso-halo" d="${k.haloOf(BASE, -BASE_H - FOOT_H, BASE_H, P)}"/>`);

  // 2. Patas de la plataforma
  for (const [x, y] of byDepth(k.corners(BASE, 20))) {
    parts.push(S(k.cylinder(x, y, 9, -BASE_H - FOOT_H, 2, P, 28), { tone: "lo" }));
    parts.push(S(k.cylinder(x, y, 7, -BASE_H - FOOT_H + 2, FOOT_H - 2, P, 28), { tone: "mid" }));
  }

  // 3. Mesa / Base sólida
  parts.push(S(k.slabOf(BASE, -BASE_H, BASE_H, P, 8, 1.8), { tone: "mid" }));
  parts.push(L(k.planOutline(k.insetPlan(BASE, 6), 0, P), { tone: "lo" }));

  // Tornillos perimetrales
  const screws = k.corners(BASE, 12);
  parts.push(L(screws.map(([x, y]) => k.ring(x, y, 2.5, 0, P, 16)).join(""), { tone: "lo" }));
  parts.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 0.5 }));

  // 4. Sector Izquierdo: Estación SENAMHI Punchana (Microclima local)
  // Placa de montaje del mástil
  const mastPlate = { x: TOWER[0] - 22, y: TOWER[1] - 22, w: 44, d: 44, r: 4 };
  parts.push(S(k.slabOf(mastPlate, 0, 5, P, 4, 0.8), { tone: "lo" }));
  parts.push(L(k.planOutline(k.insetPlan(mastPlate, 3), 5, P), { tone: "faint" }));

  // Mástil tubular metálico (acero)
  parts.push(S(k.cylinder(TOWER[0], TOWER[1], 4.5, 5, TOWER_H - 5, P, 28), { tone: "mid" }));
  // Anillos de sujeción mástil
  for (const z of [30, 60, 90]) {
    parts.push(S(k.cylinder(TOWER[0], TOWER[1], 6.5, z, 4, P, 28), { tone: "lo" }));
    parts.push(L(k.ring(TOWER[0], TOWER[1], 6.5, z + 4, P, 28), { tone: "mid" }));
  }

  // Garita meteorológica / Escudo de radiación multidiámetro (Stevenson screen compacto)
  for (let i = 0; i < 5; i++) {
    const louverZ = 65 + i * 5;
    parts.push(S(k.cylinder(TOWER[0], TOWER[1], 14 - i * 0.5, louverZ, 2.5, P, 32), { tone: i === 2 ? "hi" : "mid" }));
  }

  // Sensor digital de temperatura/humedad (PT100) en el centro de la garita
  parts.push(S(k.cylinder(TOWER[0], TOWER[1], 2, 60, 30, P, 16), { tone: "hi", lit: true }));

  // Brazo superior de instrumentación (Anemómetro sónico + veleta)
  const armZ = TOWER_H - 12;
  const arm = { x: TOWER[0] - 30, y: TOWER[1] - 3, w: 60, d: 6, r: 1.5 };
  parts.push(S(k.slabOf(arm, armZ, 4, P, 4, 0.5), { tone: "hi" }));

  // Cazoletas del anemómetro (izq)
  const cupX = TOWER[0] - 25;
  parts.push(S(k.cylinder(cupX, TOWER[1], 1.5, armZ + 4, 15, P, 16), { tone: "mid" }));
  parts.push(S(k.cylinder(cupX, TOWER[1], 7, armZ + 15, 3, P, 24), { tone: "hi", lit: true }));

  // Veleta aerodinámica (der)
  const vaneX = TOWER[0] + 25;
  parts.push(S(k.cylinder(vaneX, TOWER[1], 1.5, armZ + 4, 18, P, 16), { tone: "mid" }));
  const vaneFin = { x: vaneX - 1, y: TOWER[1] - 8, w: 2, d: 16, r: 0.5 };
  parts.push(S(k.slabOf(vaneFin, armZ + 16, 7, P, 2), { tone: "mid" }));

  // Pluvimetro de balancín en pedestal propio al lado
  const rainX = TOWER[0] + 35;
  const rainY = TOWER[1] - 20;
  parts.push(S(k.cylinder(rainX, rainY, 9, 0, 28, P, 28), { tone: "mid" }));
  parts.push(S(k.cylinder(rainX, rainY, 10.5, 28, 4, P, 28), { tone: "hi" }));
  parts.push(L(k.ring(rainX, rainY, 9.5, 32, P, 28), { tone: "lit" }));

  // Cable de datos rutado hacia la tarjeta de adquisición
  const wirePoints = [
    [TOWER[0], TOWER[1], 60],
    [TOWER[0] + 8, TOWER[1] + 5, 25],
    [TOWER[0] + 10, TOWER[1] + 15, 6],
    [-10, 30, 2],
    [40, 30, 2]
  ];
  for (let i = 0; i < wirePoints.length - 1; i++) {
    parts.push(L(k.segment(wirePoints[i], wirePoints[i + 1], P), { tone: "faint" }));
  }

  // 5. Sector Derecho: La Celda de Malla Global (NWP ECMWF / GFS)
  // Representación volumétrica en alambre y caras translúcidas de supercómputo
  // Marco del cubo de malla
  const c000 = [CUBE.x, CUBE.y, CUBE_Z0];
  const c100 = [CUBE.x + CUBE.w, CUBE.y, CUBE_Z0];
  const c010 = [CUBE.x, CUBE.y + CUBE.d, CUBE_Z0];
  const c110 = [CUBE.x + CUBE.w, CUBE.y + CUBE.d, CUBE_Z0];

  const c001 = [CUBE.x, CUBE.y, CUBE_Z0 + CUBE_H];
  const c101 = [CUBE.x + CUBE.w, CUBE.y, CUBE_Z0 + CUBE_H];
  const c011 = [CUBE.x, CUBE.y + CUBE.d, CUBE_Z0 + CUBE_H];
  const c111 = [CUBE.x + CUBE.w, CUBE.y + CUBE.d, CUBE_Z0 + CUBE_H];

  // Pedestal / Base de la celda de cálculo
  parts.push(S(k.slabOf(k.insetPlan(CUBE, -4), 0, 4, P, 2), { tone: "lo" }));
  // Líneas de cuadrícula de discretización en el suelo
  for (let step = 1; step <= 3; step++) {
    const gx = CUBE.x + (CUBE.w / 4) * step;
    parts.push(L(k.segment([gx, CUBE.y, 4], [gx, CUBE.y + CUBE.d, 4], P), { tone: "lo" }));
    const gy = CUBE.y + (CUBE.d / 4) * step;
    parts.push(L(k.segment([CUBE.x, gy, 4], [CUBE.x + CUBE.w, gy, 4], P), { tone: "lo" }));
  }

  // Cubo de volumen global (NWP)
  // Pilares verticales del prisma
  parts.push(L(k.segment(c000, c001, P), { tone: "mid" }));
  parts.push(L(k.segment(c100, c101, P), { tone: "mid" }));
  parts.push(L(k.segment(c010, c011, P), { tone: "mid" }));
  parts.push(L(k.segment(c110, c111, P), { tone: "hi" }));

  // Aristas superiores e inferiores
  parts.push(L(k.segment(c001, c101, P), { tone: "hi" }));
  parts.push(L(k.segment(c101, c111, P), { tone: "hi" }));
  parts.push(L(k.segment(c111, c011, P), { tone: "hi" }));
  parts.push(L(k.segment(c011, c001, P), { tone: "hi" }));

  // Cara superior discretizada con nodos de integración
  for (let step = 1; step <= 3; step++) {
    const gx = CUBE.x + (CUBE.w / 4) * step;
    parts.push(L(k.segment([gx, CUBE.y, CUBE_Z0 + CUBE_H], [gx, CUBE.y + CUBE.d, CUBE_Z0 + CUBE_H], P), { tone: "faint" }));
    const gy = CUBE.y + (CUBE.d / 4) * step;
    parts.push(L(k.segment([CUBE.x, gy, CUBE_Z0 + CUBE_H], [CUBE.x + CUBE.w, gy, CUBE_Z0 + CUBE_H], P), { tone: "faint" }));
  }

  // Nodos numéricos en esquinas de malla (esferas de integración de Navier-Stokes)
  const gridNodes = [
    c001, c101, c011, c111,
    [CUBE.x + CUBE.w / 2, CUBE.y + CUBE.d / 2, CUBE_Z0 + CUBE_H]
  ];
  for (const node of gridNodes) {
    parts.push(S(k.cylinder(node[0], node[1], 2.8, node[2] - 1, 3, P, 16), { tone: "mid" }));
    parts.push(D([at([node[0], node[1], node[2] + 2])], { size: 0.6, tone: "hi" }));
  }

  // Flecha / Vector de flujo orográfico / sesgo térmico atravesando la celda
  const flowFrom = [CUBE.x + 10, CUBE.y - 15, CUBE_Z0 + CUBE_H / 2];
  const flowTo = [CUBE.x + CUBE.w - 10, CUBE.y + CUBE.d + 15, CUBE_Z0 + CUBE_H / 2];
  parts.push(L(k.segment(flowFrom, flowTo, P), { tone: "red" }));

  // 6. Placas y leyendas grabadas en la máquina
  const plateTextLocal = at([TOWER[0] - 18, TOWER[1] + 35, 0]);
  const plateTextGlobal = at([CUBE.x + 15, CUBE.y + CUBE.d + 15, 0]);

  // Retornar SVG completo formateado
  return `
<svg class="iso-svg" viewBox="0 0 ${WIDTH} ${HEIGHT}" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="iso-blur" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6"/>
    </filter>
  </defs>
  ${parts.join("\n  ")}
  <g class="iso-face-text" data-tone="hi">
    <text x="${plateTextLocal[0]}" y="${plateTextLocal[1]}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.08em">SENAMHI PUNCHANA (2m)</text>
    <text x="${plateTextLocal[0]}" y="${plateTextLocal[1] + 13}" font-size="9" fill="var(--anatomy-mid)" text-anchor="middle">MAE ML: 1.88 °C (Local)</text>
  </g>
  <g class="iso-face-text" data-tone="hi">
    <text x="${plateTextGlobal[0]}" y="${plateTextGlobal[1]}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.08em">CELDA NWP (ECMWF ~9km / GFS ~28km)</text>
    <text x="${plateTextGlobal[0]}" y="${plateTextGlobal[1] + 13}" font-size="9" fill="var(--anatomy-red)" text-anchor="middle">SESGO SISTEMÁTICO: +2.58 °C</text>
  </g>
</svg>`;
}

const svgOut = buildFigure();
writeFileSync(join(process.cwd(), "front/components/anatomy/anatomy_estacion_vs_malla.svg"), svgOut);
console.log("Generado con éxito: front/components/anatomy/anatomy_estacion_vs_malla.svg");
