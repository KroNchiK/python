def sum_of_larg(arg1, arg2, arg3):
    """
    Возвращает сумму наибольших двух аргументов
    :param arg1:number
    :param arg2:number
    :param arg3:number
    :return:number
    """
    my_list = [arg1, arg2, arg3]
    my_list.remove(min(my_list))
    print(f"Сумма наибольших двух параметров: {round(sum(my_list), 2)}")

try:
    sum_of_larg(float(input("Введите первое число: ")),
                float(input("Введите второе число: ")),
                float(input("Введите третье число: ")))
except ValueError:
    print("Вводить нужно только числа!!!")
