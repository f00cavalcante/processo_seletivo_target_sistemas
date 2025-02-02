# Questão 01
Observe o trecho de código abaixo: 
```
int INDICE = 13, SOMA = 0, K = 0;  
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } Imprimir(SOMA);  
```

Ao final do processamento, qual será o valor da variável SOMA?

Para este processo, repliquei o trecho na criação de um script em Python. O resultado foi 91.
```python
indice: int = 13
soma: int = 0
k: int = 0

while k < indice:

     k = k + 1
     soma = soma + k

print(soma)
```