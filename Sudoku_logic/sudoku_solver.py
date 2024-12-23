import copy
from collections import deque

class SudokuSolver:
    def __init__(self, board):
        self.board = board

        self.variables = self._create_variables()
        self.neighbors = self._create_neighbors(self.variables)
        self.domain = self._create_domain(self.board)

        self.all_solutions = []
        self.res = 0


    def _create_variables(self):
        variables = []
        for i in range(9):
            for j in range(9):
                variables.append((i, j))
        return variables

    def _get_row_neighbors(self, var):
        neighbors = []
        for i in range(9):
            if i != var[1]:
                neighbors.append((var[0], i))
        return neighbors

    def _get_col_neighbors(self, var):
        neighbors = []
        for i in range(9):
            if i != var[0]:
                neighbors.append((i, var[1]))
        return neighbors

    def _get_box_neighbors(self, var):
        row = var[0] // 3 * 3
        col = var[1] // 3 * 3
        neighbors = []
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if (i, j) != var:
                    neighbors.append((i, j))
        return neighbors

    def _get_all_neighbors(self, x):
        row_neighbors = self._get_row_neighbors(x)
        col_neighbors = self._get_col_neighbors(x)
        box_neighbors = self._get_box_neighbors(x)
        return row_neighbors + col_neighbors + box_neighbors

    def _create_neighbors(self, variables):
        neighbors = {}
        for variable in variables:
            neighbors[variable] = self._get_all_neighbors(variable)
        return neighbors

    def _delete_constraint_values(self, values: [], neighbors: []):
        for neighbor in neighbors:
            if self.board[neighbor[0]][neighbor[1]] != '0':
                if self.board[neighbor[0]][neighbor[1]] in values:
                    values.remove(self.board[neighbor[0]][neighbor[1]])

    def _get_valid_values(self, variable):
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        row_neighbors = self._get_row_neighbors(variable)
        self._delete_constraint_values(values, row_neighbors)

        col_neighbors = self._get_col_neighbors(variable)
        self._delete_constraint_values(values, col_neighbors)

        box_neighbors = self._get_box_neighbors(variable)
        self._delete_constraint_values(values, box_neighbors)

        return values

    def _create_domain(self, board):
        domain = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == '0':
                    domain[(i, j)] = self._get_valid_values((i, j))
                else:
                    domain[(i, j)] = [board[i][j]]
        return domain

    def _consistent(self, val, xj):
        for jVal in self.domain[xj]:
            if jVal != val:
                return True
        return False

    def _select_unassigned_variable(self):
        variable = None
        for var in self.variables:
            if self.board[var[0]][var[1]] == '0':
                if variable is None or len(self.domain[var]) < len(self.domain[variable]):
                    variable = var
        return variable

    def _number_of_role_out(self, variable, value):
        var_neighbors = self._get_all_neighbors(variable)
        role_out = 0
        for neighbor in var_neighbors:
            if value in self.domain[neighbor]:
                role_out += 1
        return role_out

    def _order_domain_values(self, variable):
        valid_values = self._get_valid_values(variable)
        order_domain = sorted(valid_values, key=lambda value: self._number_of_role_out(variable, value))
        return order_domain

    def _valid_move(self, var, value):
        variable_neighbors = self._get_all_neighbors(var)
        for neighbor in variable_neighbors:
            if self.board[neighbor[0]][neighbor[1]] == value:
                return False
        return True

    def _game_solved(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '0':
                    return False
        return True

    def ac_3(self):
        queue = deque()
        for var, neighbors_list in self.neighbors.items():
            for neighbor in neighbors_list:
                queue.append((var, neighbor))

        while queue:
            top = queue.popleft()
            if self._revise(top[0], top[1]):
                if len(self.domain[top[0]]) == 0:
                    return False
                all_neighbors = self._get_all_neighbors(top[0])
                for neighbor in all_neighbors:
                    if neighbor == top[1]:
                        continue
                    queue.append((neighbor, top[0]))
        return True

    def _revise(self, xi, xj):
        revised = False
        values_to_remove = []
        for val in self.domain[xi]:
            if not self._consistent(val, xj):
                values_to_remove.append(val)
                revised = True
        for val in values_to_remove:
            self.domain[xi].remove(val)
        return revised


    def _backtrack(self):
        if self._game_solved():
            self.all_solutions.append(copy.deepcopy(self.board))
            self.res += 1
            return

        var = self._select_unassigned_variable()
        order_values = self._order_domain_values(var)

        for value in order_values:
            self.board[var[0]][var[1]] = value
            if self.ac_3():
                self._backtrack()

            self.board[var[0]][var[1]] = '0'


    def solve(self):
        self.ac_3()
        self._backtrack()

        if len(self.all_solutions) > 0:
            return self.all_solutions[0]
        return []

    def get_solutions(self):
        return self.all_solutions