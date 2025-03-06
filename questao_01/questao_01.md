# Questão 01

Observe o trecho de código abaixo:

```
int INDICE = 13, SOMA = 0, K = 0;  
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } Imprimir(SOMA);  
```

Ao final do processamento, qual será o valor da variável SOMA?

## Resposta

Para este processo, repliquei o trecho na criação de um script em Python. O resultado foi `91`. Sendo assim, a única alteração que realizei ocorreu durante a declaração do incremento para a variável `k`, onde repliquei a lócia em Python 
`k += 1`. <br>
Ocorre que, a cada nova iteração do loop, o valor de `k` será aumentado, e este, adicionado ao valor da variável `soma`, até que o valor de `k` seja maior que o índice.

```python
def questao_um_retorno_soma():
    indice: int = 13
    soma: int = 0
    k: int = 0

    while k < indice:
        k += 1              # incremento em Python, que possui o mesmo resultado k = k + 1
        soma = soma + k     # após o processo de incremento, a soma sempre receberá a adição ao seu novo valor

    print(soma)             # ao final, será exibido o resultado
```