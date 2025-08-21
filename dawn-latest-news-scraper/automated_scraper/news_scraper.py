from playwright.async_api import async_playwright
import random
import asyncio
from browser_config import create_stealth_browser
import json
async def check_and_close_cookie_popup(page):
    try:
        consent_button = page.locator("button.fc-cta-consent")
        if await consent_button.is_visible():
            await consent_button.click()
            print(" Cookie popup handled during scraping.")
    except:
        pass
#scraping function
async def news_scrape():
  browser,context,page= await create_stealth_browser()
  await check_and_close_cookie_popup(page)
  try:
   articles = await page.locator("article.story").all()
  except Exception:
      print("article not found")
  news_list=[]
  for article in articles:
     await check_and_close_cookie_popup(page)
     try:
         title = await article.locator("a.story__link").inner_text()
     except Exception: 
         title="not found"
      
     await asyncio.sleep(random.uniform(1.5, 3.5))   
     
     try:
         url = await article.locator("a.story__link").get_attribute("href")
     except Exception:
         url="not found"
         
     await asyncio.sleep(random.uniform(1.5, 3.5))
     
     try:
         summary = await article.locator("div.story__excerpt").inner_text()
     except Exception:
         summary ="not found"
         
     await asyncio.sleep(random.uniform(1.5, 3.5))
     
     try:
         timestamp = await article.locator("span.timestamp--time").get_attribute("title")
     except Exception:
         timestamp="not found"
     await asyncio.sleep(random.uniform(1.5, 3.5))
     
     news_list.append({
            "title": title,
            "url": url,
            "summary": summary,
            "timestamp": timestamp
        })
#save data to JSON file 
  with open("output/news_data.json", "w", encoding="utf-8") as f:
        json.dump(news_list, f, ensure_ascii=False, indent=4)
  await browser.close()