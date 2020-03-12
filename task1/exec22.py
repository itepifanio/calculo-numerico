import numpy as np
import PyGnuplot as gp
from functools import reduce
from math import cos, sin, factorial

a = 0 # aproximação de 0
odd  = lambda k,x: (-1)**((k-1)/2)*k*cos(x) + (-1)*((k+1)/2) * x * sin(x)
even = lambda k,x: (-1)**(k/2)*k*sin(x) + (-1)*(k/2) * x * cos(x)

def f(x):
    result_global = 0
    for i in range(0, 13):
        if i%2 == 0:
            r = (even(i, a)/factorial(i))*((x - a)**i)
        else:
            r = (odd(i, a)/factorial(i))*((x - a)**i)
        result_global += r
    
    return result_global

# func_direct = gp.PyFunction(f)
# gp.s(np.(f), filename='teste.out')