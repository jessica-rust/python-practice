"""
Project Name: Camel
Purpose: Converts a camelCase username input into a lowercase, underscore-separated format
Author: Jessica Rust
Course/Source: cs50
Date: 12/18/2025
"""
def main():
    user_input = input("What's your username? ")
    words = []
    temp_word = ""


    for letter in user_input:
        if letter.isupper():
            words.append(temp_word)
            temp_word = letter.lower()
        else:
            temp_word += letter
    if temp_word:
        words.append(temp_word)



    username = ("_").join(words)
    print(username)
    return(username)


main()

