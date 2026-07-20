from sklearn.linear_model import LinearRegression
import numpy as np

# Temperature history
time = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
temp = np.array([2, 3, 4, 5, 6])

# Train model
model = LinearRegression()
model.fit(time, temp)

# Predict next temperature
future_temp = model.predict([[6]])

print(f"Predicted Temperature: {future_temp[0]:.2f}°C")

if future_temp[0] > 4:
    print("⚠ ALERT: Milk may spoil soon!")