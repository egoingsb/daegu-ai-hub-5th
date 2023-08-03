from flask import Flask, render_template
import random

app = Flask(__name__)

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

@app.route("/read/<int:id>")
def read(id):
    selected = None
    for topic in topics:
        if topic["id"] == id:
            selected = topic
    return render_template('read.html', topics=topics, topic=selected)

app.run(debug=True)