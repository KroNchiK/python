def fact(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
        yield result


for el in fact(int(input("Введите число, фактариал которого вы хотите получить: "))):
    print(el)
