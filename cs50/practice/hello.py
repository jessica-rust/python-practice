def main():
    name = input("what's your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

# original code
# not as testable because no return value is given
# def main():
#     name = input("what's your name? ")
#     hello(name)

# def hello(to="world"):
#     print("hello," , to)


if __name__ == "__main__":
    main()
