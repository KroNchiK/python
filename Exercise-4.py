class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print("Погнали!!!")

    def stop(self):
        print("Всё приехали...")

    def turn(self, direction):
        print(f"Поварачивай на {direction}")

    def show_speed(self):
        print(f"Гоним со сокростью: {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Ты гонишь со сокростью - {self.speed} км/ч, привышаешь на {self.speed - 60} км/ч!!!")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Ты гонишь со сокростью - {self.speed} км/ч, привышаешь на {self.speed - 40} км/ч!!!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town = TownCar(90, "green", "KIA Rio", None)
work = WorkCar(60, "yellow", "Ford Transit", None)
police = PoliceCar(90, "white/black", "Ford Police Interceptor", True)
sport = SportCar(150, "red", "Porsche 911", False)

print(f"Городской автомобиль: {town.name}, цвет: {town.color}, Это копы: {town.is_police}")
town.go()
town.turn("лево")
town.turn("право")
town.show_speed()
town.stop()

print()

print(f"Рабочий автомобиль: {work.name}, цвет: {work.color}, Это копы: {work.is_police}")
work.go()
work.turn("лево")
work.turn("лево ещё раз")
work.turn("право")
work.show_speed()
work.stop()

print()

print(f"Полицейский автомобиль: {police.name}, цвет: {police.color}, Это копы: {police.is_police}")
police.go()
police.turn("тратуар")
police.turn("право")
police.turn("газон")
police.show_speed()
police.stop()

print()

print(f"Спортивный автомобиль: {sport.name}, цвет: {sport.color}, Это копы: {sport.is_police}")
sport.go()
sport.show_speed()
sport.stop()




