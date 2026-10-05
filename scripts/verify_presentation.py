import sys
import time
from playwright.sync_api import sync_playwright

def verify():
    console_errors = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe", headless=True)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()
        
        # Listen for console events
        page.on("console", lambda msg: console_errors.append(f"[{msg.type}] {msg.text}") if msg.type in ['error', 'warning'] else None)
        page.on("pageerror", lambda exc: console_errors.append(f"[pageerror] {exc}"))
        
        print("Navigating to http://localhost:8000/presentacion.html...")
        page.goto("http://localhost:8000/presentacion.html", wait_until="networkidle")
        
        # Check number of slides
        slides = page.locator(".slide")
        count = slides.count()
        print(f"Total slides found: {count}")
        
        # Step through every slide and take screenshots of data-heavy slides
        results = []
        for i in range(1, count + 1):
            # activate slide i
            page.evaluate(f"updateSlide({i})")
            time.sleep(0.4)
            
            # check current slide
            slide_sel = f".slide[data-index=\"{i}\"]"
            canvas_count = page.locator(f"{slide_sel} canvas").count()
            svg_count = page.locator(f"{slide_sel} svg").count()
            
            # Check if charts inside this slide rendered (e.g. Chart instance exists)
            chart_status = page.evaluate(f"""() => {{
                const canvases = document.querySelectorAll('{slide_sel} canvas');
                return Array.from(canvases).map(c => {{
                    return {{
                        id: c.id,
                        width: c.width,
                        height: c.height,
                        hasData: c.width > 0 && c.height > 0
                    }};
                }});
            }}""")
            
            results.append({
                "slide_idx": i,
                "slide_id": slide_sel,
                "canvas_count": canvas_count,
                "svg_count": svg_count,
                "charts": chart_status
            })
            
            page.screenshot(path=f"slide_{i:02d}.png")
            print(f"Captured screenshot slide_{i:02d}.png")
                
        browser.close()
        
    print("\n--- RESULTS ---")
    for r in results:
        print(f"Slide {r['slide_idx']:02d} ({r['slide_id']}): {r['canvas_count']} canvas, {r['svg_count']} svg, charts: {r['charts']}")
        
    print(f"\nTotal Console Warnings/Errors: {len(console_errors)}")
    for err in console_errors:
        print(f"  {err}")

if __name__ == "__main__":
    verify()
