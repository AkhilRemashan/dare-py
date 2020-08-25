from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    """Registration Form"""
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [
        Email(message=('Not a valid email address.')),
        DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')