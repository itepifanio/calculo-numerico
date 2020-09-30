# Eliminacao de Gauss com pivoteamento
from sys import maxsize

def multiplicaLinha(linha, i):
  return [x * i for x in linha]

def subtraiLinha(linhaA, linhaB):
  return [a - b for (a, b) in zip(linhaA, linhaB)]

def escolhePivo(matriz, coluna = 0):
    max = -maxsize - 1
    index = 0
    it = coluna
    while it < len(matriz):
        if abs(matriz[it][coluna]) > max:
            max = matriz[it][coluna]
            index = it
        it += 1 
    return index

def trocaLinhas(matriz, i, j):
    temp      = matriz[i]
    matriz[i] = matriz[j]
    matriz[j] = temp
    return matriz

def metodo(matriz):
    n = len(matriz)
    j = 0
    i = 0
    while j < (n-1):
        pivoIndex = escolhePivo(matriz, j)
        temp = matriz[j]
        matriz[j] = matriz[pivoIndex]
        matriz[pivoIndex] = temp
        i = j+1
        while i < n:
            m = matriz[i][j]/matriz[j][j]
            matriz[i] = subtraiLinha(matriz[i], multiplicaLinha(matriz[j], m))
            i += 1
        j += 1
    return matriz


matriz = [
    [2,1,1,0,1],
    [4,3,3,1,2],
    [8,7,9,5,4],
    [6,7,9,8,5]
]

print(
    metodo(matriz)
)