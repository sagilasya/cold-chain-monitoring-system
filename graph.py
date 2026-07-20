import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

milk = data[data["Product"] == "Milk"]

plt.figure(figsize=(8,5))
plt.plot(milk["Time"], milk["Temperature"], marker="o")

plt.title("Milk Temperature Trend")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.show()