import os

# Current working directory
print("Current working directory:")
print(os.getcwd())

# Does file exists
file_path = os.path.join("..", "data", "expenses.csv")

if os.path.exists(file_path):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

print("File path:", file_path)