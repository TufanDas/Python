print("Good Morning")
name = "Alice"
print(f"Hello, {name}")
print("Welcome to python programming")

# 1. making decisions
# 2. repeating actions
# 3. jumping to diffrent parts of the programm

""" what we learn
if, el if, else, for loop, while loop, break, continue, pass
"""

age = 19 #int(input("Enter the age:"))
if age >= 18:
    print("Your are an adult.")
    print("i said you are an adult.")
print("Outside of Block.")

temp = 2  #int(input("Enter Temprature:"))
is_raining = True # bool(input("Leave empty if not raining else else type anything:"))
if temp<10 and is_raining:
    print("Jacket pahen lijiye.")

name = "2"
if name:
    print("block is cxecuting.")

temp = 5
is_snowing = False
if temp<10:
    print("Is freezing.")
    print("Wear a heavy coat.")
    if is_snowing:
        print("And don't forget your boots.")
print("Have a nice day.")

money = 200
is_free_popcorn_available = True
if money >= 400:
    print("let's watch movie.")
    if is_free_popcorn_available:
        print("let's hava popcorn.")

score = 89
if score > 90:
    print("Excelent!")
    print("Keep up the good work.")

if score < 60:
    pass
print("You need to study more.")

if score>= 30:
    print("passed")
else:
    print("fail.")

age = 18
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

password = "sagsdgsdgdfgh" #input("enter the password.")
if len(password) >= 8:
    print(f"{password} its a valid password.")
else:
    print(f"{password} its not a valid password it must be atleast length of 8.")

number = int(input("enterr the number : "))
if number%2 == 0:
    print(f"{number} Its a even number.")
else:
    print(f"{number} Its a odd number.")

score = 36
grade = ""
if score >= 80:
    grade = "A"
elif score >= 60 and score < 80:
    grade = "B"
elif score < 60 and score >= 40:
    grade = "C"
else:
    grade = "D"
print(f"Your Grade is : {grade}")

number = -22
# 1-9 --> positive single digit
# <=0 --> zero or negetive
# > 9 --> positive

if number > 0 and number <= 9:
    print("Positive single digit.")
elif number <= 0:
    print("Zero or negetive.")
else:
    print("Positive.")

x = 5
if x == 5:
    print("x is 5")

# if a = 6,7,9 -> luckey
# else -> unluckey
a = 61
if a == 6 or a == 7 or x == 9 :
    print("Luckey")
else:
    print("Unluckey")

n = 9
lst = [6,7,9]
if n in lst:
    print("Luckey.")
else:
    print('Unluckey.')

# ternery operator
age = 18
status = "adult" if age >= 18 else "not adult"
print(status)

num = 17
divisor = 0
if divisor != 0:
    result  = num/divisor
    print(f"Result = {result}")
else:
    print("Cannot devide by Zero.")


# using ternery operator
result1 = num/divisor if divisor != 0 else "cannot devided by zero"
print(result1)

operation = input("Sub or Add:")
p = 10
q = 5
last_result = p+q if operation == "Add" else p-q if operation == "Sub" else "UNKNOWN OPERATION"
print(last_result)