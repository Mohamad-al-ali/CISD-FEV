from flask import Flask, render_template
from rugbypy.player import *

app = Flask(__name__)

@app.route("/players")
def show_players():
    players = fetch_all_players()   # this returns a list of Player objects
    print(players)
    # return render_template("helloWorld.html", players=players)

@app.route("/")
def home():
    return render_template("helloWorld.html")

if __name__ == "__main__":
    app.run(debug=True)
