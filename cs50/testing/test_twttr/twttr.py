def main():
    tweet = input("Input: ")
    shorten(tweet)
    print(new_tweet)

def shorten(tweet):
    vowels = ["a", "e", "i", "o", "u"]
    new_tweet = ""
    for letter in tweet:
        if letter.lower() not in vowels:
            new_tweet += letter
    return new_tweet



if __name__ == "__main__":
    main()
