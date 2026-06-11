# dsa/lesson2_linked_lists.py

"""
=============================================================================
DSA Lesson 2: Linked Lists (Singly & Doubly)
=============================================================================
Topic: Nodes, Pointers, Memory Allocation, and Dynamic Chain Implementation
"""

from typing import Any, Optional

# =============================================================================
# PART 1: LINKED LIST CONCEPT
# =============================================================================
"""
Unlike arrays, which store elements in contiguous (touching) memory blocks,
a Linked List stores elements in scattered memory locations called Nodes.
Each Node contains:
  1. Data (the value).
  2. A Pointer (a reference to the next node in the chain).

--- Memory Comparison ---
- Array: [ 10 | 20 | 30 ] (Contiguous block. Fast access, expensive resizing/shifting).
- Linked List: (Node 10) --next--> (Node 20) --next--> (Node 30) --> None

--- Advantages & Disadvantages ---
- Advantage: Inserting or deleting at the front is O(1) (just change pointer addresses).
  No elements need to be shifted in memory.
- Disadvantage: Reading a random index (e.g., getting index 4) takes O(N) linear time,
  as we must traverse the list node-by-node starting from the head.
"""


# =============================================================================
# PART 2: SINGLY LINKED LIST IMPLEMENTATION
# =============================================================================

class SinglyNode:
    """Represents a single node in a Singly Linked List."""
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional[SinglyNode] = None


class SinglyLinkedList:
    """A collection of nodes linked together linearly in one direction."""
    def __init__(self):
        self.head: Optional[SinglyNode] = None

    def insert_at_head(self, value: Any) -> None:
        """O(1) Insertion at the front."""
        new_node = SinglyNode(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value: Any) -> None:
        """O(N) Insertion at the end. (Can be O(1) if we maintain a tail pointer)."""
        new_node = SinglyNode(value)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_value(self, value: Any) -> bool:
        """O(N) Deletion. Links the previous node directly to the next node."""
        if not self.head:
            return False

        # Case 1: Deleting the head node
        if self.head.value == value:
            self.head = self.head.next
            return True

        # Case 2: Traversing to find the value
        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next:  # If we found the value
            current.next = current.next.next
            return True
        return False

    def search(self, value: Any) -> bool:
        """O(N) Lookup."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def display(self) -> None:
        """Prints the list in a visual format."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements) + " -> None")


# =============================================================================
# PART 3: DOUBLY LINKED LIST
# =============================================================================
"""
A Doubly Linked List adds a `prev` pointer pointing backward to the previous node.
This allows us to traverse backward and perform insertions/deletions at the tail
in O(1) time if we store a reference to the `tail` node.
"""

class DoublyNode:
    """Represents a node that links in both directions."""
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional[DoublyNode] = None
        self.prev: Optional[DoublyNode] = None


class DoublyLinkedList:
    """A list where nodes maintain references to both next and previous nodes."""
    def __init__(self):
        self.head: Optional[DoublyNode] = None
        self.tail: Optional[DoublyNode] = None

    def append(self, value: Any) -> None:
        """O(1) Append using the tail pointer."""
        new_node = DoublyNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node

    def display_forward(self) -> None:
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print("Head <-> " + " <-> ".join(elements) + " <-> Tail")


# =============================================================================
# PART 4: RUNNING DEMO
# =============================================================================

def run_demo():
    print("--- Singly Linked List Demo ---")
    s_list = SinglyLinkedList()
    s_list.insert_at_head(20)
    s_list.insert_at_head(10)
    s_list.append(30)
    s_list.display()  # 10 -> 20 -> 30 -> None

    print("Search 20:", s_list.search(20))
    s_list.delete_value(20)
    s_list.display()  # 10 -> 30 -> None

    print("\n--- Doubly Linked List Demo ---")
    d_list = DoublyLinkedList()
    d_list.append("A")
    d_list.append("B")
    d_list.append("C")
    d_list.display_forward()  # Head <-> A <-> B <-> C <-> Tail


# =============================================================================
# ACTIVITY SECTION
# =============================================================================
# Exercise 1: Finding the Middle Element (Fast & Slow Pointers)
#   - Implement `find_middle(self)` inside SinglyLinkedList.
#   - Use two pointers: a `slow` pointer moving 1 step at a time,
#     and a `fast` pointer moving 2 steps. When `fast` hits the end,
#     `slow` will be exactly in the middle! This is an O(N) time, O(1) space solution.
#
# Exercise 2: Reverse a Singly Linked List
#   - Implement `reverse(self)` to reverse the pointers in-place.
#   - Keep track of `prev`, `current`, and `next` nodes.

# =============================================================================
# MINI CHALLENGE: LRU (Least Recently Used) Cache Shell
# =============================================================================
# A Least Recently Used (LRU) Cache uses a Hash Map combined with a Doubly Linked List.
# The DLL stores cache items in order of usage (most recent at the head, oldest at tail).
# The Hash Map stores cache keys mapped directly to DLL nodes for O(1) access.
# Implement a class `SimpleCache` with `get(key)` and `put(key, value)` methods.
# When the cache reaches its capacity, the oldest node (tail) is removed.
# =============================================================================

if __name__ == "__main__":
    run_demo()
