def sum_matrix(m):
    s = 0
    for i in range(0, len(m)):
        for i2 in range(0, len(m[i])):
            s += m[i][i2]
        return s

m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print(sum_matrix(m))
