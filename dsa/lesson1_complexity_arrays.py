# dsa/lesson1_complexity_arrays.py

"""
=============================================================================
DSA Lesson 1: Time/Space Complexity & Dynamic Arrays
=============================================================================
Topic: Big O Notation, Memory Layout, and Custom Dynamic Array Implementation
"""

import sys
from typing import Any

# =============================================================================
# PART 1: TIME & SPACE COMPLEXITY (BIG O)
# =============================================================================
"""
To write optimized algorithms, we must measure how their resource usage scales
as the input size (N) grows. We use Big O Notation to represent this.

--- Common Time Complexities (Fastest to Slowest) ---
1. O(1) - Constant Time: The operation takes the same time regardless of input size.
   Example: Accessing an element in an array by index.
2. O(log N) - Logarithmic Time: The search space is halved in each step.
   Example: Binary Search.
3. O(N) - Linear Time: We must visit every element once.
   Example: Finding the maximum value in an unsorted list.
4. O(N log N) - Linearithmic Time: Usually sorting algorithms.
   Example: Merge Sort, Quick Sort.
5. O(N^2) - Quadratic Time: Nested loops over the input.
   Example: Bubble Sort, checking all pairs.
6. O(2^N) - Exponential Time: Growth doubles with each addition.
   Example: Naive recursive Fibonacci.
"""


# =============================================================================
# PART 2: STATIC VS. DYNAMIC ARRAYS
# =============================================================================
"""
- Static Array: A contiguous block of memory with a FIXED size. If you allocate
  an array of size 5, it cannot grow. Accessing index `i` is O(1) because the
  computer calculates the memory address directly: Address = Start + (i * ElementSize).
- Dynamic Array: A wrapper around a static array that automatically resizes itself
  when it fills up. Python's built-in `list` is a dynamic array.
  
When a dynamic array is full and you try to append, it:
  1. Allocates a new, larger static array (usually double the size).
  2. Copies all existing elements over to the new array.
  3. Deletes the old array.
  4. Appends the new element.
  
Time Complexity of Append:
  - Average/Amortized Case: O(1) (most appends are fast).
  - Worst Case: O(N) (when resizing occurs).
"""


# =============================================================================
# PART 3: CUSTOM DYNAMIC ARRAY IMPLEMENTATION
# =============================================================================

class DynamicArray:
    """
    A custom implementation of a Dynamic Array to demonstrate how Python's
    lists handle resizing, insertion, and deletion.
    """
    def __init__(self, initial_capacity: int = 4):
        self.capacity = initial_capacity
        self.size = 0
        # Initialize our internal "memory" with None placeholders
        self.array = [None] * self.capacity

    def get(self, index: int) -> Any:
        """O(1) Access."""
        if not 0 <= index < self.size:
            raise IndexError("Array index out of bounds.")
        return self.array[index]

    def append(self, value: Any) -> None:
        """Amortized O(1) Append. Resizes to double capacity when full."""
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        
        self.array[self.size] = value
        self.size += 1

    def insert(self, index: int, value: Any) -> None:
        """O(N) Insertion. Shifts all elements after the index to the right."""
        if not 0 <= index <= self.size:
            raise IndexError("Insertion index out of bounds.")
        
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        # Shift elements to the right starting from the end
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = value
        self.size += 1

    def delete_at(self, index: int) -> Any:
        """O(N) Deletion. Shifts all elements after the index to the left."""
        if not 0 <= index < self.size:
            raise IndexError("Deletion index out of bounds.")

        deleted_val = self.array[index]

        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None  # Clear the last element
        self.size -= 1

        # Optional: shrink capacity if size drops to 25% of capacity
        if 0 < self.size <= self.capacity // 4:
            self._resize(self.capacity // 2)

        return deleted_val

    def _resize(self, new_capacity: int) -> None:
        """O(N) Memory reallocation and data copy."""
        print(f"[*] Resizing capacity from {self.capacity} to {new_capacity}...")
        new_arr = [None] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.array[i]
        self.array = new_arr
        self.capacity = new_capacity

    def __str__(self) -> str:
        elements = [str(self.array[i]) for i in range(self.size)]
        return f"[{', '.join(elements)}] (Size: {self.size}, Capacity: {self.capacity})"


# =============================================================================
# PART 4: RUNNING DEMO
# =============================================================================

def run_demo():
    print("--- Dynamic Array Demo ---")
    arr = DynamicArray(initial_capacity=2)
    print("Initial:", arr)

    arr.append(10)
    arr.append(20)
    print("Filled to capacity:", arr)

    arr.append(30)  # Should trigger resize
    print("After appending 30:", arr)

    arr.insert(1, 15)  # Insert 15 at index 1
    print("After inserting 15 at index 1:", arr)

    arr.delete_at(2)  # Delete index 2 (which is 20)
    print("After deleting index 2:", arr)


# =============================================================================
# ACTIVITY SECTION
# =============================================================================
# Exercise 1: Implement a `find(value)` method.
#   - It should return the first index of the value, or -1 if not found.
#   - What is its time complexity?
#
# Exercise 2: Implement a `reverse()` method.
#   - Reverse the dynamic array in-place.
#   - Do it in O(N) time complexity and O(1) extra space complexity.

# =============================================================================
# MINI CHALLENGE: Dynamic String Builder
# =============================================================================
# Repeatedly adding strings using `str1 + str2` in Python is O(N^2) overall
# because strings are immutable and every concatenation copies the characters.
# Create a class `StringBuilder` that uses a DynamicArray to store string chunks,
# and joins them all at the end using `"".join(array)`. Test its speed against
# standard `+` loop for 100,000 appends.
# =============================================================================

if __name__ == "__main__":
    run_demo()
