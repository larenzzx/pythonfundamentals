# dsa/lesson5_sorting_searching.py

"""
=============================================================================
DSA Lesson 5: Searching & Sorting Algorithms
=============================================================================
Topic: Binary Search (O(log N)), Bubble Sort, Merge Sort, and Quick Sort
"""

from typing import List

# =============================================================================
# PART 1: SEARCHING ALGORITHMS
# =============================================================================
"""
--- Linear Search (O(N)) ---
Checks every element from beginning to end. Works on unsorted collections.

--- Binary Search (O(log N)) ---
Only works on SORTED collections. It compares the target to the middle element.
If they don't match, it halves the search range recursively (divide-and-conquer).
"""

def binary_search(arr: List[int], target: int) -> int:
    """Iterative Binary Search. Returns index of target, or -1 if not found."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half

    return -1


# =============================================================================
# PART 2: SORTING ALGORITHMS
# =============================================================================

# --- Bubble Sort: O(N^2) ---
# Repeatedly compares adjacent elements and swaps them if they are in the wrong order.
def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    # Clone array to avoid modifying input
    sorted_arr = arr[:]
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        # If no swaps occurred, the array is already sorted!
        if not swapped:
            break
    return sorted_arr


# --- Merge Sort: O(N log N) ---
# A recursive divide-and-conquer algorithm. Splits the array in half,
# sorts the halves, and merges them back together.
def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return _merge(left_half, right_half)

def _merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    i = j = 0

    # Compare elements from left and right arrays and merge them in order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# --- Quick Sort: O(N log N) Average ---
# Picks an element as a 'pivot' and partitions the array: elements smaller than
# the pivot go to its left, larger elements to its right. Recursively sorts halves.
def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    # Using the middle element as the pivot
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# =============================================================================
# PART 3: RUNNING DEMO
# =============================================================================

def run_demo():
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted:", unsorted_list)

    print("\nBubble Sort:", bubble_sort(unsorted_list))
    print("Merge Sort: ", merge_sort(unsorted_list))
    print("Quick Sort: ", quick_sort(unsorted_list))

    sorted_list = [11, 12, 22, 25, 34, 64, 90]
    target = 25
    print(f"\nSearching for {target} in sorted list:")
    index = binary_search(sorted_list, target)
    print(f"Index found: {index} (value: {sorted_list[index]})")


# =============================================================================
# ACTIVITY SECTION
# =============================================================================
# Exercise 1: Search in Rotated Sorted Array
#   - Suppose a sorted array is rotated at some pivot unknown to you
#     (e.g., [4, 5, 6, 7, 0, 1, 2] instead of [0, 1, 2, 4, 5, 6, 7]).
#   - Write a modified Binary Search function to find a target in O(log N) time.
#
# Exercise 2: Kth Largest Element in an Array
#   - Find the Kth largest element in an unsorted array.
#   - Hint: You could sort the array, or use a Heap (which we cover in Lesson 6).

# =============================================================================
# MINI CHALLENGE: In-place Partitioning for Quick Sort
# =============================================================================
# The implementation of Quick Sort above creates new lists (left, middle, right)
# in memory, consuming O(N) extra space.
# Write an in-place version of Quick Sort using Lomuto's Partitioning Scheme.
# Lomuto's scheme uses pointers to swap elements within the original array in-place,
# reducing the space complexity to O(log N) auxiliary space (for the call stack).
# =============================================================================

if __name__ == "__main__":
    run_demo()
