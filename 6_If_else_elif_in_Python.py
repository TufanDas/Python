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

# Example to check if the user is an adult
age = 19  # You can also use input to take age from the user
if age >= 18:
    print("You are an adult.")  # Will execute if age is 18 or more
    print("I said you are an adult.")  # Additional message inside same block
print("Outside of Block.")  # This line runs regardless of the if condition

# Example to suggest wearing a jacket based on temperature and rain
temp = 2  # You can use input for dynamic value
is_raining = True  # Simulating rain status; use bool(input(...)) for dynamic input
if temp < 10 and is_raining:
    print("Jacket pahen lijiye.")  # Advises wearing a jacket if it's cold and raining

# Example to show non-empty strings are truthy
name = "2"  # Any non-empty string is considered True in an if condition
if name:
    print("Block is executing.")  # Will print since 'name' is non-empty

# Nested condition: cold weather and snow
temp = 5
is_snowing = False
if temp < 10:
    print("Is freezing.")  # Executes because temp < 10
    print("Wear a heavy coat.")  # Suggests wearing a coat
    if is_snowing:
        print("And don't forget your boots.")  # Will only run if it's also snowing
print("Have a nice day.")  # Always runs

# Check if there's enough money to watch a movie and get popcorn
money = 200
is_free_popcorn_available = True
if money >= 400:
    print("Let's watch movie.")  # Will not run since money < 400
    if is_free_popcorn_available:
        print("Let's have popcorn.")  # Nested, also won’t run

# Grading logic using if statements
score = 89
if score > 90:
    print("Excellent!")
    print("Keep up the good work.")  # Will not run since 89 < 90

if score < 60:
    pass  # Placeholder to skip execution if score < 60
print("You need to study more.")  # Always prints regardless of the score

# Simple pass/fail based on score
if score >= 30:
    print("Passed")  # Will print since 89 >= 30
else:
    print("Fail.")

# Voting eligibility check
age = 18
if age >= 18:
    print("You can vote.")  # Will run since age is exactly 18
else:
    print("You cannot vote.")

# Password strength check
password = "sagsdgsdgdfgh"  # Simulate password input
if len(password) >= 8:
    print(f"{password} is a valid password.")  # Valid if length >= 8
else:
    print(f"{password} is not a valid password; it must be at least 8 characters.")

# Even or odd number check (actual input from user)
number = int(input("Enter the number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")  # Divisible by 2
else:
    print(f"{number} is an odd number.")  # Not divisible by 2


# Assign a score and determine the grade using if-elif-else conditions
score = 36
grade = ""

# Grade determination based on score ranges
if score >= 80:
    grade = "A"
elif score >= 60 and score < 80:
    grade = "B"
elif score < 60 and score >= 40:
    grade = "C"
else:
    grade = "D"  # For scores below 40
print(f"Your Grade is : {grade}")

# Check the nature of a number (positive single digit, zero/negative, or positive > 9)
number = -22
# Conditions explained:
# 1-9 --> positive single digit
# <=0 --> zero or negative
# > 9 --> other positive numbers

if number > 0 and number <= 9:
    print("Positive single digit.")
elif number <= 0:
    print("Zero or negative.")
else:
    print("Positive.")

# Simple equality check
x = 5
if x == 5:
    print("x is 5")

# Check if a number is "lucky" based on fixed values 6, 7, 9
a = 61
if a == 6 or a == 7 or x == 9:
    print("Lucky")  # This condition is wrong: should check 'a == 9' instead of 'x == 9'
else:
    print("Unlucky")

# Improved version using list membership to check if value is in a predefined set
n = 9
lst = [6, 7, 9]
if n in lst:
    print("Lucky.")
else:
    print('Unlucky.')

# Using ternary (conditional expression) to assign status based on age
age = 18
status = "adult" if age >= 18 else "not adult"
print(status)

# Handling division by zero safely
num = 17
divisor = 0
if divisor != 0:
    result = num / divisor
    print(f"Result = {result}")
else:
    print("Cannot divide by Zero.")

# Using ternary operator for safe division (clean one-liner)
result1 = num / divisor if divisor != 0 else "Cannot divide by zero"
print(result1)

# Taking user input to decide between subtraction and addition
# If input is neither "Add" nor "Sub", default to "UNKNOWN OPERATION"
operation = input("Sub or Add: ")
p = 10
q = 5
last_result = p + q if operation == "Add" else p - q if operation == "Sub" else "UNKNOWN OPERATION"
print(last_result)
