import os

from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hi, it`s WHAT app"


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
