"""
Project Name: Phone Number Slicer
Purpose: Demonstrates string slicing techniques to extract parts of a phone number
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
def main():
    phone = "617-495-1000"

    # first 3 digits
    print(phone[:3])
    print(phone[0:3])
    print(phone[:-9]) # includes all characters except the last 9

    # last 4 digits
    print(phone[8:])
    print(phone[8:12])
    print(phone[-4:]) # excludes all characters except the last 4
        # beneficial if you wanted the last 4 and people were entering +1



main()
