# Eliminacao de Gauss sem pivoteamento

def obterMatrizTriangular(matriz):
    n = len(matriz)
    for i in range(n-1):
        for j in range(i, n-1):
            fator = matriz[j+1][i]/matriz[i][i]
            for k in range(0, n+1):
                value = matriz[j+1][k] - matriz[i][k]*fator
                matriz[j+1][k] = value
            if matriz[j+1][i] < 1.0e-12:
                matriz[j+1][i] = 0
    return matriz


matriz = []
for i in range(1, 4):
    with open(f'./data/m{i}.txt', 'r') as f:
        next(f)
        matriz = [[float(num) for num in line.split(' ')] for line in f]

    with open(f'./data/r{i}.txt', 'w') as f:
        for linha in obterMatrizTriangular(matriz):
            for elemento in linha:
                f.write(f'{elemento} ')
            f.write("\n")