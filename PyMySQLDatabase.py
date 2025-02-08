from IDatabase import IDatabase

from pymysql import Connection, connect, MySQLError
from pymysql.cursors import DictCursor


class PyMySQLDatabase(IDatabase):
    host: str
    port: int
    user: str
    password: str
    database: str
    connection: Connection | None

    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self) -> None:
        try:
            self.connection = connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                cursorclass=DictCursor
            )
        except MySQLError as e:
            print(f"Error connecting to MySQL: {e}")
            self.connection = None

    def close(self) -> None:
        if self.connection:
            self.connection.close()

    def execute_query(self, query: str, params: tuple = None) -> None:
        if not self.connection:
            raise ConnectionError("Database not connected")

        with self.connection.cursor() as cursor:
            cursor.execute(query, params or ())
            self.connection.commit()

    def fetch_one(self, query: str, params: tuple = None) -> dict:
        if not self.connection:
            raise ConnectionError("Database not connected")

        with self.connection.cursor() as cursor:
            cursor.execute(query, params or ())
            return cursor.fetchone()

    def fetch_all(self, query: str, params: tuple = None) -> list[dict]:
        if not self.connection:
            raise ConnectionError("Database not connected")

        with self.connection.cursor() as cursor:
            cursor.execute(query, params or ())
            return cursor.fetchall()
