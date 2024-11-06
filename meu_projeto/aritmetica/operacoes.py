def soma(a, b):
    return a + b


def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f"o resultado não é encontrado")

    if b != 0:
        return a / b
    else:
        return '0'
    