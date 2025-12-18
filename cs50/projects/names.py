"""
Project Name: Name File Manager
Purpose: Adds names to a file and reads them back in sorted order, demonstrating file input/output in Python
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
""" This code creates a name file that can be added to and then reads it back to you """

""" original code """
# names = []
# for _ in range(3):
#     names.append(input("What's your name? "))
# for name in sorted(names):
#     print(f"hello {name}")



""" creates file and adds names using file I/O """
# file = open("names.txt", "w")   # "w" recreates the file everytime

# file = open("names.txt", "a")  # "a" appends to where the cursor ended
# file.write(f"{name}\n")  # user needs to manually add spaces and new line
# file.close()  # manual closing of file



""" creates file and adds names using file I/O and with function """
# name = input("What's your name? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")  # automatically closes file when done with indented code



""" code that reads file """
# with open("names.txt", "r") as file:
#     lines = file.readlines()
# for line in lines:
#     print("hello,", line.rstrip()) # rstrip removes trailing characters or newlines



""" better code that reads file """
# with open("names.txt", "r") as file:
#     for line in file:   # iterates over every line and implies readlines()
#         print("hello,", line.rstrip())



""" code that reads file w/ sorting after """
# names = []   # creates list

# with open("names.txt") as file: # "r" is default and implied
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names): # sorts list
#     print(f"hello, {name}")



""" code that reads file and sorts at the same time """
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())













