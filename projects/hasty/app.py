from flask import Flask
from flask import render_template, url_for, request, redirect
from flask_wtf import FlaskForm
# 
from useracco import RegistrationForm


app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')

 
@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    register = RegistrationForm()
    if register.validate_on_submit():
        return redirect(url_for=('success_register'))
    return render_template('register.html', register=register)


