sumX = 0
sumXX = 0
sumXXX = 0
sumXXXX = 0
sumXY = 0
sumXXY = 0
sumY = 0
n = 0

with open('barcos.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        try:
            x, y = line.strip().split(" ")
            x = float(x)
            y = float(y)
            n += 1
            sumX += x
            sumXX += x**2
            sumXXX += x**3
            sumXXXX += x**4
            sumY += y
            sumXY += x*y
            sumXXY += x*x*y
        except:
            pass

print(f'n: {n}')

print(f'[ n:     {n}    , sumXi: {sumX}   , sumXX:   {sumXX}   ]')
print(f'[ sumXi: {sumX} , sumXX: {sumXX}  , sumXXX:  {sumXXX}  ]')
print(f'[ sumXX: {sumXX}, sumXXX: {sumXXX}, sumXXXX: {sumXXXX} ]')
print()
print(f'[sumY:   {sumY}  ]')
print(f'[sumYX:  {sumXY} ]')
print(f'[sumXXY: {sumXXY}]')

# 376.0255754475703
# -75.88511749347259
# 3.8645640074211505