""" Creating sets in Python """

# A set is a collection of unique, unordered items.

# 1. Creating sets using set literals (curly braces {}) and the set() constructor.

# Creating a set of numbers
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

# Creating a set of names (strings)
names = {"Tufan Das", "pawan Das", "rajat sutradhat"}

# Creating a set with mixed data types: integer, string, float, and boolean
mixed_set = {1, "BOB", 8.99, False}
print(mixed_set)  # Output may appear in any order since sets are unordered

# Creating an empty set
# Note: {} creates an empty dictionary, not a set, so we must use set()
empty_set = set()
print(type(empty_set))   # Should print <class 'set'>
print(len(empty_set))    # Length is 0 because it's empty

# Creating a set from a list
set_from_list = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(set_from_list)     # Duplicates are automatically removed if present

# Creating a set from a string
# Each character becomes a separate item in the set
text = "hello"
set_from_string = set(text)
print(set_from_string)   # Likely to print: {'h', 'e', 'l', 'o'} (no duplicates, unordered)

# Creating a set from a tuple
tuple_data = (1, 2, 3, 4, 5, 6, 7, 8, 9)
set_from_tuple = set(tuple_data)
print("Set from Tuple Data : ", set_from_tuple)

# Creating a set using range()
s = set(range(1, 6))  # Creates a set of numbers from 1 to 5
print(s)
