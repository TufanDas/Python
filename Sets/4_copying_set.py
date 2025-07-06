""" Copying sets in Python """

# Create a set with initial values
original_set = {1, 2, 3, 4, 5}

# Assigning the original set to a new variable (this does NOT create a new copy)
# Both 'original_set' and 'new_set' now point to the same object in memory
new_set = original_set

# Modify the original set by adding an element
# Since both variables point to the same set, the change reflects in both
original_set.add(9)
print(new_set)  # Output will include 9

# Now, let's create an actual copy using the copy() method
# This creates a shallow copy — a new object with the same elements
new_set = original_set.copy()

# Modify the original set again
# This time, the copied set won't be affected
original_set.add(50)
print(new_set)       # Output does NOT include 50
print(original_set)  # Output includes 50
