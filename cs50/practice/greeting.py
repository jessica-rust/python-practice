"""
Project Name: Greeting
Purpose: Checks if a string contains 'hello' and responds with a greeting
Author: Jessica Rust
Course/Source: cs50
Date: 12/18/2025
"""
def greet(input):
    if "hello" in input:
        return("hello, there")
    else:
        return("I'm not sure what you mean")

greeting = greet("hello, computer")
print(greeting + " carter")
