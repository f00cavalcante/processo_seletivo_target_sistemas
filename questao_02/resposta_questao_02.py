# Fibonacci

def sequencia_fibonacci(numero_fibocacci: int):
    finocacci: list = [0, 1]  # inicialização da sequência Fibonacci

    for number in range(numero_fibocacci):
        continuacao_fibonacci = finocacci[-1] + finocacci[-2]   # neste processo, o índice -1 será a garantia que sempre será validado o último item da lista, que por sua vez, somará com o penúltimo número
        finocacci.append(continuacao_fibonacci)                 # após, a soma em questão, será adicionada à lista através do método append(), atualizando então o último índice da listagem, e garantindo a repetição da linha anterior
                                                                # com isto, existe a garanti que o laço será repetido até que toda a lista seja populada com a númeração Fibonacci a ser validada
    print(f'O resultado final: {continuacao_fibonacci}')
