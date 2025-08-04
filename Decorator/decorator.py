def my_decorator(func):
    def wrapper(*args):
        print("This is printing before the hello function calls.")
        func(*args)
        print("This is printing after the hello function calls.")
    return wrapper


@my_decorator
def hello(a,b):
    print("Hello Python.")
    print(a+b)
    print("Hello Tufan.")

hello(3,9)