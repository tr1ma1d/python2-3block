def find_mountain(matrix):
    max_height = 0
    i_ind = j_ind = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if max_height < matrix[i][j]:
                max_height = matrix[i][j]
                i_ind, j_ind = i, j

    return i_ind, j_ind


a = [[2, 4, 2, 3, 2], [3, 2, 3, 4, 3]]
row, col = find_mountain(a)
print(a[row][col])


