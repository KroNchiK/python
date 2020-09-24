with open("text_3.txt", "r", encoding="utf-8") as ex_3:
    count = 0
    avg = 0
    print("Сотрудники с окладом меньше 20 тыс:")
    while True:
        line = (ex_3.readline().split())
        if not line:
            print(f"Средняя велечина дохода сотрудников: {avg/count}")
            break
        if float(line[1]) < 20000:
            print(line[0])
        avg += float(line[1])
        count += 1



