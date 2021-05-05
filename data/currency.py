import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Currency(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'currency'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    iso = sqlalchemy.Column(sqlalchemy.String, nullable=True)
