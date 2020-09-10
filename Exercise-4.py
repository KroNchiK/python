number = int(input("Enter positive integer: "))
larg_num = 0
while number > 0:
    i = number % 10
    if i > larg_num:
        larg_num = i
    number = number // 10
print("The largest number is ", larg_num)


