import emoji

def main():
    try:
        response = input("Input: ")
    except ValueError:
        print("too many colons")

    emojis = emoji.emojize(response, language="alias")
    print(emojis)


main()
