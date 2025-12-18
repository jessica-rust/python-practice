"""
Project Name: Coin Flip Simulator
Purpose: Simulates a coin flip and returns "HEADS" or "TAILS"
Author: Jessica Rust
Course/Source: Personal Project
Date: 05/15/2025
"""
from random import random

def flip_coin():
	if random() > 0.5:
		return "HEADS"
	else:
		return "TAILS"

print(flip_coin())


