import asyncio
from automation import perform_automation
from job_listing_scraper import scrape_all_jobs
from playwright.async_api import async_playwright
async def main():
 page, browser, context = await perform_automation()
 await scrape_all_jobs(page,context)
 await browser.close()
  
if __name__ == "__main__":
    asyncio.run(main())