"""
Project Name: Game Recommender
Purpose: Recommends a game based on user-selected difficulty and number of players
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
def main():
    #takes the input for the players
    difficulty = input("Difficult or Casual? ").title()
    players = input("Multiplayer or Single-Player? ").title()

    #tests difficulty and number of players
    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-Player":
            recommend("Klondike")
        else:
            print("Enter a valid number of players")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single-Player":
            recommend("Clock")
        else:
            print("Enter a valid number of players")
    else:
        print("Enter a valid Difficulty")

#defines the "verb" or function recommend
def recommend(game):
    print("You might like", game)

#calls the main function
main()
