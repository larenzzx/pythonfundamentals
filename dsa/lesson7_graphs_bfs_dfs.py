# dsa/lesson7_graphs_bfs_dfs.py

"""
=============================================================================
DSA Lesson 7: Graphs - BFS & DFS
=============================================================================
Topic: Graph Representations, DFS Path Finding, and BFS "Catch the Mouse" Solver
"""

from collections import deque
from typing import List, Tuple, Set, Dict, Optional, NamedTuple

# =============================================================================
# PART 1: GRAPH CONCEPTS & REPRESENTATIONS
# =============================================================================
"""
A Graph is a network of nodes (Vertices) connected by lines (Edges).
Examples: Maps (intersections connected by roads), Facebook (users connected by friendships).

We represent graphs in code in two primary ways:
1. Adjacency Matrix: A 2D array where matrix[i][j] is 1 if node i and node j are
   connected, 0 otherwise. Space-heavy ($O(V^2)$), but fast edge checks.
2. Adjacency List: A hash map where each node maps to a list of its neighbors.
   Space-efficient ($O(V + E)$), standard for sparse graphs.
"""

class GraphAdjacencyList:
    """An undirected graph represented using an Adjacency List."""
    def __init__(self):
        self.adj_list: Dict[str, List[str]] = {}

    def add_vertex(self, vertex: str) -> None:
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1: str, v2: str) -> None:
        self.add_vertex(v1)
        self.add_vertex(v2)
        # Undirected graph: add connection both ways
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def display(self) -> None:
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex} -> {neighbors}")


# =============================================================================
# PART 2: DEPTH-FIRST SEARCH (DFS) - EXPLORING PATHS
# =============================================================================
"""
DFS goes as deep as possible down a path before backtracking.
It uses a STACK (or recursion) to remember where to backtrack when it hits a dead end.

--- Use Cases ---
- Detecting cycles in graphs.
- Maze solving where finding ANY path is enough.
- Topological sorting.
"""

def dfs_path(graph: Dict[str, List[str]], start: str, target: str, visited: Optional[Set[str]] = None) -> Optional[List[str]]:
    """Recursive DFS to find ANY path from start to target."""
    if visited is None:
        visited = set()

    visited.add(start)

    # Base Case: target reached
    if start == target:
        return [start]

    # Recursive Step: visit unvisited neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path = dfs_path(graph, neighbor, target, visited)
            if path:  # If a valid path is found in the recursive call
                return [start] + path

    return None


# =============================================================================
# PART 3: BREADTH-FIRST SEARCH (BFS) - "CATCH THE MOUSE"
# =============================================================================
"""
BFS explores level-by-layer using a FIFO QUEUE.
It is guaranteed to find the SHORTEST path in an unweighted graph or grid.

Here is the clean OOP implementation solving the "Catch the Mouse" problem.
"""

class Position(NamedTuple):
    """Represents a coordinate in the 2D grid."""
    row: int
    col: int

    def __str__(self) -> str:
        return f"({self.row}, {self.col})"


class CellSymbol:
    EMPTY = '.'
    WALL = '#'
    CAT = 'C'
    MOUSE = 'M'
    PATH_MARKER = '*'


class Grid:
    """Encapsulates the N x M grid layout and properties."""
    def __init__(self, layout: List[List[str]]):
        self._layout = [row[:] for row in layout]  # Deep copy
        self.rows = len(layout)
        self.cols = len(layout[0]) if self.rows > 0 else 0

    def is_within_bounds(self, pos: Position) -> bool:
        return 0 <= pos.row < self.rows and 0 <= pos.col < self.cols

    def is_traversable(self, pos: Position) -> bool:
        return self.is_within_bounds(pos) and self._layout[pos.row][pos.col] != CellSymbol.WALL

    def get_symbol(self, pos: Position) -> str:
        return self._layout[pos.row][pos.col]

    def find_all(self, symbol: str) -> List[Position]:
        positions = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self._layout[r][c] == symbol:
                    positions.append(Position(r, c))
        return positions

    def clone(self) -> 'Grid':
        return Grid(self._layout)

    def mark_path(self, path: List[Position]) -> None:
        for pos in path[1:-1]:
            self._layout[pos.row][pos.col] = CellSymbol.PATH_MARKER

    def display(self) -> None:
        print("    " + "   ".join(f"{c}" for c in range(self.cols)))
        print("  +" + "---+" * self.cols)
        for r in range(self.rows):
            row_str = f"{r} | "
            for c in range(self.cols):
                symbol = self._layout[r][c]
                if symbol == CellSymbol.CAT:
                    row_str += "C | "
                elif symbol == CellSymbol.MOUSE:
                    row_str += "M | "
                elif symbol == CellSymbol.WALL:
                    row_str += "# | "
                elif symbol == CellSymbol.PATH_MARKER:
                    row_str += "* | "
                else:
                    row_str += ". | "
            print(row_str)
            print("  +" + "---+" * self.cols)


class SearchResult(NamedTuple):
    target: Position
    distance: int
    path: List[Position]


class BFSPathFinder:
    """Handles Breadth-First shortest-path search on a grid."""
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Cardinal directions

    def __init__(self, grid: Grid):
        self.grid = grid

    def find_reachable_targets(self, start: Position, target_symbol: str, max_moves: int) -> List[SearchResult]:
        queue = deque([(start, [start])])
        visited: Set[Position] = {start}
        results: List[SearchResult] = []

        while queue:
            current, path = queue.popleft()
            current_moves = len(path) - 1

            if current_moves > max_moves:
                break

            if current != start and self.grid.get_symbol(current) == target_symbol:
                results.append(SearchResult(current, current_moves, path))

            for dr, dc in self.DIRECTIONS:
                neighbor = Position(current.row + dr, current.col + dc)
                if self.grid.is_traversable(neighbor) and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return results


# =============================================================================
# PART 4: RUNNING DEMO
# =============================================================================

def run_demo():
    print("--- Graph Representation and DFS Demo ---")
    g = GraphAdjacencyList()
    # Build a sample graph of cities
    g.add_edge("Manila", "Cavite")
    g.add_edge("Manila", "Laguna")
    g.add_edge("Cavite", "Batangas")
    g.add_edge("Laguna", "Quezon")
    g.display()

    print("\nDFS Path Manila -> Quezon:")
    path = dfs_path(g.adj_list, "Manila", "Quezon")
    print(" -> ".join(path) if path else "No path found.")

    print("\n--- 'Catch the Mouse' BFS Grid Demo ---")
    raw_layout = [
        ['.', '.', 'C', '.', '.', '#'],
        ['#', '.', '.', '.', 'M', '.'],
        ['.', '.', '#', '.', '.', '.'],
        ['.', 'M', '.', '.', 'C', '.'],
        ['.', '.', '.', '#', '.', '.'],
    ]
    K_limit = 4
    grid = Grid(raw_layout)
    grid.display()

    cats = grid.find_all(CellSymbol.CAT)
    pathfinder = BFSPathFinder(grid)

    for cat_pos in cats:
        print(f"\nAnalyzing Cat at {cat_pos}:")
        reachable = pathfinder.find_reachable_targets(cat_pos, CellSymbol.MOUSE, K_limit)
        if not reachable:
            print(f"  -> Cannot catch any mouse within {K_limit} moves.")
        else:
            for result in reachable:
                print(f"  -> Can catch Mouse at {result.target} in {result.distance} moves.")
                print(f"     Path: {' -> '.join(str(p) for p in result.path)}")
                visual_grid = grid.clone()
                visual_grid.mark_path(result.path)
                visual_grid.display()


# =============================================================================
# ACTIVITY SECTION
# =============================================================================
# Exercise 1: Graph Cycle Detection
#   - Write a function `has_cycle(graph: Dict[str, List[str]]) -> bool` that uses
#     DFS to check if a graph contains a cycle (a loop).
#
# Exercise 2: Grid Diagonal Movement
#   - Modify BFSPathFinder.DIRECTIONS to support 8-directional movement.
#   - Run the "Catch the Mouse" demo. How do the shortest paths change?

# =============================================================================
# MINI CHALLENGE: Grid Maze Solver (DFS vs. BFS Visual Comparison)
# =============================================================================
# Implement a function `solve_maze_dfs(grid, start, end)` and `solve_maze_bfs(grid, start, end)`.
# Run them on a 10x10 maze grid.
# Compare the paths generated. Show that while DFS finds a path quickly, it is
# often winding and suboptimal, whereas BFS guarantees the shortest path.
# =============================================================================

if __name__ == "__main__":
    run_demo()
