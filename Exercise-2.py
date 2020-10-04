from abc import ABC, abstractmethod


class Clothing(ABC):
    @abstractmethod
    def amount_of_fabric(self):
        pass


class Coat(Clothing):
    def __init__(self, v):
        self.v = v

    @property
    def amount_of_fabric(self):
        return f"Расход ткани на польто: {round(self.v / 6.5 + 0.5, 2)}"


class Suit(Clothing):
    def __init__(self, h):
        self.h = h

    @property
    def amount_of_fabric(self):
        return f"Расход ткани на костюм: {round(2 * self.h + 0.3, 2)}"


coat = Coat(45)
print(coat.amount_of_fabric)

suit = Suit(189)
print(suit.amount_of_fabric)