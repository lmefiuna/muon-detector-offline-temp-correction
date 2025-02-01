from ..IMuonCrossRepository import IMuonCrossRepository


import pymysql
from pymysql.connections import Connection
from sshtunnel import SSHTunnelForwarder
import logging


class MuonCrossPyMySQLRepository(IMuonCrossRepository):

    __connection: Connection

    def __init__(self, connection: Connection) -> None:
        self.__connection = connection

    def getTMB3ByStartAndEndTimestamp(self, start_timestamp: int, end_timestamp: int):
        # TODO: wrap start of connection and instantiation of cursor
        # TODO: map result to entity or value object
        with self.__connection:
            with self.__connection.cursor() as cursor:
                sql = """
                    SELECT `timestamp`, `TMB3`
                      FROM muon_cross mc
                     WHERE `timestamp` BETWEEN %s AND %s
                     ORDER BY `timestamp` ASC;
                """

                cursor.execute(sql, (start_timestamp, end_timestamp))

                for table in cursor.fetchall():
                    print(table)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    with SSHTunnelForwarder(
        ('', 22),
        ssh_username='',
        ssh_password='',
        remote_bind_address=('127.0.0.1', 3306)
    ) as tunnel:

        connection = pymysql.connect(
            host='127.0.0.1',
            port=tunnel.local_bind_port,
            user='',
            password='',
            database=''
        )

        MuonCrossPyMySQLRepository(
            connection).getTMB3ByStartAndEndTimestamp(1737203946, 1737203952)
