class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Пишем ручкой {self.title}")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Чертим карандашём {self.title}")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Закрашиваем маркером {self.title}")

stationery = Stationery("наших слов")
stationery.draw()

pen = Pen("первое слово")
pen.draw()

pencil = Pencil("второе слово")
pencil.draw()

handle = Handle("третье слово")
handle.draw()
