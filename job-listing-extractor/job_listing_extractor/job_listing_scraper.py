import asyncio
import csv
import random

async def scrape_all_jobs(page,context):
    all_jobs_data = []

    while True:
        await page.wait_for_selector("a:has(bdi)")
        job_cards = page.locator("a:has(bdi)")
        count = await job_cards.count()

        for i in range(count):
            job = job_cards.nth(i)
            await job.scroll_into_view_if_needed()

            try:
                job_title = await job.locator("bdi").inner_text()
            except:
                print(" Title not found")
                continue

            try:
                href = await job.get_attribute("href")
                job_link = f"https:{href}" if href and href.startswith("//") else href
            except:
                job_link = "not found"

            # Open new tab for detail
            try:
                detail_page = await context.new_page()
                await detail_page.goto(job_link, wait_until="domcontentloaded")
            except:
                print(" Failed to open job detail page")
                continue

            try:
                title = await detail_page.locator("h1.jtitle bdi").text_content()
            except:
                title = "not found"

            try:
                company = await detail_page.locator("h2.cname a bdi").text_content()
            except:
                company = "not found"

            try:
                location_parts = await detail_page.locator("h4.cname a span, h4.cname a bdi").all_text_contents()
                location = " ".join(part.strip() for part in location_parts if part.strip())
            except:
                location = "not found"

            await detail_page.close()
            await asyncio.sleep(random.uniform(2, 4))

            all_jobs_data.append({
                "title": title,
                "company": company,
                "location": location,
                "link": job_link
            })

        # Handle pagination
        try:
            next_button = page.locator("ul.pagination li a[rel='next']")
            if await next_button.count() > 0:
                await next_button.first.click()
                await page.wait_for_timeout(3000)
            else:
                break
        except Exception as e:
            print(f" Pagination check failed: {e}")
            break

    # Save all jobs to CSV
    if all_jobs_data:
        with open("output/jobs_extracted_data.csv", "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=all_jobs_data[0].keys())
            writer.writeheader()
            writer.writerows(all_jobs_data)
        print(" Data saved to CSV")
    else:
        print(" No data found to save.")


