from . import dotProduct

def isOrthogonalSet(S):
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            if dotProduct.dot_prod(S[i], S[j]) != 0:
                return False
    
    return True