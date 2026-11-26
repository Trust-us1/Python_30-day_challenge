""" Bite-Sized DE Coding Task: Calculate Daily Pipeline Totals
Scenario:
Your ingestion script just read two batch summaries from a text file,
so all the numbers are currently stored as strings. 
You need to convert them to proper numeric types to calculate the total rows loaded and total revenue.

Your Task:
Create a new file Daily_tasks/Day_2_Type_Casting.py in VS Code.

Start with these variables:
batch_1_rows = "1200"
batch_2_rows = "850"

batch_1_revenue = "4500.50"
batch_2_revenue = "3200.25"
Convert batch_1_rows and batch_2_rows to integers, 
add them together, and save the result in a variable called total_rows.
Convert batch_1_revenue and batch_2_revenue to floats, 
add them together, and save the result in a variable called total_revenue.
Print the results using an f-string so it looks like this:
Plaintext
Total Rows: 2050
Total Revenue: 7700.75
Print type(total_rows) and type(total_revenue) to confirm they are int and float"""

batch_1_rows = "1200"
batch_2_rows = "850"

batch_1_revenue = "4500.50"
batch_2_revenue = "3200.25"

total_rows = int(batch_1_rows) + int(batch_2_rows)
total_revenue = float(batch_1_revenue) + float(batch_2_revenue)
print(f"Total Rows: {total_rows}")
print(f"Total Revenue: {total_revenue}")
print(f"Type of total_rows: {type(total_rows)}")
print(f"Type of total_revenue: {type(total_revenue)}")