init = int(input("Enter the initial number of kilometers: "))
target = int(input("Enter the target number of kilometers: "))
days = 1
while init < target:
    init = init * 1.1
    days += 1
print("Day number: ", days)
