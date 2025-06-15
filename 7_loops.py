"""
for loop, while loop
keywords:continue, breaks, else
"""

# while condittion:
#     code block to be executed
# Initialize variable x with 1
x = 1

# This while loop will run as long as x is less than or equal to 500
while x <= 500:
    print("Hello world.")  # Print a message
    x = x + 1              # Increment x by 1

    # If x becomes 4, break the loop immediately
    if x == 4:
        break  # Exits the loop when x is 4

# ----------------------------

# Initialize variable x with 10
x = 10

# This while loop will run until x becomes 0
while x > 0:
    print("Hello World", x)  # Print the message along with current value of x
    x -= 1                   # Decrement x by 1 each iteration


"""
for variable in sequence:
        code block to be executed
"""

# range()
# generate a sequence of a number
# Defining values for range parameters
stop = 9
start = 1
step = 1

# Using range() with only stop value - starts from 0 by default
print(range(stop))  # Outputs: range(0, 9) — range object from 0 to 8

# Using range() with start and stop
print(range(start, stop))  # Outputs: range(1, 9) — range object from 1 to 8

# Using range() with start, stop, and step
print(range(start, stop, step))  # Outputs: range(1, 9) — same as above since step=1

# Loop through range from 1 to 9 (exclusive) with step size 2
# This picks every second number: 1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print("Hello world.", i)

# Loop in reverse order using negative step
# range(10, 0, -1) → starts from 10 and goes down to 1 (excluding 0)
for i in range(10, 0, -1):
    print(f"Hello World Reverse: {i}")

# Display the type of range object — it's not a list but a range class
print(type(range(start, stop)))  # Outputs: <class 'range'>

# Convert the range to a list to view all values from 1 to 8
print(list(range(start, stop)))  # Outputs: [1, 2, 3, 4, 5, 6, 7, 8]


# Define a list of fruits
fruites = ["apple", "banana", "chery"]

# Loop through the list directly — element by element
for i in fruites:
    print(i)  # Prints each fruit: apple, banana, chery

print()  # Prints an empty line to separate the output

# Reassigning the same fruit list (not necessary, already defined above)
fruites = ["apple", "banana", "chery"]

# Loop through the list in reverse order using range()
# range(len(fruites)-1, -1, -1) → range(2, -1, -1) → 2, 1, 0
for i in range(len(fruites)-1, -1, -1):
    print(fruites[i])  # Prints: chery, banana, apple

# Using enumerate() to loop through both index and value
for idx, fruit in enumerate(fruites):
    print(fruit)         # Prints the fruit value
    print(fruites[idx])  # Also prints the value at the same index (redundant but valid)

