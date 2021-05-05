import pyodbc


class Sql:
    def __init__(self, database, server, username, password):
        connectionString = \
            f'Provider=MSOLEDBSQL;Server={server};Database={database};UID={username};PWD={password};'

        # self.cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
        #                            "Server=" + server + ";"
        #                             "Database=" + database + ";"
        #                                                                          "Trusted_Connection=yes;")
        self.cnxn = pyodbc.connect(connectionString)
        connection = pyodbc.connect(connectionString, autocommit=True)
        dbCursor = connection.cursor()

        # self.query = "-- {}\n\n-- Made in Python".format(datetime.now()
        #                                                  .strftime("%d/%m/%Y"))

        requestString = 'select id, name,iso from currency'
        dbCursor.execute(requestString)
        # for row in dbCursor:
        #     print(f'name:{row.name} id:{str(row.id)} iso:{row.iso}' + row.name + ' id:')
