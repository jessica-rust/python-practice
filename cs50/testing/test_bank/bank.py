def main():
    greeting = input("What greeting eould you like to say? ")
    money = value(greeting)
    print(money)

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return (0)
    elif greeting.startswith("h"):
        return (20)
    else:
        return(100)

if __name__ == "__main__":
    main()
