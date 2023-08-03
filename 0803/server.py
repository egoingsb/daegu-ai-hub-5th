from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    return f"""
    <html>
      <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
          <li><a href="/read/1">html</a></li>
          <li><a href="/read/2">css</a></li>
        </ol>
        <h2>Welcome</h2>
        Hello, WEB!
        <ul>
          <li><a href="/create">create</a></li>
        </ul>
      </body>
    </html>
    """

@app.route("/create")
def create():
    return f"""
    <html>
      <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
          <li><a href="/read/1">html</a></li>
          <li><a href="/read/2">css</a></li>
        </ol>
        <h2>Create</h2>
        create!!
        <ul>
          <li><a href="/create">create</a></li>
        </ul>
      </body>
    </html>
    """

@app.route("/read/<id>")
def read(id):
    return f"""
    <html>
      <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
          <li><a href="/read/1">html</a></li>
          <li><a href="/read/2">css</a></li>
        </ol>
        <h2>Read</h2>
        Read!! {id}
        <ul>
          <li><a href="/create">create</a></li>
        </ul>
      </body>
    </html>"""

app.run(debug=True)