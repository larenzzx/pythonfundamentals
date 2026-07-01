# lesson3_operators.py

# ### Lesson 3: Operators & Calculations
# Operators are symbols that tell Python to perform specific mathematical or logical operations on values.
# 
# #### 1. Arithmetic Operators (Math)
# - `+` Addition: Adds two numbers.
# - `-` Subtraction: Subtracts the second number from the first.
# - `*` Multiplication: Multiplies two numbers.
# - `/` Division: Divides and *always* returns a float (decimal).
# - `//` Floor Division: Divides and discards the decimal remainder (returns a whole number).
# - `%` Modulus: Returns the remainder of a division. Very useful for checking even/odd numbers!
# - `**` Exponentiation: Raises the first number to the power of the second (e.g. `2 ** 3 = 8`).
# 
# #### 2. Assignment Operators (Shorthands)
# Shorthands update a variable's value based on its current value:
# - `score += 5` is identical to `score = score + 5`
# - `score -= 2` is identical to `score = score - 2`
# - `score *= 3` is identical to `score = score * 3`
# 
# #### 3. Comparison Operators
# Compare two values and return a boolean (`True` or `False`):
# - `==` Equal to (Note: a single `=` is for assigning, double `==` is for comparing!)
# - `!=` Not equal to
# - `>` Greater than
# - `<` Less than
# - `>=` Greater than or equal to
# - `<=` Less than or equal to
# 
# #### 4. Logical Operators
# Combine multiple boolean checks:
# - `and`: Returns `True` only if *both* sides are `True`.
# - `or`: Returns `True` if *at least one* side is `True`.
# - `not`: Reverses a boolean (turns `True` to `False` and vice versa).

a = 10
b = 3

print("a:", a)
print("b:", b)

print("Addition:", a + b)          # + adds values
print("Subtraction:", a - b)       # - subtracts values
print("Multiplication:", a * b)    # * multiplies values
print("Division:", a / b)          # / divides and gives a float
print("Floor division:", a // b)   # // divides and removes the decimal part
print("Modulus:", a % b)           # % gives the remainder
print("Exponent:", a ** b)         # ** raises a number to a power

# Assignment operators update variable values.

score = 10
print("Starting score:", score)

score += 5    # same as score = score + 5
print("After += 5:", score)

score -= 2    # same as score = score - 2
print("After -= 2:", score)

score *= 3    # same as score = score * 3
print("After *= 3:", score)

# Comparison operators compare values.
# They return a boolean: `True` or `False`.

x = 8
y = 12

print("x == y:", x == y)   # equal to
print("x != y:", x != y)   # not equal to
print("x > y:", x > y)     # greater than
print("x < y:", x < y)     # less than
print("x >= y:", x >= y)   # greater than or equal to
print("x <= y:", x <= y)   # less than or equal to

# Logical operators combine boolean values.

has_id = True
is_adult = False

print("has_id and is_adult:", has_id and is_adult)  # True only if both are True
print("has_id or is_adult:", has_id or is_adult)    # True if at least one is True
print("not has_id:", not has_id)                    # reverses True or False

# =========================
# Activity
print("============Activity Section==========")
# =========================

# #### Exercise 1
# Create two number variables called num1 and num2.
# Print their sum, difference, product, and quotient.

# #### Exercise 2
# Create a variable called points and `set` it to 50.
# Add 10 using +=.
# Subtract 5 using -=.
# Multiply by 2 using *=.
# Print points after each change.

# #### Exercise 3
# Create two variables called age1 and age2.
# Compare them using:
# ==, !=, >, <, >=, <=
# Print each result with a clear label.

# #### Exercise 4
# **Create two boolean variables:**
# has_ticket
# has_money
#
# Print the result of:
# has_ticket and has_money
# has_ticket or has_money
# not has_ticket

# =========================
# Mini Challenge
print("============Mini Challenge==========")
# =========================

# **Build a simple bill calculator.**
# Ask the user for:
# - item `price`
# - quantity
#
# Then calculate and print the total cost.
#
# Example:
# Item `price`: 25.50
# Quantity: 3
# Total cost: 76.5
