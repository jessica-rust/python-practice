"""
Project Name: Grocery
Purpose: Collects items from user input, counts the quantity of each item, and prints a sorted list of items with their counts
Author: Jessica Rust
Course/Source: cs50
Date: 12/18/2025
"""
lists = {}

def main():
    while True:
        try:
            item = input().upper()
            grocery_list(item)

        except (EOFError):
            printed_list()
            break

def grocery_list(item):
    if item not in lists:
        lists[item] = 1
    else:
        lists[item] = lists[item] + 1

def printed_list():
    for item in sorted(lists):
        print(lists[item], item)


main()
