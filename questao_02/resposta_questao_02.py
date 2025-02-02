# Fibonacci

sequencia_fibonacci = int(input('Informe o número de sequências Fibonacci que deseja calcular: '))

finocacci: list = [0, 1]


for number in range(sequencia_fibonacci):

     continuacao_fibonacci = finocacci[-1] + finocacci[-2]
     finocacci.append(continuacao_fibonacci)

print(f'O resultado final: {continuacao_fibonacci}')