# Questão 04

Dado o valor do faturamento mensal numa distribuidora, detalhado por estado:  
- SP – R$67.836,43
- RJ – R$36.678,66
- MG – R$29.229,88
- ES – R$27.165,48
- Outros - R$19.849,53   

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 

## Resposta

Ness caso, optei por trabalhar enviando um dicionário para uma função criada, a qual, efetuará o cálculo total de todas as distribuidoras, e após, dividir o valor individual de cada por este montande. Desta forma, será possível 
obter o percentual de cada unidade.
Desta forma, efetuo o seguinte procedimento:

- Envio um dict para a função criada;
- Percorro um loop nos valores somando-os a uma variável destianda a ser o faturamento total;
- Percorro um segundo loop, onde, através da iteração com FoEach, efetuo a criação de um novo dict para armazenar o valor faturado, e seu percentual, que será calculado na divisão `faturamento individual / faturamento total`.˚