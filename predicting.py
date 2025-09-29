import pandas as pd
from model_training import model

# PREDICTION
tomorrow = pd.DataFrame([[30, 70]], columns=['temperature', 'humidity']) # Example: 30°C and 70% humidity
rain_prob = model.predict_proba(tomorrow)[0][1]    
print(f"Probability of rain tomorrow: {rain_prob*100:.2f}%")