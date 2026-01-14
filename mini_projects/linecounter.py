import sys
from tabulate import tabulate
import csv


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames
            table = []

            for row in reader:
                new_row = []
                for header in headers:
                    value = row[header]
                    new_row.append(value)
                table.append(new_row)
            # simpler version
            # for row in reader:
                # table.append([row[header] for header in headers])
    except FileNotFoundError:
        sys.exit("File does not exist")


    print(tabulate(table, headers, tablefmt="grid"))

main()
