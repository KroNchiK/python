from googletrans import Translator

translator = Translator()
with open("text_4.txt", "r", encoding="utf-8") as ex_4:
    while True:
        line = ex_4.readline()
        if not line:
            break
        with open("text_4_ru.txt", "a", encoding="utf-8") as ex_ru_4:
            ex_ru_4.write((translator.translate(line, src='en', dest='ru')).text + "\n")
