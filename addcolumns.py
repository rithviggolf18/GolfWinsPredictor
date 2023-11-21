import sqlite3

conn = sqlite3.connect('golf_database.db')
cursor = conn.cursor()

# Define the list of new column names
new_columns = ['BIRDIEAVG', '# OF BIRDIES', 'TOTAL ROUNDS', 'FAIRWAY%', 'FAIRWAYS HIT', 'POSSIBLE FAIRWAYS', 'RELATIVE TO PAR', 'GREENS%', 'GREENS HIT', '# HOLES', 'RELATIVE/PAR', 'SCORINGAVG', 'TOTAL STROKES', 'SCRAMBLING%', 'PAR OR BETTER', 'MISSED GIR', 'SAPGAVG', 'TOTAL SG:APP', 'SATGAVG', 'TOTAL SG:ARG', 'SOTAVG', 'TOTAL SG:OTT', 'SPAVG', 'TOTAL SG:PUTTING', 'STGAVG', 'STAVG', 'TOTAL SG:T', 'TOTAL SG:T2G']

# Check if each new column already exists in the 'wins' table
for new_column in new_columns:
    cursor.execute("PRAGMA table_info(wins);")
    columns = cursor.fetchall()
    column_exists = any(new_column.upper() in col for col in columns)

    if not column_exists:
        # Add the new column to the 'wins' table
        query = 'ALTER TABLE wins ADD COLUMN "{}" TEXT;'.format(new_column)
        cursor.execute(query)

        conn.commit()
        print('New column "{}" added to "wins" table.'.format(new_column))

    else:
        print('Column "{}" already exists in the "wins" table.'.format(new_column))

cursor.close()
conn.close()
