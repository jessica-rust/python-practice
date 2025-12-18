"""
Project Name: Deep
Purpose: Prompts the user for the answer to the Great Question of Life, the Universe, and Everything and checks if it is correct
Author: Jessica Rust
Course/Source: cs50
Date: 12/18/2025
"""
def main ():
    answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print ("Yes")
    else:
        print ("No")

main()
