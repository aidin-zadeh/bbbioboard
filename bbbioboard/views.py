
from flask import render_template
from bbbioboard import app


# home route
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")