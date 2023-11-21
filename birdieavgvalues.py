import sqlite3

conn = sqlite3.connect('golf_database.db')
cursor = conn.cursor()

# Update additional columns in the 'wins' table from 'birdieavg'
columns_to_update = ['BIRDIEAVG', '"# OF BIRDIES"', '"TOTAL ROUNDS"']

for column in columns_to_update:
    query = f'''
    UPDATE wins
    SET {column} = (
        SELECT birdieavg.{column}
        FROM birdieavg
        WHERE wins.player_id = birdieavg.player_id
    )
    WHERE EXISTS (
        SELECT 1
        FROM birdieavg
        WHERE wins.player_id = birdieavg.player_id
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
