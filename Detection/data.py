import pandas as pd
from sqlalchemy import create_engine
import openai


csv_files=[
    'Detection/vehicle_count.csv',
    'Detection/vehicle_count1.csv',
    'Detection/vehicle_count2.csv',
    'Detection/vehicle_count3.csv'
]

junctions_names=['junctions1', 'junctions2', 'junctions3', 'junctions4']

engine = create_engine('sqlite:///traffic.db', echo=False)

for csv_file, junctions_name in zip(csv_files, junctions_names):
    data=pd.read_csv(csv_file)
    
    data.to_sql(junctions_name, con=engine, if_exists='replace', index=False)


for i,j in data:
    print(i,j)

print("data inserted.")

import sqlite3



OPEN_API_KEY =  ''
model = "text-davinci-003"


# def generate_query(prompt):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=100,
#         temperature=0.7,
#         n=1,
#         stop=None
#     )
#     return response.choices[0].text.strip()


# prompt = "Generate a SQL query to retrieve traffic data of a specific date."
# query = generate_query(prompt)
# query_result = pd.read_sql_query(query, engine)


# def dsa_function(data):
#   pass


# processed_data = dsa_function(query_result)

# print("Processed Data:", processed_data)