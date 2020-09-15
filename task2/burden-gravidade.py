import numpy as np
g = 32.17
s0 = 300
m = 0.25
k = 0.1
error = 0.00001

s = lambda t : s0 - t*((m*g)/k) + ((m**2)*g)/(k**2)*(1- np.exp((-k*t)/m))

# isolando s = 0

t = lambda t: s0/(m*g/k) + ((m**2)*g)/(k**2)*(1- np.exp((-k*t)/m))/(m*g/k)

#300/(0.25*32.17/0.1) + ((0.25**2)*32.17)/((0.1)**2)*((1 - e**(-0.1*t)/0.25)/(0.25*32.17)/0.1)

i = 0
x0 = 0
x1 = 0
while i < 100:
    x1 = t(x0)
    x0 = x1
    i += 1

print(x1)

