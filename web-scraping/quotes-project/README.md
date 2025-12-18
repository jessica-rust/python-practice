# Quotes Scraping & Guessing Game

This project demonstrates a small data pipeline built with Python that scrapes quotes from a public website and uses the collected data in an interactive command-line game.

The project is intentionally split into separate scripts to show good separation of concerns:
- data collection
- data storage
- data usage

---

## Project Structure

quotes_project/
├── scrape_quotes_to_csv.py
├── quote_guessing_game.py
├── quotes.csv
└── README.md

---

## scrape_quotes_to_csv.py

Purpose:  
Scrapes quotes from https://quotes.toscrape.com and saves them to a CSV file.

What it does:
- Iterates through all pages of quotes
- Extracts quote text, author name, and author biography link
- Writes structured data to `quotes.csv`

Skills demonstrated:
- Web scraping with requests and BeautifulSoup
- Pagination handling
- Writing structured data to CSV
- Clean, reusable data collection

---

## quote_guessing_game.py

Purpose:  
Uses previously scraped data to run an interactive quote-guessing game.

What it does:
- Reads quotes from `quotes.csv`
- Randomly selects a quote
- Prompts the user to guess the author
- Provides progressive hints including:
  - Author birth date and location
  - First and last name initials
- Fetches additional author data only when needed

Design note:  
This script was refactored from an earlier version that scraped live data on every run. The current design separates scraping from gameplay to improve performance, reusability, and code clarity. A commented reference to the earlier approach is preserved in the code to document this evolution.

Skills demonstrated:
- CSV reading
- Game loop logic
- User input handling
- Selective use of web requests
- Refactoring for cleaner architecture

---

## How to Run

1. Run the scraper to generate the CSV file:
   python scrape_quotes_to_csv.py

2. Run the game:
   python quote_guessing_game.py

---

## Notes

This project is a learning exercise focused on practical web scraping, basic data pipelines, clean script responsibilities, and iterative improvement through refactoring.
