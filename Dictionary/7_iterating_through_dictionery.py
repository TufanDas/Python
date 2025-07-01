student = {
    "name": "Tufan Das",
    "age": 23,
    "gender": "male"
}
""" iterating through keys by default """
for i in student:
    print(i)

""" iterating through keys """
for i in student.keys():
    print(i)

""" iterate through values """
for i in student.values():
    print(i)

""" returning key value as tuple and unpacking to i,j """
for i,j in student.items():
    print(f"{i} : {j}")

# runtime deletion error
# data = {"a" : 1, "b":2, "c":3}
# for i in data:       #RuntimeError: dictionary changed size during iteration
#     if(data[i] % 2 == 0):
#         del data[i]
# print(data)

data = {"a" : 1, "b":2, "c":3}
for i in list(data.keys()): # converting keys into list
    if(data[i] % 2 == 0):
        del data[i]
print(data) # {'a': 1, 'c': 3}
