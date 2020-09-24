"""
Считает колличество строк и слов в текстовом файле из первой задачи
"""
with open("text_1.txt", "r", encoding="utf-8") as ex_2:
    lines = 0
    while True:
        words = len(ex_2.readline().split())
        lines += 1
        print(f"Колличество слов в {lines}-й строке: {words}")

        if not words:
            print(f"Всего строк: {lines}")
            break