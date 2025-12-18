"""
Project Name: Lists and Dictionaries Demonstration
Purpose: Demonstrates the use of lists, dictionaries, and lists of dictionaries in Python, including iteration and value access
Author: Jessica Rust
Course/Source: Personal Project
Date: 12/18/2025
"""
''' Using Lists '''


students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]


# Using a For Loop to Iterate Over List
print("Lists 1:")
for student in students:
    print(student)

# Using len() and range()
print("Lists 2:")
for i in range(len(students)):
    print(students[i])

# Labling Them With Their Place in the List
print("Lists 3:")
for i in range(len(students)):
    print(i + 1, students[i])

# Acessing  Their Indexes Individually
print("Lists 4:")
print(students[0])
print(students[1])
print(students[2])
print(students[3])

# Don't Use "_" for Variables That Are Actually Used
# Like in This Print Statement:
    # for _ in students:
    #   print(_)


''' Using Dictionaries '''


students = {
    "Hermione" : "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gyffindor",
    "Draco": "Slytherin"
    }

# Prints the Key:Value Pairs
print("Dict 1:")
for student in students:
    print(student, students[student], sep=": ")

# Prints the Keys
print("Dict 2:")
for student in students:
    print(student)

# Acessing Values Directly
print("Dict 3:")
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])


''' Using a List of Dictionaries '''


students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Hermione", "house": "Gryffindor", "patronus": None},
]

# Prints The Values for all 3 Keys
print("List/Dict 1:")
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" | ")

