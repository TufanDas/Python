# Create a dictionary where keys are numbers 1 to 10 and values are their squares
res = {i: i**2 for i in range(1, 11)}
print(res)

# Create a dictionary for numbers 1 to 10:
# - if the number is even, store its square
# - if the number is odd, store the number itself
res2 = {i: i**2 if i % 2 == 0 else i for i in range(1, 11)}

# Create a dictionary for even numbers only, mapping to their squares
res3 = {i: i**2 for i in range(1, 11) if i % 2 == 0}

print(res2)
print(res3)

# Create a dictionary from a list of tuples (name, marks)
students = [("mark", 90), ("mike", 89), ("michel", 70)]
result = {i: j for i, j in students}
print(result)

# Invert a dictionary — swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
result2 = {j: i for i, j in original.items()}
print(result2)

# Create a multiplication table using nested dictionaries (without comprehension)
res = {}
for i in range(1, 6):  # Outer loop for numbers 1 to 5
    inner_dict = {}
    for j in range(1, 11):  # Inner loop for 1 to 10
        inner_dict[j] = i * j  # Each value is the product of i and j
    res[i] = inner_dict  # Assign the inner table to the outer dictionary
print(res)

# Same multiplication table using dictionary comprehension (short and clean)
res = {i: {j: i * j for j in range(1, 11)} for i in range(1, 6)}
print(res)
