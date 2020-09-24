while True:
    with open("text_1.txt", "a", encoding="utf-8") as ex_1:
        text = input("Вводите текст по-строчно, "
                     "пустая строка - окончание ввода: ")
        if text == "":
            print("Создан файл", ex_1.name)
            break
        else:
            ex_1.write(text + "\n")



