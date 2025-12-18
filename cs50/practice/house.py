"""
Project Name: House Matcher
Purpose: Prompts the user for a name and prints the corresponding Hogwarts house using Python's match-case statement
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
name = input("What's your name? ")

# most succinct form
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: #else statement
        print("Who?")

# long form
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
