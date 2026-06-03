# lesson2_input_output.py

# Lesson 2: Input and Output
# Output means showing information to the user.
# Input means getting information from the user.

# print() is used for output.
print("Welcome to Lesson 2!")

# You can print text directly.
print("Python is fun.")

# You can also print variables.
course = "Python Fundamentals"
print("Course:", course)

# input() is used to ask the user for information.
# The text inside input() is called a prompt.
student_name = input("Enter your name: ")

# input() always gives back a string.
print("Hello, " + student_name)

# If you want a number, convert the input.
# int() converts text to a whole number.
age = int(input("Enter your age: "))
print("Your age is:", age)

# float() converts text to a decimal number.
price = float(input("Enter a price: "))
print("The price is:", price)

# You can combine input and output to make a simple program.
favorite_food = input("Enter your favorite food: ")
print("Nice! Your favorite food is", favorite_food)


# =========================
# Activity
print("============Activity Section==========")
# =========================

# Exercise 1:
# Ask the user to enter their city.
# Store the answer in a variable called city.
city = input("Enter your City: ")

# Exercise 2:
# Ask the user to enter their favorite color.
# Store the answer in a variable called favorite_color.
favorite_color = input("Enter your favorite color: ")

# Exercise 3:
# Ask the user to enter their birth year.
# Convert it to an integer and store it in a variable called birth_year.
birth_year = int(input("Enter your birth year: "))


# Exercise 4:
# Ask the user to enter the price of any item.
# Convert it to a float and store it in a variable called item_price.
item_price = float(input("Enter price of the item: "))

# Exercise 5:
# Print all answers with clear labels.
print("City:", city)
print("Favorite color:", favorite_color)
print("Birth year:", birth_year)
print("Item price:", item_price)

# =========================
# Mini Challenge
print("============Mini Challenge==========")
# =========================

# Create a simple profile program.
# Ask the user for:
# - first name
# - age
# - favorite hobby
#
# Then print one complete sentence using those answers.
#
# Example format:
# Hello, my name is Ana. I am 19 years old and I enjoy drawing.
first_name = input("Enter your first name: ")
your_age = int(input("Enter your age: "))
favorite_hobby = input("Enter your favorite hobby: ")

print(f"Hello, my name is {first_name}. I am {your_age} and I enjoy {favorite_hobby}.")
