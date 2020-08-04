from flask import Flask, render_template
import datetime

app = Flask('__name__')

# @app.route("/")
# def index():
#     return "Hey, there!"

# @app.route("/<string:name>")
# def name(name):
#     name = name.capitalize()
#     return f"<h4>Hey, {name} !!!</h4>"

@app.route("/")
def index():
    headline = "this is headline"
    return render_template("index.html", headline=headline)

# ISITNEWYEAR?
@app.route("/ny")
def newyear():
    today = datetime.datetime.now()
    newyear = today.month == 1 and today.date == 1
    return render_template("ny.html", newyear=newyear)

