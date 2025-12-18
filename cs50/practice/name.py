"""
Project Name: Name Tag CLI
Purpose: Prints a greeting for each name provided as a command-line argument, with basic error handling
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
import sys

# error handling
# sys.exit() quits the program and prints an exit statement
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# nametag functionality
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)


