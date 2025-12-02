# higher functon is basically, passing a function as a parameter to the another function

def square(num):
    return num * num

def cube(num):
    return num * num * num


def operate(value,func):
    return func(value)

value = 5

result = operate(value, square)
print(result)

result = operate(value, cube)
print(result)



