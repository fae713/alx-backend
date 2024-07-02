from flask import Flask, render_template
from flask_babel import Babel, gettext as _


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "utc"


app = Flask(__name__)
babel = Babel(app)
app.url_map.strict_slashes = False
app.config.from_object(Config)


@app.route('/')
def home():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)