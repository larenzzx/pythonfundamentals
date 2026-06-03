# lesson14_oop.py

# Lesson 14: Object-Oriented Programming (OOP)
# OOP is a way of organizing code into "objects" that combine
# data (attributes) and behavior (methods).
# This is how most real-world Python projects are structured.


# =============================================
# PART 1: CLASSES AND OBJECTS
# =============================================
# A class is a blueprint. An object is an instance of a class.
# Think of a class as a cookie cutter and objects as the cookies.

class Dog:
    # Class attribute -- shared by ALL instances
    species = "Canis familiaris"

    # __init__ is the constructor. It runs when you create a new object.
    # self refers to the specific object being created.
    def __init__(self, name, age):
        self.name = name    # Instance attribute (unique to each object)
        self.age = age      # Instance attribute

    # Method -- a function that belongs to a class
    def bark(self):
        return f"{self.name} says Woof!"

    def describe(self):
        return f"{self.name} is {self.age} years old."

    def __str__(self):
        # This is what print() shows
        return f"Dog(name={self.name}, age={self.age})"


# Create objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.describe())
print(dog2.bark())
print(dog1)  # Uses __str__
print("Species:", Dog.species)
print("Species:", dog1.species)  # Can also access via instance


# =============================================
# PART 2: THE FOUR PILLARS OF OOP
# =============================================

# --- ENCAPSULATION: Hide internal details, expose only what's needed ---
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Double underscore = private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds or invalid amount."

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account({self.owner}, Balance: ${self.__balance})"


account = BankAccount("Mark", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print("Balance:", account.get_balance())
# print(account.__balance)  # AttributeError -- it's private!
# Python uses "name mangling" -- it's actually _BankAccount__balance
# but you should NEVER access it directly.


# --- INHERITANCE: A class can inherit from another ---
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"


class Cat(Animal):  # Cat inherits from Animal
    def __init__(self, name, sound="Meow", indoor=True):
        super().__init__(name, sound)  # Call parent's __init__
        self.indoor = indoor  # New attribute specific to Cat

    def purr(self):
        return f"{self.name} is purring."


class Cow(Animal):
    def __init__(self, name, sound="Moo"):
        super().__init__(name, sound)

    def produce_milk(self):
        return f"{self.name} is being milked."


cat = Cat("Whiskers")
cow = Cow("Bessie")

print(cat.speak())         # Inherited from Animal
print(cat.purr())          # Cat's own method
print(cow.speak())         # Inherited from Animal
print(cow.produce_milk())  # Cow's own method

# Check inheritance
print("Cat is Animal?", isinstance(cat, Animal))  # True
print("Cat is Cat?", isinstance(cat, Cat))         # True
print("Cow is Cat?", isinstance(cow, Cat))         # False


# --- POLYMORPHISM: Same method name, different behavior ---
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

    def describe(self):
        return f"I am a {self.__class__.__name__}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Polymorphism in action -- same method call, different results
shapes = [Rectangle(5, 3), Circle(4), Triangle(6, 8)]
for shape in shapes:
    print(f"{shape.describe()}: area = {shape.area():.2f}")


# --- ABSTRACTION: Only show essential details ---
# (Achieved through careful class design -- hiding complex logic behind
# simple method names)
class CoffeeMachine:
    def __init__(self):
        self.__water = 1000   # ml, private
        self.__beans = 500    # grams, private

    def make_coffee(self, size="medium"):
        # User doesn't need to know about water/bean management
        water_needed = {"small": 100, "medium": 200, "large": 300}
        beans_needed = {"small": 10, "medium": 20, "large": 30}

        w = water_needed.get(size, 200)
        b = beans_needed.get(size, 20)

        if self.__water >= w and self.__beans >= b:
            self.__water -= w
            self.__beans -= b
            return f"Here's your {size} coffee!"
        return "Not enough water or beans!"

    def refill(self):
        self.__water = 1000
        self.__beans = 500
        return "Machine refilled."


machine = CoffeeMachine()
print(machine.make_coffee("large"))
print(machine.make_coffee("medium"))


# =============================================
# PART 3: SPECIAL (DUNDER) METHODS
# =============================================
# These let your objects work with Python's built-in operations.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        # For print() and str()
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        # For debugging and repr()
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        # For len()
        return self.pages

    def __eq__(self, other):
        # For ==
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __lt__(self, other):
        # For < (less than) -- enables sorting
        return self.pages < other.pages

    def __add__(self, other):
        # For +
        return self.pages + other.pages

    def __getitem__(self, key):
        # For [] indexing
        data = {"title": self.title, "author": self.author, "pages": self.pages}
        return data.get(key, "Not found")


book1 = Book("Python Basics", "John Doe", 300)
book2 = Book("Advanced Python", "Jane Smith", 450)
book3 = Book("Python Basics", "John Doe", 300)

print(book1)                        # __str__
print(repr(book1))                  # __repr__
print("Pages:", len(book1))         # __len__
print("Same?", book1 == book3)      # __eq__
print("Less?", book1 < book2)       # __lt__
print("Total pages:", book1 + book2)  # __add__
print("Title:", book1["title"])     # __getitem__

# Sorting books by page count
books = [book2, book1]
books.sort()
print("Sorted:", [str(b) for b in books])


# =============================================
# PART 4: @property DECORATOR
# =============================================
# Lets you access methods like attributes (no parentheses needed).

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Single underscore = "protected" by convention

    @property
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

    @property
    def kelvin(self):
        return self._celsius + 273.15

    def __str__(self):
        return f"{self.celsius:.1f}C / {self.fahrenheit:.1f}F / {self.kelvin:.1f}K"


temp = Temperature(100)
print(temp)
print("Celsius:", temp.celsius)      # Looks like an attribute!
print("Fahrenheit:", temp.fahrenheit)
temp.fahrenheit = 32                 # Uses the setter
print("After setting F:", temp)


# =============================================
# PART 5: CLASS METHODS AND STATIC METHODS
# =============================================

class Employee:
    # Class variable
    employee_count = 0
    raise_percent = 1.04  # 4% raise

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_percent)

    @classmethod
    def set_raise_percent(cls, amount):
        """Affects ALL employees."""
        cls.raise_percent = amount

    @classmethod
    def from_string(cls, emp_string):
        """Alternative constructor from a string like 'Mark-50000'."""
        name, salary = emp_string.split("-")
        return cls(name, int(salary))

    @staticmethod
    def is_workday(day):
        """Does not need self or cls -- just a utility function."""
        return day.weekday() < 5  # Mon-Fri are 0-4

    def __str__(self):
        return f"{self.name}: ${self.salary}"


emp1 = Employee("Mark", 50000)
emp2 = Employee("Ana", 60000)
print(emp1)
print(emp2)

Employee.set_raise_percent(1.05)  # 5% raise for everyone
emp1.apply_raise()
print("After raise:", emp1)

# Alternative constructor
emp3 = Employee.from_string("Luis-55000")
print("From string:", emp3)

# Static method
from datetime import date
print("Is Monday a workday?", Employee.is_workday(date(2025, 1, 6)))
print("Is Saturday a workday?", Employee.is_workday(date(2025, 1, 11)))
print("Total employees:", Employee.employee_count)


# =============================================
# ACTIVITY SECTION
# =============================================
print("============Activity Section==========")

# Exercise 1: Create a Car Class
# Attributes: make, model, year, mileage
# Methods:
#   - drive(miles) -- adds to mileage
#   - get_info() -- returns a formatted string
#   - is_old() -- returns True if year < 2015
# Create 3 car objects and test all methods.

# Exercise 2: Inheritance - Vehicle Hierarchy
# Create a Vehicle base class with: make, model, year
# Create subclasses: Truck (adds towing_capacity), Motorcycle (adds has_sidecar)
# Each subclass should have its own __str__ that adds its unique info.
# Create instances and print them.

# Exercise 3: Encapsulation - Student Grade System
# Create a Student class with:
#   - name (public)
#   - __grades (private list)
#   - add_grade(grade) -- validates 0-100
#   - get_average() -- returns average grade
#   - get_highest() -- returns highest grade
#   - get_lowest() -- returns lowest grade
# Test with at least 5 grades.

# Exercise 4: Dunder Methods - Vector Class
# Create a Vector class that holds x and y.
# Implement: __str__, __add__ (vector addition), __sub__ (subtraction),
#   __mul__ (scalar multiplication), __len__ (magnitude/distance from origin),
#   __eq__ (equality)
# Test: v1 = Vector(3, 4), v2 = Vector(1, 2)
#   v1 + v2 should give Vector(4, 6)
#   len(v1) should give 5.0 (sqrt(9+16))

# Exercise 5: @property - Rectangle Class
# Create a Rectangle class with width and height.
# Properties: area, perimeter, is_square
# Setters for width and height that validate positive numbers.
# __str__ that shows all info.


# =============================================
# MINI CHALLENGE: Library Management System
# =============================================
print("============Mini Challenge==========")

# Build a library system with these classes:
#
# Book:
#   - title, author, isbn, is_checked_out (bool)
#   - check_out() -- marks as checked out
#   - return_book() -- marks as available
#
# Member:
#   - name, member_id, borrowed_books (list)
#   - borrow_book(book) -- adds to list if available
#   - return_book(book) -- removes from list
#
# Library:
#   - name, books (list), members (list)
#   - add_book(book), remove_book(isbn)
#   - register_member(member)
#   - find_book(title) -- returns matching books
#   - available_books() -- returns list of available books
#   - checked_out_books() -- returns list of checked out books
#
# Create a menu-driven program that lets the user:
#   1. View all books
#   2. Search for a book
#   3. Register a new member
#   4. Check out a book
#   5. Return a book
#   6. View available books
#   7. Exit
#
# Use OOP principles: encapsulation, proper __str__ methods,
# and error handling throughout.
