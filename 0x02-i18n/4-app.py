#!/usr/bin/env python3
"""
Parametrize templates.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    """
    Config class.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "utc"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
app.url_map.strict_slashes = False


@app.route('/')
def index() -> str:
    """
    This is the home route.
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Gets the locale for a web page.

    returns:
            str = best match.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])



if __name__ == '__main__':
    app.run(debug=True)
