from random import randint
my_list = [el+randint(0, 100) for el in range(10)]
print(f"Исходный список: {my_list}")
print(f"Новый список: {[my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]}")
