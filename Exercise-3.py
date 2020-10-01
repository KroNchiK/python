class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    @property
    def income(self):
        return self._income


class Position(Worker):
    def get_full_name(self):
        print(f"Full Name: {self.name} {self.surname}")

    def get_total_income(self):
        print("Total income: ", self._income["wage"]+self._income["bonus"])


p = Position("Alex", "Kronov", "DE", 130000, 200000)
print(f"Name: {p.name}, Surname: {p.surname}, Position: {p.position}, Income: {p.income}")
p.get_full_name()
p.get_total_income()
