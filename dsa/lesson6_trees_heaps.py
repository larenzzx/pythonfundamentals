# dsa/lesson6_trees_heaps.py

"""
=============================================================================
DSA Lesson 6: Trees & Heaps
=============================================================================
Topic: Binary Search Trees (BST), Traversals, and Heaps (Priority Queues)
"""

import heapq
from typing import Any, List, Optional

# =============================================================================
# PART 1: BINARY SEARCH TREES (BST)
# =============================================================================
"""
A Tree is a hierarchical structure representing relationships. A Binary Tree is
a tree where each node has at most two children: a Left child and a Right child.

A Binary Search Tree (BST) is a binary tree that maintains a sorted order:
  - The left subtree of a node contains only values LESS than the node's value.
  - The right subtree of a node contains only values GREATER than the node's value.

This rule makes searching extremely fast: $O(\log N)$ on average because we halve
our search area with every node we visit.
"""

class BSTNode:
    """Represents a node in a Binary Search Tree."""
    def __init__(self, value: int):
        self.value = value
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None


class BinarySearchTree:
    """A collection of nodes forming a Binary Search Tree."""
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, value: int) -> None:
        """Inserts a new value into the BST at its correct position."""
        if not self.root:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: BSTNode, value: int) -> None:
        if value < node.value:
            if not node.left:
                node.left = BSTNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if not node.right:
                node.right = BSTNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value: int) -> bool:
        """O(log N) Average search time."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Optional[BSTNode], value: int) -> bool:
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)


# =============================================================================
# PART 2: TREE TRAVERSALS (DFS)
# =============================================================================
"""
Traversing means visiting all nodes in the tree. The three common recursive traversals
are Depth-First:
  1. In-Order (Left, Node, Right): Visits nodes in ascending sorted order!
  2. Pre-Order (Node, Left, Right): Useful for cloning or copying a tree structure.
  3. Post-Order (Left, Right, Node): Useful for deleting trees or bottom-up tasks.
"""

def traverse_in_order(node: Optional[BSTNode]) -> List[int]:
    """Left -> Node -> Right."""
    if not node:
        return []
    return traverse_in_order(node.left) + [node.value] + traverse_in_order(node.right)

def traverse_pre_order(node: Optional[BSTNode]) -> List[int]:
    """Node -> Left -> Right."""
    if not node:
        return []
    return [node.value] + traverse_pre_order(node.left) + traverse_pre_order(node.right)

def traverse_post_order(node: Optional[BSTNode]) -> List[int]:
    """Left -> Right -> Node."""
    if not node:
        return []
    return traverse_post_order(node.left) + traverse_post_order(node.right) + [node.value]


# =============================================================================
# PART 3: HEAPS & PRIORITY QUEUES
# =============================================================================
"""
A Heap is a complete binary tree where each node is smaller than (or larger than)
its children. 
  - Min-Heap: Root holds the smallest value.
  - Max-Heap: Root holds the largest value.
  
Inserting or popping the root takes O(log N) time. Peeking at the root takes O(1).
This makes heaps perfect for implementing Priority Queues (queues that process
items by priority, not arrival order).

Python handles heaps using the built-in `heapq` module on standard list arrays.
"""

def heap_demo():
    items = [57, 12, 45, 8, 32]
    print("\n--- Heap Demo ---")
    print("Raw list:", items)
    
    # Transform list into a min-heap in-place, O(N) time
    heapq.heapify(items)
    print("Heapified (Min-heap):", items)  # items[0] is guaranteed to be the min

    # Push a new element, O(log N)
    heapq.heappush(items, 15)
    print("After pushing 15:", items)

    # Pop smallest element, O(log N)
    smallest = heapq.heappop(items)
    print("Popped smallest:", smallest)
    print("Remaining heap:", items)


# =============================================================================
# PART 4: RUNNING DEMO
# =============================================================================

def run_demo():
    print("--- BST Demo ---")
    bst = BinarySearchTree()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)

    print("Search for 60 (Exists):", bst.search(60))
    print("Search for 99 (Missing):", bst.search(99))

    print("\nTraversals:")
    print("  In-Order:  ", traverse_in_order(bst.root))
    print("  Pre-Order: ", traverse_pre_order(bst.root))
    print("  Post-Order:", traverse_post_order(bst.root))

    # Run heap demo
    heap_demo()


# =============================================================================
# ACTIVITY SECTION
# =============================================================================
# Exercise 1: Calculate Binary Tree Depth
#   - Write a function `max_depth(node: Optional[BSTNode]) -> int` that returns
#     the height/depth of a binary tree.
#   - A tree with only root has depth 1, empty tree has depth 0.
#
# Exercise 2: Validate if a Binary Tree is a Valid BST
#   - Write a function `is_valid_bst(node: Optional[BSTNode]) -> bool`.
#   - A binary tree is a valid BST if every node's left child is less than the node,
#     and every node's right child is greater than the node.
#   - Hint: Maintain range bounds `(min_val, max_val)` as you traverse recursively.

# =============================================================================
# MINI CHALLENGE: Level-Order Tree Traversal (BFS for Trees)
# =============================================================================
# Depth-First traversals explore deep paths first.
# Level-Order Traversal explores trees row-by-row (level-by-level).
# Write a function `level_order_traversal(root: Optional[BSTNode]) -> List[List[int]]`
# that returns a nested list of nodes grouped by tree levels.
# (Hint: Use a FIFO Queue, similar to the grid BFS algorithm!)
# =============================================================================

if __name__ == "__main__":
    run_demo()
