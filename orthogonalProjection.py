from . import dotProduct

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
        returnVec[i] = (dotProduct.dot_prod(u,y) / dotProduct.dot_prod(u,u)) * u[i]
        
    return returnVec