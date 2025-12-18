"""
Project Name: Word Joiner
Purpose: Prompts the user for a sentence and joins the words with '...' as a separator
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
user_input = input("Give me a sentence? ")
user_input = user_input.split()
user_input = "...".join(user_input)
print(user_input)
