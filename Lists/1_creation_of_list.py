"""
list - a built in DS thet stors an ordered mutable collection of items
List can hold items of any type including, other list

Ordered: Items have defined order and can be access by their index.
Mutable: You can change, add, remove after the list has been created.
Heterogeneous: A single list can containts elements of different data types.
Iterable: list can be looped over for loop and also comprehesions.
"""

my_list = [1, 2, 3, 4, 5]

# list of mixed type
mised_list = [1, 5, 5.90, True,"Apple"]

# empty list
Empty_list = []

# list of strings
colors = ["Red", "Green", "Black", "Yellow", "Brown", "Pink"]

# list of booleans
boolean_list = [True,False, True, True]

# list inside a list
nested_list = [[1, 2],[3, 4]]

""" Another way of creating an  empty list"""
li = list()  # actually calling a constructor
print(type(li))

""" we can pass a iterable to the list constructor | it can be reang() function, tupple, set """
li1 = list("Hello World") #
print(li1)

set1 = {10, 20, 50, 60}
print(list(set1)) # passing a set
print(list(range(10)))

""" copying a list """
origional_list = [1,2,3,4,5,6,7,8,9,10]
copy_list = list(origional_list)
print(copy_list)

# print(list(123)) # 123 is an integer not iterable