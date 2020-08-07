from flask import Flask, render_template, request
import datetime

app = Flask('__name__')


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

# LOOPING LIST
@app.route("/list")
def listing():
    names = ["Alice", "Bob", "Cache"]
    return render_template("list.html", names=names)

# FORM SUBMISSION
@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)


# 
# Route Test

# @app.route("/")
# def index():
#     return "Hey, there!"

# @app.route("/<string:name>")
# def name(name):
#     name = name.capitalize()
#     return f"<h4>Hey, {name} !!!</h4>"