import os

from flask import Flask, send_from_directory, render_template, make_response, jsonify
from flask_restful import Api, abort

from config import Config
from data import db_session, currency_resources, budget_resources
from data.budget import Budget
from data.currency import Currency

app = Flask(__name__)
app.config.from_object(Config)

db_session.global_init(Config.server, Config.database, Config.username, Config.password)

api = Api(app)
api.add_resource(currency_resources.CurrencyListResource, '/api/currency')
api.add_resource(currency_resources.CurrencyResource, '/api/currency/<int:currency_id>')

api.add_resource(budget_resources.BudgetListResource, '/api/budget')
api.add_resource(budget_resources.BudgetResource, '/api/budget/<string:budget_id>')


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='WHAT')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/currency")
@app.route("/currency/")
def currency():
    db_sess = db_session.create_session()
    row = db_sess.query(Currency).all()
    return render_template("row.html", row=row, title='Currency')


@app.route('/currency/<string:iso>', methods=['GET', 'POST'])
def currency_iso(iso):
    db_sess = db_session.create_session()
    row = db_sess.query(Currency).filter(Currency.iso == iso).all()
    if len(row) ==0:
        abort(404, message=f"Currency iso: {iso} not found")
    return render_template("row.html", row=row, title=f'Currency ISO:{iso}')


@app.route("/budget")
@app.route("/budget/")
def budget():
    db_sess = db_session.create_session()
    row = db_sess.query(Budget).all()
    return render_template("budget.html", row=row, title='Budget')


@app.route('/budget/<string:id>', methods=['GET', 'POST'])
def budget_id(id):
    db_sess = db_session.create_session()
    row = db_sess.query(Budget).filter(Budget.id == id).all()
    return render_template("budget.html", row=row, title=f'Budget id:{id}')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    # app.run(port=8080, host='127.0.0.1')
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", '127.0.0.1')
    app.run(host=host, port=port)
