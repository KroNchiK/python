from sys import argv
try:
    file, time, rate, bonus = argv
    pay = int(time) * int(rate) + int(bonus)
    print(pay)
except ValueError:
    print("Необходимо ввести три числовых параметра!")
