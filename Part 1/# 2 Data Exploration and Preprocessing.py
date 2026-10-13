
# 2. Data Exploration and Preprocessing

import pandas as pd

# Load the CSV file
data_csv = pd.read_csv("sample.csv")
print(data_csv)

print(data_csv.head()) #print the first 5 rows. You can also specify the count
print(data_csv.head(20))  #print the first 20 rows
print(data_csv.tail())  #print the last 5 rows.
print(data_csv.info())  #it will show the details of the table columns with data types.

print(data_csv.dropna()) #removes all rows that contain at least one missing value (NaN) from the DF.
print(data_csv.fillna("NULL"))  #it will replace the blank with NULL
data_csv = data_csv.drop_duplicates() #it will remove the duplicate rows.

data_csv.to_csv("sample.csv", index=False)      #To save the changes to the CSV file, you can use the to_csv() method. 
# The index=False argument is used to prevent pandas from writing row indices to the file.

print(data_csv.iloc[0:5])   # Prints rows at positions 0–4 (5 rows)
print(data_csv.loc[0:5])    # Prints rows with index labels 0–5 (6 rows)
# .iloc[] → selects using integer positions (index value which starts with 0)
# .loc[] → selects using index(column) labels (index label like a, b, c, …)

# To print the 
print(data_csv.iloc[5])  # Prints the row at position 5
print(data_csv.loc[5])   # Prints the row with index label 5

# import pandas as pd

data = pd.DataFrame({'A1': [1, 2, 3],
       'A2': [4, 5, 6],
       'A3': [7, 8, 9]},
      index=['X', 'Y', 'Z'])

print(data)
print(data.loc['X'])  #print the 'X' rows
print(data.loc[:, 'A2'])  #print the 'A2' row.
print(data.loc['Y', 'A2'])  #print the Y row and A2 column value.

print(data.iloc[:, 2]) #by column position