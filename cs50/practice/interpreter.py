"""
Project Name: Simple Calculator
Purpose: Prompts the user for a basic arithmetic equation and computes the result
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
def main():
    equation = input("Equation: ")
    x, operator, y = equation.split(" ")
    x = float(x)
    y = float(y)

    if operator == "+":
        result = x + y
    elif operator == "-":
        result = x - y
    elif operator == "/":
        result = x / y
    elif operator == "*":
        result = x * y
    else:
        print("not a valid equation")

    print (result)

main()
