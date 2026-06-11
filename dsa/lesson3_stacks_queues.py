# dsa/lesson3_stacks_queues.py

"""
=============================================================================
DSA Lesson 3: Stacks & Queues
=============================================================================
Topic: Stack (LIFO), Queue (FIFO), Queue Optimization, and Expression Parsing
"""

from collections import deque
from typing import Any, List

# =============================================================================
# PART 1: THE STACK (LIFO - Last In, First Out)
# =============================================================================
"""
A Stack is a collection of elements that follows the LIFO principle: the last
element added is the first one to be removed.
Think of a stack of dinner plates: you add new plates to the top, and you take
plates off from the top.

--- Key Stack Operations ---
- push(item): Add an item to the top. (O(1))
- pop(): Remove and return the top item. (O(1))
- peek(): Look at the top item without removing it. (O(1))
- is_empty(): Check if the stack is empty. (O(1))

--- Use Cases ---
- Function call stack in programming languages.
- Undo/Redo history in text editors.
- Backtracking algorithms.
"""

class Stack:
    """A Stack implementation using Python's list."""
    def __init__(self):
        self._items: List[Any] = []

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Pop from empty stack.")
        return self._items.pop()

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from empty stack.")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


# =============================================================================
# PART 2: THE QUEUE (FIFO - First In, First Out)
# =============================================================================
"""
A Queue is a collection of elements that follows the FIFO principle: the first
element added is the first one to be removed.
Think of a line of people waiting to buy tickets: the person at the front gets
served first.

--- Key Queue Operations ---
- enqueue(item): Add an item to the back of the queue. (O(1))
- dequeue(): Remove and return the item at the front. (O(1))
- peek(): Look at the front item. (O(1))

--- Queue Performance Trick ---
In Python, using `list.pop(0)` to dequeue elements takes O(N) linear time because
shifting elements in memory is required. To achieve true O(1) dequeue operations,
we use `collections.deque` (double-ended queue).
"""

class Queue:
    """An optimized FIFO Queue implementation using collections.deque."""
    def __init__(self):
        self._items = deque()

    def enqueue(self, item: Any) -> None:
        self._items.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Dequeue from empty queue.")
        return self._items.popleft()

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from empty queue.")
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


# =============================================================================
# PART 3: APPLICATION - PARENTHESES MATCHING
# =============================================================================
"""
Stacks are perfect for syntax validation. If we find an opening bracket, we push
it to the stack. If we find a closing bracket, we check if it matches the bracket
at the top of the stack.
"""

def is_balanced(expression: str) -> bool:
    """Verifies if parenthesis pairs (), [], {} match correctly."""
    stack = Stack()
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in mapping.values():  # Opening bracket
            stack.push(char)
        elif char in mapping.keys():  # Closing bracket
            if stack.is_empty() or stack.pop() != mapping[char]:
                return False
    
    return stack.is_empty()


# =============================================================================
# PART 4: RUNNING DEMO
# =============================================================================

def run_demo():
    print("--- Stack Demo ---")
    s = Stack()
    s.push("Step 1")
    s.push("Step 2")
    print("Top item:", s.peek())
    print("Popped:", s.pop())
    print("Popped:", s.pop())

    print("\n--- Queue Demo ---")
    q = Queue()
    q.enqueue("Client A")
    q.enqueue("Client B")
    print("Next client:", q.peek())
    print("Served:", q.dequeue())
    print("Served:", q.dequeue())

    print("\n--- Syntax Checker Demo ---")
    expr1 = "{[()()]}"
    expr2 = "{[(])}"
    print(f"Is '{expr1}' balanced?", is_balanced(expr1))  # True
    print(f"Is '{expr2}' balanced?", is_balanced(expr2))  # False


# =============================================================================
# ACTIVITY SECTION
# =============================================================================
# Exercise 1: Implement a Queue using two Stacks
#   - Create a class `QueueUsingStacks`. It must have `enqueue` and `dequeue`
#     methods, but internally only use two instances of the `Stack` class.
#
# Exercise 2: Implement a Min-Stack
#   - Create a stack that supports `push`, `pop`, `peek`, and retrieving the
#     minimum element in O(1) time. (Hint: maintain an auxiliary stack of minimums).

# =============================================================================
# MINI CHALLENGE: Reverse Polish Notation (RPN) Calculator
# =============================================================================
# In RPN, operators follow operands: e.g., "3 4 + 2 *" translates to (3 + 4) * 2.
# Write a function `evaluate_rpn(tokens: List[str]) -> int` that evaluates
# RPN mathematical statements using a Stack.
# Supported operators: '+', '-', '*', '/'.
# Test with: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# =============================================================================

if __name__ == "__main__":
    run_demo()
