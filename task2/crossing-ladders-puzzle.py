x1 = 20
x2 = 30
A = 8

def f(x):
    return x**4 - 2*A*x**3 - (x2**2 - x1**2)*x**2 + 2*A*(x2**2 - x1**2)*x - A**2*(x2**2 - x1**2)

max_iteracoes = 1000

a = -50
b = 50

i = 0
while max_iteracoes > i:
    if abs(b - a) < 0.0001:
        break

    c = b - ((b - a)/ (f(b) - f(a)))*f(b)
    a = b
    b = c

    print(f'|{i:2d} | {c:.10f} |')
    i += 1