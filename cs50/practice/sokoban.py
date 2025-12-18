def main():
    history = []
    count = 0

    while count < 5:
        action = input("Action: ")

        if action.lower() == "undo":
            undone = history.pop()
            print(f"Undone: {undone}")
            count -=1
        elif action.lower() == "restart":
            history.clear()
            count = 0
        else:
            history.append(action)
            count +=1

        print(history)


main()
print("Game Over")
