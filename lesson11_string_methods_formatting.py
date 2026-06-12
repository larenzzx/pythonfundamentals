# lesson11_string_methods_formatting.py

# Lesson 11: String Methods & Formatting
# Strings have tons of built-in methods that make text processing easy.
# This lesson covers the most important ones plus modern formatting.

# =============================================
# PART 1: ESSENTIAL STRING METHODS
# =============================================

text = "  Hello, Python World!  "
print("Original:", repr(text))  # repr shows hidden characters

# Stripping whitespace
print("strip():", repr(text.strip()))    # Removes both sides
print("lstrip():", repr(text.lstrip()))  # Removes left side
print("rstrip():", repr(text.rstrip()))  # Removes right side

# Case conversion
word = "Python"
print("upper():", word.upper())       # PYTHON
print("lower():", word.lower())       # python
print("title():", "hello world".title())  # Hello World
print("capitalize():", "hello world".capitalize())  # Hello world
print("swapcase():", "PyThOn".swapcase())  # pYtHoN

# Checking content
print("isalpha():", "Python".isalpha())    # True (letters only)
print("isdigit():", "12345".isdigit())     # True (digits only)
print("isalnum():", "Python3".isalnum())   # True (letters or digits)
print("isspace():", "   ".isspace())       # True (whitespace only)
print("startswith():", "Python".startswith("Py"))  # True
print("endswith():", "Python".endswith("on"))      # True

# Finding and counting
sentence = "Python is fun and Python is powerful"
print("find():", sentence.find("Python"))       # First occurrence: 0
print("rfind():", sentence.rfind("Python"))     # Last occurrence: 17
print("count():", sentence.count("Python"))     # 2
# find() returns -1 if not found (index() raises ValueError)

# Replacing
print("replace():", sentence.replace("Python", "Java"))
print("replace() once:", sentence.replace("Python", "Java", 1))

# Splitting and joining
csv_line = "Alex,20,New York,Student"
parts = csv_line.split(",")
print("split():", parts)

words = ["Python", "is", "awesome"]
joined = " ".join(words)
print("join():", joined)

# Splitting by lines
multi = "line1\nline2\nline3"
print("splitlines():", multi.splitlines())

# =============================================
# PART 2: STRING SLICING (DEEP DIVE)
# =============================================
# You know indexing. Slicing lets you grab substrings.

word = "Python"
print(word[0:2])    # "Py" (index 0 up to, but not including, 2)
print(word[2:5])    # "tho"
print(word[:3])     # "Pyt" (from start)
print(word[3:])     # "hon" (to end)
print(word[:])      # "Python" (full copy)
print(word[::2])    # "Pto" (every 2nd character)
print(word[::-1])   # "nohtyP" (REVERSED!)

# Negative indexing
print(word[-1])     # "n" (last character)
print(word[-3:])    # "hon" (last 3 characters)
print(word[:-2])    # "Pyth" (everything except last 2)

# =============================================
# PART 3: STRING FORMATTING (3 WAYS)
# =============================================

name = "Alex"
age = 24
score = 95.567

# Method 1: f-strings (BEST -- use this in modern Python)
print(f"My name is {name}, I am {age} years old.")
print(f"Score: {score:.1f}")          # 95.6 (1 decimal place)
print(f"Score: {score:.2f}")          # 95.57 (2 decimal places)
print(f"Padded: {age:05d}")           # 00024 (zero-padded to 5 digits)
print(f"Percent: {0.856:.1%}")        # 85.6%
print(f"Binary: {42:b}")              # 101010
print(f"Hex: {255:x}")                # ff
print(f"Upper hex: {255:X}")          # FF

# Expressions inside f-strings
print(f"Next year I'll be {age + 1}")
print(f"Name uppercase: {name.upper()}")

# Method 2: .format() (older but still common)
print("My name is {}, I am {} years old.".format(name, age))
print("My name is {0}, I am {1}. Hi, {0}!".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# Method 3: % formatting (oldest -- avoid in new code)
print("My name is %s, I am %d years old." % (name, age))
print("Score: %.1f" % score)

# =============================================
# PART 4: MULTI-LINE STRINGS & RAW STRINGS
# =============================================

# Triple quotes for multi-line strings
message = """
Hello,
This is a multi-line string.
    It preserves indentation.
"""
print(message)

# Raw strings (ignore backslashes -- useful for file paths and regex)
path = r"C:\new_folder\test.txt"
print("Raw string:", path)
# Without r: "C:\new_folder\t
#             est.txt"  (\n and \t would be escape sequences)

# Escape sequences
print("Tab:\tindented")
print("Newline:\nsecond line")
print("Quote: She said \"Hello\"")
print("Backslash: C:\\Users\\Alex")

# =============================================
# PART 5: USEFUL STRING PATTERNS
# =============================================

# Check if a string is a palindrome
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print("racecar:", is_palindrome("racecar"))        # True
print("hello:", is_palindrome("hello"))            # False
print("A man a plan:", is_palindrome("A man a plan"))  # False
print("A man a plan a canal Panama:", is_palindrome("A man a plan a canal Panama"))  # True

# Count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print("Vowels in 'Hello World':", count_vowels("Hello World"))  # 3

# Title case a sentence properly
def title_case(sentence):
    return sentence.title()

print(title_case("the quick brown fox"))

# Reverse words in a sentence
def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])

print(reverse_words("Python is fun"))  # "fun is Python"

# =============================================
# ACTIVITY SECTION
# =============================================
print("============Activity Section==========")

# Exercise 1: Clean Up Input
# Ask the user to enter their full name.
# Strip leading/trailing whitespace.
# Print it in title case.
# Print how many characters it has (excluding spaces).

# Exercise 2: Email Validator (Basic)
# Ask the user to enter an email address.
# Check if it contains "@" and ".com"
# Print "Valid email" or "Invalid email"
# (This is a basic check -- real validation is more complex)

# Exercise 3: Word Counter
# Ask the user to enter a sentence.
# Print:
#   - The number of words
#   - The number of characters (with and without spaces)
#   - The sentence in reverse
#   - The sentence with every word reversed (but word order kept)

# Exercise 4: Format a Receipt
# Create variables for 3 items with name, quantity, and price.
# Use f-strings to print a formatted receipt with columns.
# Example:
#   ITEM          QTY    PRICE    TOTAL
#   Apple          3     1.50     4.50
#   Bread          2     2.75     5.50
#   Milk           1     3.99     3.99
#   -----------------------------------
#   TOTAL                          13.99
# Use :>10 for right alignment, :<10 for left alignment.

# Exercise 5: Password Strength Checker
# Ask the user to enter a password.
# Check if it meets these rules:
#   - At least 8 characters long
#   - Contains at least one uppercase letter
#   - Contains at least one lowercase letter
#   - Contains at least one digit
# Print which rules pass and fail.

# =============================================
# MINI CHALLENGE: Text Analyzer
# =============================================
print("============Mini Challenge==========")

# Build a text analyzer that:
# 1. Asks the user to enter a paragraph of text.
# 2. Prints:
#    - Total characters (with spaces)
#    - Total characters (without spaces)
#    - Total words
#    - Total sentences (count periods, exclamation marks, question marks)
#    - The most common word (hint: use a dictionary to count)
#    - The longest word
#    - The text with every vowel replaced by "*"
#
# Use string methods and formatting to make the output clean.
