class InverterStrings:

    def __init__(self, palavra: str):
        self._palavra: str = palavra

    def inverter_a_string(self):
        palavra_invertida: str = ''
        for p in range(len(self._palavra)):
            palavra_invertida += self._palavra[- (p + 1)]

        return palavra_invertida

    @property
    def palavra(self):
        return self._palavra

    @palavra.setter
    def palavra(self, palavra: str):
        self._palavra = palavra
