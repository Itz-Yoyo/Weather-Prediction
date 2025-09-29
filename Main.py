import pandas as pd
from Model_Training import model

# PREDICTION
a,b,c = input("Enter temperature (°C), humidity (%) and pressure (hPa): ").split(",") # split ,
tomorrow = pd.DataFrame([[a, b, c]], columns=['temperature', 'humidity', 'pressure'])
rain_prob = model.predict_proba(tomorrow)[0][1]    
print(f"Probability of rain tomorrow: {rain_prob*100:.2f}%")