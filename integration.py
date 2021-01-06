def trapezoid(f,a,b,n=1000):
    delta_x = (b-a) / n
    integral_sum = 0
    partition = [a + i*delta_x for i in range(n+1)]
    for p in partition[1:-1]:
        integral_sum += 2 * f(p)
    integral_sum += f(a) + f(b)
    integral_sum = 0.5 * delta_x * integral_sum
    return integral_sum
        
def midpoint(f,a,b,n=1000):
    delta_x = (b-a) / n
    integral_sum = 0
    partition = [a + i*delta_x for i in range(n+1)]
    for p in partition[1:-1]:
        integral_sum += f(p)
    integral_sum = integral_sum * delta_x
    return integral_sum

        
    