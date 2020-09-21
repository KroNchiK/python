from functools import reduce


def multiplic(el_1, el_2):
    return el_1 * el_2


print(f"Произведение всех элементов: {reduce(multiplic, [el for el in range(100, 1001) if el % 2 == 0])}")
