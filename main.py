from arquivos.caminho_dos_arquivos import CaminhoDosArquivos

from questao_01.resposta_questao_01 import questao_um_retorno_soma

if __name__ == '__main__':
    tralha_para_ficar_bonito_no_console: str = '##########'

    print(f'Olá Mundo!')
    print(f'Para dar sorte.')

    print(f'\n{tralha_para_ficar_bonito_no_console}')
    print(f'Questão 01 - Soma')
    print(f'Nesta questão, foi passado um trecho de código, com o intuito de validar qual o resultado gerado, desta forma, efetuei a replicação em Python, para obter o resultado, e exibí-lo ao efetuar a invocação da função. Desta forma, '
          f'segue abaixo o resultado.')
    print(f'Resultao da soma: ', end='')
    questao_um_retorno_soma()
