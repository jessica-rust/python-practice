"""
Project Name: Tip Calculator
Purpose: Convert user input of dollars and percentage to floats and calculate tip
Author: Jessica Rust
Course/Source: Exercise
Date: 12/18/2025
"""
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d.replace("$",""))


def percent_to_float(p):
    return float("0." + p.replace("%",""))

main()
