from time import sleep


class TrafficLight:
    __color = None

    def running(self, color):
        self.__color = color
        print(self.__color)


tl = TrafficLight()
colors = ["red", "yellow", "green", "yellow"]

while True:
    for i in colors:
        if i == "red":
            tl.running("\033[31m" + i)
            sleep(7)
        if i == "green":
            tl.running("\033[32m" + i)
            sleep(5)
        if i == "yellow":
            tl.running("\033[33m" + i)
            sleep(2)
