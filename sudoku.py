from copy import deepcopy

def solve(array):
    children = get_children(array)
    for child in children:
        solved, child_array = solve(child)
        if solved:
            return solved, child_array
    return is_filled(array), array

def get_children(array):
    i, j = first_zero(array)
    if i is None:
        return None
    row = get_set(array[i])

    col = get_set([a[j] for a in array])
    cell = [array[ii][jj] for ii in range(len(array)) for jj in range(len(array)) if 
            ii // 3 == i // 3 and jj // 3 == j // 3]
    cell = get_set(cell)
    candidates = set(range(1, len(array) + 1))
    possibles = candidates - row - col - cell
    for val in possibles:
        tmp_array = deepcopy(array)
        tmp_array[i][j] = val
        yield tmp_array


def first_zero(array):
    for i, row in enumerate(array):
        for j, val in enumerate(row):
            if not val:
                return i, j
    return None, None


def get_set(vals):
    vals = [x for x in vals if x > 0]
    assert len(vals) == len(set(vals))
    return set(vals)


def is_solution(array):
    candidates = set(range(1, len(array) + 1))
    for row in array:
        if get_set(row) != candidates:
            return False
    for col in [[row[j] for row in array] for j in range(len(array))]:
        if get_set(col) != candidates:
            return False
    for cell in [[array[ii][jj] for ii in range(len(array)) for jj in range(len(array)) if 
            ii // 3 == i // 3 and jj // 3 == j // 3] for i in [0,3,6] for j in [0,3,6]]:
        if get_set(cell) != candidates:
            return False
    return True


def is_filled(array):
    if None in first_zero(array):
        return True
    return False 


if __name__ == "__main__":
    array = [[0 for _ in range(9)] for _ in range(9)]
    array = [[1, 2, 3, 4, 5, 8, 9, 6, 7], [4, 5, 8, 6, 7, 9, 1, 2, 3], [9, 6, 7, 1, 2, 3, 8, 4, 5], [2, 1, 9, 8, 3, 4, 5, 7, 6], [3, 8, 4, 5, 6, 7, 2, 1, 9], [5, 7, 6, 9, 1, 2, 3, 8, 4], [8, 9, 1, 3, 4, 6, 7, 5, 2], [6, 3, 2, 7, 8, 5, 4, 9, 1], [7, 4, 5, 2, 9, 0, 0, 0, 0]]
    solved, solution = solve(array)
    for row in solution:
        print(row)
    print(is_solution(solution))
    print(solution)