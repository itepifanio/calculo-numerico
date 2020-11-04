import math

f = lambda x: x * math.sin(x)

def simpson13(f, x0, xn, n):
    h = float(xn - x0) / n

    r = f(x0) + f(xn)

    for i in range(1,n):
        k = x0 + i*h

        if i%2 == 0:
            r = r + 2 * f(k)
        else:
            r = r + 4 * f(k)

    r = r * float(h/3)

    return r

print(simpson13(f, -5, 5, 10))