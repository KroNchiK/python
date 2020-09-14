my_list = []
numbers = int(input("Введите колличество элементов в списке: "))
for i in range(0, numbers):
    el = input(f"Введите {i}-й элемент списка: ")
    if el.isdigit():
        my_list.append(int(el))
    else:
        my_list.append(el)

tmp_list = my_list[::2]
if (len(tmp_list) % 2) > 0:
    tmp_list.pop(-1)
for tmp_el in tmp_list:
    ind = my_list.index(tmp_el)
    my_list.remove(tmp_el)
    my_list.insert(ind+1, tmp_el)

print("Новый список с переставленными элементами: ", my_list)
