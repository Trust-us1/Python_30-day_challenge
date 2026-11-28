""" Scenario
Your pipeline tracks tables approved for today's warehouse load. Three new batch files arrive with their row counts stored as text. A batch should only be approved and added to approved_tables if it is a .csv file and contains more than 0 rows.

Input Data
Python
approved_tables = ["users", "orders"]

file_1 = "  PAYMENTS.CSV  "
rows_1 = "350"

file_2 = "  SHIPPING.PARQUET  "
rows_2 = "500"

file_3 = "  returns.csv  "
rows_3 = "0"
Goal
Create Daily_tasks/Day_4_Lists_Append.py in VS Code. Process the three incoming batches so that:

All approved filenames are cleaned (lowercase, no extra spaces) and added to approved_tables.

You track the total number of incoming rows that were approved.

Your script prints the updated list, the total count of tables in the list, and the total approved incoming rows.

Expected Output:
Approved tables: ['users', 'orders', 'payments.csv']
Total tables ready: 3
Total incoming rows approved: 350 """

approved_tables = ["users", "orders"]

file_1 = "  PAYMENTS.CSV  "
rows_1 = "350"

file_2 = "  SHIPPING.PARQUET  "
rows_2 = "500"

file_3 = "  returns.csv  "
rows_3 = "0"

total_approved_rows = 0

clean_1 = file_1.strip().lower()
if clean_1.endswith(".csv") and int(rows_1) > 0:
    approved_tables.append(clean_1)
    total_approved_rows += int(rows_1)

clean_2 = file_2.strip().lower()
if clean_2.endswith(".csv") and int(rows_2) > 0:
    approved_tables.append(clean_2)
    total_approved_rows += int(rows_2)

clean_3 = file_3.strip().lower()
if clean_3.endswith(".csv") and int(rows_3) > 0:
    approved_tables.append(clean_3)
    total_approved_rows += int(rows_3)

print(f"Approved tables: {approved_tables}")
print(f"Total tables ready: {len(approved_tables)}")
print(f"Total incoming rows approved: {total_approved_rows}")