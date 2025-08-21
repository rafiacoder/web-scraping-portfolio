import csv
import os
from playwright.async_api import async_playwright
from filter_automation import filter_automation
import asyncio

async def scrape_tournament_details():
    browser, context, page = await filter_automation()

    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    csv_file = "output/tournaments.csv"

    # Create CSV with header if it doesn't exist
    if not os.path.exists(csv_file):
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Tournament Name", "Date", "Location", "Phone", "Email", "Director"])

    while True:
        await page.wait_for_selector('div.display-8 > a')

        # Get all tournament links
        links = await page.eval_on_selector_all(
            'div.display-8 > a',
            'elements => elements.map(el => el.href)'
        )

        # Scrape details for each link
        for link in links:
            detail_page = await context.new_page()
            await detail_page.goto(link, timeout=60000)
            await detail_page.wait_for_selector('.event')

            def safe_get(locator):
                try:
                    return locator.inner_text()
                except:
                    return "not found"

            try:
                name = await detail_page.locator('h1[itemprop="name"]').inner_text()
            except:
                name = "not found"
            try:
                date = await detail_page.locator('.date .text-secondary').inner_text()
            except:
                date = "not found"
            try:
                location = await detail_page.locator("address[itemprop='location']").inner_text()
                location = location.replace("Directions", "").strip()
            except:
                location = "not found"
            try:
                phone = await detail_page.locator('.tel').inner_text()
            except:
                phone = "not found"
            try:
                email = await detail_page.locator('.email').inner_text()
            except:
                email = "not found"
            try:
                director = await detail_page.locator('.fn').inner_text()
            except:
                director = "not found"

            # Save immediately to CSV
            with open(csv_file, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([name, date, location, phone, email, director])

            await detail_page.close()

        # Pagination - go to next page if available
        buttons = page.locator("ul.pagination.justify-content-center li.page-item:not(.disabled) a.page-link")
        count = await buttons.count()
        if count > 0:
            await buttons.nth(count - 1).click()
            await page.wait_for_selector('div.display-8 > a', state="attached")
        else:
            break

    await browser.close()
    print(f"Scraping complete! Data saved in {csv_file}")

asyncio.run(scrape_tournament_details())
