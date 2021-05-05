from flask import jsonify
from flask_restful import Resource, abort

from data import db_session
from data.currency import Currency


class CurrencyResource(Resource):
    def get(self, currency_id):
        session = db_session.create_session()
        currency = session.query(Currency).get(currency_id)
        if not currency:
            abort(404, message=f"Currency id: {currency_id} not found")
        return jsonify(currency.to_dict(only=('name', 'iso', 'id')))

        # def delete(self, news_id):
        #     abort_if_news_not_found(news_id)
        #     session = db_session.create_session()
        #     news = session.query(News).get(news_id)
        #     session.delete(news)
        #     session.commit()
        #     return jsonify({'success': 'OK'})


class CurrencyListResource(Resource):
    def get(self):
        session = db_session.create_session()
        currency = session.query(Currency).all()
        return jsonify([item.to_dict(only=('name', 'id', 'iso')) for item in currency])

    # def post(self):
    #     args = parser.parse_args()
    #     session = db_session.create_session()
    #     news = News(
    #         title=args['title'],
    #         content=args['content'],
    #         user_id=args['user_id'],
    #         is_published=args['is_published'],
    #         is_private=args['is_private']
    #     )
    #     session.add(news)
    #     session.commit()
    #     return jsonify({'success': 'OK'})
