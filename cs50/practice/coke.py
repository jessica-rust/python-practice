"""
Project Name: Coke
Purpose: Simulates a vending machine that accepts coins and calculates change owed once the total reaches or exceeds 50 cents
Author: Jessica Rust
Course/Source: cs50
Date: 12/18/2025
"""
def main():
    total = 0
    accepted_change = ["25", "10", "5"]
    while total < 50:
        print(f"Amount Due: {50-total}")
        change = input("Insert Coin: ")
        if change not in accepted_change:
            total += 0
        else:
            total += int(change)

        if total >= 50:
            print(f"Change Owed: {total-50}")



main()
