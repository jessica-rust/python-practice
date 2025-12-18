"""
Project Name: Global Counter Example
Purpose: Demonstrates the use of a global variable to maintain a counter across function calls
Author: Jessica Rust
Course/Source: Personal Project
Date: 06/15/2025
"""
total = 0

def increment():
	global total #use the global variable total
	total += 1
	return total

print(increment()) # 1
print(increment()) # 2
print(increment()) # 3