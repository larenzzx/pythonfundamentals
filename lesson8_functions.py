# lesson8_functions.py

# Lesson 8: Functions
# A function is a reusable block of code.
# Functions help you avoid repeating the same code many times.

# Use def to create a function.

def greet():
    print("Hello!")


# Call the function by writing its name with parentheses.

greet()

# A function can have parameters.
# A parameter is a variable that receives a value when the function is called.

def greet_student(name):
    print("Hello,", name)


greet_student("Mark")
greet_student("Ana")

# A function can have more than one parameter.

def introduce(name, age):
    print("My name is", name, "and I am", age, "years old.")


introduce("Mark", 24)

# A function can return a value.
# return sends a result back to the place where the function was called.

def add_numbers(a, b):
    return a + b


sum_result = add_numbers(5, 3)
print("Sum:", sum_result)

# You can use a returned value directly inside print().

print("Another sum:", add_numbers(10, 20))

# Functions can use if statements.

def check_age(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")


check_age(24)
check_age(15)

# Functions can also work with lists.

def print_foods(foods):
    for food in foods:
        print("Food:", food)


favorite_foods = ["chicken", "pizza", "fries"]
print_foods(favorite_foods)


# =========================
# Activity
print("============Activity Section==========")
# =========================

# Exercise 1:
# Create a function called say_welcome.
# It should print "Welcome to Python!"
# Call the function.
def say_welcome():
    print("Welcome to Python!")
    
say_welcome()

# Exercise 2:
# Create a function called print_name.
# It should have one parameter called name.
# It should print the name with a clear label.
# Call the function with your name.
def print_name(name):
    print("Name:", name)
    
print_name("Mark Larenz Tabotabo")

# Exercise 3:
# Create a function called multiply.
# It should have two parameters called num1 and num2.
# It should return their product.
# Store the result in a variable and print it.
def multiply(num1, num2):
    return num1 * num2

product = multiply(5, 2)
print("Product:", product)

# Exercise 4:
# Create a function called check_number.
# It should have one parameter called number.
# If the number is positive, print "Positive".
# If the number is negative, print "Negative".
# Otherwise, print "Zero".
# Call the function three times with different numbers.
def check_number(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

check_number(2)
check_number(-111)
check_number(0)

# Exercise 5:
# Create a function called print_colors.
# It should have one parameter called colors.
# Use a for loop to print each color in the list.
# Create a list of three colors and pass it to the function.
def print_colors(colors):
    for color in colors:
        print("Color:", color)
        
three_colors = ["White", "Black", "Green"] 
print_colors(three_colors)

# =========================
# Mini Challenge
print("============Mini Challenge==========")
# =========================

# Build a simple calculator with functions.
# Create four functions:
# add
# subtract
# multiply_numbers
# divide
#
# Ask the user for two numbers.
# Print the result of each function.
#
# Example:
# First number: 10
# Second number: 5
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide(x, y):
    return x / y

val1 = int(input("First number: "))
val2 = int(input("Second number: "))
ans1 = add(val1, val2)
ans2 = subtract(val1, val2)
ans3 = multiply_numbers(val1, val2)
ans4 = divide(val1, val2)

print("Addition:", ans1)
print("Subtraction:", ans2)
print("Multiplication:", ans3)
print("Division:", ans4)