"""
Project Name: Adieu
Purpose: Collects names from user input and prints a farewell message formatted with proper commas and "and" using the inflect library
Author: Jessica Rust
Course/Source: cs50
Date: 12/18/2025
"""
import inflect


def main():
    p = inflect.engine()
    words=[]
    try:
        while True:
            name = input()
            words.append(name.title())

    except EOFError:
        pass

    saying = p.join((words))
    print(f"Adieu, adieu, to {saying}")
main()
