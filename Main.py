import pandas as pd
from Model_Training import model

# PREDICTION
tomorrow = pd.DataFrame([[30, 70, 1000]], columns=['temperature', 'humidity', 'pressure']) # Example: 30°C and 70% humidity and 1000 hPa
rain_prob = model.predict_proba(tomorrow)[0][1]    
print(f"Probability of rain tomorrow: {rain_prob*100:.2f}%")