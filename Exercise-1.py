def div_of_arg(dividend, divider):
    """
    Возвращает результат деления(частное) двух чисел
    :param dividend:number
    :param divider:number
    :return:quotient(number)
    """
    try:
        quotient = dividend / divider
        return quotient
    except ZeroDivisionError:
        print("Не пытайся делить на ноль, не ломай вселенную!!!")


try:
    print(f"Частное = {div_of_arg(float(input('Введите делимое: ')), float(input('Введите делитель: ')))}")
except ValueError:
    print("Вводить нужно только числа!!!")
