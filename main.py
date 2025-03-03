from arquivos.caminho_dos_arquivos import CaminhoDosArquivos

from questao_01.resposta_questao_01 import questao_um_retorno_soma
from questao_02.resposta_questao_02 import sequencia_fibonacci

if __name__ == '__main__':
    tralha_para_ficar_bonito_no_console: str = '##########'

    print(f'Olá Mundo!')
    print(f'Para dar sorte.')

    print(f'\n{tralha_para_ficar_bonito_no_console}')
    print(f'Questão 01 - Soma')
    print(
        f'Nesta questão, foi passado um trecho de código, com o intuito de validar qual o resultado gerado, desta forma, efetuei a replicação em Python, para obter o resultado, e exibí-lo ao efetuar a invocação da função. Desta forma, '
        f'segue abaixo o resultado.'
    )
    print(f'Resultao da soma: ', end='')
    questao_um_retorno_soma()

    print(f'\n{tralha_para_ficar_bonito_no_console}')
    print(f'Questão 02 - Sequência Fibonacci')
    print(
        f'Nesta questão, foi aplicado a lógica da sequência Fibonacci, a qual, resumidamente, consiste em efetuar a soma numérica de determinada sequência repetidas vezes até seu total numérico, isto é: \n'
        f'A sequência Fibonacci de 10 consiste em sua soma sequêncial de 0 até 10, pelos seus números que os compõem, ou seja: '
        f'0 + 1 + 2 [...] 10'
    )
    print(f'Assim sendo, criquei a função "sequencia_fibonacci", a qual receberá como parâmetro a sequência Fibonacci que deseja obter. Por ser um ponto apenas para validar a lógica de programação, irei inserir o numeral 10 fixamente ao '
          f'invocá-la.')
    print(f'Desta forma, conseguimos validar que o Fibonacci(10) possui [...] ', end='')
    sequencia_fibonacci(10)
