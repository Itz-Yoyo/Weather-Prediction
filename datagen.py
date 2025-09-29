import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n = 3000

# Generate synthetic features
temperature = np.random.normal(loc=25, scale=5, size=n)   # °C, avg 25 ±5
humidity = np.random.normal(loc=70, scale=15, size=n)     # %, avg 70 ±15
pressure = np.random.normal(loc=1013, scale=10, size=n)   # hPa, avg 1013 ±10

# Rule-based probability of rain
rain = []
for t, h, p in zip(temperature, humidity, pressure):
    prob = 0.2  # base chance
    if h > 75: prob += 0.3
    if 20 < t < 28: prob += 0.2
    if p < 1008: prob += 0.2
    rain.append(1 if np.random.rand() < prob else 0)

# Build DataFrame
df = pd.DataFrame({
    'temperature': temperature.round(1),
    'humidity': humidity.round(1),
    'pressure': pressure.round(1),
    'rain': rain
})

print(df.head())

# Save to CSV
df.to_csv('data.csv', index=False)