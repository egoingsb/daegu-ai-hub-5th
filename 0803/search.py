import psycopg2
from pgvector.psycopg2 import register_vector
import numpy as np


conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="todghkfzheld",
    host="db.xnvflqoounhpdkwhsfxo.supabase.co",
    port="5432",
)
cursor = conn.cursor()
register_vector(cursor)

import openai

search = input('search? ')
response = openai.Embedding.create(
    input=search,
    model="text-embedding-ada-002"
)
embedding = np.array(response['data'][0]['embedding'])
cursor.execute("SELECT id, title, body FROM topics ORDER BY embedding <=> %s", (embedding,))
rows = cursor.fetchall()
for row in rows:
    print(row)
