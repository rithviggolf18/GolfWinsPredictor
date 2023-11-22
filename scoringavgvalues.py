import sqlite3

conn = sqlite3.connect('golf_database.db')
cursor = conn.cursor()

# Update additional columns in the 'wins' table from 'scoringavg'
columns_to_update = ['SCORINGAVG', '"TOTAL STROKES"', '"TOTAL ROUNDS"']

for column in columns_to_update:
    query = f'''
    UPDATE wins
    SET {column} = (
        SELECT scoringavg.{column}
        FROM scoringavg
        WHERE wins.player_id = scoringavg.player_id
    )
    WHERE EXISTS (
        SELECT 1
        FROM scoringavg
        WHERE wins.player_id = scoringavg.player_id
    );
    '''

    try:
        cursor.execute(query)
        conn.commit()
        print(f"{column} values updated in 'wins' table.")

    except sqlite3.Error as e:
        print("Error:", e)

cursor.close()
conn.close()
