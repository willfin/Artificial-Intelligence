# Matplotlib Tutorial in Google Colab

import matplotlib.pyplot as plt
import numpy as np

# 1. Basic Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 1, 6]

plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 2. Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
plt.show()

# 3. Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]

plt.bar(categories, values, color='green')
plt.title("Bar Chart")
plt.show()

# 4. Histogram
data = np.random.randn(1000)

plt.hist(data, bins=30, color='blue', edgecolor='black')
plt.title("Histogram")
plt.show()

# 5. Pie Chart
sizes = [30, 20, 25, 25]
labels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Pie Chart")
plt.show()

# 6. Multiple Lines on Same Plot
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")
plt.legend()
plt.title("Multiple Lines")
plt.show()

# 7. Subplots (Multiple Charts in One Figure)
x = np.linspace(0, 10, 100)

plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x))
plt.title("Sine Wave")

plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))
plt.title("Cosine Wave")

plt.tight_layout()
plt.show()
