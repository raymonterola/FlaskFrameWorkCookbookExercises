import requests
from flask import render_template_string, redirect, url_for, request, Blueprint

from .models import MESSAGES

hello2 = Blueprint('hello2', __name__, url_prefix='/hello')


@hello2.errorhandler(requests.exceptions.ConnectionError)
def on_error(e):
    print(e)
    return str(e)


@hello2.route("/")
def index():
    return render_template_string('''
    <img src="/mystatic/images.jpeg" title="bird"><img src="{{ url_for('static', filename='images.jpeg') }}" title="bird">
    ''')


@hello2.route("/message")
def message():
    return redirect(url_for('hello2.get_message', key='default'))


@hello2.route("/message/<key>", methods=["GET"])
def get_message(key):
    return MESSAGES.get(key) or '%s not found' % key


@hello2.route("/message/<key>/", methods=["POST"])
def create_message(key):
    MESSAGES[key] = request.get_json().get('message')
    return MESSAGES.get(key), 201
