from flask import Blueprint, render_template, request, url_for, redirect

from database import DB
from models import Supermarket

supermarkets = Blueprint('supermarkets', __name__,
                         url_prefix='/supermarket',
                         template_folder='./supermarkets/templates',
                         static_folder='./supermarkets/static')


@supermarkets.route('/', methods=['GET'])
def get_all_supermarkets():
    markets_all = [market.__dict__ for market in DB['supermarkets']]
    args = request.args.to_dict()
    return render_template('all_supermarkets.html',
                           markets_all=markets_all, args=args)


@supermarkets.route('/add', methods=['GET'])
def show_add_market_form():
    return render_template('add_supermarket.html')


@supermarkets.route('/', methods=['POST'])
def add_market():
    data = request.form.to_dict()
    DB['supermarkets'].append(Supermarket(name=data.get('name'),
                                      location=data.get('location'),
                                      img_name=data.get('img_name'),
                                      )
                          )
    return redirect(url_for('supermarkets.get_all_supermarkets'))


@supermarkets.route('/<uuid:uu_id>')
def show_market(uu_id):
    markets_all = [market.__dict__ for market in DB['supermarkets']]
    market_to_show = None
    for market in markets_all:
        if str(uu_id) in market.values():
            market_to_show = market
    return render_template('supermarket.html', market=market_to_show)
