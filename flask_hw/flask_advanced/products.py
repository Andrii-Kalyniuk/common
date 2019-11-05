from flask import Blueprint, render_template, Response, request

from database import DB
from models import Product

products = Blueprint('products', __name__, url_prefix='/product',
                     template_folder='./products/templates')


@products.route('/', methods=['GET'])
def get_all_products():
    products_all = [product.__dict__ for product in DB['products']]
    args = request.args.to_dict()
    print(20*'.', args)
    print(20*'.', request.form.to_dict())
    return render_template('all_products.html',
                           products_all=products_all, args=args)


@products.route('/', methods=['POST'])
def add_product():
    data = request.json
    data_from_form = request.form.to_dict()
    print(data_from_form)
    DB['products'].append(Product(name=data.get('name'),
                                  description=data.get('description'),
                                  img_name=data.get('img_name'),
                                  price=data.get('price')
                                  )
                          )
    return render_template('add_product.html', data=data['name'])


@products.route('/<uuid:uu_id>')
def show_product(uu_id):
    products_all = [product.__dict__ for product in DB['products']]
    product_to_show = None
    for product in products_all:
        if str(uu_id) in product.values():
            product_to_show = product
    return render_template('product_info.html', product=product_to_show)
