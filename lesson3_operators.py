# lesson3_operators.py

# Lesson 3: Operators
# Operators are symbols that perform actions on values.

# Arithmetic operators are used for math.

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
# They return a boolean: True or False.

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

# Exercise 1:
# Create two number variables called num1 and num2.
# Print their sum, difference, product, and quotient.
num1 = 20
num2 = 2
print("Sum: ", num1 + num2)
print("Difference: ", num1 - num2)
print("Product: ", num1 * num2)
print("Quotient: ", num1 / num2)


# Exercise 2:
# Create a variable called points and set it to 50.
# Add 10 using +=.
# Subtract 5 using -=.
# Multiply by 2 using *=.
# Print points after each change.
points = 50
print("Starting: ", points)

points += 10
print("After += 10: ", points)

points -= 5
print("After -= 5: ", points)

points *= 2
print("After *= 2: ", points)

# Exercise 3:
# Create two variables called age1 and age2.
# Compare them using:
# ==, !=, >, <, >=, <=
# Print each result with a clear label.
age1 = 24
age2 = 23
print("age1 == age2: ", age1 == age2)
print("age1 != age2: ", age1 != age2)
print("age1 > age2: ", age1 > age2)
print("age1 < age2: ", age1 < age2)
print("age1 >= age2: ", age1 >= age2)
print("age1 <= age2: ", age1 <= age2)

# Exercise 4:
# Create two boolean variables:
# has_ticket
# has_money
#
# Print the result of:
# has_ticket and has_money
# has_ticket or has_money
# not has_ticket
has_ticket = False
has_money = True
print("has_ticket and has_money: ", has_ticket and has_money)
print("has_ticket or has_money: ", has_ticket or has_money)
print("not has_ticket: ", not has_ticket)


# =========================
# Mini Challenge
print("============Mini Challenge==========")
# =========================

# Build a simple bill calculator.
# Ask the user for:
# - item price
# - quantity
#
# Then calculate and print the total cost.
#
# Example:
# Item price: 25.50
# Quantity: 3
# Total cost: 76.5
item_price = int(input("Item Price: "))
quantity = int(input("Quantity: "))
total_cost = item_price * quantity

print("Item price:", item_price)
print("Quantity:", quantity)
print("Total cost:", total_cost)