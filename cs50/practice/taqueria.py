"""
Project Name: Taco Shop Order Tracker
Purpose: Allows users to input menu items and keeps a running total of the order
Author: Jessica Rust
Course/Source: Exercise
Date: 12/18/2025
"""
MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0
    while True:
        try:
            order = input("Item: ").title()
            order_check(order)
            total += price(order)
            print(f"Total: ${total:.2f}")

        except (ValueError):
            continue
        except (EOFError):
            break

def order_check(order):
    if order not in MENU.keys():
        raise ValueError("Not a menu item")


def price(order):
        return MENU[order]


main()





