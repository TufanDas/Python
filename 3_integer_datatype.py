"""
We are learning number data types. In Python, there are two main types of numbers:
1. Integers (whole numbers): Numbers without any decimal point. An integer can be positive, negative, or zero.
2. Float: Numbers with decimal points.
"""

a = 10
b = -10
c = 0
print("Integer with Positive value:", a)
print("Integer with Negative value:", b)
print("Integer with Zero value:", c)
print("Type of variable 'a' is:", type(a))

""" In Python, integers have unlimited precision (limited only by system memory). """

# Python provides flexibility for readability using underscores
salary = 10_00_000  # Python interpreter ignores underscores
print("Salary:", salary)

# Storing a binary value
binary_value = 0b1010  # prefix 0b indicates binary (base 2)
print(binary_value)        # prints 10 (decimal)
print(bin(binary_value))   # prints '0b1010' (binary)

# Storing a hexadecimal value
hex_value = 0x2A  # prefix 0x indicates hexadecimal (base 16)
print(hex_value)        # prints 42 (decimal)
print(hex(hex_value))   # prints '0x2a' (hex)

# Arithmetic Operators
x = 10
y = 2
print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Regular Division: {x / y}")
print(f"Integer Division: {x // y}")
print(f"Power: {x ** y}")
print(f"Modulus: {x % y}")
print(f"Negation of {x} = {-x}")
print(f"Absolute value of {y - x}: {abs(y - x)}")

# Python follows BODMAS rule for arithmetic operations
# Order of precedence: () > ** > *, /, //, % > +, -
result = 10 - 2 ** 3 // 2 + 7
print("Result following BODMAS:", result)  # Should print 13

# Bitwise Operators
x = 10  # 1010 in binary
y = 6   # 0110 in binary

bitwise_and = x & y     # 0010 -> 2
bitwise_or = x | y      # 1110 -> 14
bitwise_xor = x ^ y     # 1100 -> 12
bitwise_not = ~x        # -(x + 1) -> -11
left_shift = x << 1     # 10100 -> 20
right_shift = x >> 1    # 0101 -> 5

print(f"{x} & {y} = {bitwise_and}")
print(f"{x} | {y} = {bitwise_or}")
print(f"{x} ^ {y} = {bitwise_xor}")
print(f"~{x} = {bitwise_not}")
print(f"{x} << 1 = {left_shift}")
print(f"{x} >> 1 = {right_shift}")

# Playing with decimal divisions
print(10 // 3)    # 3
print(10.0 // 3)  # 3.0
print(-10 // 3)   # -4 (floor division behavior)
print(10 // -3)   # -4
