# Cálculo mensal


def faturamento_das_distribuidoras(distribuidoras: dict):
    # keys: nomes dos estados
    # values: valores dos faturamentos nos estados

    faturamento_total: float = 0
    faturamento_por_distribuidora: dict() = {}

    for valor in distribuidoras.values():
        faturamento_total += valor

    for distribuidora, valor in distribuidoras.items():
        faturamento_por_distribuidora[distribuidora] = dict(faturamento=valor, percentual=round((valor / faturamento_total), 2))

    return faturamento_por_distribuidora, faturamento_total
