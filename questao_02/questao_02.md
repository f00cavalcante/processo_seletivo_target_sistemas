# Questão 02

Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele
calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

## Resposta

Considerando o processo para trabalhar com a sequência Fibonacci, a qual consiste na soma sequencial de todos os valores unitários que possam compor determinado numeral a ser validado, efetuei a criação de uma função, a qual receberá o 
parâmetro correspondente a este número a ser iterado, conforme o laço de repetição avança, sendo assim, acrescido a lista criada.
A variável a receber a soma desta listagem trabalhará com os índices `-1` e `-2`, para garantir que sempre o último e penúltimo números sejam consultados para a soma.
O resultado foi o seguinte:

```python
def sequencia_fibonacci(numero_fibocacci: int):
    finocacci: list = [0, 1]  # inicialização da sequência Fibonacci

    for number in range(numero_fibocacci):
        continuacao_fibonacci = finocacci[-1] + finocacci[-2]   # neste processo, o índice -1 será a garantia que sempre será validado o último item da lista, que por sua vez, somará com o penúltimo número
        finocacci.append(continuacao_fibonacci)                 # após, a soma em questão, será adicionada à lista através do método append(), atualizando então o último índice da listagem, e garantindo a repetição da linha anterior
                                                                # com isto, existe a garanti que o laço será repetido até que toda a lista seja populada com a númeração Fibonacci a ser validada
    print(f'O resultado final: {continuacao_fibonacci}')

```

Com isto, temos:

- A primeira linha da função, responsável por inicializar a listagem do Fibonacci, afinal, toda soma passará pelos numerais o e 1;
- Após, inicia-se o laço de repetição pelo range numeral enviado no parâmetro da função;
- A primeira linha do laço, refere-se a soma do último índice pelo penúltimo;
- E por fim, este resultado é acrescido à listagem, até que seja concluído a condição do laço de repetição.