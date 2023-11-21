import sqlite3

conn = sqlite3.connect('golf_database.db')
cursor = conn.cursor()

columns_to_update = ['SPAVG', '"TOTAL SG:PUTTING"']

for column in columns_to_update:
    query = f'''
    UPDATE wins
    SET {column} = (
        SELECT sgputting.{column}
        FROM sgputting
        WHERE wins.player_id = sgputting.player_id
    )
    WHERE EXISTS (
        SELECT 1
        FROM sgputting
        WHERE wins.player_id = sgputting.player_id
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
