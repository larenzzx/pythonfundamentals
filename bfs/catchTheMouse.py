from collections import deque

def bfs(grid, start, K):
    rows = len(grid)
    cols = len(grid[0])
    queue = deque()
    queue.append((start, 0))
    visited = set()
    visited.add(start)
    result = []

    while queue:
        (r, c), moves = queue.popleft()
        if moves > K:
            break
        if grid[r][c] == "M":
            result.append(((r, c), moves))
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != "#" and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), moves + 1))
    return result


def solve(grid, K):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "C":
                result = bfs(grid, (r, c), K)
                print(f"Cat at {(r, c)}:")
                if result:
                    for mouse_pos, moves_taken in result:
                        print(f"  -> Catches Mouse at {mouse_pos} in {moves_taken} moves")
                else:
                    print(f"  -> Cannot catch any mouse within {K} moves")
                print()


grid = [
    [".", ".", "C", ".", ".", "#"],
    ["#", ".", ".", ".", "M", "."],
    [".", ".", "#", ".", ".", "."],
    [".", "M", ".", ".", "C", "."],
    [".", ".", ".", "#", ".", "."],
]

K = 4
solve(grid, K)