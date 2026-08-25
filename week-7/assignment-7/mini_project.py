import os

print(os.getcwd())
if os.path.exists("../data/expenses.csv"):
        print("expenses.csv found.")
else:
    print("An error has ocurred.")

import csv 

with open('../data/expenses.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        amount = float(row['amount'])
        print(row)

with open('../data/expenses.csv', 'r') as file:
    rows = list(csv.DictReader(file))
    food = [item for item in rows if item['category'] == 'Food']
    for item in food:
        item['amount'] = float(item['amount'])
    print(food)

total_value = sum(item['amount'] for item in food)
print(f"Food expenses sum: ${total_value:.2f}")

from datetime import datetime
now = datetime.now()
with open('food_report.txt', 'w') as file:
    file.write(f"Food Expense Report - generated {now.strftime('%B %d, %Y')}.\n")
    for item in food:
        file.write(f"{item['date']}: ${item['amount']:.2f}\n")
    file.write(f"Total: ${total_value:.2f}")