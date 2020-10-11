pontos = [(0,1), (2,3), (4,-1), (7,4)]

def FXi(i):
    return Y(i)

def X(i):
    return pontos[i][0]

def Y(i):
    return pontos[i][1]

fx0 = FXi(0)
fx0x1 = (FXi(1) - fx0)/(X(1) - X(0))
fx1x2 = (FXi(2) - FXi(1)) / (X(2) - X(1))
fx0x1x2 = (fx1x2 - fx0x1)/(X(2) - X(0))
fx2x3 = (FXi(3) - FXi(2))/(X(3) - X(2))
fx1x2x3 = (fx2x3 - fx1x2)/(X(3) - X(1))
fx0x1x2x3x4 = (fx1x2x3 - fx0x1x2)/(X(3) - X(0))
results = [fx0, fx0x1, fx0x1x2, fx0x1x2x3x4]
print(results)