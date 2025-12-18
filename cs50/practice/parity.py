"""
Project Name: Even or Odd Checker
Purpose: Prompts the user for a number and prints whether it is even or odd using a function
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
def main():
    x = int(input("What's x? "))
    # is_even is returning a T/F value
    # so you can just call it with an if statement
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# pythonic option
def is_even(n):
    return True if n % 2 == 0 else False
# most succinct option
def is_even(n):
    return n % 2 == 0

main()
