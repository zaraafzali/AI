# Killer Sudoku Solver

A Python solver for Killer Sudoku puzzles. It uses backtracking to fill the empty cells so that every row, column, and 3×3 box has the digits 1–9 once each, and every cage adds up to its target sum with no repeated digits.

## Requirements

- Python 3.7 or newer
- No extra packages needed

## Files

```
killerSudokuSolver/
├── KillerSudokuSolver.py
└── Examples/
    └── Example1.txt
```

The script finds the `Examples` folder relative to its own location, so you can run it from any directory.

## Input File Format

Each puzzle is a text file with three parts, in this order.

**1. The board.** Nine lines, each with nine numbers separated by spaces. Use `0` for an empty cell.

**2. The cage count.** One line with the number of cages.

**3. The cages.** One line per cage. Each cell is written as two digits, row then column, with no space between them. Cells are separated by spaces, then ` > ` and the cage sum.

```
00 01 10 > 15
```

This cage covers the cells at row 0 column 0, row 0 column 1, and row 1 column 0, and its digits must add up to 15.

Coordinates are 0-based, so rows and columns run from 0 to 8.

Keep the spacing exact. The parser splits on ` > ` with a space on each side, and it reads each cell from exactly two characters. A cell written as `0 0` or `0,0` will cause an error.

## Usage

From the project folder:

```
python KillerSudokuSolver.py
```

The script reads `Examples/Example1.txt` and prints the solved board, one row per line. If the puzzle has no solution, it prints `no solution found!`.

To solve a different puzzle, change the file name in the `if __name__ == "__main__":` block at the bottom of the script.

## How It Works

1. The input file is read into a 9×9 board and a list of cages.
2. The solver finds the first empty cell.
3. It tries the digits 1 through 9 in that cell. A digit is kept only if it doesn't repeat in the row, column, or box, and if the cage's total still fits its target sum.
4. It moves on to the next empty cell. If a later cell has no valid digit, the solver undoes the last choice and tries the next digit.
5. When no empty cells remain, the solution is complete.

## Known Limitations

- Only 9×9 puzzles are supported.
- The input file isn't validated. A malformed line will raise an error, and the message may not explain what went wrong.
- Cells are filled in reading order. On hard puzzles this can be slow.

## Possible Improvements

- Pick the empty cell with the fewest possible digits next, which usually speeds up the search a lot.
- Accept the input file path as a command-line argument.
- Check the input file and print a clear message for each malformed line.
 