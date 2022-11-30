from os import path

from flask import Flask

instance_path = path.abspath('./my_instance_folder')
app = Flask(__name__, static_folder='../static', static_url_path='/mystatic', instance_path=str(instance_path),
            instance_relative_config=True)
app.config.from_pyfile('config.cfg')

# must import modules containing the views or blueprints
from app.hello import views
from app.hello2 import views
