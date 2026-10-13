# 4. Descriptive Statistics

# It is useful for analysing and summarising the data. It provides a concise summary of the main features of the data. It can help you to understand the data by providing measures like mean, dispersion, variance and the shape of the distribution. By using descriptive statistics, you can visualise your data. You can use histograms, box plots, bar charts, etc.

import pandas as pd
import numpy as np
#Mean: The average of all values.
data = [100, 20, 5, 26, 45, -100, 40]
mean_value = np.mean(data)
print("Mean of array:", mean_value)
#Median: The middle value when the data is arranged in ascending order.
median_value = np.median(data)
print("Median of array:", median_value)

#Mode: The value that appears most frequently in a dataset.
#NumPy does not have a built-in np.mode() function. You can use statistics or SciPy.
from scipy import stats

mode_value = stats.mode(data)
print("Mode of array:", mode_value)

#Variance: Measures how spread out data values are from the mean by calculating the average squared deviation.

variance_ = np.var(data)
print("Variance of array:", variance_)

#Standard deviation: Measures how spread out data values are from the mean, in the same units as the original data.

std_dev = np.std(data)
print("Standard Deviation of array:", std_dev)


#Loading csv file with header
data_csv = pd.read_csv("sample.csv")
print(data_csv.describe())

# #data_csv.describe() generates descriptive statistics for the numerical columns in a CSV dataset, such as count, mean, standard deviation, minimum, maximum, and quartiles.

# What each statistic means: 
# count — Number of non-missing values
# mean — Average value
# std — Standard deviation
# min — Minimum value
# 25% — First quartile (Q1)
# 50% — Median (Q2)
# 75% — Third quartile (Q3)
# max — Maximum value

