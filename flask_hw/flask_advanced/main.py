from flask import Flask, render_template

from database import DB
from supermarkets import supermarkets
from products import products


def db_create():
    DB['products'] = []
    DB['supermarkets'] = []


def app_create():
    db_create()
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Not_very_strong_keY'
    app.register_blueprint(supermarkets)
    app.register_blueprint(products)
    return app


app = app_create()


@app.route('/')
def get_home_page():
    home_page_menu = ('product', 'supermarket')
    return render_template('home.html', menu=home_page_menu)


@app.errorhandler(404)
def not_found(error):
    return render_template('error_404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
