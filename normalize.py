import math


def normalize(vector):
    total = 0
    for i in vector:
        total += i*i
    
    total = math.sqrt(total)
    
    for i in range(len(vector)):
        vector[i] = vector[i] / total
        
    return vector