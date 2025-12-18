"""
Project Name: Simple Guess Checker
Purpose: Prompts the user for a guess and checks if it matches a predefined correct value
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
def get_guess():
    guess = input("Enter a guess: ")
    return guess

def main():
    guess = get_guess()
    if guess == "50":
        print("correct")
    else:
        print("incorrect")


main()
