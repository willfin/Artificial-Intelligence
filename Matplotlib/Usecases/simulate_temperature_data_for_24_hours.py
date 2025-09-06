
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import random

# Simulate temperature data for 24 hours
times = pd.date_range(start="2025-09-06 00:00", periods=24, freq="h")
print(times)
temperature = [random.uniform(20, 30) for _ in range(24)]  # Random temps between 20-30°C

# Create a DataFrame
df = pd.DataFrame({"Time": times, "Temperature": temperature})

# Plotting
plt.figure(figsize=(12, 5))
plt.plot(df["Time"], df["Temperature"], marker="o", linestyle="-")
plt.title("24-Hour Temperature Monitoring", fontsize=16)
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)  # Rotate time labels for better readability
plt.grid(True)
plt.tight_layout()
plt.show()