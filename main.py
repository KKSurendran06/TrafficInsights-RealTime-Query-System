import sqlite3
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

def execute_sql_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except (Exception, sqlite3.Error) as error:
        print('Error executing the query:', error)
        return None

db_file = "traffic.db"
connection = sqlite3.connect(db_file)

sql_query = "SELECT lane, MAX(count) FROM traffic_data GROUP BY lane"

model_name = "gpt2-medium"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

encoded_input = tokenizer(sql_query, return_tensors='pt')
with torch.no_grad():
    output = model.generate(**encoded_input)
decoded_query = tokenizer.decode(output[0], skip_special_tokens=True)

result_set = execute_sql_query(connection, decoded_query)

max_counts = {}
if result_set:
    for row in result_set:
        junction = row[0]
        max_count = row[1]
        max_counts[junction] = max_count

connection.close()

print("Maximum Counts per Junction:", max_counts)

from dsa import Main

Main(max_counts['J1'], max_counts['J2'], max_counts['J3'], max_counts['J4'])
