students = {
    "101": {"name" : "Alice", "age" : 20, "grade" : "A"},
    "102": {"name" : "Bob", "age" : 23, "grade" : "C"},
    "103": {"name" : "Moke", "age" : 25, "grade" : "D"},
    "104": {"name" : "Rodert", "age" : 24, "grade" : "AA"},
}
print(students)
print(students["101"])
print(students["101"]['name'])

for i in students:
    print(i)
    for j in i:
        print(j)


for roll_number,details in students.items():
    for key, val in details.items():
        print(f" {key} : {val} ")
