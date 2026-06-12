from collections import deque

def bfs(grid, start, K):
    """
    Performs a Breadth-First Search (BFS) starting from the cat's position.
    Finds all mice ('M') reachable within K moves, avoiding walls ('#').
    """
    # Get grid boundaries (dimensions)
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize the queue for BFS.
    # Each item in the queue is a tuple: ((row, col), moves_taken)
    queue = deque()
    
    # Start the search at the cat's initial position with 0 moves taken
    queue.append((start, 0))
    
    # Create a set to keep track of visited coordinates so we don't visit them twice
    visited = set()
    visited.add(start)
    
    # A list to store the results: (mouse_position, moves_taken)
    result = []

    # Loop as long as there are positions in the queue to explore
    while queue:
        # Take the oldest item from the front of the queue (First In, First Out)
        (r, c), moves = queue.popleft()
        
        # BFS processes cells in order of increasing moves.
        # If the current coordinate took more than K moves to reach,
        # we stop searching because any subsequent coordinates will also exceed K.
        if moves > K:
            break
            
        # If we find a mouse ('M') at the current coordinate, record it in our results
        if grid[r][c] == "M":
            result.append(((r, c), moves))
            
        # Explore the 4 adjacent directions: Up, Down, Left, Right
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            # Calculate the neighbor's coordinate
            nr = r + dr
            nc = c + dc
            
            # 1. Check if the neighbor is within the grid boundaries
            if 0 <= nr < rows and 0 <= nc < cols:
                # 2. Check if the neighbor is not a wall ('#') and has not been visited yet
                if grid[nr][nc] != "#" and (nr, nc) not in visited:
                    # Mark the neighbor as visited so we don't queue it again
                    visited.add((nr, nc))
                    # Add the neighbor to the back of the queue with moves incremented by 1
                    queue.append(((nr, nc), moves + 1))
                    
    # Return all the mice caught and the number of moves it took to reach them
    return result


def solve(grid, K):
    """
    Finds every cat ('C') in the grid and prints which mice ('M') they can catch within K moves.
    """
    # Loop through every cell in the 2D grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # If we find a cat ('C'), perform BFS to find reachable mice
            if grid[r][c] == "C":
                result = bfs(grid, (r, c), K)
                print(f"Cat at {(r, c)}:")
                
                if result:
                    # Print each mouse caught and the moves taken
                    for mouse_pos, moves_taken in result:
                        print(f"  -> Catches Mouse at {mouse_pos} in {moves_taken} moves")
                else:
                    print(f"  -> Cannot catch any mouse within {K} moves")
                print()  # Print a blank line for readability


# Define the 2D grid
# '.' represents empty spaces, '#' represents walls, 'C' represents cats, 'M' represents mice
grid = [
    [".", ".", "C", ".", ".", "#"],
    ["#", ".", ".", ".", "M", "."],
    [".", ".", "#", ".", ".", "."],
    [".", "M", ".", ".", "C", "."],
    [".", ".", ".", "#", ".", "."],
]

# Set the maximum moves limit
K = 4

# Run the simulation
solve(grid, K)