# lesson9_error_handling.py

# ### Lesson 9: Exception & Error Handling
# When a Python script encounters a problem (like dividing by zero or inputting letters when numbers are expected), it halts execution and crashes. Error handling lets your program resolve issues gracefully.
# 
# #### 1. The `try` and `except` Structure
# - `try`: Place the code that might cause an error inside this block.
# - `except`: If an error occurs, Python jumps to this block instead of crashing.
# 
# ```python
# try:
#     age = int(input("Age: "))
# except ValueError:
#     print("Invalid entry! Please enter a whole number.")
# ```
# 
# #### 2. Handling Multiple Specific Errors
# You can catch different exceptions separately to give specific feedback:
# - `ValueError`: For incorrect data types (e.g. `int("hello")`).
# - `ZeroDivisionError`: Occurs when dividing by zero.
# - `IndexError`: Occurs when trying to access a list index that doesn't exist.
# 
# #### 3. `else` and `finally`
# - `else`: Runs only if *no* exceptions occurred in the `try` block.
# - `finally`: Runs *no matter what* (even if the program crashed). Useful for cleaning up resources.

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Please enter a valid whole number.")

# You can handle division errors too.
# Dividing by zero causes a `ZeroDivisionError`.

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("10 divided by your number is:", result)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")

# else runs only when no error happens.

try:
    score = int(input("Enter your score: "))
except ValueError:
    print("Invalid score.")
else:
    print("Score accepted:", score)

# finally runs no matter what.
# It is often used for cleanup or final messages.

try:
    price = float(input("Enter item price: "))
    print("Price:", price)
except ValueError:
    print("Invalid price.")
finally:
    print("Price check finished.")

# You can use error handling inside functions.

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."

print("Division result:", divide_numbers(20, 5))
print("Division result:", divide_numbers(20, 0))

# =========================
# Activity
print("============Activity Section==========")
# =========================

# #### Exercise 1
# **Ask the user to enter their age.**
# Use try and except to catch `ValueError`.
# If the input is valid, print the age.
# If the input is invalid, print "Invalid age."

# #### Exercise 2
# **Ask the user to enter two numbers.**
# Divide the first number by the second number.
# Handle `ValueError` if the user does not enter a number.
# Handle `ZeroDivisionError` if the second number is zero.

# #### Exercise 3
# **Ask the user to enter a `price`.**
# Use try, except, else, and finally.
# If the `price` is valid, print "Price accepted:" with the `price`.
# If the `price` is invalid, print "Invalid `price`."
# In finally, print "Done checking `price`."

# #### Exercise 4
# Create a function called `safe_multiply`.
# It should have two parameters: num1 and num2.
# Use try and except inside the function.
# Return the product if both values can be multiplied.
# Return "Invalid values." if there is a `TypeError`.
# Call the function twice.

# #### Exercise 5
# Create a `list` called numbers with at least three numbers.
# Ask the user for an index number.
# Print the item at that index.
# Handle `ValueError` if the user does not enter a whole number.
# Handle `IndexError` if the index does not exist.

# =========================
# Mini Challenge
print("============Mini Challenge==========")
# =========================

# Build a safer calculator.
# Create four functions:
# `add`
# `subtract`
# `multiply_numbers`
# `divide`
#
# Ask the user for two numbers.
# **Ask the user to choose an operation:**
# add, subtract, `multiply`, or `divide`
#
# Use error handling for:
# invalid number input
# division by zero
#
# Print the final answer.
