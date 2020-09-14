my_list = [1, 1.5, "str", 5 + 6j, ["a", "b", "c"], ("one", "two", "three"),
           {0, 6, 5}, {"key": "value", "key2": "value2"}, False]
for i in my_list:
    print(f"Элемент {i} имеет тип {type(i)}")
