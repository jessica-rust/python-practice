"""
Project Name: Quote Guessing Game
Purpose: Runs an interactive command-line game where users guess the author of a quote using pre-scraped data
Author: Jessica Rust
Course/Source: Personal Project
Date: 07/25/2025
"""
"""
NOTES ON PROJECT EVOLUTION:

This project originally combined live web scraping and game logic in a single script.
That earlier approach scraped https://quotes.toscrape.com on every game run and stored
the results in memory.

While functional, that design had several drawbacks:
- The site was scraped repeatedly on each execution
- Gameplay was tightly coupled to the scraping process
- The script was slower and less reusable

The project was later refactored into two stages:
1. A dedicated scraper that saves quote data to a CSV file
2. A separate guessing game that reads from the CSV

This separation improves performance, reusability, and code clarity.
Below is a simplified version of the original approach, preserved for reference.
"""

# ======================
# EARLIER APPROACH (REFERENCE ONLY)
# ======================

# def scrape_quotes():
#     all_quotes = []
#     new_link = "/page/1"
#     while new_link:
#         res = requests.get(f"{BASE_URL}{new_link}")
#         soup = BeautifulSoup(res.text, "html.parser")
#         quotes = soup.find_all(class_="quote")
#
#         for quote in quotes:
#             all_quotes.append({
#                 "text": quote.find(class_="text").get_text(),
#                 "author": quote.find(class_="author").get_text(),
#                 "bio": quote.find("a")["href"]
#             })
#
#         next_page = soup.find(class_="next")
#         new_link = next_page.find("a")["href"] if next_page else None
#
#     return all_quotes
#
# quotes = scrape_quotes()
# start_game(quotes)


import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

BASE_URL = "https://quotes.toscrape.com/"


def read_quotes(filename):
	with open(filename,"r", encoding="utf-8") as file:
		csv_reader = DictReader(file)
		return list(csv_reader)

read_quotes("quotes.csv")

def start_game(quotes):
	game_quote = choice(quotes)
	guesses_remaining = 4
	print("Here's a quote:")
	print(game_quote['text'])

	guess = ''
	while guess.lower() != game_quote['author'].lower() and guesses_remaining > 0:
		guess = input(f"who said this? Guesses remaining: {guesses_remaining}\n")
		if guess.lower() == game_quote["author"].lower():
			print("YOU GOT IT RIGHT!!")
			break
		guesses_remaining -= 1
		if guesses_remaining == 3:
			res = requests.get(f"{BASE_URL}{game_quote['bio']}")
			soup = BeautifulSoup(res.text, "html.parser")
			birth_date = soup.find(class_ = "author-born-date").get_text()
			birth_place = soup.find(class_ = "author-born-location").get_text()
			print(f"Here's a hint: The author was born on {birth_date} {birth_place}.")
		elif guesses_remaining == 2:
			print(f"Here's a hint: The authors first name starts with: {game_quote['author'][0]}")
		elif guesses_remaining == 1:
			last_initial = game_quote["author"].split(" ")[1][0]
			print(f"Here's a hint: The authors last name starts with: {last_initial}")
		else:
			print(f"Sorry you ran out of guesses. The answer was {game_quote['author']}")

	again = ''
	while again not in ('y', 'yes', 'n', 'no'):
		again = input("Would you like to play again? (y/n)").lower()
	if again in ('yes', 'y'):
		print("OK you play again!")
		return start_game(quotes)
	else:
		print("OK goodbye!")

quotes = read_quotes("quotes.csv")
start_game(quotes)