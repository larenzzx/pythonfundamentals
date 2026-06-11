# catchTheMouse.py

# ==============================================================================
# 1. UNDERSTANDING IMPORTS & CONTAINERS
# ==============================================================================
# - 'collections' is a standard library module built directly into Python. You
#   don't need to install anything; it comes ready out-of-the-box.
# - 'deque' (pronounced "deck") stands for "double-ended queue".
#   * In a standard Python list, removing the first item (e.g., list.pop(0)) is
#     slow (O(N) time) because Python has to shift all remaining elements in memory.
#   * A 'deque' allows us to add or remove elements from the front and back in
#     lightning-fast, constant time (O(1)). Since Breadth-First Search (BFS)
#     relies on popping elements from the front of a queue, 'deque' is essential.
from collections import deque

# ==============================================================================
# 2. THE BFS SEARCH FUNCTION
# ==============================================================================
def bfs(grid, start, K):
    """
    Executes a Breadth-First Search (BFS) to find all mice reachable from a start.
    
    Parameters:
      grid: A 2D list of characters representing the map ('.' paths, '#' walls, etc.).
      start: A tuple (row, col) representing the coordinates of the starting Cat.
      K: An integer representing the maximum moves allowed.
    """
    # Get the grid boundaries:
    # - rows: how many rows are in the grid (vertical height).
    # - cols: how many columns are in the grid (horizontal width of the first row).
    rows, cols = len(grid), len(grid[0])
    
    # Initialize the Queue:
    # We load our starting position into the queue.
    # The queue stores tuples: ( (row, col), current_moves )
    # We start at the Cat's position with 0 moves taken.
    queue = deque([(start, 0)])
    
    # Initialize the Visited Set:
    # A set is a collection that stores unique items and allows O(1) instant lookups.
    # We store coordinates we have already seen to prevent visiting them again.
    # This prevents the algorithm from looping infinitely (e.g., moving back and forth).
    visited = set([start])
    
    # A list to store the results. It will contain tuples of: ((mouse_row, mouse_col), moves)
    reachable_mice = []

    # Continue searching as long as there are cells in our queue left to explore
    while queue:
        # popleft() grabs the oldest item from the front of the queue.
        # This is LIFO/Queue behavior. It returns:
        # - (r, c): current row and column coordinates.
        # - moves: how many moves it took to get here from the starting Cat.
        (r, c), moves = queue.popleft()
        
        # Early Termination:
        # Because BFS explores layer-by-layer (distance 0, then 1, then 2, etc.),
        # the moment we pop an item that took MORE than K moves, we know that
        # all remaining items in the queue will also take more than K moves.
        # So, we can safely stop the search immediately.
        if moves > K:
            break
            
        # Target Match:
        # If the cell we just popped contains a Mouse ('M'), record it!
        # We save its position (r, c) and how many moves it took to reach it.
        if grid[r][c] == 'M':
            reachable_mice.append(((r, c), moves))

        # Explore adjacent neighbors:
        # A character can move in 4 directions:
        # - (-1,  0): Up (row decreases, column stays same)
        # - ( 1,  0): Down (row increases, column stays same)
        # - ( 0, -1): Left (row stays same, column decreases)
        # - ( 0,  1): Right (row stays same, column increases)
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            # Calculate the neighbor's coordinates
            nr, nc = r + dr, c + dc
            
            # Boundary check: Ensure the neighbor is actually inside our grid map.
            # (row must be between 0 and rows-1; column must be between 0 and cols-1).
            if 0 <= nr < rows and 0 <= nc < cols:
                # Traversability & Visited check:
                # 1. The neighbor must not be a Wall ('#').
                # 2. The neighbor must not have been visited or queued already.
                if grid[nr][nc] != '#' and (nr, nc) not in visited:
                    # Mark as visited immediately so we don't queue it multiple times
                    visited.add((nr, nc))
                    # Add to the back of the queue, incrementing the move count by 1
                    queue.append(((nr, nc), moves + 1))

    # Return the list of all caught mice with their moves
    return reachable_mice


# ==============================================================================
# 3. GAME SETUP & DRIVER CODE
# ==============================================================================
# The grid map: N = 5 rows, M = 6 columns.
# '.' = Path, '#' = Wall, 'C' = Cat, 'M' = Mouse.
grid = [
    ['.', '.', 'C', '.', '.', '#'],
    ['#', '.', '.', '.', 'M', '.'],
    ['.', '.', '#', '.', '.', '.'],
    ['.', 'M', '.', '.', 'C', '.'],
    ['.', '.', '.', '#', '.', '.'],
]

# Max moves allowed for a Cat
K = 4

# Loop through every cell in the 2D grid to find where the Cats are located
for r in range(len(grid)):
    for c in range(len(grid[0])):
        # If we find a Cat ('C')
        if grid[r][c] == 'C':
            # Run the BFS algorithm starting from this Cat's coordinates (r, c)
            result = bfs(grid, (r, c), K)
            
            # Print the results
            print(f"\nCat at {(r,c)}:")
            if result:
                for mouse_pos, moves_taken in result:
                    print(f"  -> Can catch Mouse at {mouse_pos} in {moves_taken} moves")
            else:
                print(f"  -> Cannot catch any mouse within {K} moves")