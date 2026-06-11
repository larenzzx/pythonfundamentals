# dsa/lesson8_backtracking_dp.py

"""
=============================================================================
DSA Lesson 8: Backtracking & Dynamic Programming (DP)
=============================================================================
Topic: Decision Trees, Backtracking (N-Queens), and Memoization (Fibonacci, LCS)
"""

from typing import List, Dict, Tuple

# =============================================================================
# PART 1: BACKTRACKING (N-QUEENS)
# =============================================================================
"""
Backtracking is an algorithmic technique that builds a candidate solution step-by-step
and abandons a candidate ("backtracks") as soon as it determines that the candidate
cannot lead to a valid final solution.
It is essentially a DFS traversal of the decision space, but with pruning.

--- Classic Problem: N-Queens ---
Place N non-attacking queens on an N x N chessboard. A queen can attack horizontally,
vertically, and diagonally.
"""

def solve_n_queens(n: int) -> List[List[str]]:
    """Solves the N-Queens problem and returns all valid board configurations."""
    results: List[List[str]] = []
    board = [["."] * n for _ in range(n)]

    # Tracking sets to check in O(1) time if placing a queen is valid
    cols: Set[int] = set()
    pos_diag: Set[int] = set()  # (row + col) remains constant
    neg_diag: Set[int] = set()  # (row - col) remains constant

    def backtrack(r: int):
        if r == n:  # Base Case: all queens placed successfully
            copy = ["".join(row) for row in board]
            results.append(copy)
            return

        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue  # Under attack, prune this branch

            # Place queen (make decision)
            board[r][c] = "Q"
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)

            # Recurse to place queen in next row
            backtrack(r + 1)

            # Remove queen (backtrack/undo decision)
            board[r][c] = "."
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)

    backtrack(0)
    return results


# =============================================================================
# PART 2: DYNAMIC PROGRAMMING (DP)
# =============================================================================
"""
Dynamic Programming is an optimization technique used to solve problems with:
  1. Overlapping Subproblems: The same subproblems are solved repeatedly.
  2. Optimal Substructure: The optimal solution to the problem can be constructed
     from optimal solutions to its subproblems.

--- DP Approaches ---
- Memoization (Top-Down): Start from the main problem, solve recursively, and
  cache results in a hash map to avoid redundant calls.
- Tabulation (Bottom-Up): Solve base cases first and build up to the main problem
  iteratively using a table (usually a 1D or 2D array).

--- Fibonacci Example ---
- Naive recursion: O(2^N) time due to repeating branches.
- DP Memoization: O(N) time because each Fibonacci number is computed exactly once.
"""

# --- Fibonacci with Memoization ---
def fib_memo(n: int, memo: Optional[Dict[int, int]] = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# --- Longest Common Subsequence (LCS) Tabulation ---
# Finds the length of the longest subsequence present in both strings in O(M*N) time.
def lcs_tabulation(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    # 2D table initialized with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# =============================================================================
# PART 3: RUNNING DEMO
# =============================================================================

def run_demo():
    print("--- Backtracking Demo: 4-Queens ---")
    queens_4 = solve_n_queens(4)
    print(f"Found {len(queens_4)} solutions:")
    for solution in queens_4:
        for row in solution:
            print("  ", " ".join(row))
        print()

    print("--- DP Demo: Fibonacci ---")
    print("Fibonacci of 35 (Memoized):", fib_memo(35))

    print("\n--- DP Demo: Longest Common Subsequence ---")
    str1 = "ABCBDAB"
    str2 = "BDCABA"
    print(f"LCS length of '{str1}' and '{str2}':", lcs_tabulation(str1, str2))  # Should be 4 (e.g. BDAB)


# =============================================================================
# ACTIVITY SECTION
# =============================================================================
# Exercise 1: Coin Change Problem
#   - Given a list of coin denominations and a target amount, find the minimum
#     number of coins needed to make up that amount.
#   - Solve this using bottom-up DP. If it is impossible, return -1.
#
# Exercise 2: Sudoku Solver
#   - Write a backtracking algorithm that solves a 9x9 Sudoku board in-place.
#   - Use a validation function to prune branches that violate Sudoku rules.

# =============================================================================
# MINI CHALLENGE: 0/1 Knapsack Solver
# =============================================================================
# You are a thief with a knapsack of capacity W. You have N items, each with
# a value and a weight. You cannot divide items.
# Write a function `knapsack(values: List[int], weights: List[int], capacity: int) -> int`
# that returns the maximum value you can carry.
# Test with: values = [60, 100, 120], weights = [10, 20, 30], capacity = 50.
# (Expected output: 220)
# =============================================================================

if __name__ == "__main__":
    run_demo()
