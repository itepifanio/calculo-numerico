"""
[[n     sumXi    ]] [a0] = [ sumYi   ]
[[sumXi sumXi**2 ]] [a1] = [ sumXiYi ]
"""

n = 0
somatorioXi = 0
quadradoDoSomatorioXi = 0
somatorioYi = 0
somatorioMultiplicacaoXiYi = 0

with open('pesos.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        try:
            xi, yi = line.strip().split(" ")
            somatorioXi += float(xi)
            somatorioYi += float(yi)
            quadradoDoSomatorioXi += float(xi)**2
            somatorioMultiplicacaoXiYi += float(xi) * float(yi)

            n += 1
        except:
            pass


print(f'n: {n}, Xi: {somatorioXi}, Yi: {somatorioYi}, Xi**2: {quadradoDoSomatorioXi}, XiYi: {somatorioMultiplicacaoXiYi}')
# n: 1000, Xi: 1747.3750539288005, Yi: 62833.24230949759, Xi**2: 3063.443559841964, XiYi: 110505.29703554006

"""
[[1000               1747.3750539288005]] [a0] = [ 62833.24230949759  ]
[[1747.3750539288005 3063.443559841964 ]] [a1] = [ 110505.29703554006 ]

Resolvendo esse sistema linear temos:

a0 = -60.0660831874695 and a1 = 70.3336843573680
"""
