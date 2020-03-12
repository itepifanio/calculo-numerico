import numpy as np
import PyGnuplot as gp
from functools import reduce
from math import cos, sin, factorial

a = 0 # aproximação de 0
odd  = lambda k,x: (-1)**((k-1)/2)*k*cos(x) + (-1)*((k+1)/2) * x * sin(x)
even = lambda k,x: (-1)**(k/2)*k*sin(x) + (-1)*(k/2) * x * cos(x)

def f(x):
    result_global = 0
    for i in range(0, 160):
        if i%2 == 0:
            r = (even(i, a)/factorial(i))*((x - a)**i)
        else:
            r = (odd(i, a)/factorial(i))*((x - a)**i)
        result_global += r
    
    return result_global

rng = np.linspace(-100, 100, 1000)
fx = [f(i) for i in rng]

gp.s([rng, fx], filename='teste.out')
gp.c('set xrange [-10:10]')
gp.c('plot x*cos(x) + 1 title "f(x) = x*cos(x) + 1"')
gp.c('replot "teste.out" title "aproximação" w lp ls 1 lc rgb "blue"')