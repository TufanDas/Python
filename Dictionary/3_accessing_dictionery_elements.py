""" Accessing dictionary elements in Python """

# Method 1: Access using square brackets
# This will give you the value if the key exists, but throws an error if the key is not found
person = {
    "name" : "Tufan Das",
    "age" : 23
}

# Let's print the person's name and age
print(person['name'])  # Output: Tufan Das
print(person['age'])   # Output: 23

# Method 2: Access using the get() method
# This is a safer way — it won't crash even if the key doesn't exist
print(person.get('age'))  # Output: 23 (same as above)
# If you try to get a non-existent key, it will return None (or a default value if you provide one)

# Example: Dictionary of student marks
students = {
    "amar" : 90,
    "akhbar" : 78,
    "anthony" : 76
}

# Ask the user to input a student's name
name = input("Enter the name of the student: ")

# If the name doesn't exist, it will return "NA" instead of causing an error
print(students.get(name, "NA"))

# A more user-friendly way: check if the name exists in the dictionary
if name in students:
    print("The marks of", name, "is", students[name])
