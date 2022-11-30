import requests

from flask import render_template_string, redirect, url_for, request, make_response

from app import app

from .models import MESSAGES


@app.errorhandler(requests.exceptions.ConnectionError)
def on_error(e):
    print(e)
    return str(e)


@app.route("/")
def index():
    return render_template_string('''
    <img src="/mystatic/images.jpeg" title="bird"><img src="{{ url_for('static', filename='images.jpeg') }}" title="bird">
    ''')


@app.route("/message")
def message():
    return redirect(url_for('get_message', key='default'))


@app.route("/message/<key>", methods=["GET"])
def get_message(key):
    return MESSAGES.get(key) or '%s not found' % key


@app.route("/message/<key>/", methods=["POST"])
def create_message(key):
    MESSAGES[key] = request.get_json().get('message')
    return MESSAGES.get(key), 201
