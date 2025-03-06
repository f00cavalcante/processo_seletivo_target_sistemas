from arquivos.caminho_dos_arquivos import CaminhoDosArquivos

from questao_01.resposta_questao_01 import questao_um_retorno_soma
from questao_02.resposta_questao_02 import sequencia_fibonacci
from questao_03.resposta_questao_03 import ArquivoJSON
from questao_03.resposta_questao_03 import ArquivoXML
from questao_04.resposta_questao_04 import faturamento_das_distribuidoras
from questao_05.resposta_questao_05 import InverterStrings

if __name__ == '__main__':
    tralha_para_ficar_bonito_no_console: str = '##########'

    print(f'Olá Mundo!')
    print(f'Para dar sorte.')

    print(f'\n{tralha_para_ficar_bonito_no_console}')
    print(f'Questão 01 - Soma')
    print(
        f'Nessa questão, foi passado um trecho de código, com o intuito de validar qual o resultado gerado, desta forma, efetuei a replicação em Python, para obter o resultado, e exibí-lo ao efetuar a invocação da função. Desta forma, '
        f'segue abaixo o resultado.'
    )
    print(f'Resultao da soma: ', end='')
    questao_um_retorno_soma()

    print(f'\n{tralha_para_ficar_bonito_no_console}')
    print(f'Questão 02 - Sequência Fibonacci')
    print(
        f'Nessa questão, foi aplicado a lógica da sequência Fibonacci, a qual, resumidamente, consiste em efetuar a soma numérica de determinada sequência repetidas vezes até seu total numérico, isto é: \n'
        f'A sequência Fibonacci de 10 consiste em sua soma sequêncial de 0 até 10, pelos seus números que os compõem, ou seja: '
        f'0 + 1 + 2 [...] 10'
    )
    print(f'Assim sendo, criquei a função "sequencia_fibonacci", a qual receberá como parâmetro a sequência Fibonacci que deseja obter. Por ser um ponto apenas para validar a lógica de programação, irei inserir o numeral 10 fixamente ao '
          f'invocá-la.')
    print(f'Desta forma, conseguimos validar que o Fibonacci(10) possui [...] ', end='')
    sequencia_fibonacci(10)

    print(f'\n{tralha_para_ficar_bonito_no_console}')
    print(f'Questão 03 - Manipular arquivos')

    arquivo_json = ArquivoJSON()
    setattr(arquivo_json, 'caminho_json', CaminhoDosArquivos.ARQUIVO_JSON.value)

    arquivo_xml = ArquivoXML()
    setattr(arquivo_xml, 'caminho_xml', CaminhoDosArquivos.ARQUIVO_XML.value)

    print(f'\n{tralha_para_ficar_bonito_no_console}')
    print(f'Questão 04 - Percentual de Faturamento')
    print(f'Nessa questão, foi proposto um diconário, contendo valores dos faturamentos de distribuidoras com base em cada estado da região suldeste, e solicitou a apuração do percentual de faturamento com base na soma de todas as '
          f'distribuidoras.')
    print(f'Desta forma, efetuei a iteração neste direcionário, somando seus valores em uma variável separada, e após, dividi seus valores inviduais pelo seu total. Com isto, é possível obter o seguinte:')
    faturamento_das_distribuidoras = faturamento_das_distribuidoras(
        dict(
            SP=67836.43,
            RJ=36678.66,
            MG=29229.88,
            ES=27165.48,
            Outros=19849.53
        ))
    print(f'{"":5}O valor total do faturamento de todos os estados é: {faturamento_das_distribuidoras[1]}')
    print(f'{"":5}O percentual individual de cada distribuidora, poderá ser conferiro a seguir:')
    for (distribuidora, valores) in faturamento_das_distribuidoras[0].items(): print(f'{"":10}{distribuidora}: Faturamento = {valores.get("faturamento")} | Percentual = {100 * valores.get("percentual")}%')

    print(f'\n{tralha_para_ficar_bonito_no_console}')
    print(f'Questão 05 - Inverter a String')
    print(f'Para efetuar o processo de interver determinada String, optei pelo processo de criar uma classe para inserir valores a serem destinados ao atributo "palavra", e após, pelos métodos GET e SET será possível oter estes retornos.')

    texto_para_ser_convertido: str = 'texto_para_ser_convertido'

    converter_stirng = InverterStrings(texto_para_ser_convertido)

    print(f'Palavra original: "{converter_stirng.palavra}"')
    print(f'Palavra convertida: "{converter_stirng.inverter_a_string()}"\n')

    converter_stirng.palavra = 'Uma nova String para ser convertida totalmente diferente da anterior e super extensa para sabermos se este processo irá funcionar.'
    print(f'Palavra original: "{converter_stirng.palavra}"')
    print(f'Palavra convertida: "{converter_stirng.inverter_a_string()}"')

    print(f'\n{tralha_para_ficar_bonito_no_console}')
    print(f'E com isto, chega-se ao final do teste prático. Obrigado. E lhe desejo uma vida longa e próspera. 🖖🏻')