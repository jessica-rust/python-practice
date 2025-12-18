"""
Project Name: Cowsay Greeter
Purpose: Greets users with ASCII art using the cowsay library and demonstrates modular code with imported functions
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
# install cowsay using pip before running code

import cowsay
import sys
from sayings import hello, goodbye

# using cowsay
if len(sys.argv) == 2: # checks if the user has given 2 commalnd line arguments (first being file name)
    cowsay.cow("Hello, " + sys.argv[1].title())
if len(sys.argv) == 3:
    name = " ".join(sys.argv[1:]).title()
    cowsay.trex("Hello, " + name)

# using hello and goodbye function from sayings.py file
if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])

