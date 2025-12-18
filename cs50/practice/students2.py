"""
Project Name: Add Student to CSV
Purpose: Appends a new student's name and home to a CSV file
Author: Jessica Rust
Course/Source: Exercise
Date: 12/18/2025
"""
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students2.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])
