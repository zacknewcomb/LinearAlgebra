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

'''
def main():
    A = [
        [0,0],
        [-1,2],
        [-1,-4]
    ]

    rowEchelon(A)

    for row in A:
        print(row)
  

main()
'''