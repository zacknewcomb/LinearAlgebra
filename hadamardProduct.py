def HadamardProduct(A, B):
    C = []
    for row in range(len(A)):
        resultRow = []
        for k in range(len(A[row])):
            resultRow.append(A[row][k] * B[row][k])

        C.append(resultRow)

    return C   
