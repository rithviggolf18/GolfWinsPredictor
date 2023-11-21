import sqlite3
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import mplcursors

# Connect to the SQLite database
conn = sqlite3.connect('golf_database.db')

# Load data from the database into a Pandas DataFrame
query = 'SELECT * FROM wins;'
data = pd.read_sql_query(query, conn)

# Replace "None" with NaN
data.replace("None", np.nan, inplace=True)

# Handle missing values
data = data.fillna(0)  # Replace NaN values with 0

# Handle infinite values
data.replace([np.inf, -np.inf], np.nan, inplace=True)  # Replace infinite values with NaN

# Convert percentage columns to numeric format
percentage_columns = ['FAIRWAY%', 'GREENS%', 'SCRAMBLING%']
for column in percentage_columns:
    data[column] = data[column].str.rstrip('%').astype('float') / 100.0

# Specify features and target variable
features = data[['BIRDIEAVG', '# OF BIRDIES', 'TOTAL ROUNDS', 'FAIRWAY%', 'GREENS%', 'GREENS HIT', '# HOLES', 'RELATIVE/PAR', 'SCORINGAVG', 'TOTAL STROKES', 'SCRAMBLING%', 'PAR OR BETTER', 'MISSED GIR', 'SAPGAVG', 'TOTAL SG:APP', 'SATGAVG', 'TOTAL SG:ARG', 'SOTAVG', 'TOTAL SG:OTT', 'SPAVG', 'TOTAL SG:PUTTING', 'STGAVG', 'STAVG', 'TOTAL SG:T', 'TOTAL SG:T2G']]
target = data['VICTORIES']

# Split the data into training and testing sets
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Impute missing values in features
imputer = SimpleImputer(strategy='mean')  # You can choose 'mean', 'median', or 'most_frequent'
features_train_imputed = imputer.fit_transform(features_train)
features_test_imputed = imputer.transform(features_test)

# Create a linear regression model
model = LinearRegression()

# Train the model with the imputed data
model.fit(features_train_imputed, target_train)

# Impute missing values in the entire dataset
features_imputed = imputer.transform(features)

# Make predictions on the entire dataset
data['Predicted Wins'] = model.predict(features_imputed)

# Show scatterplot with transparency and player names
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.scatter(data['VICTORIES'], data['Predicted Wins'], alpha=0.5)

# Annotate each point with player names
labels = data['PLAYER'].tolist()

mplcursors.cursor(hover=True).connect(
    "add", lambda sel: sel.annotation.set_text(labels[sel.target.index])
)

plt.xlabel('Actual Wins')
plt.ylabel('Predicted Wins')
plt.title('Actual Wins vs. Predicted Wins')
plt.show()

# Close the database connection
conn.close()
