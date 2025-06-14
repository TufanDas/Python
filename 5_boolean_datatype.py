""" boolean -> True/False (make sure True with the capital T ans False with the capital F else it consider as variable instead of value)"""
from time import process_time

a = True
b = False

print(f"The type of a is {type(a)}")

""" boolean value can be return from a expresiion """
age = 17
is_adult = age > 18
print("is_adult : ",is_adult)
print(type(is_adult))

"""actually boolean is a subclass of integer here you can check"""
print(True == 1)
print(False == 0)
print(True + True) # 2 will print
print(int(True))
print(int(False))
print(bool(1))
print(bool(0))

""" Falsy values in python """
print(bool(0))
print(bool(0.0))
print(bool(''))  # empty String
print(bool([]))  #empty list
print(bool({})) # empty dictionery
print(bool(None))

""" all other values are truthy """
print(bool(42))
print(bool(-1))  #true
print(bool('hello'))
print(bool([1,2]))

""" Every boolean is a instance of integers"""
print("Checking is boolean is a instance of integers ? :",isinstance(True,int))

""" integers are not boolean """
print("Checking is integer is a instance of boolean ? :",isinstance(1,bool))

"""using boolean is memory efficiency"""
a = 202
print(a.bit_length()) # will print 8
print(True.bit_length()) # will print 1

"""logical operators"""
# 1.AND operator
has_adhar = True
age = 17
print(has_adhar and age > 18) #True if both consition is true

# 2.OR opereator
has_dl = True
has_adhar = False
print(has_dl or has_adhar)#True if any one consition is true

# 3.not
has_injrd = False
print(not has_injrd) # True beecome False and False become True
