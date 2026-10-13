# 3. Data Aggregation - Filtering, Sorting, Grouping

# It is the process of combining and summarising data to calculate values such as sum, average, count, minimum, and maximum.

import pandas as pd

# Create a DataFrame
data = pd.DataFrame({
    'Name': ['Anna', 'Krishan', 'Ritu', 'Divya', 'Rohit', 'Ankit'],
    'Age': [28, 30, 28, 27, 35, 29],
    'Salary': [50000, 180000, 45000, 25000, 120000, 60000],
    'Department': ['Tech', 'Tech', 'Business', 'Teaching', 'Business', 'Tech']
})

# Ascending order: lowest salary first
print(data.sort_values(by='Salary'))

# Descending order: highest salary first
print(data.sort_values(by='Salary', ascending=False))

# Count non-missing values in each column, grouped by department
print(data.groupby('Department').count())
print(data.groupby('Department')['Name'].count())


#  You can use functions like sum, mean, count, apply, max, min, etc.

print(data.groupby('Department').sum(numeric_only=True))	#Sum numeric values in each department
print(data.groupby('Department')['Age'].mean())	#Average age per department
print(data.groupby('Department').count())	#Count non-missing values per column
print(data.groupby('Department')['Salary'].max())	#Highest salary per department
print(data.groupby('Department')['Salary'].min())	#Lowest salary per department
print(data.groupby('Department')['Salary'].apply(list))	#Collect salaries into a list for each department

print(data[data["Salary"] > 100000])
print(data[data["Age"].isin([28, 30])])    #Displays only the rows where Age is either 28 or 30