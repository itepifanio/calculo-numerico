# Eliminacao de Gauss sem pivoteamento

def multiplicaLinha(linha, i):
  return [x * i for x in linha]

def subtraiLinha(linhaA, linhaB):
  return [a - b for (a, b) in zip(linhaA, linhaB)]

def escalonar(matriz):
    temp = list(matriz)
    for i in range(len(matriz)):
        linhaAtiva = temp[i]
        for j, col in enumerate(temp[(i+1):]):
            j += 1
            if linhaAtiva[i] == 0: continue
            temp[j+i] = subtraiLinha(col, multiplicaLinha(linhaAtiva, col[i]//linhaAtiva[i]))
    print(temp)


matriz = [[1,2,3], [4,5,6], [7,8,9]]

escalonar(matriz)