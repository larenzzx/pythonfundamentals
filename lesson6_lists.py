# lesson6_lists.py

# Lesson 6: Lists
# A list stores multiple values in one variable.

# Lists use square brackets.

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

# append() adds an item to the end of a list.

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

# len() gives the number of items in a list.

print("Number of fruits:", len(fruits))

# You can loop through a list.

for fruit in fruits:
    print("Fruit item:", fruit)

# Lists can store different data types.

student = ["Mark", 24, True]

print("Student name:", student[0])
print("Student age:", student[1])
print("Likes Python:", student[2])


# =========================
# Activity
print("============Activity Section==========")
# =========================

# Exercise 1:
# Create a list called favorite_foods with three foods.
# Print the whole list.
favorite_foods = ["Chicken Wings", "Fries", "Sinigang"]
print("Favorite Foods:", favorite_foods)

# Exercise 2:
# Print the first item in favorite_foods.
print(favorite_foods[0])

# Exercise 3:
# Change the second item in favorite_foods to a new food.
# Print the updated list.
favorite_foods[1] = "Steak"
print("Updated fav foods:", favorite_foods)

# Exercise 4:
# Add a new food to favorite_foods using append().
# Print the updated list.
favorite_foods.append("Burger")
print("Updated fav foods:", favorite_foods)

# Exercise 5:
# Remove one food from favorite_foods using remove().
# Print the updated list.
favorite_foods.remove("Sinigang")
print("Updated fav foods:", favorite_foods)

# Exercise 6:
# Use a for loop to print each food in favorite_foods.
for fav in favorite_foods:
    print("My favorite foods:", fav)

# =========================
# Mini Challenge
print("============Mini Challenge==========")
# =========================

# Build a simple shopping list program.
# Create an empty list called shopping_list.
# Ask the user to enter three items.
# Add each item to shopping_list using append().
# Print the final shopping list.
# Then use a for loop to print each item one by one.
shopping_list = []
x = input("Enter a shopping item: ")
y = input("Enter a shopping item: ")
z = input("Enter a shopping item: ")
shopping_list.append(x)
shopping_list.append(y)
shopping_list.append(z)
print("Shopping lists:", shopping_list)
for items in shopping_list:
    print("Shopping item: ", items)