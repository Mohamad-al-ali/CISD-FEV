from flask import Flask, render_template
from rugbypy.player import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("helloWorld.html")

if __name__ == "__main__":
    app.run(debug=True)
