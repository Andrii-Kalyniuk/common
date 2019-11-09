from flask import Flask, render_template

from db.database import DB, DB_test
from models import Product, Supermarket
from products.products import products
from supermarkets.supermarkets import supermarkets


def db_create():
    DB['products'] = []
    DB['supermarkets'] = []


def db_fill_up():
    def add_product(data):
        DB['products'].append(Product(name=data.get('name'),
                                      description=data.get('description'),
                                      img_name=data.get('img_name'),
                                      price=data.get('price')
                                      )
                              )

    def add_market(data):
        DB['supermarkets'].append(Supermarket(name=data.get('name'),
                                              location=data.get('location'),
                                              img_name=data.get('img_name')
                                              )
                                  )

    for product in DB_test['products']:
        add_product(product)
    for market in DB_test['supermarkets']:
        add_market(market)


def app_create():
    db_create()
    db_fill_up()
    app = Flask(__name__,
                static_folder='home/static',
                template_folder='home/templates'
                )
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
