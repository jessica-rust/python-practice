"""
Project Name: Einstein
Purpose: Prompts the user for a mass in kilograms and calculates its energy equivalent using E=mc^2
Author: Jessica Rust
Course/Source: Pcs50
Date: 12/18/2025
"""
user_input = input("how much does it weigh in kg? ")
mass =int(user_input)
final_mass = mass*(300000000**2)
print(final_mass)
