import csv
import os
from datetime import datetime


file_path = os.path.join("..", "data", "expenses.csv")

if not os.path.exists(file_path):
    print("Error: expenses.csv not found.")
    raise SystemExit(1)


expenses = []

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["amount"] = float(row["amount"])
        expenses.append(row)


food_expenses = [
    expense for expense in expenses
    if expense["category"] == "Food"
]


total = sum(expense["amount"] for expense in food_expenses)


today = datetime.now().strftime("%B %d, %Y")


with open("food_report.txt", "w", encoding="utf-8") as file:

    file.write(f"Food Expense Report — generated {today}\n")

    for expense in food_expenses:
        file.write(
            f"{expense['date']}: ${expense['amount']:.2f}\n"
        )

    file.write(f"Total: ${total:.2f}\n")


print("Food expense report generated successfully.")