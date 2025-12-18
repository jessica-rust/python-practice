"""
Project Name: Shape Printer
Purpose: Demonstrates printing squares, rows, and columns using functions and loops in Python
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
def main():
    print_square(3)
    print_column(3)
    print_row(4)


# Most Succinct Option
def print_square(size):
    print("Square")
    for i in range(size):
            print("#" * size)

# Using a Second Function
# def print_square1(size):
#      for i in range(size):
#           print_row(size)


# Longer Option
# def print_square(size):
#     # for each row in square, for each brick in row, print brick
#     for i in range(size):
#         for j in range (size):
#             print("#", end="")
#         #This moves the cursor to a new line
#         print()


def print_column(height):
    print("column")
    for _ in range(height):
        print("#")
    # print("#\n" * height, end="") is another option

def print_row(width):
    print("row")
    print("#" * width)


main()
