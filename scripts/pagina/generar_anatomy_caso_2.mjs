import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import * as k from "/home/aprietor/.gemini/antigravity-cli/skills/anatomy/kit/iso-kit.mjs";

const WIDTH = 840;
const HEIGHT = 560;

// Escena: Agro-observatorio de Precisión en Jaén (Café bajo Sombra)
// Distribución espacial en cuadrantes claros:
// Base: -150..150 x, -110..110 y
// Izquierda abajo (y: 20..60, x: -120..20): Cafetos en sotobosque con cerezas rojas
// Centro-derecha (x: 20, y: -20): Árboles de sombra (Pacae) elevándose
// Izquierda arriba (x: -95, y: -45, z: 125): Nube orográfica amazónica
// Centro-izquierda arriba (x: -45, y: 15, z: 85): Dron multiespectral volando a 25m
// Derecha arriba (x: 85, y: -45, z: 150): Satélite MODIS con paneles solares
const BASE = { x: -150, y: -110, w: 300, d: 220, r: 8 };
const BASE_H = 12;
const FOOT_H = 6;

// Satélite MODIS (Órbita alta en esquina superior derecha)
const SAT = [ 95, -35, 165 ];

// Dron multiespectral (Despejado en zona media-izquierda sobre los cafetos)
const DRONE = [ -60, 20, 80 ];

// Nube orográfica (Aislada en cuadrante superior izquierdo)
const CLOUD_CENTERS = [
  { x: -95, y: -55, z: 125, rx: 36, ry: 22, h: 14 }
];

// Árboles de sombra (Pacae / Guaba)
const SHADE_TREES = [
  { x: -10, y: -45, r: 24, z: 46, h: 26 },
  { x: 50, y: -20, r: 28, z: 52, h: 30 }
];

// Cafetos en sotobosque
const COFFEE_PLANTS = [
  { x: -115, y: -10, r: 13, h: 25 },
  { x: -80, y: -10, r: 14, h: 26 },
  { x: -120, y: 40, r: 13, h: 25 },
  { x: -80, y: 45, r: 15, h: 28 },
  { x: -35, y: 45, r: 15, h: 27 },
  { x: 10, y: 40, r: 14, h: 26 },
  { x: 55, y: 40, r: 14, h: 25 },
  { x: 95, y: 35, r: 13, h: 24 }
];

const P = k.fitProjection(
  [
    ...k.boxCorners(BASE, -BASE_H - FOOT_H, 0),
    [SAT[0] + 34, SAT[1] + 30, SAT[2] + 25],
    [SAT[0] - 34, SAT[1] - 30, SAT[2] - 20],
    [DRONE[0] - 24, DRONE[1] - 24, DRONE[2] + 20],
    [DRONE[0] + 24, DRONE[1] + 24, DRONE[2] - 20],
    [CLOUD_CENTERS[0].x - 35, CLOUD_CENTERS[0].y, CLOUD_CENTERS[0].z + 20],
    [CLOUD_CENTERS[0].x + 35, CLOUD_CENTERS[0].y, CLOUD_CENTERS[0].z - 15]
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

  // 1. Base instrumental
  parts.push(`<path class="iso-halo" d="${k.haloOf(BASE, -BASE_H - FOOT_H, BASE_H, P)}"/>`);

  for (const [x, y] of byDepth(k.corners(BASE, 20))) {
    parts.push(S(k.cylinder(x, y, 9, -BASE_H - FOOT_H, 2, P, 28), { tone: "lo" }));
    parts.push(S(k.cylinder(x, y, 7, -BASE_H - FOOT_H + 2, FOOT_H - 2, P, 28), { tone: "mid" }));
  }

  parts.push(S(k.slabOf(BASE, -BASE_H, BASE_H, P, 8, 1.8), { tone: "mid" }));
  parts.push(L(k.planOutline(k.insetPlan(BASE, 6), 0, P), { tone: "lo" }));

  const screws = k.corners(BASE, 12);
  parts.push(L(screws.map(([x, y]) => k.ring(x, y, 2.5, 0, P, 16)).join(""), { tone: "lo" }));
  parts.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 0.5 }));

  // Surcos agrícolas
  for (let dy = -85; dy <= 85; dy += 18) {
    parts.push(L(k.segment([-125, dy, 0.4], [125, dy, 0.4], P), { tone: "faint" }));
  }

  // 2. Cafetos en el sotobosque
  for (const p of COFFEE_PLANTS) {
    parts.push(S(k.cylinder(p.x, p.y, 1.8, 0, p.h * 0.45, P, 16), { tone: "lo" }));
    parts.push(S(k.cylinder(p.x, p.y, p.r, p.h * 0.35, p.h * 0.3, P, 24), { tone: "mid" }));
    parts.push(S(k.cylinder(p.x, p.y, p.r * 0.75, p.h * 0.65, p.h * 0.25, P, 20), { tone: "hi" }));
    parts.push(S(k.cylinder(p.x, p.y, p.r * 0.45, p.h * 0.9, p.h * 0.18, P, 16), { tone: "hi", lit: true }));

    // Cerezas rojas
    const angles = [0, 50, 100, 150, 200, 250, 300];
    for (let i = 0; i < angles.length; i++) {
      const rad = angles[i] * (Math.PI / 180);
      const bx = p.x + (p.r * 0.68) * Math.cos(rad);
      const by = p.y + (p.r * 0.68) * Math.sin(rad);
      const bz = p.h * (0.42 + (i % 3) * 0.12);
      const bpt = at([bx, by, bz]);
      parts.push(`<circle cx="${bpt[0]}" cy="${bpt[1]}" r="2.2" fill="var(--anatomy-red)" stroke="var(--anatomy-shade-0)" stroke-width="0.5"/>`);
    }
  }

  // 3. Dosel Superior de Sombra (Pacae)
  for (const tree of SHADE_TREES) {
    parts.push(S(k.cylinder(tree.x, tree.y, 5, 0, tree.z, P, 20), { tone: "lo" }));
    for (const rz of [15, 30]) {
      parts.push(L(k.ring(tree.x, tree.y, 5.2, rz, P, 20), { tone: "faint" }));
    }
    const arm1 = [tree.x - 12, tree.y - 10, tree.z - 4];
    const arm2 = [tree.x + 14, tree.y + 12, tree.z - 4];
    parts.push(L(k.segment([tree.x, tree.y, tree.z - 10], arm1, P), { tone: "mid" }));
    parts.push(L(k.segment([tree.x, tree.y, tree.z - 10], arm2, P), { tone: "mid" }));

    parts.push(S(k.cylinder(tree.x, tree.y, tree.r, tree.z, tree.h * 0.5, P, 32), { tone: "mid" }));
    parts.push(S(k.cylinder(tree.x, tree.y, tree.r * 0.85, tree.z + tree.h * 0.45, tree.h * 0.45, P, 28), { tone: "hi", lit: true }));
    parts.push(L(k.ring(tree.x, tree.y, tree.r * 0.85, tree.z + tree.h * 0.9, P, 28), { tone: "green" }));
  }

  // 4. Nube Orográfica Amazónica (Izquierda alta)
  for (const c of CLOUD_CENTERS) {
    for (let step = 0; step < 3; step++) {
      const cz = c.z + step * 3.5;
      const crx = c.rx - step * 3.5;
      const cry = c.ry - step * 2;
      const cplan = { x: c.x - crx, y: c.y - cry, w: crx * 2, d: cry * 2, r: cry * 0.8 };
      parts.push(S(k.slabOf(cplan, cz, 3.5, P, 6, 0.5), { tone: step === 2 ? "hi" : "mid" }));
    }
    parts.push(L(k.ring(c.x, c.y, c.rx * 0.7, c.z + c.h, P, 20), { tone: "faint" }));
  }

  // 5. Dron Multiespectral (Flotando a 25m sobre cafetos)
  const dBody = { x: DRONE[0] - 8, y: DRONE[1] - 8, w: 16, d: 16, r: 3 };
  parts.push(S(k.slabOf(dBody, DRONE[2], 5, P, 4, 0.6), { tone: "hi", lit: true }));
  parts.push(S(k.cylinder(DRONE[0], DRONE[1], 2.2, DRONE[2] + 5, 4, P, 16), { tone: "hi" }));
  parts.push(D([at([DRONE[0], DRONE[1], DRONE[2] + 9])], { size: 0.6, tone: "hi" }));

  const armLen = 16;
  const rotorPos = [
    [DRONE[0] - armLen, DRONE[1] - armLen],
    [DRONE[0] + armLen, DRONE[1] - armLen],
    [DRONE[0] - armLen, DRONE[1] + armLen],
    [DRONE[0] + armLen, DRONE[1] + armLen]
  ];
  for (const [rx, ry] of rotorPos) {
    parts.push(L(k.segment([DRONE[0], DRONE[1], DRONE[2] + 2], [rx, ry, DRONE[2] + 2], P), { tone: "mid" }));
    parts.push(S(k.cylinder(rx, ry, 2.5, DRONE[2] + 1, 4, P, 16), { tone: "mid" }));
    parts.push(L(k.ring(rx, ry, 6.5, DRONE[2] + 5, P, 20), { tone: "blue" }));
  }
  parts.push(S(k.cylinder(DRONE[0], DRONE[1], 2.8, DRONE[2] - 4, 4, P, 16), { tone: "lo" }));
  const droneTarget = [ DRONE[0], DRONE[1], 28 ];
  parts.push(L(k.segment([DRONE[0], DRONE[1], DRONE[2] - 4], [droneTarget[0] - 12, droneTarget[1] - 12, droneTarget[2]], P), { tone: "blue" }));
  parts.push(L(k.segment([DRONE[0], DRONE[1], DRONE[2] - 4], [droneTarget[0] + 12, droneTarget[1] + 12, droneTarget[2]], P), { tone: "blue" }));

  // 6. Satélite Espacial MODIS (Derecha alta)
  const satBody = { x: SAT[0] - 14, y: SAT[1] - 12, w: 28, d: 24, r: 2 };
  parts.push(S(k.slabOf(satBody, SAT[2], 18, P, 4, 0.8), { tone: "hi", lit: true }));

  const panelL = { x: SAT[0] - 48, y: SAT[1] - 10, w: 32, d: 20, r: 1.2 };
  parts.push(S(k.slabOf(panelL, SAT[2] + 8, 2.2, P, 2, 0.3), { tone: "mid" }));
  for (let step = 1; step <= 3; step++) {
    const px = panelL.x + (panelL.w / 4) * step;
    parts.push(L(k.segment([px, panelL.y, SAT[2] + 10.2], [px, panelL.y + panelL.d, SAT[2] + 10.2], P), { tone: "blue" }));
  }

  const panelR = { x: SAT[0] + 16, y: SAT[1] - 10, w: 32, d: 20, r: 1.2 };
  parts.push(S(k.slabOf(panelR, SAT[2] + 8, 2.2, P, 2, 0.3), { tone: "mid" }));
  for (let step = 1; step <= 3; step++) {
    const px = panelR.x + (panelR.w / 4) * step;
    parts.push(L(k.segment([px, panelR.y, SAT[2] + 10.2], [px, panelR.y + panelR.d, SAT[2] + 10.2], P), { tone: "blue" }));
  }

  parts.push(S(k.cylinder(SAT[0], SAT[1], 5.5, SAT[2] - 8, 8, P, 24), { tone: "hi", lit: true }));
  parts.push(L(k.ring(SAT[0], SAT[1], 5.5, SAT[2] - 8, P, 24), { tone: "lit" }));

  const antPos = [ SAT[0] - 6, SAT[1] - 16, SAT[2] + 18 ];
  parts.push(S(k.cylinder(antPos[0], antPos[1], 1.5, antPos[2], 8, P, 16), { tone: "mid" }));
  parts.push(S(k.cylinder(antPos[0], antPos[1], 5.5, antPos[2] + 8, 2.5, P, 24), { tone: "hi" }));

  // Haz satelital verde hacia la copa de sombra
  const satBeam = [ SHADE_TREES[1].x, SHADE_TREES[1].y, SHADE_TREES[1].z + SHADE_TREES[1].h ];
  parts.push(L(k.segment([SAT[0], SAT[1], SAT[2] - 8], satBeam, P), { tone: "green" }));

  // 7. Textos técnicos con etiquetas bien ubicadas sin solapamiento
  const tagSat = at([SAT[0] - 10, SAT[1] - 30, SAT[2] + 45]);
  const tagCloud = at([CLOUD_CENTERS[0].x, CLOUD_CENTERS[0].y + 36, CLOUD_CENTERS[0].z + 10]);
  const tagDrone = at([DRONE[0] - 42, DRONE[1] - 8, DRONE[2] + 22]);
  const tagCanopy = at([SHADE_TREES[1].x + 36, SHADE_TREES[1].y + 16, SHADE_TREES[1].z + 28]);
  const tagCoffee = at([0, 80, 0]);

  const bodyContent = `
  ${parts.join("\n  ")}
  <g class="iso-face-text" data-tone="hi">
    <text x="${tagSat[0]}" y="${tagSat[1]}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.08em">MODIS TERRA/AQUA (705 km)</text>
    <text x="${tagSat[0]}" y="${tagSat[1] + 13}" font-size="9" fill="var(--anatomy-blue)" text-anchor="middle">NDVI ÓPTICO RED/NIR · PIXEL 250m</text>
  </g>
  <g class="iso-face-text" data-tone="hi">
    <text x="${tagCloud[0]}" y="${tagCloud[1]}" font-size="10" font-weight="700" text-anchor="middle" letter-spacing="0.06em">COBERTURA DE NUBES</text>
    <text x="${tagCloud[0]}" y="${tagCloud[1] + 12}" font-size="8.5" fill="var(--anatomy-muted)" text-anchor="middle">CONTAMINACIÓN ESPECTRAL &amp; NEBLINA</text>
  </g>
  <g class="iso-face-text" data-tone="hi">
    <text x="${tagDrone[0]}" y="${tagDrone[1]}" font-size="10.5" font-weight="700" text-anchor="middle" letter-spacing="0.06em">DRON MULTIESPECTRAL (25m)</text>
    <text x="${tagDrone[0]}" y="${tagDrone[1] + 12}" font-size="8.5" fill="var(--anatomy-blue)" text-anchor="middle">RESOLUCIÓN SUB-CENTIMÉTRICA</text>
  </g>
  <g class="iso-face-text" data-tone="hi">
    <text x="${tagCanopy[0]}" y="${tagCanopy[1]}" font-size="10.5" font-weight="700" text-anchor="middle" letter-spacing="0.06em">DOSEL DE SOMBRA (PACAE)</text>
    <text x="${tagCanopy[0]}" y="${tagCanopy[1] + 12}" font-size="8.5" fill="var(--anatomy-green)" text-anchor="middle">SATURACIÓN EN COPA (NDVI ~0.80)</text>
  </g>
  <g class="iso-face-text" data-tone="hi">
    <text x="${tagCoffee[0]}" y="${tagCoffee[1]}" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.08em">CAFETOS EN SOTOBOSQUE (COSECHA REAL)</text>
    <text x="${tagCoffee[0]}" y="${tagCoffee[1] + 13}" font-size="9" fill="var(--anatomy-red)" text-anchor="middle">OCULTO AL SATÉLITE · AFECTADO POR ROYA Y DÉFICIT HÍDRICO</text>
  </g>`;

  return k.figureSvg({ body: bodyContent, standalone: "dark", width: WIDTH, height: HEIGHT });
}

const svgOut = buildFigure();
writeFileSync(join(process.cwd(), "front/components/anatomy/anatomy_cafe_sombra_ndvi.svg"), svgOut);
console.log("Generado con éxito con distribución armónica: front/components/anatomy/anatomy_cafe_sombra_ndvi.svg");
