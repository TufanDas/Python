""" key differencr from a list """
# 1. tupples are immutable
# 2. tuples are use parenthases and list use square brackets
# 3. tuples are generally smaller and faster
# for read only data use tuple instead of lists

my_tup = (1, 2 ,3)
print("----Accessing elements of a tuple --------->>",my_tup[0])
print("----Accessing elements of a tuple --------->>",my_tup[1])
print("----Accessing elements of a tuple --------->>",my_tup[2])
# my_tup[0]  = 23  # 'tuple' object does not support item assignment

#----------------->  Memory allocation (Bytes)  <-------------------
import sys
print(sys.getsizeof([1,2,3])) # more bytes
print(sys.getsizeof((1,2,3,))) # few bytes

#----------------->  Immutability  <---------------------------------
t = (2,3,2)
# t[0] = 90 # raise an error
# del t[1] # 'tuple' object doesn't support item deletion
del t
# print(t) #NameError: name 't' is not defined-- > tuple is deleted

""" Immutability applies to the tuple container not to the objects inside it,
means the structure of the tupple is fixed you cannot add, remove, or assigning things to the tuple
but if a tuple containts mutable object then you can change the valuse of the mutable object inside the tupple  
for example : """

my_new_tuple = (1,2,3,[7,8,9],4,5,6)
print("----Accessing elements of a tuple --------->>",my_new_tuple[0])
print("----Accessing elements of a tuple --------->>",my_new_tuple[1])
print("----Accessing elements of a tuple --------->>",my_new_tuple[2])
print("----Accessing elements of a tuple --------->>",my_new_tuple[3])
print("----Accessing elements of a tuple --------->>",my_new_tuple[4])
print("----Accessing elements of a tuple --------->>",my_new_tuple[5])

""" changing the vlaues in index : 3 """
my_new_tuple[3].append(10)
print("After adding the value 10 to the list inside the tuple : ",my_new_tuple) # (1, 2, 3, [7, 8, 9, 10], 4, 5, 6)
my_new_tuple[3].remove(9)# remove element
print("After removing the value 9 to the list inside the tuple : ",my_new_tuple) # (1, 2, 3, [7, 8, 9, 10], 4, 5, 6)
my_new_tuple[3].remove(8) # remove element
print("After removing the value 8 to the list inside the tuple : ",my_new_tuple) # (1, 2, 3, [7, 8, 9, 10], 4, 5, 6)

#----------------->  Immutability  <---------------------------------

""" tupple concatination with another tuple is allowed """
origional_tuple = (1,2,3)
new_tuple = origional_tuple + (1,2,3)
print(f"New tuple : {new_tuple}") #(1, 2, 3, 1, 2, 3)
origional_tuple += new_tuple
print(f"Origional Tuple : {origional_tuple}")

#----------------->  Immutability  <---------------------------------