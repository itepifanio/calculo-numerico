import math

f = lambda x: x * math.sin(x)
  
def simpson38(f, x0, xn, n ): 
    h = float(xn - x0)/n
    r = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i*h

        if (i % 3 == 0): 
            r = r + 2 * f(k) 
        else: 
            r = r + 3 * f(k) 
      
    r = float((3*h)/8) * r

    return r

print(simpson38(f, -5, 5, 10))