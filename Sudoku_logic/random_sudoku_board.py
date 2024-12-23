import random
import math
from Sudoku_logic.arc import SudokuSolver

class random_sudoku_board:
    def __init__(self, N, K):
        self.N = N
        self.K = K
        self.SRN = int(math.sqrt(N))

        self.mat = [[0 for _ in range(N)] for _ in range(N)]

    def fill_board(self):
        self.fill_diagnoal()

        self.fill_undiagonal(0, self.SRN)

        self.remove_k_digit_random()


    def fill_diagnoal(self):
        for i in range(0, self.N, self.SRN):
            self.fill_box(i, i)

    def fill_box(self, start_row, start_col):
        for i in range(self.SRN):
            for j in range(self.SRN):
                while True:
                    num = self.random_generator()
                    if self.valid_play_in_box(start_row, start_col, num):
                        self.mat[start_row + i][start_col + j] = num
                        break

    def random_generator(self):
        return math.floor(random.random() * self.N + 1)

    def valid_play_in_box(self, start_row, start_col, num):
        for i in range(self.SRN):
            for j in range(self.SRN):
                if self.mat[start_row + i][start_col + j] == num:
                    return False

        return True

    def valid_play_in_row(self, row, num):
        for col in range(self.N):
            if self.mat[row][col] == num:
                return False

        return True

    def valid_play_in_col(self, col, num):
        for row in range(self.N):
            if self.mat[row][col] == num:
                return False

        return True

    def valid_play(self, row, col, num):
        return (self.valid_play_in_row(row, num) and
                self.valid_play_in_col(col, num) and
                self.valid_play_in_box(row - row % self.SRN, col - col % self.SRN, num))

    def fill_undiagonal(self, i, j):
        if i >= self.N and j >= self.N:
            return True

        if j >= self.N:
            i += 1
            j = 0
            if i >= self.N:
                return True

        if self.mat[i][j] != 0:
            return self.fill_undiagonal(i, j + 1)

        for num in range(1, self.N + 1):
            if self.valid_play(i, j, num):
                self.mat[i][j] = num
                if self.fill_undiagonal(i, j + 1):
                    return True

                self.mat[i][j] = 0

        return False

    def remove_k_digit_random(self):

        count = self.K
        while count != 0:
            i = self.random_generator() - 1
            j = self.random_generator() - 1

            if self.mat[i][j] != 0:
                self.mat[i][j] = 0
                count -= 1


    def get_board(self):
        """ Return the generated Sudoku board. """
        return self.mat

    def find_conflicting_cells(self, solutions):
        conflicting_cells = []
        for i in range(self.N):
            for j in range(self.N):
                values = [solution[i][j] for solution in solutions]
                if len(set(values)) > 1:  # Multiple values in different solutions
                    conflicting_cells.append((i, j))
                    return conflicting_cells
        return conflicting_cells

    def get_board_with_unique_solution(self):
        self.fill_diagnoal()

        self.fill_undiagonal(0, self.SRN)

        self.remove_k_digit_random()

        board = [[str(i) for i in row] for row in self.mat]

        sudoku_solver = SudokuSolver(board)
        sudoku_solver.solve()

        solutions = sudoku_solver.get_solutions()

        while len(solutions) > 1:
            # Find conflicting positions across all solutions
            conflicting_cells = self.find_conflicting_cells(solutions)

            if len(conflicting_cells) == 0:
                break

            # Fill the conflicting cells with any valid value (choose one from the conflicting solutions)
            for (i, j) in conflicting_cells:
                possible_values = [solution[i][j] for solution in solutions]
                chosen_value = random.choice(possible_values)
                board[i][j] = chosen_value

            # Clear solutions and solve again
            sudoku_solve = SudokuSolver(board)  # Create a new solver with updated board
            sudoku_solve.solve()
            solutions = sudoku_solve.get_solutions()

        return board

