"""
Project Name: Exponent Function
Purpose: Defines a function to raise a number to a specified power, with the default power set to 2
Author: Jessica Rust
Course/Source: Personal Project
Date: 05/19/2025
"""
def exponent(num, power=2):
	"""exponent(num, power)raises num to specified power. Power defaults to 2."""
	return num ** power

print(exponent(2,3)) #8
print(exponent(3)) #9
print(exponent(7)) #49

print(exponent.__doc__)






