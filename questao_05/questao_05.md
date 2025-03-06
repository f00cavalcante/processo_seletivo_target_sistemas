# Questão 05
Escreva um programa que inverta os caracteres de uma string.
IMPORTANTE:  
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;  
b) Evite usar funções prontas, como, por exemplo, reverse;

## Resposta
Nesse processo, optei por percorrer todos os índices da String, efetuando a sua iteração ao contário, isto é, buscando o último índice, e enviando-o ao primeiro lugar, iniciando então, através do valor `-1` para este acesso.

Para ficar bonito, resolvi criar uma classe contendo os métodos padrões de `GET` e `SET`, desta forma, é possível criar um objeto para realizar esta inversão.