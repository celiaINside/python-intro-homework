import os
import csv

print(os.getcwd())
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("Error: expenses.csv not found.")
    exit()

with open('../data/expenses.csv', 'r') as file:
    rows = list(csv.DictReader(file))
    for row in rows:
        row["amount"] = float(row["amount"])
    food = [item for item in rows if item['category'] == 'Food']
    for item in food:
        item['amount'] = (item['amount'])

total_value = sum(item['amount'] for item in food)

from datetime import datetime
now = datetime.now()
with open('food_report.txt', 'w') as file:
    file.write(f"Food Expense Report — generated {now.strftime('%B %d, %Y')}\n")
    for item in food:
        file.write(f"{item['date']}: ${item['amount']:.2f}\n")
    file.write(f"Total: ${total_value:.2f}")