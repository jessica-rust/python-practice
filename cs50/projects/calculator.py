"""
Project Name: Square Calculator
Purpose: Prompts the user for a number and prints its square
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
def main():
    x = input("What's x? ")
    print("x squared is", square(x))


def square(n):
    return n * n

if __name__ == "__main__":
    main()
