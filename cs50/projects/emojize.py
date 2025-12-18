"""
Project Name: Emoji Converter
Purpose: Prompts the user for text containing emoji aliases and converts them into actual emojis using the emoji library
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
import emoji

def main():
    try:
        response = input("Input: ")
    except ValueError:
        print("too many colons")

    emojis = emoji.emojize(response, language="alias")
    print(emojis)


main()
