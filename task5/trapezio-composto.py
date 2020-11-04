import math

f = lambda x: x * math.sin(x)

def trapezioComposto(f, a, b, n):
    h = float(b - a)/n
    r = 0
    r += f(a)
    for i in range(1, n):
        r += f(a + i*h)*2.0
    r += f(b)
    return r*(h/2.0)

print(trapezioComposto(f, -5, 5, 10))
