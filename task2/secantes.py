import numpy as np

f = lambda x: x**3 - 1.7*(x**2) - 12.78*x - 10.08

max_iteracoes = 100 # evita loops infinitos

# valores que delimitam a raíz
a = -3
b = 0
c = (a + b)/2 # ponto médio

i = 0
while max_iteracoes > i:
    if(f(b) - f(a)) == 0:
        break

    c = b - ((b - a)/ (f(b) - f(a)))*f(b)
    a = b
    b = c

    print(f'|{i:2d} | {c:.10f} |')
    i += 1