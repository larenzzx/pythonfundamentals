# lesson7_dictionaries.py

# ### Lesson 7: Dictionaries (Key-Value Maps)
# A **dictionary** is an unordered, mutable collection that stores data in **key-value pairs**. Instead of accessing items by index, you access them by a unique key (like looking up a word in a real dictionary).
# 
# #### 1. Creating Dictionaries
# Dictionaries use curly braces `{}`. Each key is separated from its value by a colon `:`, and pairs are separated by commas:
# ```python
# student = {
#     "name": "Alex",
#     "age": 20,
#     "course": "Python"
# }
# ```
# 
# #### 2. Basic Operations
# - **Accessing**: Retrieve a value using its key inside square brackets: `student["name"]`.
# - **Modifying**: Update a value by assigning to its key: `student["age"] = 21`.
# - **Adding**: Create a new pair by assigning to a new key: `student["city"] = "New York"`.
# - **Deleting**: Remove a key-value pair using `.pop(key)`: `student.pop("course")`.
# 
# #### 3. Iteration & Utility Methods
# - `dict.keys()`: Returns a list-like collection of all keys.
# - `dict.values()`: Returns a list-like collection of all values.
# - `dict.items()`: Returns tuples of key-value pairs. Great for looping:
#   ```python
#   for key, value in student.items():
#       print(key, ":", value)
#   ```

student = {
    "name": "Alex",
    "age": 20,
    "course": "Python"
}

print("Student:", student)

# You can get a value by using its key.

print("Student name:", student["name"])
print("Student age:", student["age"])
print("Student course:", student["course"])

# You can change a value by using its key.

student["age"] = 25
print("Updated student:", student)

# You can `add` a new key-value pair.

student["city"] = "New York"
print("After adding city:", student)

# You can remove a key-value pair with pop().

student.pop("course")
print("After pop:", student)

# len() gives the number of key-value pairs.

print("Number of items:", len(student))

# You can check if a key exists in a dictionary.

if "name" in student:
    print("The name key exists.")

# keys() shows all the keys.

print("Keys:", student.keys())

# values() shows all the values.

print("Values:", student.values())

# items() shows all key-value pairs.

print("Items:", student.items())

# You can loop through a dictionary.

for key in student:
    print("Key:", key)

# You can loop through keys and values together using items().

for key, value in student.items():
    print(key, ":", value)

# =========================
# Activity
print("============Activity Section==========")
# =========================

# #### Exercise 1
# Create a dictionary called `favorite_movie`.
# It should have these keys: title, year, and `genre`.
# Print the whole dictionary.

# #### Exercise 2
# Print only the movie title using its key.

# #### Exercise 3
# Change the year in `favorite_movie` to a different year.
# Print the updated dictionary.

# #### Exercise 4
# Add a new key called `rating`.
# Give it a value from 1 to 10.
# Print the updated dictionary.

# #### Exercise 5
# Remove the `genre` key using pop().
# Print the updated dictionary.

# #### Exercise 6
# Use a for loop with items() to print each key and value.

# =========================
# Mini Challenge
print("============Mini Challenge==========")
# =========================

# **Build a simple `contact` card program.**
# Create an empty dictionary called `contact`.
# Ask the user for their name, phone number, and `email`.
# Store each answer in the dictionary using these keys:
# name, phone, `email`
# Print the final `contact` dictionary.
# Then use a for loop with items() to print each key and value one by one.
