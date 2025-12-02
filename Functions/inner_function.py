# function inside another function is called inner function and returning the function also

def outer():
    print("inside outer function.")

    def inner(data):
        print(data,"Inside inner function...")

    return inner

data = 10
something = outer()
something(data)
