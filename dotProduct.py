def dot_prod(v1,v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i]*v2[i]
        
    return result
