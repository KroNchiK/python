def exponent(arg1, arg2):
    """
    Возводит первый аргумент в степень, равную второму
    :param arg1: positive float number
    :param arg2: negative integer number
    :return: float number
    """
    temp_result = arg1
    for i in range(2, arg2+1):
        temp_result = temp_result * arg1

    print(f"Возведение числа x в степень y = {round(1 / temp_result, 4)}")

try:
    exponent(abs(float(input("Введите действительное положительное число x: "))),
             abs(int(input("Введите целое отрицательное число y: "))))
except ValueError:
    print("Вводить нужно только числа!!!")