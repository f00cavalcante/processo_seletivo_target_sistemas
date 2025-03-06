import locale

locale.setlocale(locale.LC_ALL, locale='pt_BR')


class FaturamentoMensal:
    dados_do_faturamento: dict() = {}
    total_faturamento: float = 0
    dias_com_valores_zerados: list = []

    def __init__(self, faturamento):
        self._faturamento = faturamento

    def _converter_dicionario(self):

        for dados in self._faturamento:
            self.dados_do_faturamento.update({dados.get('dia'): dados.get('valor')})
            self.total_faturamento += dados.get('valor')

            if dados.get('valor') == 0: self.dias_com_valores_zerados.append(dados.get('dia'))

        for dia in self.dias_com_valores_zerados:
            del self.dados_do_faturamento[dia]

    def _maior_faturamento(self):

        maior_dia: int = 0
        maior_valor: float = self.dados_do_faturamento.get(30)

        for dia, valor in self.dados_do_faturamento.items():

            if maior_valor < valor:
                maior_dia = dia
                maior_valor = valor

        print(f'O dia com maior faturamento foi {maior_dia}, com o valor de R$ {locale.currency(val=maior_valor, grouping=True, symbol=False)}.')

    def _menor_faturamento(self):

        menor_dia: int = 0
        menor_valor: float = self.dados_do_faturamento.get(30)

        for dia, valor in self.dados_do_faturamento.items():

            if menor_valor > valor:
                menor_dia = dia
                menor_valor = valor

        print(f'O dia com menor faturamento foi {menor_dia}, com o valor de R$ {locale.currency(val=menor_valor, grouping=True, symbol=False)}.')

    def _media_faturamento(self):

        quantidade_de_dias_que_foram_maiores_que_a_media_mensal: int = 0

        valor_da_media_mensal = self.total_faturamento / len(self.dados_do_faturamento)

        print(f'{"":10}Valor da média mensal: R$ {locale.currency(val=valor_da_media_mensal, grouping=True, symbol=False)}.')

        for dia, valor in self.dados_do_faturamento.items():

            if valor > valor_da_media_mensal:
                quantidade_de_dias_que_foram_maiores_que_a_media_mensal += 1
                print(f'{"":10}Dia: {dia} | Valor: R$ {locale.currency(val=valor, grouping=True, symbol=False)}')

        print(f'{"":10}Com isto, ocorreram {quantidade_de_dias_que_foram_maiores_que_a_media_mensal} dias em que os valores do faturamento foram maior que a média mensal.')
