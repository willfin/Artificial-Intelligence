
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample dataset: weekly data for 20 weeks
np.random.seed(42)
data = pd.DataFrame({
    "Ad_Spend": np.random.uniform(1000, 5000, 20),
    "Discount": np.random.uniform(5, 30, 20),
    "Foot_Traffic": np.random.uniform(200, 1000, 20),
    "Sales": np.random.uniform(5000, 20000, 20)
})

# Compute correlation matrix
corr = data.corr()

# Plotting
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Business Metrics")
plt.tight_layout()
plt.show()