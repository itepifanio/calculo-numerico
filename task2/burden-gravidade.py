import math
g = 32.17
s0 = 300
m = 0.25
k = 0.1
erro = 0.0000000000000000000001

f = lambda t : s0 - t*((m*g)/k) + (((m**2)*g)/(k**2))*(1 - math.exp((-k*t)/m))

max_iteracoes = 10000 # evita loops infinitos

# utilizando o método da secante
a = 0
b = 99
c = (a + b)/2 # ponto médio

i = 0
while max_iteracoes > i:
    if abs(b - a) < erro:
        break

    c = b - ((b - a)/ (f(b) - f(a)))*f(b)
    a = b
    b = c

    print(f'|{i:2d} | {c:.10f} |')
    i += 1

