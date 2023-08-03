from flask import Flask, render_template
import random

app = Flask(__name__)

topics = [
    {"id":1, "title":"html", "body":"html is ..."},
    {"id":2, "title":"css", "body":"css is ..."}
]

@app.route("/")
def index():
    return render_template('index.html', topics=topics)

@app.route("/create")
def create():
    return render_template('create.html', topics=topics)

@app.route("/read/<id>")
def read(id):
    return render_template('read.html', topics=topics)

app.run(debug=True)