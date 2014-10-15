import copy
from sum_matrix import sum_matrix


NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)]


def within_bounds(m, at):
    if at[0] < 0 or at[0] >= len(m):
        return False
    if at[1] < 0 or at[1] >= len(m[0]):
        return False
    return True


def bomb(m, at):
    if not within_bounds(m, at):
        return m
    target_value = m[at[0]][at[1]]
    dx, dy = 0, 1
    for position in NEIGHBORS:
        position = (at[dx] + position[dx], at[dy] + position[dy])
        if within_bounds(m, position):
            position_value = m[position[dx]][position[dy]]
            m[position[dx]][position[dy]] -= min(target_value, position_value)
    return m


def matrix_bombing_plan(m):
    result = {}
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            bombed = bomb(copy.deepcopy(m), (i, j))
            result[(i, j)] = sum_matrix(bombed)
    return result

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_bombing_plan(m))
