"""
what is sets
# unordered, unindexed, mutable, unique, hetrerogeneous
should have immutable items

# union, intersaction, difference
# fast membership testing

operations:
union: inclued all
intersection : common elements
a - b = uncommon elements are remains
symetric difference: both set containts uncommon elements

why sets is very important?
creation of a set
operations can perform sets
mathometical operations on set
practical examples
frozen sets
"""

""" Set Operations in Python """

# Creating a set with initial values
my_set = {1, 2, 3}
print("Original Set:", my_set)

# Adding a single element (4) to the set
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Adding multiple elements using update()
# You can pass a list, set, tuple, or even a string
my_set.update([5, 6, 7])  # Adds 5, 6, 7
print(my_set)

# Adding characters from a string individually
my_set.update("abc")  # Adds 'a', 'b', 'c' as separate elements
print(my_set)

# Adding elements from multiple iterables at once
my_set.update([9, 8, 10], {99, 100}, "MNOP")  # Adds numbers and each character
print(my_set)

# --------------------------------------
""" Removing elements from a set """

my_set = {1, 2, 3, 4, 5}
print(my_set)

# Remove a specific element (4)
my_set.remove(4)  # Throws error if element not found
print(my_set)

# Discard an element (no error if not found)
my_set.discard(45)  # 45 is not in the set, but no error
print(my_set)

# Pop removes a random element from the set
print(my_set.pop())  # Which element is removed depends on internal ordering
print(my_set)

# --------------------------------------
""" Performance Comparison: List vs Set """

import time

# Create a large list and a large set with 10 million items
large_list = list(range(10000000))
large_set = set(range(10000000))

# Search for a value that does NOT exist in either
search_value = 999999999

# Search in list
start_time = time.time()
result_list = search_value in large_list
list_time = time.time() - start_time

# Search in set
start_time = time.time()
result_list = search_value in large_set
set_time = time.time() - start_time

# Print out the time it took for each search
print(f"List Search Time: {list_time} seconds.")  # Usually slower
print(f"Set Search Time: {set_time} seconds.")    # Much faster


