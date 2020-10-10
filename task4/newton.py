# pn(x) = somatorioDeZeroAteN(
#   diferencaDivididaEntreX0AteXk()*Nk(x)
# )

# Nk(x) = produtorioZeroAteK-1(x-xi)
# diferencaDivididaEntreX0AteXk = (f[X1...Xk] - f[X0...X(k-1)])/(Xk - X0)

# casoBase (1 termo) f[Xk] = f(Xk)

# Pontos (0,1), (2,3), (4,-1), (7,4)

# temos 4 pontos, então lidaremos com polinomio de grau 3

pontos = [(0,1), (2,3), (4,-1), (7,4)]
# pontos = [(1,2), (2,5), (3,3)]
# p3x = diferencaDivida(x0)*1+diferencaDivida(x0,x1)*N()

def FXi(i):
    return Y(i)

def X(i):
    return pontos[i][0]

def Y(i):
    return pontos[i][1]

# fx0 = FXi(0)
# fx0x1 = (FXi(1) - fx0)/(X(1) - X(0))
# fx1x2 = (FXi(2) - FXi(1)) / (X(2) - X(1))
# fx0x1x2 = (fx1x2 - fx0x1)/(X(2) - X(0))
# print(f'f[x0] = f(x0) = {fx0}')
# print(f'f[x0,x1] = f[x1] - f[x0]/x1 - x0 = {fx0x1}')
# print(f'f[x0,x1,x2] = f[x1,x2] - f[x0,x1]/x2 - x0 = {fx0x1x2}')

results = []
for i in range(len(pontos)):
    if i == 0:
        results.append(FXi(i))
    elif i < len(pontos)-1:
        r = FXi(i) - results[i-1]/(X(i) - X(i-1))
        results.append(r)
    else:
        r = (FXi(i) - FXi(i-1))/(X(i) - X(i-1))
        r = (r - results[i-1])/(X(i) - X(0))
        results.append(r)

polinomios = []
for i in range(len(pontos)):
    if i == 0:
        polinomios.append(str(results[i]))
    else:
        r = ''
        for j in range(i):
            r += f'(x-{X(j)})*'
        polinomios.append(r)

print(results)
print(polinomios)