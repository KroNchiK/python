my_str = input("Введите строку из нескольких слов, разделённую пробелами: ")
my_list = my_str.split()
for ind, el in enumerate(my_list):
    if len(el) > 10:
        print(ind, el[0:10])
    else:
        print(ind, el)