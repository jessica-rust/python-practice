"""
Project Name: Grade
Purpose: Prompts the user for a numeric score and prints the corresponding letter grade
Author: Jessica Rust
Course/Source: cs50
Date: 12/18/2025
"""
score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

