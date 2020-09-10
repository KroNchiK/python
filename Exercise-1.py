print("Enter two values and type of arithmetic expression")
a = int(input("Enter value 1: "))
b = int(input("Enter value 2: "))
exp = input("Enter expression(sum, diff, multipli, div): ")
if exp == "sum":
    result = a + b
elif exp == "diff":
    result = a - b
elif exp == "multipli":
    result = a * b
elif exp == "div":
    result = a / b
else:
    print("WTF?!")
print(f"The result of {exp} {a} and {b} is {result}")