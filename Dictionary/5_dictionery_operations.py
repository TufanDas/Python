""" Dictionary operations in Python """

# Creating a dictionary of students with their marks
students = {
    "Ankit": 85,
    "Bhavna": 92,
    "Chetan": 76,
    "Divya": 89,
    "Eshan": 95
}

# Check if 'Ankit' is present in the dictionary keys
print("Ankit" in students)  # Output: True

# Get the number of key-value pairs in the dictionary
print(len(students))  # Output: 5

# Loop through the dictionary and print each student's name and their marks
for i in students:
    print(i, ":", students[i])

# A nested dictionary to store complex data
data = {
    'id': 101,
    'info': {
        'name': "Tufan Das",
        'city': "Madarihat"
    }
}

# Accessing the 'city' value from inside the nested 'info' dictionary
print(data['info']['city'])  # Output: Madarihat

# Get the number of top-level keys in the 'data' dictionary (i.e., 'id' and 'info')
print(len(data))  # Output: 2
