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
            temp[j+i] = subtraiLinha(col, multiplicaLinha(linhaAtiva, col[i]/linhaAtiva[i]))
    return temp

def obterVetorSolucao(matrizTriangular):
    m = len(matrizTriangular)
    result = []
    for i in range(m - 1, -1, -1): # itera pelo fim 3, 2, 1, 0...
        result.insert(0, matrizTriangular[i][m] / matrizTriangular[i][i])
        for k in range(i - 1, -1, -1):
            matrizTriangular[k][m] -= matrizTriangular[k][i] * result[0]
    return result


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