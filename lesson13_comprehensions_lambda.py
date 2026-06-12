# lesson13_comprehensions_lambda.py

# Lesson 13: List Comprehensions & Lambda Functions
# These are powerful Python features that let you write
# concise, expressive code. This is where Python starts to shine.

# =============================================
# PART 1: LIST COMPREHENSIONS
# =============================================
# A list comprehension creates a new list in one line.
# It replaces a for loop that builds a list.

# Traditional way:
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
print("Traditional:", squares)  # [1, 4, 9, 16, 25]

# List comprehension way:
squares = [n ** 2 for n in range(1, 6)]
print("Comprehension:", squares)  # [1, 4, 9, 16, 25]

# The pattern: [expression for item in iterable]

# More examples:
doubles = [n * 2 for n in range(1, 11)]
print("Doubles:", doubles)

lengths = [len(word) for word in ["hello", "world", "python"]]
print("Lengths:", lengths)

uppercased = [name.upper() for name in ["mark", "ana", "luis"]]
print("Uppercased:", uppercased)

# =============================================
# PART 2: LIST COMPREHENSIONS WITH CONDITIONS
# =============================================

# Filter with if (at the end):
evens = [n for n in range(1, 21) if n % 2 == 0]
print("Evens:", evens)

long_words = [w for w in ["hi", "hello", "hey", "greetings"] if len(w) > 3]
print("Long words:", long_words)

# if-else at the beginning (ternary):
labels = ["even" if n % 2 == 0 else "odd" for n in range(1, 8)]
print("Labels:", labels)

# Replace negative numbers with 0:
numbers = [5, -3, 8, -1, 0, -7, 4]
cleaned = [n if n >= 0 else 0 for n in numbers]
print("Cleaned:", cleaned)

# =============================================
# PART 3: NESTED LIST COMPREHENSIONS
# =============================================

# Flatten a 2D list (matrix):
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print("Flattened:", flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a multiplication table:
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("Multiplication table:")
for row in table:
    print(row)

# Get diagonal of a matrix:
diagonal = [matrix[i][i] for i in range(len(matrix))]
print("Diagonal:", diagonal)  # [1, 5, 9]

# =============================================
# PART 4: DICTIONARY & SET COMPREHENSIONS
# =============================================

# Dictionary comprehension:
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
print("Word lengths:", word_lengths)

# Swap keys and values:
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print("Swapped:", swapped)

# Filter a dictionary:
scores = {"Mark": 95, "Ana": 88, "Luis": 92, "Sara": 78, "Tom": 85}
high_scorers = {name: score for name, score in scores.items() if score >= 90}
print("High scorers:", high_scorers)

# Set comprehension (removes duplicates):
words = ["hello", "world", "hello", "python", "world"]
unique_lengths = {len(w) for w in words}
print("Unique lengths:", unique_lengths)

# =============================================
# PART 5: LAMBDA FUNCTIONS
# =============================================
# A lambda is a small anonymous function (no name).
# Syntax: lambda parameters: expression

# Regular function:
def square(x):
    return x ** 2

# Equivalent lambda:
square_lambda = lambda x: x ** 2
print("Lambda square:", square_lambda(5))  # 25

# Lambda with multiple parameters:
add = lambda a, b: a + b
print("Lambda add:", add(3, 7))  # 10

# Lambda with no parameters:
greet = lambda: "Hello!"
print("Lambda greet:", greet())

# Lambdas are most useful when passed to other functions.

# =============================================
# PART 6: SORTING WITH LAMBDA
# =============================================

# Sort a list of tuples by second element:
students = [("Mark", 95), ("Ana", 88), ("Luis", 92), ("Sara", 78)]
students.sort(key=lambda student: student[1])  # Sort by score
print("Sorted by score:", students)

# Sort descending:
students.sort(key=lambda s: s[1], reverse=True)
print("Sorted desc:", students)

# Sort strings by length:
words = ["banana", "pie", "Washington", "book"]
words.sort(key=lambda w: len(w))
print("Sorted by length:", words)

# Sort dictionary by value:
scores = {"Mark": 95, "Ana": 88, "Luis": 92, "Sara": 78}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))
print("Sorted by score:", sorted_scores)

# =============================================
# PART 7: map(), filter(), sorted()
# =============================================
# These built-in functions work great with lambdas.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() -- apply a function to every item
squares = list(map(lambda x: x ** 2, numbers))
print("map squares:", squares)

# filter() -- keep only items that pass a test
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("filter evens:", evens)

# sorted() -- return a new sorted list (doesn't modify original)
desc = sorted(numbers, key=lambda x: -x)
print("sorted desc:", desc)

# Combine map and filter:
# Square only the even numbers:
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print("Even squares:", result)

# Same thing with comprehension (usually preferred):
result2 = [x ** 2 for x in numbers if x % 2 == 0]
print("Even squares (comp):", result2)

# =============================================
# PART 8: USEFUL ONE-LINERS
# =============================================

# Find all vowels in a sentence:
sentence = "The quick brown fox jumps over the lazy dog"
vowels = [ch for ch in sentence.lower() if ch in "aeiou"]
print("Vowels found:", vowels)

# Extract all numbers from a mixed list:
mixed = [1, "hello", 3.14, "world", 42, True, None, 7]
numbers_only = [x for x in mixed if isinstance(x, (int, float)) and not isinstance(x, bool)]
print("Numbers only:", numbers_only)

# Create a dict from two lists:
keys = ["name", "age", "city"]
values = ["Mark", 24, "New York"]
combined = {k: v for k, v in zip(keys, values)}
print("Combined:", combined)

# zip() pairs items from multiple lists:
names = ["Mark", "Ana", "Luis"]
scores = [95, 88, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# =============================================
# ACTIVITY SECTION
# =============================================
print("============Activity Section==========")

# Exercise 1: Basic Comprehensions
# Create the following using list comprehensions:
# a) A list of cubes for numbers 1-10
# b) A list of only the vowels from the string "Programming is fun"
# c) A list of tuples (number, square) for numbers 1-5
# d) A list of all numbers 1-100 divisible by both 3 and 5

# Exercise 2: Dictionary Comprehension
# Given: words = ["apple", "banana", "cherry", "date", "elderberry"]
# Create a dictionary where keys are words and values are:
#   - "short" if length <= 5
#   - "medium" if length is 6-8
#   - "long" if length > 8

# Exercise 3: Sorting Challenge
# Given a list of dictionaries:
#   people = [{"name": "Mark", "age": 24}, {"name": "Ana", "age": 30}, ...]
# Sort them by age (ascending) using sorted() and lambda.
# Then sort them by name length (descending).

# Exercise 4: map/filter
# Given: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using map and filter (not comprehensions):
# a) Get a list of odd numbers doubled
# b) Get a list of numbers > 5, each subtracted by 1
# Then do the same with list comprehensions and compare.

# Exercise 5: Matrix Operations
# Given matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Using comprehensions:
# a) Get the second column: [2, 5, 8]
# b) Get all even numbers from the matrix
# c) Create a new matrix where each value is doubled

# =============================================
# MINI CHALLENGE: Data Processing Pipeline
# =============================================
print("============Mini Challenge==========")

# Process a list of student records.
# Given raw data as a list of strings:
#   ["Mark,95,Math", "Ana,88,Science", "Luis,92,Math", "Sara,78,English"]
#
# 1. Parse each string into a dictionary with keys: name, score, subject
# 2. Filter to only students with score >= 85
# 3. Sort by score descending
# 4. Create a summary: list of strings like "Mark (Math): 95"
# 5. Calculate average score per subject
#
# Use comprehensions, lambda, map, filter, and sorted.
# Do it once with a traditional loop approach, then with comprehensions.
# Compare the two approaches.
