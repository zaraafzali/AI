# Killer Sudoku Solver (CSP)

A backtracking solver for Killer Sudoku puzzles, written in Python. It treats the puzzle as a constraint satisfaction problem (CSP): each empty cell must take a digit from 1 to 9 that satisfies the Sudoku rules and the sum constraint of the cage it belongs to.

## Features

- Solves a 9×9 Killer Sudoku from a plain-text input file
- Enforces row, column, and 3×3 nonet uniqueness
- Enforces cage sums and (after the fixes in the checklist) unique digits within each cage
- Prints the solved grid, or `no solution found!` if the puzzle is unsolvable

## Requirements

- Python 3.7 or newer
- No third-party packages

## Project Structure

```
.
├── killerSudokuSolver.py   # Solver class, input parser, and main script
└── input3.txt         # Example puzzle (your input file)
```

## Input File Format

The input file has three parts, in this order:

1. **Board**: 9 lines, each with 9 integers separated by spaces. Use `0` for empty cells.
2. **Cage count**: one line with the number of cages.
3. **Cages**: one line per cage, in the form

   ```
   r c r c ... > sum
   ```

   Each `r c` pair is a cell's row and column, separated by a space. The cells are followed by ` > ` and then the cage's target sum. Example:

   ```
   0 0 0 1 1 0 > 15
   ```

   This is a cage of three cells, (0,0), (0,1), and (1,0), with a sum of 15.

### Example

```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
2
0 0 0 1 1 0 > 15
0 2 0 3 > 10
```

> **Note:** Cell coordinates are 0-based, so valid values are 0 through 8. The example above is a stub; a real puzzle must cover every cell with exactly one cage.

## Usage

Set the path to your input file in the script, then run:

```bash
python killerSudokuSolver.py
```

Example output for a solvable puzzle:

```
[5, 3, 4, 6, 7, 8, 9, 1, 2]
[6, 7, 2, 1, 9, 5, 3, 4, 8]
...
```

## How It Works

1. **Parse** the input file into a 9×9 board and a list of cages.
2. **Find** the first empty cell (value `0`).
3. **Try** digits 1 through 9 in that cell. A digit is kept only if `is_valid` passes:
   - no repeat in the row, column, or nonet
   - the cage's partial sum stays within its target
4. **Recurse** on the next empty cell. If the recursion fails, reset the cell to `0` and try the next digit (backtracking).
5. **Stop** when no empty cells remain, or report that no solution exists.

## Known Limitations

- Only 9×9 boards are supported.
- The file path is hardcoded in the script. Update it before running.
- The solver always fills the first empty cell it finds, which can be slow on hard puzzles.
- Cage input must be well formed. Missing sums or uncovered cells can cause incorrect results.

## License

