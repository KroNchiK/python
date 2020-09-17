def int_func(word):
    word = word.title()
    return word


text = input("Введите слова латиницей и в нижнем регистре: ")
for i in text:
    if ord(i) != 32 and (ord(i) > 122 or ord(i) < 97) or i.isupper() == True:
        out = True
        break
    else:
        out = False
        continue

if out == True:
    print("Кажется, вы ввели слова не латиницей или в верхнем регистре :)")
else:
    print(f"int_func(text)")