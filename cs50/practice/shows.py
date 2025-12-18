SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "jimmy Neutron ",
    "the Proud family"
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        print(show.strip().title())
        cleaned_shows.append(show.strip().title())

    print(', '.join(cleaned_shows))



main()
