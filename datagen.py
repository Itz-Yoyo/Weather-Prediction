import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n = 200

# Generate synthetic features
temperature = np.random.normal(loc=25, scale=5, size=n)   # average 25°C, ±5
humidity = np.random.normal(loc=70, scale=15, size=n)     # average 70%, ±15

# Rule of thumb: higher humidity + moderate temps = more likely rain
rain = []
for t, h in zip(temperature, humidity):
    prob = 0.3
    if h > 75: prob += 0.4
    if 20 < t < 28: prob += 0.2
    rain.append(1 if np.random.rand() < prob else 0)

# Build DataFrame
df = pd.DataFrame({
    'temperature': temperature.round(1),
    'humidity': humidity.round(1),
    'rain': rain
})

print(df.head())

# Save to CSV
df.to_csv('data.csv', index=False)
