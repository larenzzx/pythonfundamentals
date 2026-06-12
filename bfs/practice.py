# 1. 2D List (the grid)
grid = [
    ['.', '.', 'C', '.', '.', '#'],
    ['#', '.', '.', '.', 'M', '.'],
    ['.', '.', '#', '.', '.', '.'],
    ['.', 'M', '.', '.', 'C', '.'],
    ['.', '.', '.', '#', '.', '.'],
]

print("Cat 1:", grid[0][2]) # (row 0, col 2)
print("Mouse 1:", grid[1][4]) # (row 1, col 4)

rows = len(grid)
cols = len(grid[0])
print("Total rows:", rows)
print("Total cols:", cols)

for r in range(rows):
    for c in range(cols):
        print(grid[r][c])
        
        
# 2. Tuples - used for positions
position = (0, 2)
r, c = position
print(r, c)

# 3. Set - used for visited tracking
visited = set()
visited.add((0, 2))
visited.add((1, 4))
# This asks: "Is the coordinate  (0, 2)  inside our  visited  set?"
# Since we added it on line 30, it is present. Therefore, it output True.
print((0, 2) in visited)  # true

#  This asks: "Is the coordinate  (3, 3)  inside our  visited  set?"
# Since we never added  (3, 3)  to the set, it is not present. Therefore, it outputs False .
print((3, 3) in visited) # false


# 4. Deque - the queue for BFS
from collections import deque

queue = deque()
queue.append(((0, 2), 0)) # add to back
item = queue.popleft() # take from front
print(item) # ((0, 2), 0)

# 5. Unpacking from queue
(r, c), moves = ((0, 2), 0)
print(r)      # 0
print(c)      # 2
print(moves)  # 0

# 6. The 4 directions
directions = [(-1,0), (1,0), (0,-1), (0,1)]
#              up      down   left    right

r, c = 2, 2   # current position

for dr, dc in directions:
    nr = r + dr
    nc = c + dc
    print(f"Neighbor: ({nr}, {nc})")

# Output:
# Neighbor: (1, 2)  ← up
# Neighbor: (3, 2)  ← down
# Neighbor: (2, 1)  ← left
# Neighbor: (2, 3)  ← right