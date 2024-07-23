import sqlite3
from .queries import Queries

class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        # контекстный менеджер
        with sqlite3.connect(self.path) as connect:
            connect.execute(Queries.CREATE_SURVEY_TABLE)
            connect.execute(Queries.DROP_CATEGORIES)
            connect.execute(Queries.CREATE_CATEGORIES_TABLE)
            connect.execute(Queries.POPULATE_CATEGORIES)
            connect.execute(Queries.DROP_DISHES)
            connect.execute(Queries.CREATE_DISHES_TABLE)
            connect.execute(Queries.POPULATE_DISHES)

    def execute(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as connect:
            connect.execute(query, params)

    def fetch(self, query: str, params: tuple = None, fetchmany: bool = True):
        with sqlite3.connect(self.path) as connect:
            result = connect.execute(query, params)

            return result.fetchall()
