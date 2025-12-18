"""
Project Name: Word Frequency Counter
Purpose: Demonstrates counting word occurrences in a string using list comprehension, filtering by word length, and dictionary comprehension
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
def main():

    """ Using List Comprehension """

    counts_1 = {}
    words = "I like to eat apples and bananas and grapes. And i like to Eat dinner"
    words = words.split() # splits up the string into a list
    lowercase_words = [word.lower() for word in words] # makes all the words in the list lowercase

    # adds a count everytime the word is said
    for word in lowercase_words:
        if word in counts_1:
            counts_1[word] += 1
        else:
            counts_1[word] = 1

    print("Counts_1: ", counts_1)


    """ Using len() to filter lists """

    counts = {}
    words = "I like to eat apples and bananas and grapes. And i like to Eat dinner"
    words = words.split() # splits up the string into a list
    # only keeps words that are longer than 4 letters
    lowercase_words = [word.lower() for word in words if len(word) > 4]

    # adds a count everytime the word is said
    for word in lowercase_words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    print("Counts_2: ", counts)



    """ Simplifying Further Using Dictionary Comprehension """

    words = "I like to eat apples and bananas and grapes. And i like to Eat dinner"
    words = words.split()
    lowercase_words = [word.lower() for word in words if len(word) > 4]

    counts_3= {word: lowercase_words.count(word) for word in lowercase_words}

    print("Counts_3: ", counts_3)


main()

