from flask import Blueprint, jsonify, render_template, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators

vegetable = Blueprint('vegetables', __name__, template_folder='template')

vegetables = {"veg1": "carrot",
              "veg2": 'tomato'}


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])


@vegetable.route('/vegetable')
def get_vegetable():
    form = RegistrationForm(request.form)
    return render_template('main_.html', vegetables=vegetables)
