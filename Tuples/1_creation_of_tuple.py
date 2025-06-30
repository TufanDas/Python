"""
creating tuples
Data accessing
tuple Unpacking
loops
concatination
repeatation
methods in tuple
"""

# tuple is an oedered immutable collection of items |lists are mutable and tuples are immutable
# --------------->  Different ways to create a tupple  <----------------------------------------

""" coma (,) is mandatory in tuples , comma seperarted valuse are considered as tuple """
my_tuple = (1, 2, 3, 4, 5, 6)
my_tuple2  = 1, 2, 3, 4, 5, 6

""" not considering as a tuple"""
my_tuple3  = (1) # it is not consider as a tuple, just a avalue assigned to a variable
my_tuple3  = 1   # it is not consider as a tuple, just a avalue assigned to a variable
# my_tuple = tuple(3)   # it is not consider as a tuple, beacuse tuple constructor ony accept iterable as parameter

"""considering as a tuple"""
my_tuple4  = (1,)     # it is  consider as a tuple due to has comma(,)
my_tuple4  = 1,       # it is  consider as a tuple due to has comma(,)
my_tuple = tuple([3]) # it is  consider as a tuple because of a iterable(list) is passing as parameter

""" calling tuple constructor | make sure iterable(string,list,set) passing as argument"""
tuple_from_string = tuple("qwertyuiop")
print(f"Creating tuple by constructor call : {tuple_from_string}")  # ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p')

tupple_from_list = tuple([1,2,3,4,5,6,7,8,9])
print(f"Creating tuple by tuple constructor call : {tupple_from_list}")

# --------------->  Creating an empty tupple  <----------------------------------------
empty_tuple = ()  # this is consider as a empty tuple
print(type (empty_tuple)) # <class 'tuple'>

empty_tuple2 = tuple()  # this is consider as a empty tuple
print(type (empty_tuple2))  # <class 'tuple'>






