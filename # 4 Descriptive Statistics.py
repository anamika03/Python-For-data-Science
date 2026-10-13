# 4. Descriptive Statistics

# It is useful for analysing and summarising the data. It provides a concise summary of the main features of the data. It can help you to understand the data by providing measures like mean, dispersion, variance and the shape of the distribution. By using descriptive statistics, you can visualise your data. You can use histograms, box plots, bar charts, etc.

import numpy as np
#Mean: The average of all values.
data = [100, 20, 5, 26, 45, -100, 40]
mean_value = np.mean(data)
print(“Mean of array:”, mean_value)
#Median: The middle value when the data is arranged in ascending order.
median_value = np.median(data)
print(“Median of array:’, median_value)

#Mode: The value that appears most frequently in a dataset.
#NumPy does not have a built-in np.mode() function. You can use statistics or SciPy.
from scipy import stats

mode_value = stats.mode(data)
print(“Mode of array:”, mode_value)

#Variance: Measures how spread out data values are from the mean by calculating the average squared deviation.

variance_ = np.var(data)
print(“Variance of array:”, variance_)

#Standard deviation: Measures how spread out data values are from the mean, in the same units as the original data.

std_dev = np.std(data)
print(“Standard Deviation of array:”, std_dev)

Formulas
Variance (population):  2=(xi-)2N
Standard deviation: =Variance
Remember: Standard deviation is the square root of variance. By default, np.var() and np.std() calculate population variance and standard deviation (ddof=0). For sample statistics, use np.var(data, ddof=1) and np.std(data, ddof=1).

#Loading csv file with header
data_csv = pd.read_csv(“filename.csv”)
print(data_csv.describe())

#data_csv.describe() generates descriptive statistics for the numerical columns in a CSV dataset, such as count, mean, standard deviation, minimum, maximum, and quartiles.

What each statistic means: 
count — Number of non-missing values
mean — Average value
std — Standard deviation
min — Minimum value
25% — First quartile (Q1)
50% — Median (Q2)
75% — Third quartile (Q3)
max — Maximum value

Data Merging

In Python Pandas, joins combine two DataFrames using a common column or index.

import pandas as pd

#creating 2 dataframes
data1 = pd.DataFrame({‘key’: [‘A’, ‘B’, ‘C’, ‘D’, ‘E’, ‘F’, ‘G’],
			‘Value1’: [1, 2, 3, 4, 5, 6, 7] } )
data2 = pd.DataFrame({‘key’: [‘C’, ‘D’, ‘E’, ‘F’, ‘G’, ‘H’],
			‘Value1’: [8, 9, 10, 11, 12, 13] } )
print(data1)
print(data2)

Inner Join - Returns only rows with matching IDs in both DataFrames. 
#pd.merge(df1, df2, on='ID', how='inner')

merge_inner_join = pd.merge(data1, data2, on='key', how='inner')
print(merge_inner_join)

Left Join - Returns all rows from the left DataFrame (df1) and matching rows from the right DataFrame (df2).
#pd.merge(df1, df2, on='ID', how='left')

merge_left_join = pd.merge(data1, data2, on='key', how='left')
print(merge_left_join)

Right Join - Returns all rows from the right DataFrame (df2) and matching rows from the left DataFrame (df1).
#pd.merge(df1, df2, on='ID', how='right')

merge_right_join = pd.merge(data1, data2, on='key', how='right')
print(merge_right_join)

Left Anti Join - Returns rows from the left DataFrame that have no matching ID in the right DataFrame.
#pd.merge(df1, df2, on='ID', how='left_anti')

merge_left_anti = pd.merge(data1, data2, on='key', how='left_anti')
print(merge_left_anti)
OR
merged_left = pd.merge(data1, data2, on='key', how='left’, indicator = True)
merge_left_anti_join = merged_left[merged_left[‘_merge’] == ‘left_only ‘]
merge_left_anti_join = merge_left_anti_join.drop(‘_merge’, axis = 1)
print(merge_left_anti_join)

Right Anti Join - Returns rows from the right DataFrame that have no matching ID in the left DataFrame.
#pd.merge(df1, df2, on='ID', how='right_anti')
Note: left_anti and right_anti are supported in Pandas 3.0 and later.

merge_right_anti = pd.merge(data1, data2, on='key', how='right_anti')
print(merge_right_anti)
OR
merged_right = pd.merge(data1, data2, on='key', how='right’, indicator = True)
merge_right_anti_join = merged_right[merged_right[‘_merge’] == ‘right_only ‘]
merge_right_anti_join = merge_right_anti_join.drop(‘_merge’, axis = 1)
print(merge_right_anti_join)


