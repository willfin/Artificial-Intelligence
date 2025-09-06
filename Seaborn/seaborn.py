import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load an example dataset
tips = sns.load_dataset("tips")  # Built-in dataset with restaurant tips
tips.head()

plt.figure(figsize=(6,4))
sns.histplot(tips["total_bill"], kde=True, color="skyblue")
plt.title("Distribution of Total Bills")
plt.xlabel("Total Bill ($)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(data=tips, x="day", hue="sex")
plt.title("Count of Customers by Day and Gender")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("Total Bill Distribution by Day and Gender")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
sns.regplot(data=tips, x="total_bill", y="tip")
plt.title("Relationship between Bill and Tip")
plt.tight_layout()
plt.show()

sns.pairplot(tips, hue="sex")
plt.suptitle("Pairwise Plots by Gender", y=1.02)
plt.show()

corr = tips.corr(numeric_only=True)

plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

sns.set_style("darkgrid")
sns.histplot(tips["total_bill"], kde=True, color="coral")
plt.title("Styled Histogram")
plt.show()