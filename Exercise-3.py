month = int(input("Enter number of month: "))
if month <= 0 or month > 12:
    month = int(input(f"The {month} is not correct, "
                      f"the value must be between 1-12. "
                      f"Enter number of month: "))

seasons = {
    12: ["Dec", "Winter"], 1: ["Jan", "Winter"], 2: ["Feb", "Winter"],
    3: ["Mar", "Spring"], 4: ["Apr", "Spring"], 5: ["May", "Spring"],
    6: ["Jun", "Summer"], 7: ["Jul", "Summer"], 8: ["Aug", "Summer"],
    9: ["Sep", "Autumn"], 10: ["Oct", "Autumn"], 11: ["Now", "Autumn"]
}

print(f"Season: {seasons.get(month)[1]} \n"
      f"Month: {seasons.get(month)[0]}")