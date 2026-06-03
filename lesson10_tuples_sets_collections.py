# lesson10_tuples_sets_collections.py

# Lesson 10: Tuples, Sets & Collections Deep Dive
# You already know lists and dicts. Now let's cover the other
# important data structures: tuples, sets, and some advanced
# collection techniques.


# =============================================
# PART 1: TUPLES
# =============================================
# A tuple is like a list, but it is IMMUTABLE (cannot be changed).
# Use parentheses () instead of square brackets [].
# Tuples are faster than lists and protect data from being modified.

coordinates = (10, 20)
print("Coordinates:", coordinates)
print("X:", coordinates[0])
print("Y:", coordinates[1])

# You can access items by index, just like lists.
# But you CANNOT change, add, or remove items.
# coordinates[0] = 99  # This would cause a TypeError

# A tuple with one item needs a trailing comma.
single_item = ("hello",)  # The comma is required
print("Single item tuple:", single_item)
print("Type:", type(single_item))

# Without the comma, it's just a string in parentheses:
not_a_tuple = ("hello")
print("Not a tuple:", type(not_a_tuple))  # str

# Tuple unpacking -- assign each item to a variable.
point = (3, 4, 5)
x, y, z = point
print("x:", x, "y:", y, "z:", z)

# Swapping variables with tuples (Python trick!)
a = 1
b = 2
a, b = b, a  # Swap in one line
print("a:", a, "b:", b)

# Tuples can be used as dictionary keys (lists cannot).
locations = {
    (0, 0): "origin",
    (1, 0): "east",
    (0, 1): "north",
}
print("Origin location:", locations[(0, 0)])

# Common tuple methods: count() and index()
scores = (90, 85, 90, 70, 90)
print("Count of 90:", scores.count(90))
print("Index of 85:", scores.index(85))

# When to use tuples vs lists:
# - Use a tuple when data should NOT change (coordinates, RGB colors, dates)
# - Use a list when data needs to change (shopping cart, to-do list)


# =============================================
# PART 2: SETS
# =============================================
# A set is an unordered collection of UNIQUE items.
# Sets automatically remove duplicates.
# Use curly braces {} or the set() constructor.

fruits = {"apple", "banana", "cherry", "apple"}
print("Fruits set:", fruits)  # "apple" appears only once

# You cannot access items by index (unordered).
# print(fruits[0])  # TypeError

# Adding items
fruits.add("mango")
print("After add:", fruits)

# Removing items
fruits.remove("banana")  # Raises error if item doesn't exist
fruits.discard("grape")  # No error if item doesn't exist
print("After remove:", fruits)

# Set operations (very powerful!)
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union: all items from both sets
print("Union:", set_a | set_b)           # {1,2,3,4,5,6,7,8}
print("Union method:", set_a.union(set_b))

# Intersection: items in BOTH sets
print("Intersection:", set_a & set_b)    # {4, 5}
print("Intersection method:", set_a.intersection(set_b))

# Difference: items in A but NOT in B
print("Difference:", set_a - set_b)      # {1, 2, 3}
print("Difference method:", set_a.difference(set_b))

# Symmetric difference: items in either set, but NOT both
print("Symmetric diff:", set_a ^ set_b)  # {1, 2, 3, 6, 7, 8}

# Removing duplicates from a list using sets
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)

# Checking membership (sets are very fast for this)
print("Is 3 in set_a?", 3 in set_a)  # True
print("Is 99 in set_a?", 99 in set_a)  # False


# =============================================
# PART 3: NESTED DATA STRUCTURES
# =============================================
# You can combine lists, dicts, tuples, and sets in powerful ways.

# List of dictionaries
students = [
    {"name": "Mark", "grade": 95},
    {"name": "Ana", "grade": 88},
    {"name": "Luis", "grade": 92},
]
print("First student:", students[0]["name"])

# Dictionary of lists
classroom = {
    "math": ["Mark", "Ana"],
    "science": ["Luis", "Mark"],
    "art": ["Ana"],
}
print("Math students:", classroom["math"])

# Nested dictionary
company = {
    "engineering": {
        "head": "Alice",
        "team_size": 10,
    },
    "marketing": {
        "head": "Bob",
        "team_size": 5,
    },
}
print("Engineering head:", company["engineering"]["head"])

# List of tuples
grades = [("Mark", 95), ("Ana", 88), ("Luis", 92)]
for name, score in grades:
    print(name, "scored", score)


# =============================================
# PART 4: *args AND **kwargs
# =============================================
# These let functions accept any number of arguments.

# *args collects extra positional arguments into a tuple.
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum:", add_all(1, 2, 3))
print("Sum:", add_all(10, 20, 30, 40, 50))
print("Args type:", type(add_all()))  # args is a tuple

# **kwargs collects extra keyword arguments into a dictionary.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

print_info(name="Mark", age=24, city="New York")

# You can combine regular params, *args, and **kwargs.
def full_function(name, *args, **kwargs):
    print("Name:", name)
    print("Args:", args)
    print("Kwargs:", kwargs)

full_function("Mark", 1, 2, 3, city="NYC", role="student")


# =============================================
# ACTIVITY SECTION
# =============================================
print("============Activity Section==========")

# Exercise 1: Tuple Basics
# Create a tuple called rgb with three values: 255, 128, 0.
# Print each value using indexing.
# Try to change the first value (observe the error, then comment it out).

# Exercise 2: Set Operations
# Create two sets:
#   python_students = {"Mark", "Ana", "Luis", "Sara"}
#   java_students = {"Ana", "Sara", "Tom", "Joe"}
# Print:
#   - Students in BOTH courses (intersection)
#   - Students in EITHER course (union)
#   - Students in Python but NOT Java (difference)

# Exercise 3: Remove Duplicates
# Given the list [5, 3, 5, 2, 3, 1, 2, 4, 1],
# Use a set to remove duplicates, then convert back to a list.
# Print the result sorted in ascending order.

# Exercise 4: Nested Data
# Create a dictionary called inventory.
# It should have at least 3 items, each with:
#   - "name": item name
#   - "price": item price
#   - "quantity": how many in stock
# Loop through and print each item's total value (price * quantity).

# Exercise 5: *args and **kwargs
# Create a function called describe_pet.
# It should accept the pet's name as a normal parameter.
# It should accept any number of traits using *args.
# It should accept any extra info using **kwargs.
# Print all the information nicely.
# Call it like: describe_pet("Buddy", "friendly", "fluffy", age=3, breed="Lab")


# =============================================
# MINI CHALLENGE: Contact Book
# =============================================
print("============Mini Challenge==========")

# Build a contact book using a dictionary.
# Each key is a person's name.
# Each value is a dictionary with: phone, email, and city.
#
# Features:
# 1. Add a contact
# 2. Look up a contact by name
# 3. Delete a contact
# 4. Print all contacts
# 5. Find all contacts in a given city
#
# Use a while loop with a menu so the user can keep choosing.
# Use error handling for invalid menu choices and missing contacts.
