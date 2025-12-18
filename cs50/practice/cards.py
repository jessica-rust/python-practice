import random

cards = ["jack", "queen", "king"]

def main():
    # k is the number of items
    # weights changes the odds
    print(f"choice {random.choice(cards)}")
    print(f"choices {random.choices(cards, weights = [75, 20, 5], k=2)}")
    print(f"sample {random.sample(cards, k=2)}")

    random.seed(1) # It sets the starting point (or “seed”) for Python’s random number generator
    print(f"Seed: {random.choices(cards, k=2)}")


main()
