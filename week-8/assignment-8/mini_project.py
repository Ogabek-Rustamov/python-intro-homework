import csv

a = [
    {"name": "Alice", "category": "Food", "amount": "12.50"},
    {"name": "Bob", "category": "Transport", "amount": "8.75"},
    {"name": "Carol", "category": "Food", "amount": ""},
    {"name": "David", "category": "Utilities", "amount": "45.00"},
    {"name": "Eve", "category": "Food", "amount": "not_a_number"},
    {"name": "Frank", "category": "Transport", "amount": "22.30"},
    {"name": "Grace", "category": "Food", "amount": "15.00", None: ["extra_field"]},
    {"name": "Hana", "category": "Utilities", "amount": "88.00"},
    {"name": "Ivan", "category": "Food", "amount": "6.40"},
    {"name": "Jess", "category": "Transport", "amount": "14.20"},
    {"name": "Karl", "category": "Utilities", "amount": ""},
    {"name": "Lena", "category": "Food", "amount": "9.80"},
    {"name": "Marco", "category": "Transport", "amount": "fifteen"},
    {"name": "Nina", "category": "Utilities", "amount": "33.60"},
]


clean_data = []
skipped_rows = []
rows_attempted = 0

try:
    with open("../data/messy_data.csv", "r") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=1):
            rows_attempted += 1

            try:
                if None in row:
                    skipped_rows.append(f"Row {row_number}: extra column detected — skipped")
                    continue

                name = row["name"]
                category = row["category"]
                amount = row["amount"]

                if not name or not category or not amount:
                    raise ValueError(f"could not convert '{amount}' to float")

                amount = float(amount)

                clean_data.append({"name": name, "category": category, "amount": amount})

            except ValueError as error:
                skipped_rows.append(f"Row {row_number}: ValueError — {error}")

            except KeyError as error:
                skipped_rows.append(f"Row {row_number}: KeyError — missing column {error}")

            except TypeError as error:
                skipped_rows.append(f"Row {row_number}: TypeError — {error}")

except FileNotFoundError:
    print("Error: messy_data.csv was not found. Check the file path.")

else:
    print("=== CSV Report ===")
    print(f"Rows attempted:  {rows_attempted}")
    print(f"Rows parsed:    {len(clean_data)}")
    print(f"Rows skipped:   {len(skipped_rows)}")

    print("\nSkipped rows:")
    for skipped in skipped_rows:
        print(f"{skipped}")

    print("\nClean data:")
    for row in clean_data:
        print(f"  {row['name']} | {row['category']} | " f"${row['amount']:.2f}")
