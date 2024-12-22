import random
import math

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
