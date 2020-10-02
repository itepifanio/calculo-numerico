# Eliminacao de Gauss com pivoteamento
def escolhePivo(matriz, i, j):
    maior = 0
    maiorIndice = i
    while i < len(matriz):
       # print(mat[i][j])
        if abs(matriz[i][j]) > maior:
            maior = matriz[i][j]
            maiorIndice = i
        i += 1
    return maiorIndice

def obterMatrizTriangular(matriz):
    n = len(matriz)
    for i in range(n-1):
        pivoIndex = escolhePivo(matriz, i, i)
        aux = matriz[i]
        matriz[i] = matriz[pivoIndex]
        matriz[pivoIndex] = aux
        for j in range(i, n-1):
            fator = matriz[j+1][i]/matriz[i][i]
            for k in range(0, n+1):
                matriz[j+1][k] = matriz[j+1][k] - matriz[i][k]*fator
    return matriz

matriz = []
for i in range(1, 5):
    with open(f'./data/m{i}.txt', 'r') as f:
        next(f)
        matriz = [[float(num) for num in line.split(' ')] for line in f]

    with open(f'./data/r{i}.txt', 'w') as f:
        for linha in obterMatrizTriangular(matriz):
            for elemento in linha:
                f.write(f'{elemento} ')
            f.write("\n")