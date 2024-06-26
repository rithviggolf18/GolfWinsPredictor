import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplcursors
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error


conn = sqlite3.connect('golf_database.db')
query = 'SELECT * FROM wins;'
data = pd.read_sql_query(query, conn)

data.replace("None", np.nan, inplace=True)
data = data.fillna(0)  
data.replace([np.inf, -np.inf], np.nan, inplace=True)  

percentage_columns = ['FAIRWAY%', 'GREENS%', 'SCRAMBLING%']
for column in percentage_columns:
    data[column] = data[column].str.rstrip('%').astype('float') / 100.0

features = data[['BIRDIEAVG', '# OF BIRDIES', 'TOTAL ROUNDS', 'FAIRWAY%', 'FAIRWAYS HIT', 'POSSIBLE FAIRWAYS', 'RELATIVE TO PAR', 'GREENS%', 'GREENS HIT', '# HOLES', 'RELATIVE/PAR', 'SCORINGAVG', 'TOTAL STROKES', 'SCRAMBLING%', 'PAR OR BETTER', 'MISSED GIR', 'SAPGAVG', 'TOTAL SG:APP', 'SATGAVG', 'TOTAL SG:ARG', 'SOTAVG', 'TOTAL SG:OTT', 'SPAVG', 'TOTAL SG:PUTTING', 'STGAVG', 'STAVG', 'TOTAL SG:T', 'TOTAL SG:T2G']]
target = data['VICTORIES']

# Split the data into training and testing sets
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Impute missing values in features
imputer = SimpleImputer(strategy='mean')  
features_train_imputed = imputer.fit_transform(features_train)
features_test_imputed = imputer.transform(features_test)
features_imputed = imputer.transform(features)

# Create and train the neural network model
model = make_pipeline(StandardScaler(), MLPRegressor(random_state=42))
model.fit(features_train_imputed, target_train)

# Make predictions on the entire dataset
data['Predicted Wins'] = np.maximum(model.predict(features_imputed), 0)

# Show scatterplot with player names
plt.figure(figsize=(10, 6))  
plt.scatter(data['VICTORIES'], data['Predicted Wins'], alpha=0.5)
labels = data['PLAYER'].tolist()
mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(labels[sel.index]))

plt.xlabel('Actual Wins')
plt.ylabel('Predicted Wins')
plt.title('Actual Wins vs. Predicted Wins')
plt.show()

# Make predictions on the test set
predictions_test = model.predict(features_test_imputed)

# Calculate MSE and MAE
mse = mean_squared_error(target_test, predictions_test)
mae = mean_absolute_error(target_test, predictions_test)

print(f"Mean Squared Error (MSE): {mse}")
print(f"Mean Absolute Error (MAE): {mae}")

conn.close()
