import math

def distanceBetween(A, B):
    if len(A) != len(B):
        raise Exception("The two input vectors must be of the same length")
    
    total = 0
    
    for i in range(len(A)):
        total += (A[i] - B[i]) * (A[i] - B[i])
        
    total = math.sqrt(total)
    
    return total
    