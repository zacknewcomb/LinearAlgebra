def secant(f, x0, x1, n = 50, accuracy = 10**-6, currIteration = 0):
    if n <= 0:
        raise Exception("Number of Iterations performed in Secant method must be greater than 0, you input " + str(n))
    
    if abs(x1-x0) <= accuracy:
        return x1
    
    x2 = x1 - f(x1) * (x1-x0) / (f(x1) - f(x0))
    currIteration += 1
    if currIteration < n:
        root = secant(f,x1,x2,n,accuracy,currIteration)
        
    return root

def newton(f, fprime, x0, n = 50, accuracy = 10**-6, currIteration = 0):
    if n <= 0:
        raise Exception("Number of Iterations performed in Newton's method must be greater than 0, you input " + str(n)) 
    
    x1 = x0 - (f(x0) / fprime(x0))
    
    if abs(x1-x0) <= accuracy:
        return x1
    
    if currIteration < n:
            root = newton(f,fprime,x1,n,accuracy,currIteration)
            
    return root