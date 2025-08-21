import asyncio
from scraping import scrape_tournament_details

if __name__ == "__main__":
    asyncio.run(scrape_tournament_details())
