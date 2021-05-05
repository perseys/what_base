from flask import jsonify
from flask_restful import Resource, abort

from data import db_session
from data.budget import Budget


class BudgetResource(Resource):
    def get(self, budget_id):
        session = db_session.create_session()
        budget = session.query(Budget).get(budget_id)
        if not budget:
            abort(404, message=f"Budget id: {budget_id} not found")
        return jsonify(budget.to_dict(only=('name', 'id')))


class BudgetListResource(Resource):
    def get(self):
        session = db_session.create_session()
        budgets = session.query(Budget).all()
        return jsonify([item.to_dict(only=('name', 'id')) for item in budgets],)
