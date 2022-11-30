from werkzeug.exceptions import abort

import ccy
from flask import Blueprint, render_template, request, redirect, url_for

from .models import PRODUCTS

product_app = Blueprint('product', __name__)


@product_app.route('/', methods=["GET"])
def home():
    return render_template('products/home.html', products=PRODUCTS)


@product_app.route('/<key>')
def get_product(key):
    product = PRODUCTS.get(key)
    if product is None:
        abort(404)
    return render_template('products/product.html', product=product)


@product_app.route("/", methods=["POST"])
def create_product():
    data = request.form.to_dict()
    print(data)
    price = int(data.get('price'))
    product = {
        'name': data.get('name'),
        'category': data.get('category'),
        'price': price
    }
    PRODUCTS[product['name'].lower().replace(' ', '-')] = product
    return redirect(url_for('product.home'))


@product_app.context_processor
def product_name_processor():
    def full_name(product):
        return f'{product["category"]} / {product["name"]}'
    return {'full_name': full_name}


@product_app.add_app_template_filter
def currency_filter(amount):
    print(request.accept_languages, request.accept_languages.best)
    currency_code = ccy.countryccy(request.accept_languages.best[-2:])
    return f'{currency_code} {amount}'
