with open("text_6.txt", "r", encoding="utf-8") as ex_6:
    time_digit = {}
    while True:
        time_list = []
        line = ex_6.readline().split()
        if not line:
            break
        for i in line:
            digit = ''
            for el in i:
                if el.isdigit():
                    digit += el
            if digit != '':
                time_list.append(int(digit))
        time_digit[line[0][:-1]] = sum(time_list)
    print(time_digit)





    # print(line[2])
    # my_list = []
    # for el in line[2]:
    #     my_list.append(el)
    # print(my_list)
    # # my_dict = {line[0]: my_list.append(el) for el in line[2]}
    # # print(my_dict)
    # # print(line)
    # # l = ''
    # # for i in line[2]:
    # #     if i.isdigit():
    # #         l += i
    # #         print(l)
    # # my_dict = {}
