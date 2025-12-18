WORDS = {"PAIR" : 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")
    response = input("Do you want to know what the words and point values were today?(y/n) ")
    wordbank(response)

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ").upper()

        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won!")

        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good Job! You scored {points} points.")

    print("That's the game!")

# Tells you the words and point values
def wordbank(response):
    if response.lower() == "y":
        for word, points in WORDS.items():  # for key, value in dict.items()
            print(f"{word} was worth {points} points.")

        WORDS.clear() # stops the game





main()

