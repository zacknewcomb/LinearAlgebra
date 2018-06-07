
def matrix_mult(m1, m2):
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


def main():
    matrix1 = []
    matrix2 = []

    print("Matrix multiplication will be performed by calculating Matrix 1 * Matrix 2. Remember 'order matters' in matrix multiplication")
    rows1 = int(input("How many rows in first matrix? "))
    cols1 = int(input("How many columns in first matrix? "))
    rows2 = int(input("How many rows in second matrix? "))
    cols2 = int(input("How many columns in second matrix? "))
    if rows1 != cols2:
        print("Please remember order matters in Matrix multiplication. The dimension you gave for the two matricies will not produce matricies that are compatible with matrix multiplication.")
        main()
    else:
        print("Input each row of matrix one and hit enter")
        for i in range(rows1):
            row = list(map(int, input().rstrip().split()))
            matrix1.append(row)
            
        print(matrix1)
        print("Input each row of matrix two and hit enter")
        for x in range(rows2):
            row = list(map(int, input().rstrip().split()))
            matrix2.append(row)
        print(matrix2)
    
        result = matrix_mult(matrix1, matrix2)
        for row in result:
            print(row)
            
        
    
main()
