from playwright.async_api import async_playwright
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
    "Mozilla/5.0 (X11; Linux x86_64)...",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0)..."
]

async def create_stealth_browser():
    p = await async_playwright().start()
    random_user_agent = random.choice(user_agents)

    browser = await p.chromium.launch(headless=False)

    context = await browser.new_context(
        user_agent=random_user_agent,
        viewport={"width": 1280, "height": 720},
        locale="en-US",
        geolocation={"longitude": 74.3587, "latitude": 31.5204},
        permissions=["geolocation"]
    )

    await context.set_extra_http_headers({
        "Accept-Language": "en-US,en;q=0.9",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document"
    })

    page = await context.new_page()
    return browser, context, page
  
