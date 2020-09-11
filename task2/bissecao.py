f = lambda x: x**3 - 1.7*(x**2) - 12.78*x - 10.08
intervalo = {'a': -5, 'b': 5}

def ponto_medio(x, y):
    return (x + y)/2

max_interacoes = 100 # evita loops infinitos
n = 0
result = -1
erro = 0.0001

a = intervalo['a']; b = intervalo['b'] # variaveis para o intervalo
print(f'   I | Intervalo a | Intervalo b | Valor médio c |     f(c)   |')

# teorema de bolzano
if f(a)*f(b) < 0:
    while n < max_interacoes and abs((a - b)/2) > erro:
        c = ponto_medio(a, b)
        fc = f(c)
        # encontrado a raiz
        if fc == 0:
            print(f' {n} | {a} | {b} | {c} | {f(c)} |')
            result = c
            break
        n += 1

        # busca binária no intervalo
        if f(a)*fc < 0:
            b = c
        else:
            a = c

        print(f' {n:3d} | {a:11f} | {b:11f} | {c:13f} | {fc:10f} |')
    
    print(f'O valor da raiz é {c}')
else:
    print('Não há raízes no intervalo selecionado')