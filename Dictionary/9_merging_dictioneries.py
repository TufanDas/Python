# Define the first dictionary
dict1 = {
    "a": 1,
    "b": 3
}

# Define the second dictionary
dict2 = {
    "a": 20,
    "d": 4
}

# Merge dict1 and dict2 using the '|' (union) operator
# If the same key exists in both, the value from dict2 will override dict1
print(dict1 | dict2)  
# Output: {'a': 20, 'b': 3, 'd': 4}

# This time, merge in the opposite direction (dict2 | dict1)
# So dict1's values override dict2 where keys overlap
print(dict2 | dict1)  
# Output: {'a': 1, 'd': 4, 'b': 3}

# Use the shorthand merging operator '|=' to update dict1 in-place
# This will permanently change dict1 by merging in dict2's contents
dict1 |= dict2

# Now dict1 is updated with dict2's values (overlapping keys replaced)
print(dict1)  
# Output: {'a': 20, 'b': 3, 'd': 4}
