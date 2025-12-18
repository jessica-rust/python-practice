lists = {}

def main():
    while True:
        try:
            item = input().upper()
            grocery_list(item)

        except (EOFError):
            printed_list()
            break

def grocery_list(item):
    if item not in lists:
        lists[item] = 1
    else:
        lists[item] = lists[item] + 1

def printed_list():
    for item in sorted(lists):
        print(lists[item], item)


main()
