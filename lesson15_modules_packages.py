# lesson15_modules_packages.py

# ### Lesson 15: Modules and Packages
# As projects grow larger, putting all code in one file becomes unmanageable. Modules and packages allow you to separate code into logical files.
# 
# #### 1. What is a Module?
# A module is simply a Python file (`.py` file) containing functions, classes, and variables.
# 
# #### 2. Importing Modules
# - **Standard import**: `import math` (access using `math.sqrt()`).
# - **Alias import**: `import datetime as dt`.
# - **Specific features**: `from random import randint` (access `randint()` directly without prefix).
# 
# #### 3. Custom Modules
# If you have `helpers.py` in the same folder, you can import its features inside `main.py` using:
# `import helpers` or `from helpers import my_function`
# 
# #### 4. Entry Point: `__name__ == '__main__'`
# Inside any python script:
# - `__name__` is a special variable.
# - If the script is run directly, `__name__` equals `__main__`.
# - If imported, `__name__` equals the filename.
# This prevents test code from executing automatically when a file is imported.

import math
print("Pi:", math.pi)
print("Square root of 16:", math.sqrt(16))
print("Ceil of 4.3:", math.ceil(4.3))
print("Floor of 4.7:", math.floor(4.7))
print("Factorial of 5:", math.factorial(5))

# Import specific items
from math import pi, sqrt, pow
print("Pi:", pi)
print("Sqrt:", sqrt(25))
print("Pow:", pow(2, 10))

# Import with an alias
import random as rand
print("Random int:", rand.randint(1, 100))
print("Random choice:", rand.choice(["apple", "banana", "cherry"]))
print("Random float:", rand.random())  # 0.0 to 1.0

# Import everything (generally NOT recommended -- can cause name conflicts)
# from math import *

# =============================================
# #### Exercise 2
# =============================================

# --- os: Operating System ---
import os
print("Current directory:", os.getcwd())
print("Home directory:", os.path.expanduser("~"))
print("Path separator:", os.sep)

# --- datetime ---
from datetime import datetime, timedelta, date
now = datetime.now()
print("Now:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Formatted:", now.strftime("%B %d, %Y at %I:%M %p"))

# Date arithmetic
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))
print("Next week:", next_week.strftime("%Y-%m-%d"))

# --- random ---
import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sample 3:", random.sample(numbers, 3))
random.shuffle(numbers)
print("Shuffled:", numbers)

# --- collections ---
from collections import Counter, defaultdict, OrderedDict

# Counter: count occurrences
text = "mississippi"
letter_count = Counter(text)
print("Letter counts:", letter_count)
print("Most common:", letter_count.most_common(3))

# defaultdict: auto-creates default values
word_groups = defaultdict(list)
words = ["apple", "bat", "car", "apple", "bat"]
for word in words:
    word_groups[len(word)].append(word)
print("Grouped by length:", dict(word_groups))

# --- itertools ---
import itertools
# Infinite counter
counter = itertools.count(start=10, step=5)
print("Count:", next(counter), next(counter), next(counter))

# Cycle through items
cycler = itertools.cycle(["A", "B", "C"])
print("Cycle:", next(cycler), next(cycler), next(cycler), next(cycler))

# Permutations and combinations
print("Permutations:", list(itertools.permutations([1, 2, 3], 2)))
print("Combinations:", list(itertools.combinations([1, 2, 3, 4], 2)))

# --- re: Regular Expressions ---
import re
text = "My email is mark@example.com and backup is mark2@test.org"

# Find all emails
emails = re.findall(r'[\w.]+@[\w.]+', text)
print("Emails found:", emails)

# Search
match = re.search(r'(\w+)@(\w+)', text)
if match:
    print("Full match:", match.group(0))
    print("Username:", match.group(1))
    print("Domain:", match.group(2))

# Replace
censored = re.sub(r'[\w.]+@[\w.]+', '[EMAIL]', text)
print("Censored:", censored)

# Validate phone number pattern
phone = "555-123-4567"
if re.match(r'\d{3}-\d{3}-\d{4}', phone):
    print("Valid phone number!")

# =============================================
# #### Exercise 3
# =============================================
# Any .py file is a module. You can import it.

# Create a helper module (we'll write it below)
# For now, here's how you'd use it:

# Suppose you have a file called "helpers.py" with:
#   def greet(name): ...
#   def `add`(a, b): ...

# You can import it:
# import helpers
# helpers.greet("Alex")

# Or import specific functions:
# from helpers import greet, `add`
# greet("Alex")

# Or import with an alias:
# import helpers as h
# h.greet("Alex")

# =============================================
# #### Exercise 4
# =============================================
# This is a Python idiom. Code under this block only runs
# when the file is executed directly, NOT when imported.

# if __name__ == "__main__":
#     print("This file is being run directly")
#     # Put test code or main program here
# else:
#     print("This file was imported as a module")

# This is why you'll see this pattern in almost every Python file.
# It lets a file be both a reusable module AND a runnable script.

# =============================================
# #### Exercise 5
# =============================================
# A package is a folder containing modules and an __init__.py file.
#
# Example structure:
#   myproject/
#   ├── __init__.py        (makes it a package)
#   ├── main.py
#   ├── utils/
#   │   ├── __init__.py
#   │   ├── string_utils.py
#   │   └── math_utils.py
#   └── models/
#       ├── __init__.py
#       ├── user.py
#       └── product.py
#
# Import like:
#   from utils.string_utils import clean_text
#   from models.user import User

# =============================================
# #### Exercise 6
# =============================================
# Virtual environments keep project dependencies isolated.
# This is ESSENTIAL for real projects.
#
# Creating and using a venv:
#
#   # Create a virtual environment
#   python3 -m venv myenv
#
#   # Activate it
#   source myenv/bin/activate    # Linux/Mac
#   myenv\Scripts\activate       # Windows
#
#   # Install packages (only in this environment)
#   pip install requests flask
#
#   # See what's installed
#   pip `list`
#
#   # Save dependencies to a file
#   pip freeze > requirements.txt
#
#   # Install from a requirements file
#   pip install -r requirements.txt
#
#   # Deactivate when done
#   deactivate
#
# Using uv (faster alternative to pip):
#   uv venv myenv
#   source myenv/bin/activate
#   uv pip install requests flask

# =============================================
# #### Exercise 7
# =============================================
# Python has a massive ecosystem of third-party packages.
# Install them with pip or uv.
#
# Popular packages for beginners:
#   requests      -- HTTP requests (APIs, web scraping)
#   flask         -- Web framework (lightweight)
#   rich          -- Beautiful terminal output
#   python-dotenv -- Load .env files
#   pytest        -- Testing framework
#
# Example with requests (install first: pip install requests):
#   import requests
#   response = requests.get("https://api.github.com")
#   print(response.status_code)
#   print(response.json())

# =============================================
# #### Exercise 8
# =============================================
# Let's create a simple project structure right here.

# First, create a utils module:
utils_code = '''
"""Utility functions for our project."""

def format_currency(amount, currency="$"):
    """Format a number as currency."""
    return f"{currency}{amount:,.2f}"

def slugify(text):
    """Convert text to URL-friendly slug."""
    import re
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text

def truncate(text, length=50, suffix="..."):
    """Truncate text to a maximum length."""
    if len(text) <= length:
        return text
    return text[:length - len(suffix)] + suffix

if __name__ == "__main__":
    print(format_currency(1234.5))
    print(slugify("Hello World! This is a Test"))
    print(truncate("This is a very long sentence.", 20))
'''

with open("utils.py", "w") as f:
    f.write(utils_code)

# Now import and use it
import utils
print("Currency:", utils.format_currency(1234.5))
print("Slug:", utils.slugify("Hello World!"))
print("Truncated:", utils.truncate("This is a very long sentence.", 20))

# =============================================
# ACTIVITY SECTION
# =============================================
print("============Activity Section==========")

# #### Exercise 1
# Use the math module to:
# a) Calculate the area of a circle with radius 7
# b) Calculate the hypotenuse of a right triangle (sides 3 and 4)
# c) Convert 45 degrees to radians
# d) Calculate log base 10 of 1000

# #### Exercise 2
# Create a "Magic 8-Ball" program:
# - Store 8 possible answers in a `list`
# - Ask the user to ask a question
# - Use random.choice() to pick and display an answer
# - Loop until the user types "quit"

# #### Exercise 3
# Create a "Days Until" calculator:
# - Ask the user for a future date
# - Calculate how many days until that date
# - Also show how many weeks and remaining days
# - Handle invalid dates with try/except

# #### Exercise 4
# Write a function that validates:
# a) A valid `email` (has @ and a domain with a dot)
# b) A valid phone number (format: XXX-XXX-XXXX)
# c) A valid zip code (5 digits)
# Test each with valid and invalid inputs.

# #### Exercise 5
# Create a file called "string_tools.py" with these functions:
#   - reverse_string(text)
#   - count_words(text)
#   - is_palindrome(text)
#   - capitalize_words(text)
# Each function should have a docstring.
# Import and test all functions from this lesson file.

# =============================================
# MINI CHALLENGE: Project Structure
# =============================================
print("============Mini Challenge==========")

# Create a small project with this structure:
#
# calculator_project/
# ├── __init__.py
# ├── main.py          (menu and user interaction)
# ├── operations.py    (add, subtract, `multiply`, `divide`, power, sqrt)
# ├── history.py       (save/load calculation history to JSON)
# └── formatter.py     (format results nicely)
#
# operations.py: Functions for each math operation.
#   Each function should accept two numbers and return the result.
#   Include proper docstrings.
#
# history.py:
#   - save_history(history_list) -- saves to history.json
#   - load_history() -- loads from history.json
#   - clear_history() -- clears the file
#
# formatter.py:
#   - format_result(operation, num1, num2, result) -> "5 + 3 = 8"
#   - format_history(history_list) -> numbered `list` of past calculations
#
# main.py:
#   - Menu with: calculate, view history, clear history, quit
#   - Import from your modules
#   - Use if __name__ == "__main__"
#
# This teaches you real-world project organization!
