def main():
    total = 0
    accepted_change = ["25", "10", "5"]
    while total < 50:
        print(f"Amount Due: {50-total}")
        change = input("Insert Coin: ")
        if change not in accepted_change:
            total += 0
        else:
            total += int(change)

        if total >= 50:
            print(f"Change Owed: {total-50}")



main()
