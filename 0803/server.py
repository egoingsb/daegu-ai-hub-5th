from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/create")
def create():
    return render_template('create.html')

@app.route("/read/<id>")
def read(id):
    return render_template('read.html')

app.run(debug=True)