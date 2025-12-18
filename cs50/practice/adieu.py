import inflect


def main():
    p = inflect.engine()
    words=[]
    try:
        while True:
            name = input()
            words.append(name.title())

    except EOFError:
        pass

    saying = p.join((words))
    print(f"Adieu, adieu, to {saying}")
main()
