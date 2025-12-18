import csv

""" using csv reader assuming no headers in csv doc. """
# students = []
# with open("studentshomes.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:  # iterating over the reader not the file itself
#         students.append({"name":name, "home": home})

# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")


""" using csv dict reader assuming headers in csv doc """

# allows data to be reordered because headers are labled
students = []
with open("studentshomes.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:  # iterating over the reader not the file itself
        students.append({"name":row["name"], "home": row["home"]})

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
