#This can handle any size matrix
#Learned painful, painful lessons on the 'del' function of python
#Surprisingly, I was able to conceptualize and think about the recursive
#ideas easily. Thanks to my linear algebra class!


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
            #del temp[0:(len(temp))][col]
            for i in range(len(temp)):
                del temp[i][col]
            del temp[0]
            if col % 2 == 0:
                mult = 1
            else:
                mult = -1
            det += ((mult * m1[0][col]) * determinant(temp))
        
    return (det)


def main():
    print("Input matrix row by row After completed a full row, hit enter")
    print("***Note, however manty entries you place in the***\n***first row, will be how many rows there will be***")
    matrix = []
    row1 = list(map(int, input().strip().split()))
    matrix.append(row1)
    for i in range(len(row1)-1):
        row = list(map(int, input().strip().split()))
        matrix.append(row)
    det = determinant(matrix)
    print (det)
    
main()
