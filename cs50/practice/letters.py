"""
Project Name: Letter Generator
Purpose: Generates personalized letters for a list of recipients using a function and formatted strings
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in names:
        print(write_letter(name, "Princess Peach"))

    # using len()
    # for i in range(len(names)):
        # print(write_letter(names[i], "Princess Peach"))


def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},

        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

main()
