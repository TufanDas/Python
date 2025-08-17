"""  map functions """
# map functions excepts two parameters first is function and secome is an object like list, tuple, set, dictionery

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_numbers = map(square, numbers) # single iterable
print(square_numbers) # returns a map object
print(list (square_numbers)) # converted into a list

def add(a,b):
    return a+b

def add2(a):
    return a*a

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(add, list1, list2)
print(result)
print(list(result))

""" >>>  Q: practice question 1: convert the elements in  int  <<< """
srt1 = ["1", "2", "3", "4", "5"]
int_list = map(int, srt1)
print(list(int_list))

""" >>> filter functions  """
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter(is_even, numbers)
print(even_numbers)
print(list(even_numbers))

""" reduce """
from functools import  reduce
def addition(x ,y):
    return x+y

numbers = [1, 2, 3, 4, 5]
total  = reduce(add, numbers)
print(total)

""" lamda function or lamda expressions """
"""
single expression only no statement
No name(anonymous)
can be assigned to a variable
often used for shorts, simple operations
returns the result of their expression autometically
"""

add_lambda = lambda x, y : x + y
print(add_lambda(3,8))

sq_lambds = lambda x: x ** 2
print(sq_lambds(3))

greet_lambda = lambda : "Hello Tufan"
print(greet_lambda())

power = lambda x, y = 10 : x ** y
print(power(2))

celsius_temp = [0, 20, 30, 40]
f_temps = list(map(lambda x : (x * 9/5) + 32, celsius_temp))
print(f_temps)

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = list(filter(lambda x : x % 2 == 0,numbers2))
print(res)

# Filter a string longer than 5 character
words = ["apple", "banana", "cat", "elephent", "dog"]
srt_res = list(filter(lambda s : len(s) > 5, words))
print(srt_res)

""" function as first class object """
# functin treated as a value is called function as first class object
"""
Being passed as arguments to other function
Being returnd as a value from other function 
being assigned to variables
being stored in data structures(list, dictioneries, etc)
Being created at runtime
"""

def greet(name):
    return f"Hello, {name}"

say_hello = greet   # assign function to a variable
print(say_hello("Tufan"))  # Hello, Tufan


def square(x):
    return x * x

def apply_function(func, values):
    return [func(v) for v in values]

nums = [1, 2, 3, 4]
print(apply_function(square, nums))  # [1, 4, 9, 16]


def power(exponent):
    def inner(base):
        return base ** exponent
    return inner

square = power(2)
cube = power(3)

print(square(5))  # 25
print(cube(2))    # 8


def add(a, b): return a+b
def sub(a, b): return a-b
def mul(a, b): return a*b

operations = {
    "add": add,
    "sub": sub,
    "mul": mul
}

print(operations["add"](5, 3))  # 8
print(operations["mul"](5, 3))  # 15