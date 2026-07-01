# lesson6_lists.py

# ### Lesson 6: Lists (Data Collections)
# A **list** is an ordered collection that stores multiple items in a single variable. Lists are mutable, meaning they can be modified after creation.
# 
# #### 1. Creating and Accessing Lists
# Lists use square brackets `[]` with items separated by commas:
# - **Example**: `fruits = ["apple", "banana", "cherry"]`
# - **Indexing**: Items are indexed starting at `0`.
#   - First item: `fruits[0]` (`"apple"`)
#   - Last item: `fruits[-1]` (`"cherry"`)
# 
# #### 2. Adding Elements
# - `list.append(item)`: Adds the item to the *end* of the list.
# - `list.insert(index, item)`: Inserts the item at the specific *index*, pushing subsequent items back.
# 
# #### 3. Removing Elements
# - `list.remove(value)`: Removes the first item that matches `value`.
# - `list.pop(index)`: Removes and returns the item at `index`. If no index is specified, it removes the *last* item.
# 
# #### 4. Useful List Utilities
# - `len(list)`: Returns the number of elements in the list.
# - You can iterate over items easily using a `for` loop:
#   ```python
#   for fruit in fruits:
#       print(fruit)
#   ```

fruits = ["apple", "banana", "cherry"]

print("Fruits:", fruits)

# Each item has an index.
# Indexes start at 0.

print("First fruit:", fruits[0])   # apple
print("Second fruit:", fruits[1])  # banana
print("Third fruit:", fruits[2])   # cherry

# You can change an item using its index.

fruits[1] = "mango"
print("Updated fruits:", fruits)

# append() adds an item to the end of a `list`.

fruits.append("orange")
print("After append:", fruits)

# insert() adds an item at a specific index.

fruits.insert(1, "grape")
print("After insert:", fruits)

# remove() removes an item by value.

fruits.remove("apple")
print("After remove:", fruits)

# pop() removes an item by index.
# If no index is given, it removes the last item.

fruits.pop()
print("After pop:", fruits)

# len() gives the number of items in a `list`.

print("Number of fruits:", len(fruits))

# You can loop through a `list`.

for fruit in fruits:
    print("Fruit item:", fruit)

# Lists can store different data types.

student = ["Alex", 24, True]

print("Student name:", student[0])
print("Student age:", student[1])
print("Likes Python:", student[2])

# =========================
# Activity
print("============Activity Section==========")
# =========================

# #### Exercise 1
# Create a list called `favorite_foods` with three foods.
# Print the whole `list`.

# #### Exercise 2
# Print the first item in `favorite_foods`.

# #### Exercise 3
# Change the second item in `favorite_foods` to a new food.
# Print the updated `list`.

# #### Exercise 4
# Add a new food to `favorite_foods` using append().
# Print the updated `list`.

# #### Exercise 5
# Remove one food from `favorite_foods` using remove().
# Print the updated `list`.

# #### Exercise 6
# Use a for loop to print each food in `favorite_foods`.

# =========================
# Mini Challenge
print("============Mini Challenge==========")
# =========================

# **Build a simple shopping `list` program.**
# Create an empty list called `shopping_list`.
# **Ask the user to enter three items.**
# Add each item to `shopping_list` using append().
# Print the final shopping `list`.
# Then use a for loop to print each item one by one.
