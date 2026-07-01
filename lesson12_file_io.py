# lesson12_file_io.py

# ### Lesson 12: File Operations (File I/O)
# File handling allows your programs to persist data by reading from and writing to files on the hard drive.
# 
# #### 1. Opening and Closing Files
# - `open(filename, mode)`: Opens a file. Modes include:
#   - `'r'`: Read (default). Opens file for reading; raises error if file doesn't exist.
#   - `'w'`: Write. Opens file for writing; *overwrites* existing content or creates a new file.
#   - `'a'`: Append. Opens file for adding text to the *end* of the file without deleting existing content.
# 
# #### 2. Context Manager (`with` statement)
# Always use the `with` statement when working with files. It ensures the file is automatically closed when the code block finishes, even if errors occur.
# ```python
# with open("notes.txt", "r") as file:
#     content = file.read()
# ```
# 
# #### 3. Reading Methods
# - `file.read()`: Reads the entire file into a single string.
# - `file.readline()`: Reads one line at a time.
# - `file.readlines()`: Reads all lines and returns them as a list of strings.

with open("my_first_file.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is my first file.\n")
    file.write("Python file I/O is easy.\n")

print("File written successfully!")

# Writing multiple lines at once
lines = ["Line 1: Apple\n", "Line 2: Banana\n", "Line 3: Cherry\n"]
with open("fruits.txt", "w") as file:
    file.writelines(lines)

# Appending to a file (does NOT overwrite)
with open("my_first_file.txt", "a") as file:
    file.write("This line was appended.\n")

print("Lines appended!")

# =============================================
# #### Exercise 2
# =============================================

# Method 1: read() -- reads the ENTIRE file as one string
with open("my_first_file.txt", "r") as file:
    content = file.read()
    print("--- read() output ---")
    print(content)

# Method 2: readlines() -- reads all lines into a `list`
with open("my_first_file.txt", "r") as file:
    lines_list = file.readlines()
    print("--- readlines() output ---")
    print(lines_list)

# Method 3: readline() -- reads one line at a time
with open("my_first_file.txt", "r") as file:
    first = file.readline()
    second = file.readline()
    print("--- readline() output ---")
    print("First:", first.strip())
    print("Second:", second.strip())

# Method 4: Loop through the file directly (BEST for large files)
print("--- Loop output ---")
with open("my_first_file.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())  # strip() removes the \n

# =============================================
# #### Exercise 3
# =============================================
import os

# Check if a file exists
print("Does my_first_file.txt exist?", os.path.exists("my_first_file.txt"))
print("Does ghost.txt exist?", os.path.exists("ghost.txt"))

# Get the absolute path of a file
print("Absolute path:", os.path.abspath("my_first_file.txt"))

# Get file size in bytes
print("File size:", os.path.getsize("my_first_file.txt"), "bytes")

# Delete a file
# os.remove("fruits.txt")  # Uncomment to delete
# print("fruits.txt deleted")

# Check if it's a file or directory
print("Is file?", os.path.isfile("my_first_file.txt"))
print("Is directory?", os.path.isdir("my_first_file.txt"))

# =============================================
# #### Exercise 4
# =============================================

# Create a sample data file
with open("scores.txt", "w") as file:
    file.write("Alex:95\n")
    file.write("Ana:88\n")
    file.write("Luis:92\n")
    file.write("Sara:78\n")
    file.write("Tom:85\n")

# Read and process the data
print("\n--- Score Report ---")
scores = {}
with open("scores.txt", "r") as file:
    for line in file:
        line = line.strip()
        if ":" in line:
            name, score = line.split(":")
            scores[name] = int(score)

for name, score in scores.items():
    print(f"{name}: {score}")

# Calculate average
average = sum(scores.values()) / len(scores)
print(f"Average score: {average:.1f}")

# Find highest score
highest_name = max(scores, key=lambda name: scores[name])
print(f"Highest: {highest_name} with {scores[highest_name]}")

# =============================================
# #### Exercise 5
# =============================================
# CSV = Comma Separated Values. Very common data format.

# Writing CSV data
students = [
    ["Name", "Age", "Grade"],
    ["Alex", "24", "A"],
    ["Ana", "22", "B+"],
    ["Luis", "25", "A-"],
]

with open("students.csv", "w") as file:
    for row in students:
        line = ",".join(row)
        file.write(line + "\n")

print("CSV file written!")

# Reading CSV data
print("\n--- Student Records ---")
with open("students.csv", "r") as file:
    header = file.readline().strip().split(",")
    print("Columns:", header)
    for line in file:
        row = line.strip().split(",")
        print(f"  {row[0]} is {row[1]} years old, grade: {row[2]}")

# =============================================
# #### Exercise 6
# =============================================
# JSON is the most common format for storing structured data.
import json

# Writing JSON
data = {
    "name": "Alex",
    "age": 20,
    "courses": ["Python", "DevOps", "AI"],
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # indent=4 makes it pretty

print("JSON file written!")

# Reading JSON
with open("data.json", "r") as file:
    loaded = json.load(file)

print("Loaded JSON:", loaded)
print("Name:", loaded["name"])
print("Courses:", loaded["courses"])

# =============================================
# #### Exercise 7
# =============================================

# Always handle file errors -- files might not exist or be accessible.

try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
except PermissionError:
    print("Error: No permission to read this file!")
except Exception as e:
    print(f"Unexpected error: {e}")

# =============================================
# ACTIVITY SECTION
# =============================================
print("============Activity Section==========")

# #### Exercise 1
# Create a file called "about_me.txt".
# Write 5 lines about yourself (name, age, hobbies, etc.).
# Read it back and print each line with a line number.

# #### Exercise 2
# Create a function called log_message.
# It should accept a message string.
# It should append the message to "log.txt" with a timestamp.
# Hint: from datetime import datetime; datetime.now()
# Call it 3 times with different messages, then read the file.

# #### Exercise 3
# Create a file called "story.txt" with a short paragraph.
# Read it and count how many times each word appears.
# Print the top 5 most common words.
# Hint: use a dictionary and the .get() method.

# #### Exercise 4
# Create a JSON config file for a game with:
#   - player_name, level, health, inventory (`list` of items)
# Write it to "config.json".
# Read it back and print a summary.
# Then modify the level to +1 and save it again.

# #### Exercise 5
# Create a function called copy_file.
# It should accept a source filename and destination filename.
# It should read the source and write its contents to the destination.
# Handle the case where the source file doesn't exist.

# =============================================
# MINI CHALLENGE: To-Do List with File Persistence
# =============================================
print("============Mini Challenge==========")

# Build a to-do `list` that SAVES to a file.
# The program should:
# 1. Load existing tasks from "todo.json" on startup.
# 2. Show a menu:
#    - Add a task
#    - View all tasks
#    - Mark a task as done
#    - Delete a task
#    - Save and quit
# 3. Save all tasks to "todo.json" when quitting.
#
# Each task should have: id, description, done (`True`/`False`)
# Use JSON to store the `list` of tasks.
# Use error handling for invalid input and missing files.
