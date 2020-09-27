# Eliminacao de Gauss sem pivoteamento

def multiplicaLinha(linha, i):
  return [x * i for x in linha]

def subtraiLinha(linhaA, linhaB):
  return [a - b for (a, b) in zip(linhaA, linhaB)]

def obterMatrizTriangular(matriz):
    temp = list(matriz)
    for i in range(len(matriz)):
        linhaAtiva = temp[i]
        for j, col in enumerate(temp[(i+1):]):
            j += 1
            if linhaAtiva[i] == 0: continue
            temp[j+i] = subtraiLinha(col, multiplicaLinha(linhaAtiva, col[i]//linhaAtiva[i]))
    return temp

def obterVetorSolucao(matrizTriangular):
    m = len(matrizTriangular)
    result = []
    for i in range(m - 1, -1, -1): # itera pelo fim 3, 2, 1, 0...
        result.insert(0, matrizTriangular[i][m] / matrizTriangular[i][i])
        for k in range(i - 1, -1, -1):
            matrizTriangular[k][m] -= matrizTriangular[k][i] * result[0]
    return result

matriz = [
    [3,1,2,1,15],
    [6,5,9,1,45],
    [9,-3,-2,6,25],
    [-6,10,18,1,52]
]

print(
    obterVetorSolucao(
        obterMatrizTriangular(matriz)
    )
)