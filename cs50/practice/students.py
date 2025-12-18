""" uses file I/O to open, read, and sort harry potter csv file """


""" original code """
# with open("students.csv") as file:
#     for line in file:   # iterates over line and returns them as is
#         row = line.rstrip().split(",")   # splits the line on the commas
#         print(f"{row[0]} is in {row[1]}")   # row[0] is first element in row (student name)


""" improved original code """
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",") # assigns both variables at once
#                                                # only works if you know there are only 2 variables in every row,
#                                                # otherwise throws ValueError
#         print(f"{name} is in {house}")



""" Reads code first and sorts by whole phrase """
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)


""" Reads code, collects it, and sorts it by name """
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)

# for student in students:
#     print(f"{student['name']} is in {student['house']}")


""" improved: reads code, collects it, and sorts it by name or house using functions """

# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}  # assigns k,v in one line
#         students.append(student)

# # the sole purpose of these functions is to return the name/house
# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]

# # sorts the students using the get_name/get_house functions
# # the function name no "()" is passed into key becuase the sorted function calls it for you
# print("Sorted by houses")
# for student in sorted(students, key=get_house):
#     print(f"{student['name']} is in {student['house']}")

# print("\nSorted by names in reverse")
# for student in sorted(students, key=get_name, reverse=True):
#     print(f"{student['name']} is in {student['house']}")


""" Most Concise using lambda """

students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}  # assigns k,v in one line
        students.append(student)

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")





