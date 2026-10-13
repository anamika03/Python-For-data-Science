# 5. Data Visualization

# Matplotlib is a Python library used to create graphs and charts to visualise data and understand patterns, trends, and relationships.

import matplotlib.pyplot as plt
x_values = [1,2,3,4,5,6,7,8,9,10]
y_values = [1,4,6,8,10,12,14,16,18,20]

# Line plot (plt.plot()) displays trends or changes in data by connecting data points with lines, often over time.
plt.plot(x_values, y_values, color = 'green')
plt.xlabel("x-axis")	#Adds a label to the X-axis (horizontal axis)
plt.ylabel("y-axis")	#Adds a label to the Y-axis (Vertical axis).
plt.title("Line Plot")	#Adds a title at the top of the graph to describe what the plot represents
plt.show()	#Displays the plot or graph on the screen

# Scatter plot (plt.scatter()) displays the relationship between two numerical variables using dots.
plt.scatter(x_values, y_values, color = 'orange', marker = 'o')	#marker = 'o' specifies the shape of the data points as circles.
plt.xlabel("x-axis")	
plt.ylabel("y-axis")	
plt.title("Scatter Plot")
plt.show()

# Bar chart (plt.bar()) compares values across different categories using rectangular bars.
animal = ['cat', 'dog', 'horse', 'mouse', 'rabbit']
animal_value = [10, 30, 45, 70, 25]

plt.bar(animal, animal_value, color = "forestgreen") 
plt.xlabel("Animal")
plt.ylabel("Animal Value")
plt.title("Animal Bar Chart")
plt.show()

# Histogram (plt.hist()) shows the frequency distribution of numerical data by grouping values into intervals called bins.

import numpy as np
X_normal = np.random.normal(0, 1, 100)
plt.hist(X_normal, color = "forestgreen")
plt.xlabel("X")
plt.ylabel("Frequency")
plt.title("Randomly Sampled Data from Standard Normal Distribution")
plt.show()

# Population Distribution
from scipy.stats import norm

x_values = np.arange(-5, 5, 0.01)
y_values = norm.pdf(x_values)

counts, bins, ignored = plt.hist(X_normal, 30, density = True, color = "purple", label = "Sampling Distribution")
plt.plot(x_values, y_values, color = 'y', linewidth = 2.5, label = "Population Distribution")
plt.ylabel("Probability")
plt.title("Randomly generating 1000 obs from normal Distribution mu = 0 sigma = 1")
plt.legend()
plt.show()