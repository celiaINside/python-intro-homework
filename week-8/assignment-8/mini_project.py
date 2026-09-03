import os
import csv

try:
   with open("../data/messy_data.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
except FileNotFoundError:
    print('Error: "messy_data.csv" was not found. Please check the file path.')

else: 
    skipped_rows = []
    clean_rows = []
    for row_number, row in enumerate(rows, start = 1):
        if None in row:
            none_message = f"  Row {row_number}: extra column detected — skipped"
            skipped_rows.append(none_message)
            continue

        try:
            entry = {
                "name": row["name"],
                "category": row["category"],
                "amount": float(row["amount"])
            }

            clean_rows.append(entry)
        except ValueError: 
            value_error_message = f"  Row {row_number}: ValueError — could not convert '{row['amount']}' to float"
            skipped_rows.append(value_error_message)
        except KeyError as e:
            key_error_message = f"  Row {row_number}: KeyError - could not find key {e}"
            skipped_rows.append(key_error_message)

    skipped_total = len(skipped_rows)
    attempted = len(rows)
    parsed = len(clean_rows)

    print("=== CSV Report ===")
    print(f"Rows attempted: {attempted}")
    print(f"Rows parsed: {parsed}")
    print(f"Rows skipped: {skipped_total}")
    print()
    print("Skipped rows:")
    for row in skipped_rows: 
        print(f"{row}")
    print()
    print(f"Clean data:")
    for row in clean_rows:
        name = row['name']
        category = row['category']
        amount = row['amount']
        print(f"  {name} | {category} | ${amount:.2f}")