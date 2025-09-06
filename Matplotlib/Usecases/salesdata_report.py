import matplotlib.pyplot as plt
import pandas as pd

# Example dataset: monthly sales data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Sales": [12000, 15000, 18000, 17000, 22000, 25000,
              24000, 26000, 23000, 28000, 30000, 35000]
}

df = pd.DataFrame(data)
print(df)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df["Month"], df["Sales"], marker="o", linestyle="-")
plt.title("Monthly Sales Performance", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()