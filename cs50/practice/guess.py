def get_guess():
    guess = input("Enter a guess: ")
    return guess

def main():
    guess = get_guess()
    if guess == "50":
        print("correct")
    else:
        print("incorrect")


main()
