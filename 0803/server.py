from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

nextId = 4
topics = [
    {"id":1, "title":"html", "body":"html is ..."},
    {"id":2, "title":"css", "body":"css is ..."}, 
    {"id":3, "title":"js", "body":"js is ..."}
]

@app.route("/")
def index():
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