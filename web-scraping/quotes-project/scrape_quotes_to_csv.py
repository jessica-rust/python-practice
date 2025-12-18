"""
Project Name: Quotes Scraper to CSV
Purpose: Scrapes quotes, authors, and biography links from quotes.toscrape.com and saves them to a CSV file
Author: Jessica Rust
Course/Source: Personal Project
Date: 07/25/2025
"""
import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictWriter

BASE_URL = "https://quotes.toscrape.com/"


def scrape_quotes():
	all_quotes = []
	new_link = "/page/1"
	while new_link: 
		res = requests.get(f"{BASE_URL}{new_link}")
		print(f"Now scraping {BASE_URL}{new_link}...")
		soup = BeautifulSoup(res.text, "html.parser")
		quotes = soup.find_all(class_ = "quote")
		
		for quote in quotes:
			all_quotes.append({
				"text": quote.find(class_ = "text").get_text(),
				"author": quote.find(class_ = "author").get_text(),
				"bio": quote.find("a")["href"]
			})
		next_page = soup.find(class_ = "next")
		new_link = next_page.find("a")["href"] if next_page else None
	return all_quotes

def write_quotes(quotes):
	with open("quotes.csv", "w", encoding="utf-8", newline="") as file:
		headers = ["text", "author", "bio"]
		csv_writer = DictWriter(file, fieldnames= headers)
		csv_writer.writeheader()
		for quote in quotes:
			csv_writer.writerow(quote)


quotes = scrape_quotes()
write_quotes(quotes)