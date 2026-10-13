# 1. Data Loading

# Pandas Python Library - Pandas is a Python library used to work with, analyse, clean, and manipulate data. 
# It is especially useful for data analysis, data science, and machine learning.

# Think of Pandas as Excel inside Python. You can organise data into tables, filter rows, calculate values, and analyse large datasets.

import pandas as pd

# Load the CSV file
data_csv = pd.read_csv("sample.csv")
print(data_csv)

# Load the text file
data_txt = pd.read_csv("sample.txt", header = 0, sep =',')
print(data_txt)

# Load the json file
data_json = pd.read_json("employees.json")
print(data_json)

# Load the Excel file
data_excel = pd.read_excel("employees.xlsx", sheet_name =  "Employees")
print(data_excel)


import sqlite3

connection_db = sqlite3.connect("giraffe_demo.db")

# Save the data to the database
data_csv.to_sql(
    "employees",
    connection_db,
    if_exists="replace",
    index=False
)

print("Data saved successfully!")

query1 = 'SELECT * FROM employees'
query2 = 'SELECT * FROM employees WHERE Age > 30'
data_sql = pd.read_sql(query1, connection_db)
print(data_sql)

data_sql_filtered = pd.read_sql(query2, connection_db)
print(data_sql_filtered)

connection_db.close()


# Important: to_sql() creates the table automatically if it doesn't exist. 
# With if_exists="replace", it replaces an existing table; use "append" to add rows instead.