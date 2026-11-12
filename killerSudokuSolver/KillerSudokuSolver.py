import os

class KillerSudokuCSP:
    def __init__(self, sudoku_board, cages):
        self.board = sudoku_board
        self.cages = cages

    # Check if 'num' can be placed in the specified cell
    def is_valid(self, row, col, num):
        return (
            self.is_valid_row(row, num) and
            self.is_valid_col(col, num) and
            self.is_valid_nonet(row, col, num) and
            self.is_valid_cage(row, col, num)
        )

    # Check if 'num' exists in row
    def is_valid_row(self, row, num):
        return num not in self.board[row]

    # Check if 'num' exists in column
    def is_valid_col(self, col, num):
        for r in range(9):
            if self.board[r][col] == num:
                return False
        return True

    # Check if 'num' exists in the 3x3 nonet
    def is_valid_nonet(self, row, col, num):
        start_row = 3 * (row // 3)
        start_col = 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True

    # Check if 'num' can be placed in its cage
    def is_valid_cage(self, row, col, num):
        for cage in self.cages:
            if (row, col) in cage['cells']:
                total = num
                empty_count = 0
                for (i, j) in cage['cells']:
                    if (i, j) == (row, col):
                        continue
                    if self.board[i][j] == 0:
                        empty_count += 1
                    else:
                        if self.board[i][j] == num:
                            return False
                        total += self.board[i][j]

                if total > cage['sum']:
                    return False
                if empty_count == 0:
                    return total == cage['sum']
                return True
        return False

    # Finds the first empty cell (value 0) on the board
    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None, None

    # Solves the puzzle using backtracking
    def solve(self):
        empty_row, empty_col = self.find_empty_cell()

        if empty_row is None:
            return True

        for num in range(1, 10):
            if self.is_valid(empty_row, empty_col, num):
                self.board[empty_row][empty_col] = num

                if self.solve():
                    return True

                self.board[empty_row][empty_col] = 0

        return False

    def get_solution(self):
        if self.solve():
            for row in self.board:
                print(row)
            return self.board
        print("no solution found!")
        return None


def read_input(filename):
    with open(filename, 'r') as file:
        content = file.read().splitlines()

    sudoku_size = 9
    sudoku_board = [list(map(int, row.split())) for row in content[:sudoku_size]]

    num_cages = int(content[sudoku_size])
    cages = []

    for i in range(sudoku_size + 1, sudoku_size + 1 + num_cages):
        cage_info = content[i].split(' > ')
        cage_cells = [(int(cell[0]), int(cell[1])) for cell in cage_info[0].split()]
        cage_sum = int(cage_info[1]) if len(cage_info) > 1 else 0
        cages.append({'cells': cage_cells, 'sum': cage_sum})

    return sudoku_board, cages


if __name__ == "__main__":
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'Examples', 'Example1.txt')
    sudoku_board, cages = read_input(file_path)

    killer_sudoku = KillerSudokuCSP(sudoku_board, cages)
    killer_sudoku.get_solution()