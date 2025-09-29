from data import df

# PREPROCESSING

# replace missing values
df.dropna(inplace=True)

# convert rain into binary values
df['rain'] = df['rain'].apply(lambda x: 1 if x > 0 else 0)

# Features and Target
X = df[['temperature','humidity','pressure']]
y = df['rain']
