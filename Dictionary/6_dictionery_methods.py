"""
.keys() helps when you want to loop through or check just the keys.
.values() is useful for searching or printing all the values.
.items() is great for looping through both keys and values at once."""

# Creating a dictionary with student information
student = {
    "name": "Tufan Das",
    "age": 23,
    "gender": "male"
}

# Get all the keys from the dictionary
# This returns a special view object showing the keys
print(student.keys())
# Output: dict_keys(['name', 'age', 'gender'])

# Get all the values from the dictionary
# This returns a view of just the values stored in the dictionary
print(student.values())
# Output: dict_values(['Tufan Das', 23, 'male'])

# Get all the key-value pairs from the dictionary
# This returns a list of tuples — each tuple is (key, value)
print(student.items())
# Output: dict_items([('name', 'Tufan Das'), ('age', 23), ('gender', 'male')])

