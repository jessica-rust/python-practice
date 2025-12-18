"""
Project Name: Marathon Pace Calculator
Purpose: Calculates the pace per mile given a total distance and time, with validation for positive time values
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
def main():
    pace = get_pace(miles = 26.2, minutes = 0)
    print(f"You need to run each mile in {round(pace,2)} minutes.")


def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Minutes must be grater than 0.")

    return minutes/miles


main()
