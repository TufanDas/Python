""" Topic: Floating Point Numbers in Python """
# A float is a number with a decimal point or in exponential form

# Basic float declarations
x = 3.14
y = -2.5
z = 0.0

print("Positive float:", x)
print("Negative float:", y)
print("Zero float:", z)
print("Type of x:", type(x))  # <class 'float'>

# Using scientific notation (exponential form)
a = 1.5e3  # 1.5 * 10^3 = 1500.0
b = 2.5e-2 # 2.5 * 10^-2 = 0.025
print("Float in scientific notation (1.5e3):", a)
print("Float in scientific notation (2.5e-2):", b)

# Arithmetic operations with floats
f1 = 5.5
f2 = 2.0

print("Addition:", f1 + f2)
print("Subtraction:", f1 - f2)
print("Multiplication:", f1 * f2)
print("True Division:", f1 / f2)
print("Floor Division:", f1 // f2)
print("Modulus:", f1 % f2)
print("Exponentiation:", f1 ** f2)

# Rounding and absolute value
print("Rounded value of 3.675:", round(3.675, 2))  # floating point rounding caveats
print("Absolute value of -4.2:", abs(-4.2))

# Float precision issue demonstration
print("0.1 + 0.2 =", 0.1 + 0.2)  # May print 0.30000000000000004 due to floating point arithmetic

# Comparison
print("Is 0.1 + 0.2 == 0.3?", (0.1 + 0.2) == 0.3)  # False due to precision

# Use of math.isclose for safe float comparison
import math
print("Using math.isclose for comparison:", math.isclose(0.1 + 0.2, 0.3))

# Special float values
inf = float('inf')
neg_inf = float('-inf')
nan = float('nan')

print("Positive Infinity:", inf)
print("Negative Infinity:", neg_inf)
print("Not a Number (NaN):", nan)
print("Is NaN == NaN?", nan == nan)  # False, by definition