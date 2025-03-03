# int INDICE = 13, SOMA = 0, K = 0;  
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } Imprimir(SOMA);  


def questao_um_retorno_soma():
    indice: int = 13
    soma: int = 0
    k: int = 0

    while k < indice:
        k += 1              # incremento em Python, que possui o mesmo resultado k = k + 1
        soma = soma + k     # após o processo de incremento, a soma sempre receberá a adição ao seu novo valor

    print(soma)             # ao final, será exibido o resultado
