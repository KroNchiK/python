from random import randint

with open("text_5.txt", "w+", encoding="utf-8") as ex_5:
    """Генерируем в файл набор псевдослучайных чисел"""
    ex_5.write(' '.join(str(el + randint(1, 100)) for el in range(10)))
    ex_5.seek(0)
    sum_of_el = 0
    """Считаем сумму чисел из файла"""
    for el in (ex_5.read()).split():
        sum_of_el += int(el)
    print("Сумма чисел в файле:", sum_of_el)