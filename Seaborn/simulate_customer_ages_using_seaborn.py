import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Simulate customer ages (normally distributed with some variation)
np.random.seed(42)
ages = np.random.normal(loc=35, scale=10, size=500)  # mean=35, std=10, 500 customers
ages = np.clip(ages, 18, 70)  # restrict ages between 18 and 70

# Plotting with Seaborn
plt.figure(figsize=(8, 5))
sns.histplot(ages, kde=True, bins=20, color="skyblue")
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()