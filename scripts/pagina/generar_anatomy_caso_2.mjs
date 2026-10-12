import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import * as k from "/home/aprietor/.gemini/antigravity-cli/skills/anatomy/kit/iso-kit.mjs";

const WIDTH = 680;
const HEIGHT = 460;

// Escena: El Sistema Café bajo Sombra (Caso 2)
// 1. Suelo / Cuenca agrícola de Jaén
// 2. Estrato Arbóreo (Árboles de sombra / Pacae-Guaba)
// 3. Estrato Cafeto (Sotobosque con granos de café pergamino)
// 4. Sensor Satelital MODIS (NASA Terra/Aqua) en órbita observando solo la canopia superior
const BASE = { x: -130, y: -90, w: 260, d: 180, r: 8 };
const BASE_H = 10;
const FOOT_H = 5;

// Dosel de árboles de sombra (Guaba / Pacae)
const SHADE_TREES = [
  { x: -50, y: -30, r: 24, z: 50, h: 25 },
  { x: 30, y: -20, r: 28, z: 55, h: 28 }
];

// Plantas de café bajo sombra (Sotobosque vulnerable al déficit hídrico)
const COFFEE_BUSHES = [
  { x: -65, y: 15, r: 12, z: 0, h: 24 },
  { x: -30, y: 25, r: 14, z: 0, h: 26 },
  { x: 10, y: 20, r: 13, z: 0, h: 25 },
  { x: 50, y: 25, r: 12, z: 0, h: 23 }
];

// Satélite MODIS en la esquina superior derecha apuntando hacia abajo
const SAT_POS = [ 75, -55, 155 ];

const P = k.fitProjection(
  [
    ...k.boxCorners(BASE, -BASE_H - FOOT_H, 0),
    [SAT_POS[0] + 25, SAT_POS[1] + 25, SAT_POS[2] + 25],
    [SAT_POS[0] - 25, SAT_POS[1] - 25, SAT_POS[2] - 25]
  ],
  WIDTH,
  HEIGHT,
  { pad: 26, azimuth: 45, elevation: 32 }
);

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const byDepth = (points) => [...points].sort((a, b) => k.depthOf([a[0], a[1], 0], P) - k.depthOf([b[0], b[1], 0], P));

function buildFigure() {
  const parts = [];

  // 1. Halo base
  parts.push(`<path class="iso-halo" d="${k.haloOf(BASE, -BASE_H - FOOT_H, BASE_H, P)}"/>`);

  // 2. Patas
  for (const [x, y] of byDepth(k.corners(BASE, 18))) {
    parts.push(S(k.cylinder(x, y, 8, -BASE_H - FOOT_H, 2, P, 28), { tone: "lo" }));
    parts.push(S(k.cylinder(x, y, 6, -BASE_H - FOOT_H + 2, FOOT_H - 2, P, 28), { tone: "mid" }));
  }

  // 3. Mesa base / Suelo de cultivo
  parts.push(S(k.slabOf(BASE, -BASE_H, BASE_H, P, 8, 1.6), { tone: "mid" }));
  parts.push(L(k.planOutline(k.insetPlan(BASE, 5), 0, P), { tone: "lo" }));

  // Tornillos base
  const screws = k.corners(BASE, 10);
  parts.push(L(screws.map(([x, y]) => k.ring(x, y, 2.2, 0, P, 16)).join(""), { tone: "lo" }));
  parts.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 0.5 }));

  // Surcos agrícolas en el suelo (Jaén, 1,200 - 1,800 msnm)
  for (let dy = -60; dy <= 60; dy += 20) {
    parts.push(L(k.segment([-105, dy, 0.4], [105, dy, 0.4], P), { tone: "faint" }));
  }

  // 4. Plantas de Café en el sotobosque (Arbustos con bayas)
  for (const bush of COFFEE_BUSHES) {
    // Tallo
    parts.push(S(k.cylinder(bush.x, bush.y, 2, 0, bush.h * 0.4, P, 16), { tone: "lo" }));
    // Follaje del cafeto (forma de cono/cilindro escalonado)
    parts.push(S(k.cylinder(bush.x, bush.y, bush.r, bush.h * 0.35, bush.h * 0.45, P, 24), { tone: "mid" }));
    parts.push(S(k.cylinder(bush.x, bush.y, bush.r * 0.65, bush.h * 0.7, bush.h * 0.3, P, 20), { tone: "hi" }));
    // Bayas / cerezas de café (puntos rojos en ramas exteriores)
    const berryPts = [
      at([bush.x + bush.r * 0.7, bush.y, bush.h * 0.5]),
      at([bush.x - bush.r * 0.7, bush.y, bush.h * 0.45]),
      at([bush.x, bush.y + bush.r * 0.7, bush.h * 0.6]),
      at([bush.x, bush.y - bush.r * 0.7, bush.h * 0.55])
    ];
    for (const b of berryPts) {
      parts.push(`<circle cx="${b[0]}" cy="${b[1]}" r="2" fill="var(--anatomy-red)"/>`);
    }
  }

  // 5. Troncos y Dosel Superior de Sombra (Árboles de Pacae/Guaba)
  for (const tree of SHADE_TREES) {
    // Tronco alto que sobrepasa el café
    parts.push(S(k.cylinder(tree.x, tree.y, 4, 0, tree.z, P, 20), { tone: "lo" }));
    // Dosel denso de sombra (Copa amplia que cubre el campo)
    parts.push(S(k.cylinder(tree.x, tree.y, tree.r, tree.z, tree.h * 0.6, P, 32), { tone: "mid" }));
    parts.push(S(k.cylinder(tree.x, tree.y, tree.r * 0.8, tree.z + tree.h * 0.5, tree.h * 0.5, P, 28), { tone: "hi", lit: true }));
    // Anillo de follaje superior (la canopia que ve el satélite)
    parts.push(L(k.ring(tree.x, tree.y, tree.r * 0.8, tree.z + tree.h, P, 28), { tone: "green" }));
  }

  // 6. El Satélite MODIS (En órbita, chasis cúbico + paneles solares + lente espectral)
  // Cuerpo del satélite
  const satBody = { x: SAT_POS[0] - 12, y: SAT_POS[1] - 10, w: 24, d: 20, r: 2 };
  parts.push(S(k.slabOf(satBody, SAT_POS[2], 16, P, 4, 0.6), { tone: "hi" }));

  // Panel solar izquierdo
  const panelL = { x: SAT_POS[0] - 38, y: SAT_POS[1] - 8, w: 24, d: 16, r: 1 };
  parts.push(S(k.slabOf(panelL, SAT_POS[2] + 6, 2, P, 2), { tone: "mid" }));
  // Celdas solares fotovoltaicas
  parts.push(L(k.segment([panelL.x + 8, panelL.y, SAT_POS[2] + 8], [panelL.x + 8, panelL.y + panelL.d, SAT_POS[2] + 8], P), { tone: "blue" }));
  parts.push(L(k.segment([panelL.x + 16, panelL.y, SAT_POS[2] + 8], [panelL.x + 16, panelL.y + panelL.d, SAT_POS[2] + 8], P), { tone: "blue" }));

  // Panel solar derecho
  const panelR = { x: SAT_POS[0] + 14, y: SAT_POS[1] - 8, w: 24, d: 16, r: 1 };
  parts.push(S(k.slabOf(panelR, SAT_POS[2] + 6, 2, P, 2), { tone: "mid" }));
  parts.push(L(k.segment([panelR.x + 8, panelR.y, SAT_POS[2] + 8], [panelR.x + 8, panelR.y + panelR.d, SAT_POS[2] + 8], P), { tone: "blue" }));
  parts.push(L(k.segment([panelR.x + 16, panelR.y, SAT_POS[2] + 8], [panelR.x + 16, panelR.y + panelR.d, SAT_POS[2] + 8], P), { tone: "blue" }));

  // Sensor óptico MODIS apuntando hacia la tierra
  parts.push(S(k.cylinder(SAT_POS[0], SAT_POS[1], 4.5, SAT_POS[2] - 6, 6, P, 20), { tone: "hi", lit: true }));
  parts.push(L(k.ring(SAT_POS[0], SAT_POS[1], 4.5, SAT_POS[2] - 6, P, 20), { tone: "lit" }));

  // 7. Haz espectral / Rayo de visión MODIS (Pirámide de cono visual)
  // El rayo satelital impacta en el dosel superior (árboles), bloqueando la vista de los cafetos
  const rayTarget1 = [ SHADE_TREES[0].x, SHADE_TREES[0].y, SHADE_TREES[0].z + SHADE_TREES[0].h ];
  const rayTarget2 = [ SHADE_TREES[1].x, SHADE_TREES[1].y, SHADE_TREES[1].z + SHADE_TREES[1].h ];
  const rayTargetFloor = [ 10, 20, 0 ];

  parts.push(L(k.segment([SAT_POS[0], SAT_POS[1], SAT_POS[2] - 6], rayTarget1, P), { tone: "green" }));
  parts.push(L(k.segment([SAT_POS[0], SAT_POS[1], SAT_POS[2] - 6], rayTarget2, P), { tone: "green" }));
  // Línea punteada que intenta llegar al café pero se detiene/satura
  parts.push(L(k.segment(rayTarget2, rayTargetFloor, P), { tone: "faint" }));

  // 8. Textos y Badges técnicos grabados
  const textSat = at([SAT_POS[0] + 5, SAT_POS[1] + 25, SAT_POS[2] + 15]);
  const textCanopy = at([SHADE_TREES[1].x + 35, SHADE_TREES[1].y, SHADE_TREES[1].z + 30]);
  const textUnder = at([COFFEE_BUSHES[1].x, COFFEE_BUSHES[1].y + 25, 0]);

  return `
<svg class="iso-svg" viewBox="0 0 ${WIDTH} ${HEIGHT}" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  ${parts.join("\n  ")}
  <g class="iso-face-text" data-tone="hi">
    <text x="${textSat[0]}" y="${textSat[1]}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.08em">MODIS TERRA/AQUA (705 km)</text>
    <text x="${textSat[0]}" y="${textSat[1] + 13}" font-size="9" fill="var(--anatomy-blue)" text-anchor="middle">NDVI ÓPTICO RED/NIR</text>
  </g>
  <g class="iso-face-text" data-tone="hi">
    <text x="${textCanopy[0]}" y="${textCanopy[1]}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.08em">DOSEL DE SOMBRA (PACAE)</text>
    <text x="${textCanopy[0]}" y="${textCanopy[1] + 13}" font-size="9" fill="var(--anatomy-green)" text-anchor="middle">SATURACIÓN ESPECTRAL: NDVI ~0.80</text>
  </g>
  <g class="iso-face-text" data-tone="hi">
    <text x="${textUnder[0]}" y="${textUnder[1]}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.08em">CAFETOS EN SOTOBOSQUE (COSECHA REAL)</text>
    <text x="${textUnder[0]}" y="${textUnder[1] + 13}" font-size="9" fill="var(--anatomy-red)" text-anchor="middle">CEGUERA ANTE LA ROYA Y EL CLIMA FLORAL</text>
  </g>
</svg>`;
}

const svgOut = buildFigure();
writeFileSync(join(process.cwd(), "front/components/anatomy/anatomy_cafe_sombra_ndvi.svg"), svgOut);
console.log("Generado con éxito: front/components/anatomy/anatomy_cafe_sombra_ndvi.svg");
