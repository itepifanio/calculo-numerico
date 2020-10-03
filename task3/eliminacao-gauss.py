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

def vetorResidual(matrizTriangular):
    m = len(matrizTriangular)
    result = []
    for i in range(m - 1, -1, -1): # itera pelo fim 3, 2, 1, 0...
        result.insert(0, matrizTriangular[i][m] / matrizTriangular[i][i])
        for k in range(i - 1, -1, -1):
            matrizTriangular[k][m] -= matrizTriangular[k][i] * result[0]
    return result

def norma(vetorResidual):
    value = 0
    for elem in vetorResidual:
        value += pow(abs(elem), 2)
    return pow(value, 0.5)

matriz = []
for i in range(1, 4):
    with open(f'./data/m{i}.txt', 'r') as f:
        next(f)
        matriz = [[float(num) for num in line.split(' ')] for line in f]

    with open(f'./data/r{i}.txt', 'w') as f:
        matrizTriangular = obterMatrizTriangular(matriz)
        normaVetor       = vetorResidual(matrizTriangular)
        print(normaVetor)
        for linha in matrizTriangular:
            for elemento in linha:
                f.write(f'{elemento} ')
            f.write("\n")
