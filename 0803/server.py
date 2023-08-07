from flask import Flask, render_template, request, redirect
import psycopg2
from pgvector.psycopg2 import register_vector
import numpy as np

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import os

app = Flask(__name__)

from psycopg2.pool import SimpleConnectionPool

def create_conn_pool():
    return SimpleConnectionPool(1, 10, 
                                database="postgres",
                                user="postgres",
                                password=os.environ.get('PASSWORD'),
                                host=os.environ.get('HOST'),
                                port="5432")

# Initialize connection pool
connection_pool = create_conn_pool()

from flask import g
@app.before_request
def get_conn():
    print('before')
    g.conn = connection_pool.getconn()

@app.teardown_request
def close_conn(exception):
    print('teardown')
    connection_pool.putconn(g.conn)


@app.route("/")
def index():
    cursor = g.conn.cursor()
    cursor.execute("SELECT id, title FROM topics")
    topics = cursor.fetchall()
    return render_template('index.html', topics=topics)

@app.route("/create")
def create():
    cursor = g.conn.cursor()
    cursor.execute("SELECT id, title FROM topics")
    topics = cursor.fetchall()
    return render_template('create.html', topics=topics)

@app.route("/search")
def search():
    cursor = g.conn.cursor()
    register_vector(cursor)
    cursor.execute("SELECT id, title FROM topics")
    topics = cursor.fetchall()
    
    query = request.args.get('query')
    import openai
    response = openai.Embedding.create(
        input=query,
        model="text-embedding-ada-002"
    )
    embeddings = np.array(response['data'][0]['embedding'])
    cursor.execute("SELECT id, title, body FROM topics ORDER BY embedding <=> %s", (embeddings,))
    searched = cursor.fetchall()
    print('searched', searched)
    return render_template('search.html', topics=topics, searched=searched)

@app.route("/create_process", methods=['POST'])
def create_process():
    t = request.form['title']
    b = request.form['body']
    import openai
    response = openai.Embedding.create(
        input=f'''title:{t}\n\nbody:{b}''',
        model="text-embedding-ada-002"
    )
    embeddings = np.array(response['data'][0]['embedding'])
    cursor = g.conn.cursor()
    register_vector(cursor)
    cursor.execute("""
        INSERT INTO topics 
            (title, body, embedding) 
        VALUES(%s,%s,%s) 
            RETURNING id""", 
        (t, b, embeddings))
    lastid = cursor.fetchone()[0]
    g.conn.commit()
    return redirect(f'/read/{lastid}')

@app.route("/read/<int:id>")
def read(id):
    cursor = g.conn.cursor()
    cursor.execute("SELECT id, title, body FROM topics")
    topics = cursor.fetchall()
    selected = None
    for topic in topics:
        if topic[0] == id:
            selected = topic
    return render_template('read.html', topics=topics, topic=selected)

app.run(debug=True)