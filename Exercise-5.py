my_list = [7, 5, 3, 3, 2]
while True:
    el = input(f"Текущий рейтинг {my_list} \n"
               f"Введите новый элемент рейтинга, чтобы выйти ввидите quite: ")
    if el == "quite":
        break
    elif int(el) < my_list[-1]:
        my_list.append(int(el))
    else:
        for i in my_list:
            if int(el) > i:
                my_list.insert(my_list.index(i), int(el))
                break
