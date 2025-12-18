import random



while True:
    try:
        level = input("Level: ")
        int_level = int(level)
        if int_level > 0:
            break
    except ValueError:
        pass

number = random.randint(1,int_level)

while True:
    try:
        guess = input("Guess: ")
        int_guess = int(guess)
        if int_guess < 1:
            continue
    except ValueError:
        continue

    if int_guess > number:
        print("Too large!")
    elif int_guess < number:
        print("Too small!")
    else:
        print("Just right!")
        break


