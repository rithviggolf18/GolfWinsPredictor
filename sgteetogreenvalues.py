import sqlite3

conn = sqlite3.connect('golf_database.db')
cursor = conn.cursor()

# Update the STGAVG column in the 'wins' table from 'sgteetogreen'
query = '''
UPDATE wins
SET STGAVG = (
    SELECT sgteetogreen.STGAVG
    FROM sgteetogreen
    WHERE wins.player_id = sgteetogreen.player_id
)
WHERE EXISTS (
    SELECT 1
    FROM sgteetogreen
    WHERE wins.player_id = sgteetogreen.player_id
);
'''

try:
    cursor.execute(query)
    conn.commit()
    print("STGAVG values updated in 'wins' table.")

except sqlite3.Error as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()
