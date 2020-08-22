def transpose(matrix):
    newMatrix = []
    
    row = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        newMatrix.append(row)
        row = []
    
    return newMatrix