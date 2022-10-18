def setZeroUnderDiagMatrix(matrix):
    for i in range(1, len(matrix)):
        for j in range(i):
            matrix[i][j] = 0
    return matrix
