class Road:
    weight = 25
    thickness = 5

    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def mass_calculation(self):
        print(f"Масса асфальта: {self._width * self._lenght * self.weight * self.thickness} килограмм")


r = Road(25, 7500)
r.mass_calculation()
