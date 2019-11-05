from flask import Blueprint, render_template

supermarkets = Blueprint('supermarkets', __name__, url_prefix='/supermarkets',
                         template_folder='./supermarkets/templates')


@supermarkets.route('/')
def get_all_supermarkets():
    return render_template('supermarkets.html')
