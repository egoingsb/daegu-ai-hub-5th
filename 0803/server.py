from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    return f"""
      <h1>Python</h1>
      {random.random()}
      <h1>JavaScript</h1>
      <script>
        document.write(Math.random());
      </script>
    """

app.run(debug=True)