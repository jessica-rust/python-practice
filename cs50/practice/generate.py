"""
Project Name: Generate
Purpose: Demonstrates the use of Python's random module, including random choice, randint, and list shuffling
Author: Jessica Rust
Course/Source: cs50
Date: 12/18/2025
"""
import random
# useful when you have variables or functions with the same names
# as the dictionary your using, so specifying random.randint() means
# you can have a randint() fuction of your own

# because choice is imported it's not scoped
from random import choice
coin = choice(["heads", "tails"])
print(coin)

# randint is scoped to random
number = random.randint(1,10)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
