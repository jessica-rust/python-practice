"""
Project Name: Emoticon Conversation
Purpose: Demonstrates using a global variable to include an emoticon in printed messages
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
emoticon = "v.v"


def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()
