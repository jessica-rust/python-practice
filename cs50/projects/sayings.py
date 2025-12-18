"""
Project Name: Hello and Goodbye Functions
Purpose: Defines simple greeting functions and demonstrates the use of __name__ to control script execution
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")


# This line makes sure that your main() function only runs when the file is executed directly,
# and not when it is imported into another file as a library

if __name__ == "__main__":
    main()
