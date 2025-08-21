import asyncio
from news_scraper import news_scrape

async def main():
    await news_scrape()

if __name__ == "__main__":
    asyncio.run(main())
