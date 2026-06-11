# BFS Concept Guide: 2D Grids, Queues, Sets & Directions

This guide walks you through the core concepts used in Breadth-First Search (BFS) on a 2D grid, based on the exercises in [bfs/practice.py](file:///C:/PythonFundamentals/bfs/practice.py).

---

## Part 1: 2D List (The Grid)

In Python, a 2D grid is represented as a **list of lists**.

```python
grid = [
    ['.', '.', 'C', '.', '.', '#'],
    ['#', '.', '.', '.', 'M', '.'],
    ['.', '.', '#', '.', '.', '.'],
    ['.', 'M', '.', '.', 'C', '.'],
    ['.', '.', '.', '#', '.', '.'],
]
```

### Key Concepts:
1. **Indexing `[row][col]`**: To access any cell, you first specify the row index, then the column index (both 0-indexed).
   * `grid[0][2]` refers to Row `0`, Column `2` → `'C'` (Cat 1)
   * `grid[1][4]` refers to Row `1`, Column `4` → `'M'` (Mouse 1)
2. **Grid Size**:
   * `rows = len(grid)` (Height: number of outer lists. Here it is `5`).
   * `cols = len(grid[0])` (Width: number of items in the first list. Here it is `6`).
3. **Traversal**: Nested loops are used to visit every cell in the grid:
   ```python
   for r in range(rows):
       for c in range(cols):
           print(grid[r][c])
   ```

---

## Part 2: Tuples for Positions

Positions in a 2D grid are typically represented as a coordinate tuple: `(row, col)`.

```python
position = (0, 2)
r, c = position
```

### Key Concepts:
1. **Immutability**: Unlike lists, tuples cannot be changed once created. This makes them safe to use as keys in dictionaries or elements in sets.
2. **Tuple Unpacking**: Writing `r, c = position` unpacks the tuple, assigning `0` to `r` and `2` to `c` in a single clean line.

---

## Part 3: Sets for Visited Tracking

A set is an unordered collection of **unique** elements. 

```python
visited = set()
visited.add((0, 2))
visited.add((1, 4))

print((0, 2) in visited)  # True
print((3, 3) in visited)  # False
```

### Key Concepts:
1. **Visited Set**: In pathfinding algorithms (like BFS), we store visited coordinates in a set. This prevents the algorithm from visiting the same position twice and getting stuck in an infinite loop.
2. **Membership Check (`in`)**:
   * `(0, 2) in visited` asks: *"Is the coordinate `(0, 2)` in the set?"* Since we added it, Python returns `True`.
   * `(3, 3) in visited` asks: *"Is the coordinate `(3, 3)` in the set?"* Since we never added it, Python returns `False`.
3. **Why use a Set instead of a List?**
   * Checking membership (`x in set`) is extremely fast—taking **$O(1)$ constant time**.
   * Checking membership in a list (`x in list`) takes **$O(n)$ linear time** because Python has to scan the list item-by-item.

---

## Part 4: Deque (Double-Ended Queue)

A `deque` is a specialized queue container imported from Python's standard `collections` library.

```python
from collections import deque

queue = deque()
queue.append(((0, 2), 0))  # add to back
item = queue.popleft()     # take from front
```

### Visualizing the Queue (First In, First Out)
Think of a queue like a line of people waiting to buy tickets at a theater. The ticket booth is at the **Front (Left)**. New people join at the **Back (Right)**.

1. **Starting empty**:
   ```text
   Front (Left)                                      Back (Right)
   [ Ticket Booth ]  |                                          |
   ```
2. **Adding to the back (`append`)**:
   Adding `"Alice"`, then `"Bob"`, then `"Charlie"` using `queue.append()`:
   ```text
   Front (Left)                                      Back (Right)
   [ Ticket Booth ]  |  [ Alice ]  [ Bob ]  [ Charlie ]         |
   ```
3. **Removing from the front (`popleft`)**:
   Calling `queue.popleft()` takes the person at the front (Alice) out of the line:
   ```text
   Front (Left)                                      Back (Right)
   [ Ticket Booth ]  |             [ Bob ]  [ Charlie ]         |
   ```
   Now, Bob is at the front of the line.

### Time Complexity: List vs. Deque

| Operation | Standard List (`list.pop(0)`) | Deque (`deque.popleft()`) |
| :--- | :--- | :--- |
| **Speed** | **$O(n)$ (Linear Time) - SLOW** | **$O(1)$ (Constant Time) - FAST** |
| **How it works** | Everyone must stand up and shift one seat to the left. For `1,000,000` items, Python does `999,999` shifts. | Nobody moves! Python just shifts the "Start Here" pointer. Always takes **1 step**. |

---

## Part 5: Unpacking from Queue

In BFS, we queue a tuple representing the state: `((row, col), distance)`.

```python
(r, c), moves = ((0, 2), 0)
```

### Key Concepts:
1. **Nested Unpacking**: This extracts values from multiple layers of tuples at once.
2. **Mapping**:
   * The inner tuple `(0, 2)` is unpacked into variables `r` and `c` (`r = 0`, `c = 2`).
   * The integer `0` is unpacked into `moves` (`moves = 0`).

---

## Part 6: The 4 Directions (Grid Movement)

To explore neighbors in a 2D grid, we define relative offsets for moving **Up, Down, Left, and Right**.

```python
directions = [(-1,0), (1,0), (0,-1), (0,1)]
#              up      down   left    right

r, c = 2, 2  # Starting position
```

### Visualizing the Offsets:
When moving from a cell `(r, c)`:

```text
             (r-1, c) [Up]
                   ▲
                   │
(r, c-1) [Left] ◄──(r, c)──► (r, c+1) [Right]
                   │
                   ▼
             (r+1, c) [Down]
```

### Loop Walkthrough:
We loop through `dr` (change in row) and `dc` (change in col) to compute neighbor coordinates:
```python
for dr, dc in directions:
    nr = r + dr
    nc = c + dc
```

Starting at `(2, 2)`:
* **Up** `(-1, 0)`: `nr = 2 + (-1) = 1`, `nc = 2 + 0 = 2` → **`(1, 2)`**
* **Down** `(1, 0)`: `nr = 2 + 1 = 3`, `nc = 2 + 0 = 2` → **`(3, 2)`**
* **Left** `(0, -1)`: `nr = 2 + 0 = 2`, `nc = 2 + (-1) = 1` → **`(2, 1)`**
* **Right** `(0, 1)`: `nr = 2 + 0 = 2`, `nc = 2 + 1 = 3` → **`(2, 3)`**
