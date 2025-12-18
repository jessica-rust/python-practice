"""
Project Name: Scoping Example – UnboundLocalError
Purpose: Demonstrates a scoping problem in Python when trying to modify a variable without using 'global'
Author: Jessica Rust
Course/Source: Personal Project
Date: 05/19/2025
"""
# EXAMPLE OF A SCOPING PROBLEM:
total = 0

def increment():
	total += 1
	return total

print(increment()) # Error! 
# "I can't find a variable named total in this function"