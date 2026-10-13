# 5. Data Visualization

# Matplotlib is a Python library used to create graphs and charts to visualise data and understand patterns, trends, and relationships.

import matplotlib.pyplot as plt
x_values = [1,2,3,4,5,6,7,8,9,10]
y_values = [1,4,6,8,10,12,14,16,18,20]

Line plot (plt.plot()) displays trends or changes in data by connecting data points with lines, often over time.
plt.plot(x_values, y_values, color = ‘green’)
plt.xlabel(“x-axis placement”)	#Adds a label to the X-axis (horizontal axis)
plt.ylabel(“y-axis placement”)	#Adds a label to the Y-axis (Vertical axis).
plt.title(“Title Placement”)	#Adds a title at the top of the graph to describe what the plot represents
plt.show()	#Displays the plot or graph on the screen

Scatter plot (plt.scatter()) displays the relationship between two numerical variables using dots.
plt.scatter(x_values, y_values, color = ‘green’)
plt.xlabel(“x-axis placement”)	
plt.ylabel(“y-axis placement”)	
plt.title(“Title Placement”)
plt.show()

Bar chart (plt.bar()) compares values across different categories using rectangular bars.
animal = [‘cat’, ‘dog’, ‘horse’, ‘mouse’, ‘rabbit’]
animal_value = [10, 30, 45, 70, 25]

plt.bar(animal, animal_value, color = “forest green”) 
plt.xlabel("Animal")
plt.ylabel("Animal Value")
plt.title("Animal Bar Chart")
plt.show()

Histogram (plt.hist()) shows the frequency distribution of numerical data by grouping values into intervals called bins.

import numpy as np
x_normal = np.random.normal(0, 1, 100)
plt.hist(x_normal, color = “forestgreen”)
plt.xlabel("X")
plt.ylabel(“Frequency")
plt.title("Randomly Sampled Data from Standard Normal Distribution")
plt.show()

# Population Distribution
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x_values = np.arrange(-4, 4, 0.01)
y_values = norm.pdf(x_values)
Counts, bins, ignored = plt.hist(_normal, 30, density = True, color = “bottelgreen”, label = “Sampling Distribution”)
plt.plot(x_values, y_values, color = ‘y’, linewidth = 2.5, label = “Population Distribution”)
plt.ylabel("Probability")
plt.title("Randomly generating 1000 obs from normal Distribution mu = 0 sigma = 1")
plt.legend()
plt.show()




