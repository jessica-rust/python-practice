"""
Project Name: Hello Function Unit Tests
Purpose: Test the hello() function for both default and argument-based outputs
Author: Jessica Rust
Course/Source: Exercise
Date: 12/18/2025
"""
from hello import hello

    # if the hello() function had a print statement
    # this wouldnt work because the function
    # hello() doesnt return a value

def test_argument():

    assert hello("David") == "hello, David"

    # using a loop and list
    for name in ["hermione", "harry", "ron"]:
        assert hello(name) ==f"hello, {name}"


def test_default():
    assert hello() == "hello, world"
