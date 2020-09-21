from itertools import count, cycle
my_list = []
new_list = []

for i in count(10):
    if i > 30:
        counter = 0
        for i in cycle(my_list):
            if counter > 300:
                print(f"Генерация списка чисел: {my_list}\n"
                      f"Повторения елементов предыдущего списка: {new_list}")
                break
            else:
                new_list.append(i)
                counter += 1
        break
    else:
        my_list.append(i)

