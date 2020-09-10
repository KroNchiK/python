proceeds = int(input("Введите размер выручки: "))
costs = int(input("Введите размер издержек: "))
if proceeds > costs:
    print(f"Прибыль фирмы: {proceeds - costs}")
    print(f"Рентабельность выручки: {(proceeds - costs) / proceeds:.2f}")
    staff = int(input("Введите колличество сотрудников: "))
    print(f"Прибыль фирмы в расчёте на одного сотрудника: {(proceeds - costs) / staff:.2f}")
elif proceeds == costs:
    print("Фирма работает в ноль")
else:
    print(f"Убыток фирмы: {costs - proceeds}")