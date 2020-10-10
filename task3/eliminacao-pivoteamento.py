import copy

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
                value = matriz[j+1][k] - matriz[i][k]*fator
                matriz[j+1][k] = value
            if matriz[j+1][i] < 1.0e-12:
                matriz[j+1][i] = 0
    return matriz

def obterResultado(matrizTriangular): # xBarra
    m = len(matrizTriangular)
    result = []
    for i in range(m - 1, -1, -1): # itera pelo fim 3, 2, 1, 0...
        result.insert(0, matrizTriangular[i][m] / matrizTriangular[i][i])
        for k in range(i - 1, -1, -1):
            matrizTriangular[k][m] -= matrizTriangular[k][i] * result[0]
    return result

def obterVetorResidual(b, matriz, xBarra): # B - A*xBarra
    # A*xBarra
    result = []
    for i in range(len(xBarra)):
        value = 0
        for j in range(len(xBarra)):
            value += xBarra[j] * matriz[i][j]
        result.append(value)
    # B - A*xBarra

    for i, value in enumerate(b):
        result[i] = value - result[i]

    return result

def obterNorma(vetorResidual):
    value = 0
    for elem in vetorResidual:
        value += pow(abs(elem), 2)
    return pow(value, 0.5)

matriz = []
for i in range(2, 4):
    # lê arquivo
    with open(f'./data/m{i}.txt', 'r') as f:
        next(f)
        matriz = [[float(num) for num in line.split(' ')] for line in f]
    
    matrizA = copy.deepcopy(matriz) # copia da matriz para ser usada no calculo do vetor residual
    norma   = -1
    cont    = 0
    while norma != 0:
        matrizTriangular = obterMatrizTriangular(matriz)
        print(matrizTriangular)
    #     xBarra           = obterResultado(matrizTriangular)
        
    #     # vetorResidual  = B - A * xBarra onde xBarra é o primeiro valor aproximado da matriz.
    #     vetorResidual    = obterVetorResidual([i[-1] for i in matrizA], [i[:-1] for i in matrizA], xBarra)
    #     # print(vetorResidual)
    #     norma            = obterNorma(vetorResidual)
    #     if norma != 0:
    #         # transforma a proxima matriz para calcular Ay = r, onde r é o vetor residual (B - AxBarra)
    #         ayr = list(matrizA)
    #         for i in range(len(vetorResidual)):
    #             ayr[i][-1] = vetorResidual[i]
    #         y = obterResultado(obterMatrizTriangular(ayr)) # encontra y
    #         x = [xBarra[i] + y[i] for i in range(len(y))] # x = xBarra + y
            
    #         # coloca a matriz para receber o valor Ax = b que será calculado até a norma ser zero
    #         ayr = list(matrizA)
    #         for i in range(len(x)):
    #             ayr[i][-1] = x[i]

    #         matriz = ayr
    #     cont += 1 # conta refinamentos
    # print(cont)

