import random

def main():
    level = get_level()
    score = 0
    count = 0

    while count < 10:
        a = generate_integer(level)
        b = generate_integer(level)
        c = a + b
        tries = 0

        while tries < 3:
            try:
                user_input = int(input(f"{a} + {b} = "))

                if user_input != c:
                    print("EEE")
                    tries += 1
                else:
                    score +=1
                    break

            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"{a} + {b} = {c}")

        count += 1
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)




if __name__ == "__main__":
    main()
