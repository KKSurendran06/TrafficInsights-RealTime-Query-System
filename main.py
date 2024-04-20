import sqlite3
import subprocess
from Algorithms import dsa
from Detection import Countingmain



db_file = 'traffic.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

try:
    cursor.execute('SELECT Lane, MAX(Count) FROM traffic_data GROUP BY Lane')
    rows = cursor.fetchall()

    max_counts = {}
    for row in rows:
        lane, max_count = row
        max_counts[lane] = max_count

    print("Maximum Counts Per Lane:")
    print(max_counts)

except sqlite3.Error as e:
    print("Error fetching data:", e)

finally:
    conn.close()
L=[]
for i in max_counts:
    L.append(max_counts[i])
subprocess.run(["./run_all.sh"], check=True)

dsa.dsa_function(L)



