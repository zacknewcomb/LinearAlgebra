import numpy as np

def gamma(s, a, b, f, tn, delta_t, y, k):
    # Define c from the matrix A
    c = [sum(a[i]) for i in range(len(a))]
    summation = sum([b[j] * f(tn+c[j]*delta_t, k[j]) for j in range(s)])
    Energy = np.linalg.norm(summation)**2

    if Energy == 0:
        return 1

    numerator = 0
    for i in range(s):
        for j in range(s):
            fi = k[i]
            fj = k[j]
            numerator += b[i]*a[i][j] * np.dot(fi, fj)
    numerator = 2 * numerator

    denominator = 0
    for i in range(s):
        for j in range(s):
            fi = k[i]
            fj = k[j]
            denominator += b[i]*b[j]*np.dot(fi,fj)

    gam = numerator / denominator
    return gam

def RK4(f,x0,t0,h):
    k1 = f(t0,x0)
    k2 = f(t0 + h/2, x0+((h/2)*k1))
    k3 = f(t0 + h/2, x0+((h/2)*k2))
    k4 = f(t0 + h, x0 + h*k3)
    x1 = x0 + (h/6)*(k1+2*k2+2*k3+k4)
    return t0+h, x1
    
def RRK4(f,x0,t0,h):
    s = 4
    b = np.array([1/6, 1/3, 1/3, 1/6])
    A = np.array([
        [0,0,0,0],
        [1/2,0,0,0],
        [0,1/2,0,0],
        [0,0,1,0]
    ])
    k1 = f(t0,x0)
    k2 = f(t0 + h/2, x0+((h/2)*k1))
    k3 = f(t0 + h/2, x0+((h/2)*k2))
    k4 = f(t0 + h, x0 + h*k3)
    k = [k1,k2,k3,k4]
    gam = gamma(s, A, b, f, t0, h, x0, k)
    x1 = x0 + gam*(h/6)*(k1+2*k2+2*k3+k4)
    t = t0 + gam*h
    return t, x1    

def euler(f, x0, t0, h):
    return x0 + h * f(t0, x0)

def midpoint(f, x0, t0, h):
    return x0 + h*f(t0+0.5*h, x0 + 0.5*h*f(t0, x0))
