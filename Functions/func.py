def prin():
    print("Hello world.")

for i in range(1,11):
    prin()

""" function to return square of sum """
def sum_then_square(a, b):
    return (a+b) ** 2

res = sum_then_square(2,3)
print(res)

""" args """
# parameters converted as a tuple
def sum_of_numbers(*nums): # positional arguments
    total = 0
    for i in nums:
        total += i
    return total

print(sum_of_numbers(34,3,23,235,76,8,9,2))

""" k-args """
# parameters converted as a dictonary
def build_profile(**things): # keyword arguments
    print("building profiles....")
    print(things)
    print(type(things))
    for i, j in things.items():
        print(f"{i} : {j}")

build_profile(name="Tufan Das", age=23, profession="SD", hobbies=["cricket", "footbal"], )


""" unpacking """
def add_numbers(a, b, c):# positional arguments
    return a+b+c

val = [4,5,6]
print(add_numbers(*val)) # unpacking

data = {
    "a":23,
    "b":30,
    "c":50,
}
print(add_numbers(**data)) # a=23, b=30, c=50