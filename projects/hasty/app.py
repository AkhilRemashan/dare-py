from flask import Flask
from flask import render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home_page.html')


