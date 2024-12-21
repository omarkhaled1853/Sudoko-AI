from collections import deque

def create_variables():
    variables = []
    for i in range(9):
        for j in range(9):
            variables.append((i, j))

    return variables

def get_row_neighbors(var):
    neighbors = []
    for i in range(9):
        if i != var[1]:
            neighbors.append((var[0], i))

    return neighbors


def get_col_neighbors(var):
    neighbors = []
    for i in range(9):
        if i != var[0]:
            neighbors.append((i, var[1]))

    return neighbors


def get_box_neighbors(var):
    row = var[0] // 3 * 3
    col = var[1] // 3 * 3

    neighbors = []
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if (i, j) != var:
                neighbors.append((i, j))

    return  neighbors

def get_all_neighbors(x):
    row_neighbors = get_row_neighbors(x)
    col_neighbors = get_col_neighbors(x)
    box_neighbors = get_box_neighbors(x)

    return row_neighbors + col_neighbors + box_neighbors

def create_neighbors(variables):
    neighbors = {}
    for variable in variables:
        neighbors[variable] = get_all_neighbors(variable)

    return neighbors




board = [
    ['8','0','9','5','0','1','7','3','6'],
    ['2','0','7','0','6','3','0','0','0'],
    ['1','6','0','0','0','0','0','0','0'],
    ['0','0','0','0','9','0','4','0','7'],
    ['0','9','0','3','0','7','0','2','0'],
    ['7','0','6','0','8','0','0','0','0'],
    ['0','0','0','0','0','0','0','6','3'],
    ['0','0','0','9','3','0','5','0','2'],
    ['5','3','2','6','0','4','8','0','9']
]
def delete_constraint_values(values: [], neighbors:[]):
    for neighbor in neighbors:
        if board[neighbor[0]][neighbor[1]] != '0':
            if board[neighbor[0]][neighbor[1]] in values:
                values.remove(board[neighbor[0]][neighbor[1]])


def get_valid_values(variable):
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    row_neighbors = get_row_neighbors(variable)
    delete_constraint_values(values, row_neighbors)

    col_neighbors = get_col_neighbors(variable)
    delete_constraint_values(values, col_neighbors)

    box_neighbors = get_box_neighbors(variable)
    delete_constraint_values(values, box_neighbors)

    return values

def create_domain(board:[[]]):
    domain = {}
    allValues = ['1','2','3','4','5','6','7','8','9']

    for i in range(9):
        for j in range(9):
            if board[i][j] == '0':
                domain[(i,j)] = get_valid_values((i, j))
            else:
                domain[(i, j)] = board[i][j]

    return domain

def consistent(val, xj):
    for jVal in domain[xj]:
        if jVal != val:
            return True

    return False

# There is always unselected variable when we call this method
def select_unassigned_variable(variables):
    variable = None

    for var in variables:
        if board[var[0]][var[1]] == '0':
            if variable is None or len(domain[var]) < len(domain[variable]):
                variable = var

    return variable



def number_of_role_out(variable, value):
    var_neighbors = get_all_neighbors(variable)

    role_out = 0
    for neighbor in var_neighbors:
        if value in domain[neighbor]:
            role_out += 1

    return role_out


def order_domain_values(variable):
    valid_values = get_valid_values(variable)

    order_domain = sorted(valid_values, key=lambda  value: number_of_role_out(variable, value))

    return order_domain


def ac_3():
    queue = deque()

    for var, neighbors_list in neighbors.items():
        for neighbor in neighbors_list:
            queue.append((var, neighbor))



    while queue:
        top = queue.popleft()

        if revise(top[0], top[1]):
            if len(domain[top[0]]) == 0:
                return False

            all_neighbors = get_all_neighbors(top[0])
            for neighbor in all_neighbors:
                if neighbor == top[1]:
                    continue
                queue.append((neighbor, top[0]))

    return True



def revise(xi, xj):
    revised = False
    values_to_remove = []

    for val in domain[xi]:
        if not consistent(val, xj):
            values_to_remove.append(val)
            revised = True

    for val in values_to_remove:
        domain[xi].remove(val)

    return revised


variables = create_variables()
neighbors = create_neighbors(variables)
domain = create_domain(board)

ac_3()

for t in domain.items():
    print(t)

# print(number_of_role_out((1,1), '4'))
# print(number_of_role_out((1,1), '5'))
# print(order_domain_values((1,1)))
#

# for i in range(9):
#     for j in range(9):
#         print(board[i][j] + " ", end="")
#     print()

# for neighbor in neighbors[0,1]:
#     revise((0,1),neighbor)
#
#
# domain[(0,1)].remove('3')
# print(domain[(8,7)])
#
# for neighbor in neighbors[(0,1)]:
#     print(revise((0,1), neighbor))
#     print("nn ", neighbor)
#     for value in domain[(0, 1)]:
#         print(value)

# domain[(0,1)] = '4'
#
# print(revise((0,1), (1,1)))

# for value in domain.values():
#     print(value)
# # print(domain)
# ac_3()
#
# print()
# for value in domain.values():
#     print(value)

# domain[0,1].remove('3')
# for val in domain[0,1]:
#     print(val)


# print(len(neighbors[(0,0)]))

# r_n = row_neighbors((0,0))
# c_n = col_neighbors((0,0))
#
# x = r_n + c_n
# print(x)
# print(box_neigbors((0,4)))

# def create_neighbors(variables):
#     neighbors = {}
#
#     for var in variables:






