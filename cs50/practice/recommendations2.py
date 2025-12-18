"""
Project Name: Game Recommender (Validated Version)
Purpose: Recommends a game based on user-selected difficulty and number of players, with input validation using early returns
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
def main():
    # takes the input for the difficulty and number of players
    difficulty = input("Difficult or Casual? ").title()

    # put the if statement in parenthesis and add not at the front
    # this removed the need for an else statement
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid Difficulty")
        return
        # this return ends our program
        # it also sends the user feedback immediately


    players = input("Multiplayer or Single-Player? ").title()
    if not (players == "Multiplayer" or players == "Single-Player"):
        print("Enter a valid number of players")
        return

    #tests difficulty and number of players
    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-Player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")


#defines the "verb" or function recommend
def recommend(game):
    print("You might like", game)

#calls the main function
main()
