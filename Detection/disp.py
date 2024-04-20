import sqlite3

db_file = 'traffic.db'

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

x=cursor.execute('Select * from traffic_data')

for i in x:
    print(i)