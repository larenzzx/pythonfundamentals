# lesson1_variables.py

# Lesson 1: Variables and Data Types
# A variable stores a value so you can use it later.

name = "Mark"        # str: text data, written inside quotes
age = 25             # int: whole number
height = 5.9         # float: decimal number
is_student = True    # bool: True or False value

# print() displays information on the screen.
print(name)
print(age)
print(height)
print(is_student)

# You can print labels with values to make output clearer.
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# type() tells you the data type of a value.
print(type(name))        # str
print(type(age))         # int
print(type(height))      # float
print(type(is_student))  # bool

# Variables can be changed after they are created.
age = 26
print("Updated age:", age)

# Good variable names are clear and descriptive.
favorite_color = "blue"
score = 100

print("Favorite color:", favorite_color)
print("Score:", score)


# =========================
# Activity
print("============Activity Section==========")
# =========================

# Exercise 1:
# Create a variable called city and store your city name.
city = "Zamboanga City"

# Exercise 2:
# Create a variable called birth_year and store your birth year.
birth_year = 2001

# Exercise 3:
# Create a variable called price and store any decimal number.
price = 22.2

# Exercise 4:
# Create a variable called likes_python and store True or False.
likes_python = True

# Exercise 5:
# Print each variable with a clear label
print("City:", city)
print("Birth year:", birth_year)
print("Price:", price)
print("Likes Python:", likes_python)

# Exercise 6:
# Print the type of each variable
print(type(city))
print(type(birth_year))
print(type(price))
print(type(likes_python))

# =========================
# Mini Challenge
print("============Mini Challenge==========")
# =========================

# Create variables for:
# - your first name
# - your current age
# - your favorite food
# - whether you like coding
#
# Then print one sentence using those variables.
#
# Example format:
# My name is Alex, I am 20 years old, my favorite food is pizza, and it is True that I like coding.
first_name = "Mark Tabotabo"
current_age = 24
favorite_food = "Fried Chicken"
likes_coding = True

print(f"My name is {first_name}, I am {current_age} years old, my favorite food is {favorite_food}, and it is {likes_coding} that I like coding.")
