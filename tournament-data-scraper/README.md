# 🏀 Tournament Scraper — Automated Basketball Event Data (Playwright + Python)


This project is a **web automation & data extraction tool** built with **Python** and **Playwright (async API)**.  
It automatically scrapes **1,000+ basketball tournament records** (name, date, location, contacts, director) from
**Exposure Events** and saves them to CSV — **no manual effort required**.

---

## 🚀 Highlights

- ⚡ **End-to-end automation**: open → filter → paginate → extract → save
- 🕵️ **Stealth config**: randomized user-agents & helpful headers
- 📅 **Dynamic filters**: date range + event type (Tournament)
- 🧭 **Pagination aware**: crawls through all event pages
- 💾 **Real-time CSV writes**: resilient to interruptions
- 📈 **Proven at scale**: **1000+ records** successfully collected

---

## 🧠 Skills Demonstrated

**Web Scraping (Playwright async)** · **Python (asyncio)** · **Browser Automation** ·  
**Anti-bot/Stealth tactics** · **Data Engineering (CSV pipeline)** · **Clean modular code** · **Git/GitHub**

---

## 📂 Project Structure
tournament-data-scraper-playwright/
│
├─ tournament-scraper/
│ ├─ scraping.py # Core scraper logic (loops, pagination, CSV)
│ ├─ filter_automation.py # Applies filters (dates, event type) and search
│ ├─ browser_config.py # Stealth browser/context configuration
│ └─ main.py # Entry point to run the scraper
│
├─ output/
│ └─ tournaments.csv # Auto-generated CSV (add a small sample to repo)
│
├─ README.md
└─ requirements.txt # (optional) pin dependencies for easy setup
