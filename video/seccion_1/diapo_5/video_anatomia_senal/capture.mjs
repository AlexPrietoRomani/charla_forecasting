#!/usr/bin/env node
import { spawn } from "node:child_process";
import { mkdirSync, writeFileSync, readFileSync, rmSync, existsSync, readdirSync, unlinkSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";

const [sceneArg, outArg, fpsArg, durMsArg, startMsArg, timeScaleArg] = process.argv.slice(2);
if (!sceneArg || !outArg) {
  console.error("uso: node capture.mjs <scene.html> <framesDir> [fps=30] [durationMs=30000] [startMs=0] [timeScale=1]");
  process.exit(2);
}
const scene = resolve(sceneArg);
const outDir = resolve(outArg);
const fps = Number(fpsArg || 30);
const durMs = Number(durMsArg || 30000);
const startMs = Number(startMsArg || 0);
const timeScale = Number(timeScaleArg || 1);
const totalFrames = Math.round((durMs / 1000) * fps);

mkdirSync(outDir, { recursive: true });
for (const f of readdirSync(outDir)) if (f.endsWith(".png")) unlinkSync(join(outDir, f));

const profile = join(tmpdir(), `chrome-cdp-${process.pid}`);
rmSync(profile, { recursive: true, force: true });
mkdirSync(profile, { recursive: true });

const chrome = spawn("chromium", [
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
  deviceScaleFactor: 1,
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
    if (w !== 1600 || h !== 900) {
      console.error(`frame inesperado ${w}x${h}`); cleanup(1);
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
