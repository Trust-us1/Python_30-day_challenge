""" Start with these three variables:
Python
raw_table_1 = "  ORDERS  "
raw_table_2 = "  CuStOmErS "
raw_table_3 = "PRODUCTS   "

Clean each one using .strip() and .lower(), 
and save the results into three new variables: clean_table_1, clean_table_2, and clean_table_3.
Create a list called clean_tables containing all three cleaned variables.
Print clean_tables.
Expected Output:
['orders', 'customers', 'products']

Run it in your VS Code terminal (python day_01_variables_strings/challenge.py), 
and once it matches the expected output, commit and push it to GitHub.

Quick Concept Check
What happens if you write raw_table_1.strip().lower() on a line by itself 
without putting clean_table_1 = in front of it, and then run print(raw_table_1)? """

raw_table_1 = "  ORDERS  "
raw_table_2 = "  CuStOmErS "
raw_table_3 = "PRODUCTS   "

clean_table1 = raw_table_1.strip().lower()
clean_table2 = raw_table_2.strip().lower()
clean_table3 = raw_table_3.strip().lower()

clean_tables = [clean_table1,clean_table2,clean_table3]
print(clean_tables)

# then the outcome of raw_table_1.strip().lower() is not saved to the variable clean_table_1