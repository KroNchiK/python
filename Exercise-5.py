total = 0
while True:
    subtotal = []
    values = input("Введите строку чисел, разделённых пробелом,"
                   " или q для выхода из программы: ")
    values = values.split()
    for i in values:
        if i == "q":
            quite = True
            break
        else:
            quite = None
            try:
                subtotal.append(int(i))
            except ValueError:
                print("Необходимо вводить только числа!!!")
    subtotal = sum(subtotal)
    total = total + subtotal
    if quite == True:
        print(f"Общая сумма: {total}")
        break
    else:
        print(f"Промежуточная сумма: {subtotal}, общая сумма: {total}")