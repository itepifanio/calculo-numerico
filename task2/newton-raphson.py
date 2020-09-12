import numpy as np

f = lambda x: x**3 - 1.7*(x**2) - 12.78*x - 10.08
df = lambda x: 3*x**2 - 3.4*x - 12.78

max_iteracoes = 100 # evita loops infinitos
x0 = 3 #chute inicial
erro = 1

i = 0
while erro > 0.0001 and max_iteracoes > i:
    # x_{n+1} = x_{n} - f(x_{n})/df(x_{n})
    x1 = x0 - (f(x0)/df(x0))
    erro = abs(x1 - x0)
    x0 = x1

    print(f'|{i:2d} | {x1:.10f} |')
    i += 1