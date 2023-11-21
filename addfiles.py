import pandas as pd
import sqlite3
import os

# Set the directory containing your CSV files
csv_directory = "csvfiles"

# List all CSV files in the directory
csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]

# Initialize an SQLite database connection
conn = sqlite3.connect('golf_database.db')

# Iterate through each CSV file and import it into the database
for csv_file in csv_files:
    # Read CSV into a pandas DataFrame
    df = pd.read_csv(os.path.join(csv_directory, csv_file))

    # Use the pandas to_sql function to insert the DataFrame into the SQLite database
    df.to_sql(name=os.path.splitext(csv_file)[0], con=conn, if_exists='replace', index=False)

# Close the database connection
conn.close()
