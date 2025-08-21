from playwright.async_api import async_playwright
import time 
import random 
from browser_config import browser_stealth  
import asyncio
async def filter_automation ():
    browser, context, page = await browser_stealth()
    
    #open page 
    await page.goto("https://basketball.exposureevents.com/youth-basketball-events")
    
    #click filters
    await page.wait_for_selector("button.btn.btn-secondary", state="visible",timeout=0)
    await asyncio.sleep(random.uniform(0.5, 1.5))
    await page.click("button.btn.btn-secondary")
    
    #scroll
    await page.mouse.wheel(0, 300)
    await asyncio.sleep(random.uniform(0.5, 1))

    # Fill Start Date
    await page.click("#StartDateString", click_count=3)  # triple click to select
    await page.keyboard.press("Backspace")               # clear
    await page.type("#StartDateString", "01/01/2025", delay=100)


    # Fill End Date
    await page.type("#EndDateString", "12/31/2025",delay=100)
    await asyncio.sleep(random.uniform(0.5, 1))
    await page.select_option("#EventType", "Tournament")
    
    #search
    await page.click("button:has-text('Search')")
    await asyncio.sleep(random.uniform(2, 3))
    await asyncio.sleep(5) 
    
    return browser , context ,page

