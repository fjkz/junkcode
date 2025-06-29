# Pentomino Solver Algorithm Explanation

This document details the algorithm used in `pentomino.py` to solve the Pentomino puzzle. The program fits 12 unique pentomino pieces onto a rectangular board (e.g., 6x10) without any overlap.

The core of the solver is a **heuristic-guided backtracking search algorithm**.

## 1. Core Concepts & Data Structures

The problem is modeled using several key Python classes:

-   **`Board`**: Represents the rectangular grid. It's essentially a 2D array that stores the state of each cell: either empty (`None`) or occupied by a piece's label (e.g., 'P', 'Q'). It provides methods to check if a cell is empty, if a piece can be placed, and to place a piece.

-   **`Piece`**: Represents one of the 12 pentomino pieces (O, P, Q, R, S, T, U, V, W, X, Y, Z). Each piece is defined by its shape, which is a collection of 5 blocks, or "minos".

-   **`MinoPosition`**: Represents the specific coordinates of a piece on the board. It's a list of (y, x) tuples. This class contains logic to perform transformations on a piece:
    -   **Rotation and Flipping**: The `turn_flip()` method can generate all 8 unique orientations of a piece.
    -   **Translation**: The `move()` method translates the piece to a specific (y, x) anchor point on the board.

## 2. The Search Algorithm

The main logic resides in the `backtrack()` function, which recursively explores the search space of possible piece placements.

### Key Components of the Algorithm:

#### a. Priority Queue for Empty Cells

Instead of trying to fill empty cells in a fixed order (e.g., row by row), the algorithm uses a **priority queue (`cell_queue`)** to select the next empty cell to try. This is a crucial heuristic.

-   **`prioritize()` function**: This function calculates a priority for each empty cell. The default strategy prioritizes cells that have **fewer open neighbors**. The idea is that filling a more constrained or enclosed cell first is more likely to lead to a dead end quickly, which allows the algorithm to "fail fast" and prune the search tree more efficiently.

#### b. Piece Selection Strategy

When trying to fill a selected empty cell, the algorithm must also decide which of the remaining pieces to try first. The script implements three strategies:

1.  **`FitDifficultPieceChoice` (Default)**: This strategy prioritizes trying the piece that has historically been the hardest to fit (i.e., has the lowest `fit_rate`). The `fit_rate` is the ratio of successful placements to total attempts for that piece. The intuition is to place the most awkward pieces first, as they are the most likely to constrain the board and cause failures.
2.  **`FitEasyPieceChoice`**: The opposite of the above; it tries the "easiest" pieces first.
3.  **`RandomPieceChoice`**: Tries the remaining pieces in a random order.

#### c. Backtracking Workflow

The `backtrack` function works as follows:

1.  **Select Cell**: Extract the highest-priority empty cell `(y, x)` from the priority queue.
2.  **Select Piece**: Choose a piece from the `remaining_pieces` list based on the selected `piece_choice_strategy`.
3.  **Try Placements**: For the chosen piece, generate all of its possible valid positions (`MinoPosition`) that start at the anchor cell `(y, x)` and fit on the board without overlapping existing pieces.
4.  **Recurse**: For the first valid placement found:
    a. Place the piece on a **deep copy** of the board.
    b. Remove the piece from the list of available pieces.
    c. Find all empty cells that are neighbors to the newly placed piece and add them to a **copy** of the priority queue.
    d. Make a recursive call to `backtrack()` with the new board state, reduced piece list, and updated cell queue.
    e. If the recursive call eventually returns a full board, a solution has been found. Propagate this solution up the call stack.
5.  **Backtrack**: If the loop over all possible placements for the selected piece completes without finding a solution (i.e., all subsequent recursive calls resulted in a `NoAnswer` exception), it means this path is a dead end. The function then raises its own `NoAnswer` exception to signal failure to the level above it, effectively "backtracking".

This process continues until either a complete solution is found or the entire search space has been exhausted.

## 3. Statistics and Analysis

The script collects two main types of statistics to analyze the search process:

-   **`FitStatistics`**: Tracks how many times each piece was tried and how many times it was successfully placed. This is used to calculate the `fit_rate` for the piece selection strategy.
-   **`SearchStatistics`**: Tracks the depth of the search. It counts how many times the algorithm backtracked from a certain depth (number of pieces already placed). This helps in understanding the efficiency of the search heuristics.

At the end of a run, the program prints these statistics, providing insight into which pieces were "hardest" and how deeply the algorithm had to search.
