<h1 align="center">Target Sistemas: Processo Seletivo Dev Jr</h1>

Esse projeto refere-se à aplicação para as vagas de Desenvolvedor Júnior junto a empresa Target Sistemas. Para seu desenvolvimento, optei pela criação básica de uma aplicação em Python, exibindo seus resultados diretamente no console, após sua execução. Alguns requisitos utilizados neste projeto:

- Versão Python: 3.12
- Biblioteca externa: XMLtodict
    - Para instalar esta bibliotecla, poderá executar no diretório o comando `pip install <nome_da_biblioteca>`

```bash
❯ pip install xmltodict --verbose
```

## Desenvolvimento

Durante o desenvolvimento do projeto, optei por demonstrar os conhecimento estruturais para a criação de um diretório para Python, e também, a estruturação de funções e classes, sendo o padrão para orientação objeto, onde:

- É criado a classe, e inserido atributos e métodos;
- Criado um objeto desta classe;
- A partir deste objeto, invocado seus métodos e acessado os atributos.

Os arquivos enviados para manipulação, os inseri no subdiretório `arquivos`, e neste, efetuei a criação de um ENUM contendo literais com seu Path, considerando-os desde a raiz, uma vez que as classes e método dos demais arquivos serão executadas no `main.py`.

## Questões

Abaixo, a descrição das questões, e o que busquei aplicar para as respostas.

### Questão 01

Observe o trecho de código abaixo:

```
int INDICE = 13, SOMA = 0, K = 0;  
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } Imprimir(SOMA);  
```

Ao final do processamento, qual será o valor da variável SOMA?

#### Resposta

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

Para maiores informações, acessar [questao_01/resposta_questao_01.py](questao_01/resposta_questao_01.py).

### Questão 02

Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#### Resposta

Considerando o processo para trabalhar com a sequência Fibonacci, a qual consiste na soma sequencial de todos os valores unitários que possam compor determinado numeral a ser validado, efetuei a criação de uma função, a qual receberá o  parâmetro correspondente a este número a ser iterado, conforme o laço de repetição avança, sendo assim, acrescido a lista criada. A variável a receber a soma desta listagem trabalhará com os índices `-1` e `-2`, para garantir que sempre o último e penúltimo números sejam consultados para a soma. O resultado foi o seguinte:

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

Para maiores informações, acessar [questao_02/resposta_questao_02.py](questao_02/resposta_questao_02.py).

### Questão 03

Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:

- O menor valor de faturamento ocorrido em um dia do mês;
- O maior valor de faturamento ocorrido em um dia do mês;
- Número de dias no mês em que o valor de faturamento diário foi superior à média mensal. 
 
IMPORTANTE:

a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; 
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média.

#### Resposta

No arquivo `resposta_questao_03.py` efetuei o processo de converter o conteúdo do JSON em um dicionário. As informações abaixo, manipulei pelo arquivo `faturamento_mensal.py`.

Para este processo, optei por trabalhar com um a classe contendo variáveis internas, neste caso, alguns atributos, para retornar as informações para os métodos internos, mas não privados, permitindo o acesso ao Main. <br>
Iterei um novo diconário local para a classe,  faclitando a manipulação das informações, e após, removi todos os dias com valores zerados, facilitando assim, o cálculo da média e soma dos valores. Para isto, implementei a seguinte lógica:

- Criei uma listagem com os valores das chaves com os dias zerados, que neste caso, corresponde ao próprio inteiro do dia, isto é, a chave do dia 1 seria o valor `1`
- Após, percorri a listagem com estes dias, e executei a exclusão dos índices no dicionário pelo nome da chave com o comando `del`, sendo a seguinte sintaxe: `del <nome_do_dicionario>[<nome_da_chave>]`
  
Quanto ao valor total do faturamento, somei no processo de conversão do dicionário, afinal, a soma zero não altera em nada, e para localizar a média, efetuei a divisão pelo length do dicionário convertido. Caso fosse necessário considerar todos os dias, incluindo os zerados, bastaria buscar o length do valor recebido ao instanciar o objeto no Main. Por fim, para facilitar o processo e acesso, criquei métodos para localizar o mair valor, menor valor, e médias.

Para maiores informações, acessar [questao_03/resposta_questao_03.py](questao_03/resposta_questao_03.py) e [questao_03/faturamento_mensal.py](questao_03/faturamento_mensal.py).

### Questão 04

Dado o valor do faturamento mensal numa distribuidora, detalhado por estado:  
- SP – R$67.836,43
- RJ – R$36.678,66
- MG – R$29.229,88
- ES – R$27.165,48
- Outros - R$19.849,53   

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 

#### Resposta

Ness caso, optei por trabalhar enviando um dicionário para uma função criada, a qual, efetuará o cálculo total de todas as distribuidoras, e após, dividir o valor individual de cada por este montande. Desta forma, será possível  obter o percentual de cada unidade.
Desta forma, efetuo o seguinte procedimento:

- Envio um dict para a função criada;
- Percorro um loop nos valores somando-os a uma variável destianda a ser o faturamento total;
- Percorro um segundo loop, onde, através da iteração com FoEach, efetuo a criação de um novo dict para armazenar o valor faturado, e seu percentual, que será calculado na divisão `faturamento individual / faturamento total`.˚

Para maiores informações, acessar [questao_04/resposta_questao_04.py](questao_04/resposta_questao_04.py).

### Questão 05

Escreva um programa que inverta os caracteres de uma string.
IMPORTANTE:  
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;  
b) Evite usar funções prontas, como, por exemplo, reverse;

#### Resposta
Nesse processo, optei por percorrer todos os índices da String, efetuando a sua iteração ao contário, isto é, buscando o último índice, e enviando-o ao primeiro lugar, iniciando então, através do valor `-1` para este acesso.

Para ficar bonito, resolvi criar uma classe contendo os métodos padrões de `GET` e `SET`, desta forma, é possível criar um objeto para realizar esta inversão.

Para maiores informações acessar [questao_05/resposta_questao_05.py](questao_05/resposta_questao_05.py).
