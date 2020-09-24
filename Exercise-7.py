import json

with open("text_7.txt", "r", encoding="utf-8") as ex_7:
    sum_profit = 0
    company_profit = 0
    companies = {}
    while True:
        line = ex_7.readline().split()
        if not line:
            break
        profit = int(line[2]) - int(line[3])
        if profit >= 0:
            sum_profit += profit
            company_profit += 1
        companies[line[0]] = profit
    average_profit = {"average_profit": sum_profit / company_profit}
    to_json = [companies, average_profit]
    with open("text_77.json", "w", encoding="utf-8") as ex_7_json:
        json.dump(to_json, ex_7_json, ensure_ascii=False, indent=1)
