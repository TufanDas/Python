""" list concatination like strings"""
from tkinter.font import names

a = [1, 2, 3, 4, 5, 6]
b = [7, 8]

# creatung a new list
print(a + b + [9, 10]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

""" repeating list 3 times inside the list  """
c = [0,1]
print(c * 3)

""" creating a list containts 0 , size of 5 """
a = [0] * 5
print(a)

""" check a string is exists in the list or not """
fruites = ["apple", "banana", "mango", " pinaple", "jackfruite"]

print("orange" in fruites)# False
print("mango" in fruites)# True

print("mal" in "malayalam") # True
print("malw" in "malayalam") # False

print("orange" not in fruites) # True --> internal implementation linear search
print("mango" not in fruites)  # False --> internal implementation linear search

""" creating nested list"""
nested_list = [[0]*3] * 3 # shalow copy
print(nested_list)# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
nested_list[0][0] = 10
print(nested_list)  #[[10, 0, 0], [10, 0, 0], [10, 0, 0]]