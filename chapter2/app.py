import datetime

from flask import Flask, render_template
from markupsafe import Markup


class MomentJS(object):
    def render(self, fmt):
        return Markup(
            '<script type="application/javascript">document.write(moment().%s);</script>' % fmt)

    def fromNow(self):
        return self.render('fromNow()')

    def format(self, fmt):
        return self.render('format(\"%s\")' % fmt)


app = Flask(__name__, static_folder='./static', static_url_path='/static')
app.config.from_object('config.BaseConfig')

from product.views import product_app

app.register_blueprint(product_app, url_prefix='/product')

app.jinja_env.globals['now'] = datetime.datetime.now
app.jinja_env.globals['momentjs'] = MomentJS


@app.route('/')
def index():
    return render_template('hello.html', user='John Doe')


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
