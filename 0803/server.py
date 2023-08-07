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
    return render_template('create.html', topics=topics)

@app.route("/create_process", methods=['POST'])
def create_process():
    global nextId
    topics.append({"id":nextId, "title":request.form['title'], "body":request.form['body']})
    nextId = nextId + 1
    return redirect(f'/read/{nextId-1}')
@app.route("/read/<int:id>")
def read(id):
    selected = None
    for topic in topics:
        if topic["id"] == id:
            selected = topic
    return render_template('read.html', topics=topics, topic=selected)

app.run(debug=True)