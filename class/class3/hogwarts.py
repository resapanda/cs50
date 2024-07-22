# list
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

# When you want list to be as int
for i in range(len(students)):
    print(i + 1, students[i])

# dict
students = ["Hermione", "Harry", "Ron"]
house = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

students1 = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# output their house
print(students1["Hermione"])
print(students1["Harry"])
print(students1["Ron"])
print(students1["Draco"])

# output both their name and house
for student in students1:
    print(student, students1[student], sep=",")

# a dict inside the list
students2 = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students2:
    print(student["name"], student["house"], student["patronus"], sep=",")
