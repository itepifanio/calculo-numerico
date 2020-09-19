f = lambda x: x**3 - 1.7*(x**2) - 12.78*x - 10.08

max_iteracoes = 100 # evita loops infinitos

# valores que delimitam a raíz
a = -3
b = 0
m = (f(b) - f(a))/(b-a)
c = a - f(a)/m

i = 0
while abs(f(c)) > 0.0001 and max_iteracoes > i:
    if abs(b - a) < 0.0001:
        break

    if f(c)*f(a) > 0:
        a = c
    else:
        b = c
    m = (f(b) - f(a))/(b-a)
    c = a - f(a)/m

    print(f'|{i:2d} | {c:.10f} | {f(c):.10f}')
    i += 1  