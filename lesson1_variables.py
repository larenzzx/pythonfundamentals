# lesson1_variables.py

# ### Lesson 1: Variables and Data Types
# Welcome to your first Python lesson! In programming, we need a way to store information so we can use it later. That's where **variables** come in.
# 
# #### 1. What is a Variable?
# Think of a variable as a labeled storage box. You can put a value inside the box, put a label on it, and refer to it later by its label.
# - **Assignment**: We use the equals sign `=` to store a value. For example: `age = 20`.
# 
# #### 2. Fundamental Data Types
# Python has several built-in data types to represent different kinds of information:
# - `str` (String): Text data. Must be written inside single or double quotes. Example: `"Alex"`.
# - `int` (Integer): Whole numbers (positive or negative) without decimals. Example: `20`.
# - `float` (Floating-point): Decimal numbers. Example: `5.9`.
# - `bool` (Boolean): True or False values. Useful for checking conditions. (Note the capital **T** and **F**: `True` and `False`).
# 
# #### 3. Displaying Output
# We use the `print()` function to show information on the screen. You can print variables directly or pass strings.
# - **Example**: `print(name)` displays the value stored in the name variable.
# - **Labeling**: You can pass multiple values to print, separated by commas, to create clear labels: `print("Name:", name)`.
# 
# #### 4. Checking Data Types
# You can find the data type of any variable using the `type()` function:
# - **Example**: `print(type(age))` will display `<class 'int'>`.
# 
# #### 5. Naming Rules
# Good variable names are clear and descriptive. Follow these Python naming rules:
# - Must start with a letter or an underscore (`_`).
# - Can only contain letters, numbers, and underscores.
# - Cannot contain spaces. Use `snake_case` (e.g. `favorite_color`) to separate words.
# - Case-sensitive: `age`, `Age`, and `AGE` are three different variables!
# 
# > **Note**: Variables can be updated or overwritten at any time.

name = "Alex"        # str: text data, written inside quotes
age = 20             # int: whole number
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
age = 21
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

# #### Exercise 1
# Create a variable called `city` and store your `city` name.

# #### Exercise 2
# Create a variable called `birth_year` and store your birth year.

# #### Exercise 3
# Create a variable called `price` and store any decimal number.

# #### Exercise 4
# Create a variable called `likes_python` and store `True` or `False`.

# #### Exercise 5
# Print each variable with a clear label

# #### Exercise 6
# Print the type of each variable

# =========================
# Mini Challenge
print("============Mini Challenge==========")
# =========================

# **Create variables for:**
# - your first name
# - your current age
# - your favorite food
# - whether you like coding
#
# Then print one sentence using those variables.
#
# Example format:
# My name is Alex, I am 20 years old, my favorite food is pizza, and it is `True` that I like coding.

