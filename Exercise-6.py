products = []
analytics = {"название": [], "цена": [], "количество":[], "ед":[]}
numbers = int(input("Введите колличество товра: "))
for i in range(1, numbers+1):

    name = input(f"Введите название {i}-го товара: ")
    price = float(input(f"Введите цену {i}-го товара: "))
    count = int(input(f"Введите колличество {i}-го товара: "))
    unit = input(f"Введите единицу измерения {i}-го товара: ")
    my_dict = {"Название": name, "Цена": price, "Колличесвто": count, "Единица измерения": unit}
    products.append((i, my_dict))

    analytics["название"].append(name)
    analytics["цена"].append(price)
    analytics["количество"].append(count)
    analytics["ед"].append(unit)

print(f"Товары в базе: {products} \n"
      f"Аналитика: {analytics}")