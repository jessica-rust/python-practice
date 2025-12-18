"""
Project Name: Simple Pyramid Printer
Purpose: Prompts the user for a height and prints a left-aligned pyramid of hashes of that height
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        print("#" * (i+1))



if __name__ == "__main__":
    main()
