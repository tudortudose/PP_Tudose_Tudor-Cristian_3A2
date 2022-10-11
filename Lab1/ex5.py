def traverseSpiralMatrix(matrix):
    n = len(matrix)

    dir_i = [0, 1, 0, -1]
    dir_j = [1, 0, -1, 0]
    current_dir_index = 0

    current_i = 0
    current_j = 0

    string = ""
    visited = [[False for i in range(n)] for j in range(n)]

    for i in range(0, n * n):
        string += matrix[current_i][current_j]
        visited[current_i][current_j] = True
        current_i += dir_i[current_dir_index]
        current_j += dir_j[current_dir_index]

        if not (0 <= current_i < n and 0 <= current_j < n and visited[current_i][current_j] == False):
            current_i -= dir_i[current_dir_index]
            current_j -= dir_j[current_dir_index]
            current_dir_index = (current_dir_index + 1) % 4
            current_i += dir_i[current_dir_index]
            current_j += dir_j[current_dir_index]

    return string
