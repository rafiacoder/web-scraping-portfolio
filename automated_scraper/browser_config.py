from playwright.async_api import async_playwright
import random 
import asyncio
#useragents 
useragents=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows 7 Enterprise; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6099.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Edge/79.0.1451.30 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0",
    "Mozilla/5.0 (Windows NT 6.2; rv:109.0) Gecko/20100101 Firefox/111.0",
    "Mozilla/5.0 (Windows Server 2012 R2 Standard; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5975.80 Safari/537.36"
]
#proxies 
proxy = {"server": "http://p.webshare.io:80",
         "username":"ibxavsku-rotate",
          "password":"b43bhob1awce"}
#create_stealth_browser
async def create_stealth_browser():
    playwright = await async_playwright().start()

    browser = await playwright.chromium.launch(headless=False,proxy=proxy)
    random_ua = random.choice(useragents)
    context = await browser.new_context(
        user_agent=random_ua,
        viewport={"width": 1280, "height": 800},
        locale="en-US",
        timezone_id="Asia/Karachi",
        geolocation={"longitude": 74.3587, "latitude": 31.5204},  # Lahore
        permissions=["geolocation"],
    )
#custom headers 
    await context.set_extra_http_headers({
        "Accept-Language": "en-US,en;q=0.9",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document"
    })
#open page and random wait & scroll 
    page = await context.new_page()
    await page.goto("https://www.dawn.com/latest-news", wait_until="domcontentloaded")
    await asyncio.sleep(random.uniform(2, 5)) 
    scroll_y=random.randint(200,1000)
    await page.evaluate(f"window.scrollBy(0, {scroll_y});")
    return browser, context, page
    