from app import app
from app.hello2.views import hello2

app.register_blueprint(hello2)
