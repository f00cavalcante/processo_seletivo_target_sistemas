# Cálculo mensal

faturamento_mensal_estados = dict(espirito_santo = 27165.48, minas_gerais = 29229.88, sao_paulo = 67836.43, rio_de_janeiro = 36678.66, outros = 19849.53)

faturamento_total = 0

for f in faturamento_mensal_estados.values():

     faturamento_total += f

print('Percentual de faturamento de cada estado pelo total: \n')

for estado in faturamento_mensal_estados:

     print(f'{estado}: {round((faturamento_mensal_estados[estado] / faturamento_total) * 100)}% - VALORES ARREDONDADOS')