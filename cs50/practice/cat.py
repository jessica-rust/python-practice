"""
Project Name: Cat
Purpose: Demonstrates different ways to use for loops, while loops, user input, and functions in Python to print repeated output
Author: Jessica Rust
Course/Source: cs50
Date: 12/18/2025
"""
''' For Loops '''

# Using a Range
for _ in range(3):
    print("For Loop Meow")

# Using a Manual List
# for i in [0,1,2]:
#     print("Meow")


''' While Loops '''

# Most Pythonic Option
i = 0
while i < 3:
    print("While Loop Meow")
    i += 1

# Option Starting at 1
# i = 1
# while i <= 3:
#     print("Meow")
#     i += 1
    #  this is the same as i = i + 1

# Not Option
# i = 3
# while i != 0:
#     print("Meow")
#     i -= 1


''' Simplest Pythonic Way '''

print("Print Method Meow\n" * 3, end="")


''' Using User Input '''


# Best practice
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("User Input Meow")


# Using Continue
# while True:
#     n = int(input("What's n?"))
#     if n < 0:
#         continue
#     else:
#         break
#
# for _ in range(n):
#     print("meow")


''' Using Functions '''


# Using User Input
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
def meow(n):
    for _ in range(n):
        print("Function Meow")

main()

# Using Set Numbers
# def main():
#     meow(3)

# def meow(n):
#     for _ in range(n):
#         print("Function Meow")

# main()
