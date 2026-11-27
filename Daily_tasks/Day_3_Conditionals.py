""" file_name = "sales_2026.csv"

if file_name.endswith(".csv"):
    print("Supported file format.")
else:
    print("Unsupported file format.")
2. Bite-Sized DE Coding Task: Batch Quality Gate
Scenario:
Before loading a daily export into your database, 
your pipeline runs a quick quality check on the file's row count and file format.

Your Task:
Create a new file Daily_tasks/Day_3_Conditionals.py in VS Code.

Start with these two variables:

file_name = "orders_20261127.csv"
row_count = 250
Check 1 (File Format): Write an if / else block that checks if file_name ends with ".csv".

If it does, print "Format OK: CSV detected"

Otherwise, print "Format Error: Expected CSV"

Check 2 (Row Count): Write an if / elif / else block for row_count:

If row_count == 0, print "Status: Empty batch - skip load"

Else if row_count < 100, print "Status: Low volume - review required"
Else, print "Status: Ready to load" """

file_name = "orders_20261127.csv"
row_count = 250

if file_name.endswith("csv"):
    print("Format OK: CSV detected")
else:
    print("Format Error: Expected CSV")
if row_count == 0:
    print("Status: Empty batch - skip load")
elif row_count < 100:
    print("Status: Low volume - review required")
else:
    print("Status: Ready to load")