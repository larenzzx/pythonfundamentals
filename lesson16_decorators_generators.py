# lesson16_decorators_generators.py

# Lesson 16: Decorators, Generators & Iterators
# These are advanced Python features that separate beginners from
# intermediate/advanced developers. They're used everywhere in
# real Python code -- web frameworks, data science, automation.


# =============================================
# PART 1: FUNCTIONS AS FIRST-CLASS OBJECTS
# =============================================
# In Python, functions are objects. You can:
# - Assign them to variables
# - Pass them as arguments
# - Return them from other functions

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

# Assign function to a variable
my_func = greet
print(my_func("Mark"))  # "Hello, Mark!"

# Pass function as argument
def execute_function(func, value):
    return func(value)

print(execute_function(greet, "Ana"))
print(execute_function(farewell, "Luis"))

# Return function from function
def get_function(choice):
    if choice == "greet":
        return greet
    else:
        return farewell

selected = get_function("greet")
print(selected("Sara"))


# =============================================
# PART 2: CLOSURES
# =============================================
# A closure is a function that remembers variables from the outer
# scope even after the outer function has finished running.

def make_multiplier(factor):
    """Returns a function that multiplies by the given factor."""
    def multiplier(number):
        return number * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
quadruple = make_multiplier(4)

print("Double 5:", double(5))       # 10
print("Triple 5:", triple(5))       # 15
print("Quadruple 5:", quadruple(5))  # 20

# Each function "remembers" its own factor value.
print("Double 10:", double(10))     # 20
print("Triple 10:", triple(10))     # 30

# Another closure example: counter
def make_counter():
    count = 0
    def counter():
        nonlocal count  # Allows modifying the outer variable
        count += 1
        return count
    return counter

counter_a = make_counter()
counter_b = make_counter()
print(counter_a())  # 1
print(counter_a())  # 2
print(counter_a())  # 3
print(counter_b())  # 1 (independent of counter_a)


# =============================================
# PART 3: DECORATORS
# =============================================
# A decorator wraps a function to add extra behavior.
# This is one of Python's most powerful and common patterns.

import time
import functools

# Manual decorator (the concept):
def my_decorator(func):
    @functools.wraps(func)  # Preserves the original function's name and docstring
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished.")
        return result
    return wrapper

@my_decorator  # This is syntactic sugar for: say_hello = my_decorator(say_hello)
def say_hello(name):
    """Says hello to someone."""
    print(f"Hello, {name}!")

say_hello("Mark")
print("Function name:", say_hello.__name__)  # Thanks to functools.wraps
print("Docstring:", say_hello.__doc__)


# --- Timing decorator ---
def timer(func):
    """Measures how long a function takes to run."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    total = 0
    for i in range(1_000_000):
        total += i
    return total

result = slow_function()
print("Result:", result)


# --- Retry decorator ---
def retry(max_attempts=3):
    """Retries a function if it fails."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        print("All attempts failed.")
                        raise
        return wrapper
    return decorator

@retry(max_attempts=3)
def risky_operation():
    """Simulates something that might fail."""
    import random
    if random.random() < 0.5:
        raise ValueError("Random failure!")
    return "Success!"

try:
    print(risky_operation())
except ValueError:
    print("Operation failed after all retries.")


# --- Logging decorator ---
def log_calls(func):
    """Logs function calls with arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join([str(a) for a in args])
        kwargs_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"[LOG] Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(3, 5)
add(10, b=20)


# --- Chaining multiple decorators ---
@timer
@log_calls
@my_decorator
def process_data(data):
    """Processes data slowly."""
    time.sleep(0.1)
    return [x * 2 for x in data]

print("Processed:", process_data([1, 2, 3, 4, 5]))
# Decorators execute bottom-up: my_decorator -> log_calls -> timer


# =============================================
# PART 4: GENERATORS
# =============================================
# A generator produces values one at a time using yield.
# It "pauses" between values, saving memory.

# Normal function: computes ALL values at once, returns a list.
def get_squares_list(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

print("List:", get_squares_list(10))  # All in memory at once

# Generator: yields one value at a time, pauses between each.
def get_squares_gen(n):
    for i in range(n):
        yield i ** 2  # yield = "give me one value, then pause"

# It returns a generator object (not a list)
gen = get_squares_gen(10)
print("Generator object:", gen)

# Get values one at a time with next()
print("Next:", next(gen))   # 0
print("Next:", next(gen))   # 1
print("Next:", next(gen))   # 4

# Or loop through the rest
for square in gen:
    print("Remaining:", square)


# Why generators matter: memory efficiency
import sys

# A list of 1 million numbers
big_list = list(range(1_000_000))
print("List size:", sys.getsizeof(big_list), "bytes")

# A generator of 1 million numbers (just the recipe, not the values)
big_gen = range(1_000_000)
print("Generator size:", sys.getsizeof(big_gen), "bytes")
# range() is a generator -- it doesn't store all values in memory!


# --- Generator expressions (like list comprehensions but lazy) ---
# List comprehension: []
squares_list = [x ** 2 for x in range(10)]
print("List comp:", squares_list)

# Generator expression: ()
squares_gen = (x ** 2 for x in range(10))
print("Gen exp:", squares_gen)
print("Gen values:", list(squares_gen))


# --- Real-world generator: reading large files line by line ---
def read_large_file(filename):
    """Reads a file line by line without loading it all into memory."""
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

# for line in read_large_file("huge_log.txt"):
#     process(line)


# --- Infinite generator ---
def fibonacci():
    """Generates the Fibonacci sequence forever."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print("First 15 Fibonacci numbers:")
for _ in range(15):
    print(next(fib), end=" ")
print()


# --- send() -- two-way communication with generators ---
def running_total():
    """Accumulates values sent to it."""
    total = 0
    while True:
        value = yield total  # Receives value AND yields total
        if value is not None:
            total += value

acc = running_total()
next(acc)  # Prime the generator (advance to first yield)
print(acc.send(10))   # 10
print(acc.send(20))   # 30
print(acc.send(5))    # 35


# =============================================
# PART 5: ITERATORS
# =============================================
# Any object with __iter__() and __next__() is an iterator.
# You can make your own iterable classes.

class Countdown:
    """Counts down from a number to 0."""
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

print("Countdown from 5:")
for num in Countdown(5):
    print(num, end=" ")
print()

# Another example: iterate over characters in a string, skip spaces
class NoSpaceIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        while self.index < len(self.text):
            char = self.text[self.index]
            self.index += 1
            if char != " ":
                return char
        raise StopIteration

print("No spaces:", list(NoSpaceIterator("Hello World")))
# ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']


# =============================================
# PART 6: PUTTING IT ALL TOGETHER
# =============================================

# A practical example: a pipeline using generators
def read_records(filename):
    """Generator that reads records from a CSV file."""
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

def parse_records(lines):
    """Generator that parses comma-separated lines into dicts."""
    header = None
    for line in lines:
        values = line.split(",")
        if header is None:
            header = values
        else:
            yield dict(zip(header, values))

def filter_records(records, key, min_value):
    """Generator that filters records by a minimum value."""
    for record in records:
        try:
            if float(record.get(key, 0)) >= min_value:
                yield record
        except (ValueError, TypeError):
            pass

# If we had a students.csv file named "data.csv", we could do:
# pipeline = filter_records(
#     parse_records(
#         read_records("data.csv")
#     ),
#     "score", 85
# )
# for record in pipeline:
#     print(record)
# Each step processes ONE record at a time -- almost zero memory!


# =============================================
# ACTIVITY SECTION
# =============================================
print("============Activity Section==========")

# Exercise 1: Closures
# Create a make_power(exponent) function that returns a closure.
# The closure should raise any number to that exponent.
# square = make_power(2)  -> square(5) = 25
# cube = make_power(3)    -> cube(3) = 27

# Exercise 2: Simple Decorator
# Create a @shout decorator that:
#   - Converts the return value to uppercase
#   - Adds "!!!" to the end
# Apply it to a function that returns a greeting string.
# Example: greet("mark") -> "HELLO, MARK!!!"

# Exercise 3: Timer Decorator
# Add the @timer decorator from this lesson to:
#   - A function that sorts a list of 100,000 random numbers
#   - A function that builds a list of 100,000 squares
# Compare the execution times.

# Exercise 4: Generator -- Primes
# Create a generator function called primes() that yields
# prime numbers infinitely.
# Use it to print the first 20 prime numbers.
# Hint: A number is prime if it's not divisible by any number from 2 to sqrt(n).

# Exercise 5: Custom Iterator
# Create a Range class that works like Python's range() but:
#   - Accepts start, stop, step
#   - Is its own iterator
#   - Works with for loops
# Test: for i in Range(0, 20, 3): print(i)
# Expected: 0, 3, 6, 9, 12, 15, 18


# =============================================
# MINI CHALLENGE: Decorator Logger + Generator Pipeline
# =============================================
print("============Mini Challenge==========")

# Part A: Create a @cache decorator
#   - Stores the results of a function based on its arguments.
#   - If called again with the same arguments, return the stored result.
#   - Print "Computing..." when actually computing.
#   - Print "Using cache!" when returning cached result.
#   Test with a slow function like:
#     @cache
#     def expensive_calc(x, y):
#         import time
#         time.sleep(1)
#         return x + y
#
#     expensive_calc(1, 2)  # Takes 1 second, prints "Computing..."
#     expensive_calc(1, 2)  # Instant, prints "Using cache!"
#     expensive_calc(3, 4)  # Takes 1 second, different args


# Part B: Build a log file analyzer using a generator pipeline:
#   1. read_lines(filename) -- generator that yields lines from a file
#   2. parse_errors(lines) -- generator that yields only lines with "ERROR"
#   3. extract_messages(errors) -- generator that yields the error message only
#   4. count_errors(messages) -- counts total errors
#
# Create a sample log file with mixed INFO, WARNING, and ERROR lines.
# Run the pipeline and print the error count and each error message.
# The key benefit: even a 10GB log file uses almost no memory!
