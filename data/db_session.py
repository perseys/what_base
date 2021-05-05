import sqlalchemy.ext.declarative as dec

import sqlalchemy.orm as orm
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session

SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(server, database, username, password):
    global __factory

    if __factory:
        return

    if not server and not database:
        raise Exception("Необходимо указать сервер и/или имя базы данных.")

    driver = '{SQL Server}'
    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

    # print(f"Подключение к базе данных по адресу {connection_string}")

    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    engine = create_engine(connection_url)

    __factory = orm.sessionmaker(bind=engine)

    SqlAlchemyBase.metadata.create_all(engine)

def create_session() -> Session:
    global __factory
    return __factory()
