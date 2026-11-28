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

incoming_1 = "  PAYMENTS  "
incoming_2 = ""
incoming_3 = "  Shipping_Logs"

incoming_1_clean = incoming_1.strip().lower()
incoming_3_clean = incoming_3.strip().lower()
approved_tables.append(incoming_1_clean)
approved_tables.append(incoming_3_clean)
print(approved_tables)
print(f"Total tables ready:{len(approved_tables)}")

