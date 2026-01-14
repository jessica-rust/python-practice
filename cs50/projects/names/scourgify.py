import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("initial file Not a CSV file")

    if not sys.argv[2].endswith(".csv"):
        sys.exit("secondary file Not a CSV file")

    students = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last,first = row["name"].split(", ")
                students.append({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}" )

    with open(sys.argv[2], "w", newline="") as newfile:
        writer = csv.DictWriter(newfile, fieldnames = ["first", "last", "house"])
        writer.writeheader()
        writer.writerows(students)

main()








