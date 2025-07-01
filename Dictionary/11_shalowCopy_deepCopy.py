
# Original dictionary with a nested dictionary
original = {
    'name': 'Tufan',
    'marks': {'math': 90, 'science': 95}
}

shallow = original.copy()
# Change outer key
shallow['name'] = 'Rajat'  # This affects only 'shallow'

# Change nested dictionary
shallow['marks']['math'] = 60  # This also changes 'original' because 'marks' is still shared

print("Original:", original)
print("Shallow:", shallow)






import copy
deep = copy.deepcopy(original)

# Modify nested dictionary in the deep copy
deep['marks']['math'] = 100

print("Original:", original)
print("Deep Copy:", deep)
