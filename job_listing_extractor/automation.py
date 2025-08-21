from playwright.async_api import async_playwright
import asyncio
import random
from browser_config import create_stealth_browser

async def perform_automation():
    browser, context, page = await create_stealth_browser()
    await page.goto("https://www.rozee.pk/", wait_until="domcontentloaded")
    await page.mouse.move(100, 250, steps=30)

    search_box = page.locator("#search")
    await search_box.click()
    await page.keyboard.type("Python Developer", delay=100)
    await asyncio.sleep(random.uniform(1.5, 3.0))

    try:
        await page.locator('[data-id="homeSearchCity"]').click()
        await page.locator(".form-control").nth(2).fill("Lahore")
        await page.keyboard.press("Enter")
        await asyncio.sleep(random.uniform(1.0, 4.0))
    except Exception as e:
        print(f"City input error: {e}")
    await asyncio.sleep(random.uniform(1.0, 3.5))
    
    try:
        await page.locator('[title="Min. Salary"]').click()
        await page.wait_for_timeout(1000)
        salary_options = page.locator(".dropdown-menu.inner li")
        count = await salary_options.count()
        for i in range(count):
            option = salary_options.nth(i)
            text = (await option.inner_text()).strip()
            if text == "8,000":
                await option.scroll_into_view_if_needed()
                await page.wait_for_timeout(5000)
                await option.click()
                break
    except Exception as e:
        print(f"Salary not found: {e}")
        
    await page.click('[type="submit"]')
    await asyncio.sleep(random.uniform(1.0, 6.0))
    await page.mouse.wheel(0, 300)
    await asyncio.sleep(random.uniform(1.0, 2.0))
    return page,browser,context
