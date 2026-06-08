# lesson5_loops.py

# Lesson 5: Loops
# Loops let you repeat code without writing it many times.

# A for loop repeats over a sequence.
# range(5) gives numbers from 0 to 4.

for number in range(5):
    print("For loop number:", number)

# You can choose a start and stop number.
# range(1, 6) gives numbers from 1 to 5.

for number in range(1, 6):
    print("Counting:", number)

# You can loop through text.

word = "Python"

for letter in word:
    print("Letter:", letter)

# A while loop repeats while a condition is True.

count = 1

while count <= 5:
    print("While loop count:", count)
    count += 1  # update the variable so the loop can stop

# break stops a loop early.

for number in range(1, 10):
    if number == 5:
        break
    print("Before break:", number)

# continue skips the current loop step and moves to the next one.

for number in range(1, 6):
    if number == 3:
        continue
    print("After continue:", number)


# =========================
# Activity
print("============Activity Section==========")
# =========================

# Exercise 1:
# Use a for loop to print numbers from 1 to 10.


# Exercise 2:
# Use a for loop to print each letter in your first name.


# Exercise 3:
# Use a while loop to print numbers from 1 to 5.


# Exercise 4:
# Use a for loop with range(1, 11).
# Print only the even numbers.
# Hint: A number is even if number % 2 == 0.


# Exercise 5:
# Use a while loop to count down from 5 to 1.


# =========================
# Mini Challenge
print("============Mini Challenge==========")
# =========================

# Build a simple multiplication table.
# Ask the user for a number.
# Use a for loop to print that number multiplied by 1 through 10.
#
# Example:
# Enter a number: 3
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# ... continue until 10
