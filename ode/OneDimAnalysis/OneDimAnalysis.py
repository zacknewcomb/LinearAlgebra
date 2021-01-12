import roots
import integration

def stability(fixedPoint, f, ep=10**-8):
    accuracy = 10**-8
    if abs(f(fixedPoint)) > accuracy:
        raise Exception("The point provided as the fixed point isn't a fixed point for the function given")
    
    left_of_point = f(fixedPoint-ep)
    right_of_point = f(fixedPoint+ep)
    
    # Definition of stable
    if left_of_point > 0 and right_of_point < 0:
        return "stable"
    
    # Definition of unstable
    if left_of_point < 0 and right_of_point > 0:
        return "unstable"
    
    # Definition of a semi-stable point
    if (left_of_point < 0 and right_of_point < 0) or (left_of_point > 0 and right_of_point > 0):
        return "semi-stable"
    
    if left_of_point == 0 or right_of_point == 0:
        raise Exception("One of the test points to check for stability was also 0. That means that the fixed point given and a sample point were both 0, please consider making epsilon smaller")
    
def fixedPoint(phasePoint, f):
    
    # accuracy
    accuracy = 10**-8
    
    # Check which direction the phase point is flowing
    direction = f(phasePoint)
    
    # If it is positive find the next fixed point greater than the current phase point
    if direction > 0:
        fixedPoint = phasePoint - 1
        iterations = 0
        phaseAdjuster = iterations * 0.25
        
        while fixedPoint < phasePoint and iterations < 100:
            phaseAdjuster = iterations * 1
            phaseAdjuster2 = (iterations + 1) * 1
            x1 = phasePoint + phaseAdjuster2
            x0 = phasePoint + phaseAdjuster
            fixedPoint = roots.secant(f, x0, x1, n = 100)
            iterations += 1
        
        if f(fixedPoint) > accuracy:
            raise Exception("No fixed point found, phase point possibly trending to infintiy")
        
        return fixedPoint
    
    if direction < 0:
        fixedPoint = phasePoint + 1
        iterations = 0
        phaseAdjuster = iterations * 0.25
        
        while fixedPoint > phasePoint and iterations < 100:
            phaseAdjuster = iterations * 1
            phaseAdjuster2 = (iterations + 1) * 1
            x1 = phasePoint - phaseAdjuster2
            x0 = phasePoint - phaseAdjuster
            fixedPoint = roots.secant(f, x0, x1, n = 100)
            iterations += 1
        
        if f(fixedPoint) > accuracy:
            raise Exception("No fixed point found, phase point possibly trending to infintiy")
        
        return fixedPoint

def linearStability(fixedpt, f):
    ep = 10**-4
    derivative = f((fixedpt + ep) - f(fixedpt)) / ep
    if derivative < 0:
        return "stable"
    elif derivative > 0:
        return "unstable"
    else:
        return "Derivative is 0, need to perform other analysis to determine stability"
    
            
    