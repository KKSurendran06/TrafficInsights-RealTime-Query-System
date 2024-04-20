
import sqlite3

db_file = 'traffic.db'

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

create_table_query = 'CREATE TABLE traffic_data (timestamp String  default 0 ,Lane String,Count INTEGER default 0)'

cursor.execute(create_table_query)
conn.close()