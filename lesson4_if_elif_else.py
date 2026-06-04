# lesson4_if_elif_else.py

# Lesson 4: If, Elif, Else
# Conditional statements let your program make decisions.

# if runs code only when a condition is True.

age = 18

if age >= 18:
    print("You are an adult.")

# Indentation matters in Python.
# The indented line belongs to the if statement.

temperature = 30

if temperature > 25:
    print("It is warm today.")

# else runs when the if condition is False.

is_raining = False

if is_raining:
    print("Bring an umbrella.")
else:
    print("No umbrella needed.")

# elif means "else if".
# It checks another condition when the first condition is False.

grade = 85

if grade >= 90:
    print("Excellent")
elif grade >= 80:
    print("Very good")
elif grade >= 75:
    print("Passed")
else:
    print("Try again")

# You can use input with if statements.

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# You can combine conditions with and / or.

has_id = True
age = 21

if has_id and age >= 18:
    print("Entry allowed.")
else:
    print("Entry denied.")


# =========================
# Activity
print("============Activity Section==========")
# =========================

# Exercise 1:
# Ask the user to enter their age.
# If the age is 18 or older, print "You can vote."
# Otherwise, print "You cannot vote yet."
x_age = int(input("Input your age: "))
if x_age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")

# Exercise 2:
# Ask the user to enter a number.
# Print whether the number is positive, negative, or zero.
x_number = int(input("Enter a number: "))
if x_number > 0:
    print("Positive")
elif x_number < 0:
    print("Negative")
else: 
    print("Zero")

# Exercise 3:
# Ask the user to enter their grade.
# Use this grading guide:
# 90 and above: "Excellent"
# 80 to 89: "Very good"
# 75 to 79: "Passed"
# Below 75: "Failed"
x_grade = float(input("Enter your grade: "))
if x_grade >= 90:
    print("Excellent")
elif x_grade >= 80:
    print("Very good")
elif x_grade >= 75:
    print("Passed")
else:
    print("Failed")

# Exercise 4:
# Create two boolean variables:
# has_username
# has_password
#
# If both are True, print "Login allowed."
# Otherwise, print "Login denied."
has_username = True
has_password = True

if has_username and has_password:
    print("Login allowed.")
else:
    print("Login denied")


# =========================
# Mini Challenge
print("============Mini Challenge==========")
# =========================

# Build a simple discount checker.
# Ask the user for:
# - total purchase amount
# - whether they are a member
#
# If the amount is 1000 or more and they are a member,
# print "You get a discount."
#
# Otherwise, print "No discount available."
#
# Hint:
# For membership, ask the user to type yes or no.
# Then compare the answer to "yes".
total_purhase = float(input("Enter your total purchase amount: "))
membership = input("Are you a member? ").lower()

if total_purhase >= 1000 and membership == 'yes':
    print("You get a discount.")
else:
    print("No discount available.")