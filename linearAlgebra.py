import math

def crossProduct(v1,v2):
    i = (v2[2]*v1[1])-(v2[1]*v1[2])
    j = -1* ((v2[2]*v1[0])-(v2[0]*v1[2]))
    k = (v2[1]*v1[0])-(v2[0]*v1[1])
    
    return ([i, j, k])

def determinant(m1):
    if len(m1) == 1:
        return (m1[0][0])
    if len(m1) == 2:
        return ((m1[0][0]*m1[1][1])-(m1[0][1]*m1[1][0]))
    else:
        det = 0
        mult = 1
        for col in range(len(m1)):
            temp = []
            for row in m1:
                new_row = []
                for i in row:
                    new_row.append(i)
                temp.append(new_row)
            for i in range(len(temp)):
                del temp[i][col]
            del temp[0]
            if col % 2 == 0:
                mult = 1
            else:
                mult = -1
            det += ((mult * m1[0][col]) * determinant(temp))
        
    return (det)

def distanceBetween(A, B):
    if len(A) != len(B):
        raise Exception("The two input vectors must be of the same length")
    
    total = 0
    
    for i in range(len(A)):
        total += (A[i] - B[i]) * (A[i] - B[i])
        
    total = math.sqrt(total)
    
    return total

def dotProduct(v1,v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i]*v2[i]
        
    return result

def hadamardProduct(A, B):
    C = []
    for row in range(len(A)):
        resultRow = []
        for k in range(len(A[row])):
            resultRow.append(A[row][k] * B[row][k])

        C.append(resultRow)

    return C 

def isOrthogonalSet(S):
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            if dotProduct.dot_prod(S[i], S[j]) != 0:
                return False

    return True

def kroneckerProduct(A,B):
    C = []
    for rowA in A:
        for rowB in B:
            newRow = []
            for entryA in rowA:
                for entryB in rowB:
                    newRow.append(entryA * entryB)

            C.append(newRow)
    return C

def multiplyMatrices(m1, m2):
    result_matrix =[]
    result_rows = len(m1)
    result_cols = len(m2[0])
    for i in range(result_rows):
        row = []
        for j in range(result_cols):
            element = 0
            for k in range(len(m2)):
                element += m1[i][k]*m2[k][j]
            row.append(element)
        result_matrix.append(row)
           
    return result_matrix

def normalize(vector):
    total = 0
    for i in vector:
        total += i*i
    
    total = math.sqrt(total)
    
    for i in range(len(vector)):
        vector[i] = vector[i] / total
        
    return vector

def projectionOf_y_Onto_u(u,y):
    nonZero = False
    ct = 0
    while not nonZero and ct < len(u):
        if u[ct] != 0:
            nonZero = True
        ct += 1
    
    if not nonZero:
        raise Exception('Orthogonal Projection cannot be applied to the zero vector')
        
    returnVec = [None for i in range(len(y))]
    for i in range(len(u)):
        returnVec[i] = (dotProduct(u,y) / dotProduct(u,u)) * u[i]
        
    return returnVec

def rowEchelon(A):
    for row in range(len(A)):
        col = min(row,len(A[row])-1)
        changed = reOrderMatrix(A, row , col)
        while (not changed and col < len(A[row])-1):
            col = col + 1
            changed = reOrderMatrix(A, row, col)

    for row in range(len(A)):
        normalizer = 1
        for col in range(len(A[row])):
            if A[row][col] != 0:
                normalizer = A[row][col]
                for column in range(len(A[row])):
                    A[row][column] = A[row][column] / normalizer
                break

    # Now begin row ops
        for row1 in range(row+1,len(A)):
            if A[row1][col] != 0:
                scaledRow = map(lambda x: x * A[row1][col], A[row])
                negativeRow = map(lambda x: x * -1, A[row1])
                A[row1] = [sum(x) for x in zip(scaledRow, negativeRow)]


def reOrderMatrix(A, row, column):
    changed = False
    allZeros = True
    i = row
    nonZeroEntry = A[i][column]
    while nonZeroEntry == 0 and i < len(A)-1:
        i += 1
        nonZeroEntry = A[i][column]

    if nonZeroEntry != 0:
        allZeros = False

    if not allZeros:
        temp = A[row]
        A[row] = A[i]
        A[i] = temp
        changed = True

    return changed

def transpose(matrix):
    newMatrix = []
    
    row = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        newMatrix.append(row)
        row = []
    
    return newMatrix