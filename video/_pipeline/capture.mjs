#!/usr/bin/env node
import { spawn, spawnSync } from "node:child_process";
import { mkdirSync, writeFileSync, readFileSync, rmSync, existsSync, readdirSync, unlinkSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";

// Orden de búsqueda: CHROME_BIN → chromium de playwright (Python) → Edge → chromium/chrome en PATH.
const EDGE_PATHS = [
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
  "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
];
const PLAYWRIGHT_PROBE =
  "from playwright.sync_api import sync_playwright; p = sync_playwright().start(); print(p.chromium.executable_path); p.stop()";

function firstExisting(paths) {
  return paths.find((p) => existsSync(p)) || null;
}

function fromPlaywright() {
  // Respeta PYTHON_BIN (render.py lo fija a sys.executable); sin él usa `python` del PATH.
  const result = spawnSync(process.env.PYTHON_BIN || "python", ["-c", PLAYWRIGHT_PROBE], { encoding: "utf8" });
  if (result.error || result.status !== 0) return null;
  const lines = result.stdout.split("\n").map((l) => l.trim()).filter(Boolean);
  return firstExisting([lines[lines.length - 1] || ""]);
}

function fromPath(name) {
  const finder = process.platform === "win32" ? "where" : "which";
  const result = spawnSync(finder, [name], { encoding: "utf8" });
  if (result.error || result.status !== 0) return null;
  return result.stdout.split("\n").map((l) => l.trim()).find(Boolean) || null;
}

function resolveBrowser() {
  if (process.env.CHROME_BIN) {
    if (existsSync(process.env.CHROME_BIN)) return process.env.CHROME_BIN;
    throw new Error(`CHROME_BIN apunta a un ejecutable inexistente: ${process.env.CHROME_BIN}`);
  }
  const found =
    fromPlaywright() ||
    firstExisting(EDGE_PATHS) ||
    fromPath("chromium") ||
    fromPath("google-chrome");
  if (!found) {
    throw new Error("no hay navegador: define CHROME_BIN, instala playwright (chromium) o Edge");
  }
  return found;
}

const [sceneArg, outArg, fpsArg, durMsArg, startMsArg, timeScaleArg, dprArg] = process.argv.slice(2);
if (!sceneArg || !outArg) {
  console.error("uso: node capture.mjs <scene.html> <framesDir> [fps=30] [durationMs=30000] [startMs=0] [timeScale=1] [dpr=1]");
  process.exit(2);
}
const scene = resolve(sceneArg);
const outDir = resolve(outArg);
const fps = Number(fpsArg || 30);
const durMs = Number(durMsArg || 30000);
const startMs = Number(startMsArg || 0);
const timeScale = Number(timeScaleArg || 1);
const dpr = Number(dprArg || 1);
const totalFrames = Math.round((durMs / 1000) * fps);

mkdirSync(outDir, { recursive: true });
for (const f of readdirSync(outDir)) if (f.endsWith(".png")) unlinkSync(join(outDir, f));

const profile = join(tmpdir(), `chrome-cdp-${process.pid}`);
rmSync(profile, { recursive: true, force: true });
mkdirSync(profile, { recursive: true });

const browserBin = resolveBrowser();
console.log(`navegador: ${browserBin}`);
const chrome = spawn(browserBin, [
  "--headless",
  "--no-sandbox",
  "--disable-gpu",
  "--disable-dev-shm-usage",
  "--hide-scrollbars",
  "--window-size=1600,900",
  "--force-device-scale-factor=1",
  "--no-first-run",
  "--disable-extensions",
  "--remote-allow-origins=*",
  "--remote-debugging-port=0",
  `--user-data-dir=${profile}`,
  `file://${scene}`,
], { stdio: ["ignore", "ignore", "pipe"] });

let chromeErr = "";
chrome.stderr.on("data", (d) => { chromeErr += d.toString(); });

function cleanup(code) {
  try { chrome.kill("SIGTERM"); } catch {}
  setTimeout(() => {
    try { chrome.kill("SIGKILL"); } catch {}
    rmSync(profile, { recursive: true, force: true });
    process.exit(code);
  }, 400);
}

const portFile = join(profile, "DevToolsActivePort");
const t0 = Date.now();
while (!existsSync(portFile)) {
  if (Date.now() - t0 > 15000) {
    console.error("timeout esperando DevToolsActivePort\n", chromeErr.slice(-2000));
    cleanup(1);
  }
  await new Promise((r) => setTimeout(r, 100));
}
const port = readFileSync(portFile, "utf8").split("\n")[0].trim();

const targets = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
const page = targets.find((tg) => tg.type === "page");
if (!page) { console.error("no page target", targets); cleanup(1); }

const ws = new WebSocket(page.webSocketDebuggerUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });

let seq = 0;
const pending = new Map();
ws.onmessage = (ev) => {
  const msg = JSON.parse(ev.data);
  if (msg.id && pending.has(msg.id)) {
    const { res, rej } = pending.get(msg.id);
    pending.delete(msg.id);
    msg.error ? rej(new Error(JSON.stringify(msg.error))) : res(msg.result);
  }
};
function cdp(method, params = {}) {
  const id = ++seq;
  ws.send(JSON.stringify({ id, method, params }));
  return new Promise((res, rej) => pending.set(id, { res, rej }));
}

await cdp("Page.enable");
await cdp("Runtime.enable");
await cdp("Emulation.setDeviceMetricsOverride", {
  width: 1600,
  height: 900,
  deviceScaleFactor: dpr,
  mobile: false,
});

const readyT0 = Date.now();
for (;;) {
  const r = await cdp("Runtime.evaluate", { expression: "window.__ready === true", returnByValue: true });
  if (r.result?.value === true) break;
  if (Date.now() - readyT0 > 15000) { console.error("timeout esperando __ready"); cleanup(1); }
  await new Promise((rr) => setTimeout(rr, 120));
}

const tStart = Date.now();
for (let i = 0; i < totalFrames; i++) {
  const ms = Math.round(startMs + (i * 1000) / fps / timeScale);
  await cdp("Runtime.evaluate", { expression: `window.__setTime(${ms})` });
  const shot = await cdp("Page.captureScreenshot", {
    format: "png",
    captureBeyondViewport: false,
    optimizeForSpeed: true,
  });
  const buf = Buffer.from(shot.data, "base64");
  if (i === 0) {
    const w = buf.readUInt32BE(16), h = buf.readUInt32BE(20);
    const expW = Math.round(1600 * dpr), expH = Math.round(900 * dpr);
    if (w !== expW || h !== expH) {
      console.error(`frame inesperado ${w}x${h} (esperado ${expW}x${expH})`); cleanup(1);
    }
  }
  writeFileSync(join(outDir, `f${String(i + 1).padStart(5, "0")}.png`), buf);
  if ((i + 1) % 60 === 0 || i === totalFrames - 1) {
    const el = (Date.now() - tStart) / 1000;
    const rate = (i + 1) / el;
    const eta = Math.max(0, (totalFrames - i - 1) / rate);
    console.log(`frame ${i + 1}/${totalFrames} · ${rate.toFixed(1)} fps render · ETA ${eta.toFixed(0)}s`);
  }
}

console.log(`OK ${totalFrames} frames en ${((Date.now() - tStart) / 1000).toFixed(0)}s → ${outDir}`);
cleanup(0);
