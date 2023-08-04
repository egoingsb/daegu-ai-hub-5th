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

title = input('title?')
body = input('body?')
embeddings = ''
response = openai.Embedding.create(
    input=f'''title:{title}\n\nbody:{body}''',
    model="text-embedding-ada-002"
)
embeddings = np.array(response['data'][0]['embedding'])

cursor.execute('INSERT INTO topics (title, body, embedding) VALUES(%s, %s, %s)', (title, body, embeddings))
conn.commit()
conn.close()
