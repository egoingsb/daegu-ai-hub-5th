from flask import Flask, render_template, request, redirect
import psycopg2
from pgvector.psycopg2 import register_vector
import numpy as np

app = Flask(__name__)

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="todghkfzheld",
    host="db.xnvflqoounhpdkwhsfxo.supabase.co",
    port="5432",
)
cursor = conn.cursor()
register_vector(cursor)


nextId = 4
topics = [
    {"id":1, "title":"html", "body":"html is ..."},
    {"id":2, "title":"css", "body":"css is ..."}, 
    {"id":3, "title":"js", "body":"js is ..."}
]

@app.route("/")
def index():
    cursor.execute("SELECT id, title FROM topics")
    topics = cursor.fetchall()
    print(topics)
    return render_template('index.html', topics=topics)

@app.route("/create")
def create():
    cursor.execute("SELECT id, title FROM topics")
    topics = cursor.fetchall()
    return render_template('create.html', topics=topics)

@app.route("/create_process", methods=['POST'])
def create_process():
    t = request.form['title']
    b = request.form['body']
    cursor.execute("INSERT INTO topics (title, body) VALUES(%s,%s) RETURNING id", (t, b))
    lastid = cursor.fetchone()[0]
    conn.commit()
    return redirect(f'/read/{lastid}')

@app.route("/read/<int:id>")
def read(id):
    cursor.execute("SELECT id, title, body FROM topics")
    topics = cursor.fetchall()
    selected = None
    for topic in topics:
        if topic[0] == id:
            selected = topic
    return render_template('read.html', topics=topics, topic=selected)

app.run(debug=True)