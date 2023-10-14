def recursivo2(valor, inicio=(0, 1)):
    if len(inicio) == valor:
        return inicio
    return recursivo2(valor, inicio + (sum(inicio[-2:]),))


def recursivo3(valor1, inicio1=(0, 1)):
    return inicio1 if len(inicio1) == valor1 else \
        recursivo3(valor1, inicio1 + (sum(inicio1[-2:]),))


if __name__ == '__main__':
    for R1 in recursivo3(15):
        print(R1)
    for R in recursivo2(15):
        print(R)
