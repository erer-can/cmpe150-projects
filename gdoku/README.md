# G-Doku Puzzle Game

This project implements a simplified console-based puzzle game called **G-Doku**, a generalized variation of Sudoku. The program allows users to interactively fill out a puzzle board and checks for board validity based on predefined constraints.

Developed as part of the CMPE150 – Introduction to Computing course at Boğaziçi University.

## Overview

G-Doku differs from traditional Sudoku in that:
- The board is a `k^2 x k^2` grid, divided into `k x k` boxes.
- Numbers can repeat in rows, columns, or boxes.
- The sum of the values in each row, column, and box must be equal to a target integer `n`.
- Empty cells are represented by `0`.

## Functionalities

The main gameplay loop supports the following operations:

### `make_move(mv)`
- Applies a move to the board by placing a value into a specified cell (based on box and relative position).
- Returns the previous value of the cell for undo capability.

### `verify_board()`
- Verifies the current state of the board.
- Returns:
  - `-1` if any row/column/box exceeds the sum `n` (invalid),
  - `0` if valid but incomplete,
  - `1` if valid and completely filled (solved).

### `print_board()`
- Nicely formats and prints the board.
- Displays values with fixed-width cells; empty cells are shown as whitespace.

## Game Interface

The game accepts the following user commands through the terminal:

- `move <box_num> <box_pos> <value>`  
  Attempts to place the given `value` in the corresponding position. Behavior depends on the resulting board status:
  - If solved: game ends.
  - If valid: board updates and prints.
  - If invalid: move is reverted.

- `end`  
  Terminates the game.

## Board Layout

For `k = 3`, the 9 boxes and the 9 positions inside each box are numbered as follows:

**Box Numbers:**

```
[ 0 | 1 | 2 ]
[ 3 | 4 | 5 ]
[ 6 | 7 | 8 ]
```

**Box Cell Positions (example: Box 0):**

```
[ 0 | 1 | 2 ]
[ 3 | 4 | 5 ]
[ 6 | 7 | 8 ]
```

## Constraints

- No external libraries are used.
- Code is written using basic Python constructs only.
- Fully interactive via terminal.

## Course

CMPE150 – Introduction to Computing  
Boğaziçi University, Fall 2023
