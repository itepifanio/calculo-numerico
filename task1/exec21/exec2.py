import math
d = lambda x: math.cos(x) - x*math.sin(x)
x = 0
c = 0
aux = -1
h = -0.5

while x > -6:
	xh = x + h
	if c == 0:
		aux = 1 + h*d(x)
		x = xh
	else:
		aux = aux + h*d(x)
		x = xh
	print(f'{x} {aux}')

	c += 1

x = 0
c = 0
aux = -1
h = 0.5

while x <= 6:
	xh = x + h
	if c == 0:
		aux = 1 + h*d(x)
		x = xh
	else:
		aux = aux + h*d(x)
		x = xh
	print(f'{x} {aux}')

	c += 1
	


