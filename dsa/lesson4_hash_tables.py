# dsa/lesson4_hash_tables.py

"""
=============================================================================
DSA Lesson 4: Hash Tables & Hash Maps
=============================================================================
Topic: Hash Functions, Index Mapping, Collision Resolution, and Separate Chaining
"""

from typing import List, Tuple, Any, Optional

# =============================================================================
# PART 1: HASH TABLE CONCEPT
# =============================================================================
"""
A Hash Table (Hash Map) is a data structure that maps keys to values for highly
efficient lookups, insertions, and deletions ($O(1)$ average time complexity).

--- How It Works ---
1. Key: The unique identifier (e.g., username "mark_12").
2. Hash Function: An algorithm that converts the key into a number (hash code).
3. Index Mapping: The hash code is converted to an index within an internal array:
   Index = HashCode % ArrayCapacity
4. Value Storage: The value is stored at that array index.

--- The Problem of Collisions ---
Since our array has a finite size, sometimes two different keys will map to the
EXACT same index (e.g., hash("mark") % 5 and hash("john") % 5 might both equal 3).
This is called a Collision.

How do we solve it?
- Separate Chaining: Each index in the array points to a Linked List of key-value pairs.
  If a collision occurs, we append the pair to the list.
- Open Addressing: We find another empty slot in the array (e.g., linear probing).
"""


# =============================================================================
# PART 2: CUSTOM HASH MAP IMPLEMENTATION (SEPARATE CHAINING)
# =============================================================================

class HashTable:
    """A custom Hash Table resolving collisions using Separate Chaining."""
    def __init__(self, capacity: int = 8):
        self.capacity = capacity
        # Create an array of buckets, each initialized as an empty list (our chain)
        self.buckets: List[List[Tuple[Any, Any]]] = [[] for _ in range(self.capacity)]
        self.size = 0

    def _hash(self, key: Any) -> int:
        """A simple hash function converting a key to an index."""
        # hash() is Python's built-in hash function
        return abs(hash(key)) % self.capacity

    def insert(self, key: Any, value: Any) -> None:
        """O(1) Average insertion. Updates value if key already exists."""
        index = self._hash(key)
        bucket = self.buckets[index]

        # Check if the key already exists in the chain, update if it does
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Otherwise, append the new key-value pair
        bucket.append((key, value))
        self.size += 1

    def get(self, key: Any) -> Any:
        """O(1) Average lookup. Raises KeyError if key is missing."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found.")

    def remove(self, key: Any) -> bool:
        """O(1) Average deletion."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False

    def display(self) -> None:
        """Prints the table buckets to visualize collisions and chains."""
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")


# =============================================================================
# PART 3: RUNNING DEMO
# =============================================================================

def run_demo():
    print("--- Hash Table Demo (Capacity: 5 to force collisions) ---")
    # Capacity set to 5 to demonstrate collision chains
    table = HashTable(capacity=5)

    table.insert("apple", 100)
    table.insert("banana", 200)
    table.insert("cherry", 300)
    # This might collide with one of the above keys
    table.insert("date", 400) 

    table.display()

    print("\nValue for 'banana':", table.get("banana"))

    # Update value
    table.insert("banana", 250)
    print("Updated value for 'banana':", table.get("banana"))

    # Remove item
    table.remove("cherry")
    print("\nAfter removing 'cherry':")
    table.display()


# =============================================================================
# ACTIVITY SECTION
# =============================================================================
# Exercise 1: Two Sum (Classic Interview Question)
#   - Given an array of integers `nums` and an integer `target`, return indices of
#     the two numbers such that they add up to `target`.
#   - Use Python's built-in dictionary to solve this in O(N) time complexity instead
#     of a nested loop O(N^2) search.
#
# Exercise 2: Find the First Non-Repeating Character
#   - Given a string, find the first non-repeating character and return its index.
#   - If it doesn't exist, return -1. Use a hash map to count character frequencies.

# =============================================================================
# MINI CHALLENGE: Table Rehashing & Resizing
# =============================================================================
# As a hash table fills up, collisions increase, and performance degrades to O(N).
# The Load Factor is defined as: Size / Capacity.
# 1. Modify the HashTable class to track the Load Factor.
# 2. When the Load Factor exceeds 0.7 (70%), trigger a resize:
#    - Double the capacity.
#    - Rehash ALL existing keys and distribute them into the new, larger bucket array.
# =============================================================================

if __name__ == "__main__":
    run_demo()
