"""Audita el layout de cada diapositiva: captura PNG y mide espacio vacio por panel."""
import os
import time
from playwright.sync_api import sync_playwright

OUT = "docs/audit_layout"
JS = """(i) => {
  const s = document.querySelector(`.slide[data-index="${i}"]`);
  const r = (el) => {
    if (!el) return null;
    const b = el.getBoundingClientRect();
    let maxBottom = b.top;
    el.querySelectorAll('*').forEach(c => {
      const cb = c.getBoundingClientRect();
      if (cb.height > 0 && cb.bottom > maxBottom && cb.bottom <= b.bottom + 2) maxBottom = cb.bottom;
    });
    const empty = Math.max(0, b.bottom - maxBottom);
    return {h: Math.round(b.height), w: Math.round(b.width), emptyPx: Math.round(empty), emptyPct: Math.round(100*empty/b.height)};
  };
  return {narr: r(s.querySelector('.panel-narrative')), vis: r(s.querySelector('.visual-card'))};
}"""


def run():
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe", headless=True)
        page = b.new_context(viewport={"width": 1920, "height": 1080}).new_page()
        page.goto("http://localhost:8000/presentacion.html", wait_until="networkidle")
        n = page.locator(".slide").count()
        for i in range(1, n + 1):
            page.evaluate(f"updateSlide({i})")
            time.sleep(0.9)
            m = page.evaluate(JS, i)
            page.screenshot(path=f"{OUT}/slide_{i:02d}.png")
            print(i, m)
        b.close()


if __name__ == "__main__":
    run()
