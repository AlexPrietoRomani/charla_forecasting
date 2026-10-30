import os
import asyncio
from playwright.async_api import async_playwright

async def main():
    os.makedirs('screenshots', exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, channel="msedge")
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        
        url = 'file:///' + os.path.abspath('presentacion.html').replace('\\', '/')
        await page.goto(url, wait_until='networkidle')
        await page.wait_for_timeout(1000)

        slides_to_capture = [4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 24]
        for s in slides_to_capture:
            await page.evaluate(f'updateSlide({s - 1})')
            await page.wait_for_timeout(800)
            path = f'screenshots/slide_{s:02d}.png'
            await page.screenshot(path=path)
            print(f'Captured: {path}')

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
