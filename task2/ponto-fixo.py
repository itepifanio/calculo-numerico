f = lambda x: x**3 - 1.7*(x**2) - 12.78*x - 10.08

#reescrevendo f

g = lambda x: (x**3)/12.78 + (1.7*(x**2))/12.78 + 10.08/12.78



erro = 0.00001

# chute inicial
x0 = 0.5

i = 0

while i < 10000:
    x1 = g(x0)
    
    print(f'|{i:2d} | {x1:.10f} |')

    if abs(x1 - x0) < erro:
        break

    x0 = x1
    i += 1

