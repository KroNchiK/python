seconds = int(input("Enter the number of seconds: "))
print(f"{seconds // 3600:02.0f}:{seconds % 3600 // 60:02.0f}:{seconds % 3600 % 60:02.0f}")
