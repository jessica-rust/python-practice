import pyfiglet
import random
import sys

figlet = pyfiglet.Figlet()


if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")

    response = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(response))


elif len(sys.argv) == 1:
    response = input("Input: ")
    random_pick = random.choice(figlet.getFonts())
    figlet.setFont(font=random_pick)
    print(figlet.renderText(response))
else:
    sys.exit("Invalid usage")




