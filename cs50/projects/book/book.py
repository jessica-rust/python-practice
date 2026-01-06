""" returns entire text as is """
# def main():
#     with open("alice.txt", "r") as story:
#         contents = story.read()

#     print(contents)



""" returns every line in this file as an item in a list """
# def main():
#     with open("alice.txt", "r") as story:
#         contents = story.readlines()

#     print(contents)



""" creates new txt file and writes the contents of chapter 1 from original file to new """

def main():
    with open("alice.txt", "r") as story:
        contents = story.readlines()

    chapter_1 = contents[52:271]  # index starts at 0
    with open("chapter1.txt", "w") as story:
        story.writelines(chapter_1)


main()
