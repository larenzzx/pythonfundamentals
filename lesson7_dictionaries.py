# lesson7_dictionaries.py

# Lesson 7: Dictionaries
# A dictionary stores data using key-value pairs.
#
# A key is the name used to find a value.
# A value is the data stored under that key.

# Dictionaries use curly braces.

student = {
    "name": "Mark",
    "age": 24,
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

# You can add a new key-value pair.

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

# Exercise 1:
# Create a dictionary called favorite_movie.
# It should have these keys: title, year, and genre.
# Print the whole dictionary.
favorite_movie = {
    "title": "John Wick",
    "year": 2014,
    "genre": "Action"
}
print("Favorite Movie:", favorite_movie)

# Exercise 2:
# Print only the movie title using its key.
print("Movie title:", favorite_movie["title"])

# Exercise 3:
# Change the year in favorite_movie to a different year.
# Print the updated dictionary.
favorite_movie["year"] = 2017
print("After favorite movie update:", favorite_movie)

# Exercise 4:
# Add a new key called rating.
# Give it a value from 1 to 10.
# Print the updated dictionary.
favorite_movie["rating"] = 10
print("Updated favorite movie:", favorite_movie)

# Exercise 5:
# Remove the genre key using pop().
# Print the updated dictionary.
favorite_movie.pop("genre")
print("After pop:", favorite_movie)

# Exercise 6:
# Use a for loop with items() to print each key and value.
for key, value in favorite_movie.items():
    print(key, ":", value )

# =========================
# Mini Challenge
print("============Mini Challenge==========")
# =========================

# Build a simple contact card program.
# Create an empty dictionary called contact.
# Ask the user for their name, phone number, and email.
# Store each answer in the dictionary using these keys:
# name, phone, email
# Print the final contact dictionary.
# Then use a for loop with items() to print each key and value one by one.
contact = {}
name = input("Enter your name: ")
number = int(input("Enter your number: "))
email = input("Enter your email: ")
contact["names"] = name
contact["number"] = number
contact["email"] = email
print(contact)
for key, value in contact.items():
    print(key, ":", value)