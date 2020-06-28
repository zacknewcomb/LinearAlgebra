def KroneckerProduct(A,B):
    C = []
    for rowA in A:
        for rowB in B:
            newRow = []
            for entryA in rowA:
                for entryB in rowB:
                    newRow.append(entryA * entryB)
                    
            C.append(newRow)
                
                
    return C