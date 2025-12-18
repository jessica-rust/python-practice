months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]

def main():
    while True:
        try:
            date = input("Date: ")
            convert(date)
            break
        except(KeyError,ValueError):
            continue


def convert(date):
    if "/" in date:
        month, day, year = date.split("/")

    else:
        month, day, year = date.split(" ")
        day = day[:-1]

        if month.title() not in months:
            raise(KeyError)
        else:
            month = months.index(month.title()) + 1

    month_int = int(month)
    day_int = int(day)
    year_int = int(year)

    if month_int > 12 or month_int < 1:
        raise ValueError()
    elif day_int > 31 or day_int < 1:
        raise ValueError()

    print (f"{year_int:04d}-{month_int:02d}-{day_int:02d}")

main()
