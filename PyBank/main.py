import os
import csv
from statistics import mean

budget_data = os.path.join("Resources", "budget_data.csv")

with open(budget_data, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    total_months = 0
    net_total = 0
    prev_profit = 0
    changes = []
    greatest_increase = {"date": "", "amount": 0}
    greatest_decrease = {"date": "", "amount": 0}
    average_change = 0.0

    for row in csv_reader:
        date = row[0]
        profit = int(row[1])

        total_months = total_months + 1
        net_total = net_total + profit

        change = profit - prev_profit
        if prev_profit > 0:
            changes.append(change)
        prev_profit = profit

        if change > greatest_increase["amount"]:
            greatest_increase["date"] = date
            greatest_increase["amount"] = change

        if change < greatest_decrease["amount"]:
            greatest_decrease["date"] = date
            greatest_decrease["amount"] = change
        
    average_change = mean(changes)

    financial_results = 'Analysis/budget_results.txt'

    with open (financial_results, 'w') as output:
        print("Financial Analysis")
        print("")
        print("------------------")
        print("")
        print(f"Total Months: {total_months}")
        print(f"Total: ${net_total}")
        print(f"Average Change: ${average_change:.2f}")
        print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
        print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

        output.write("Financial Analysis\n")
        output.write("\n")
        output.write("------------------")
        output.write("\n")
        output.write(f"Total Months: {total_months}\n")
        output.write(f"Total: ${net_total}\n")
        output.write(f"Average Change: ${average_change:.2f}\n")
        output.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
        output.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

