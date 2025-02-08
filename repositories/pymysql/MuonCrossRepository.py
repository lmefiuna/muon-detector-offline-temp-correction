from ..IMuonCrossRepository import IMuonCrossRepository


from IDatabase import IDatabase


class MuonCrossPyMySQLRepository(IMuonCrossRepository):

    __db: IDatabase

    def __init__(self, db: IDatabase) -> None:
        self.__db = db

    def getTMB3ByStartAndEndTimestamp(self, start_timestamp: int, end_timestamp: int) -> list[dict]:
        # TODO: map result to entity or value object
        sql = """
            SELECT `timestamp`, `TMB3`
              FROM muon_cross mc
             WHERE `timestamp` BETWEEN %s AND %s
             ORDER BY `timestamp` ASC;
        """
        return self.__db.fetch_all(sql, (start_timestamp, end_timestamp))


if __name__ == '__main__':
    from sshtunnel import SSHTunnelForwarder
    from PyMySQLDatabase import PyMySQLDatabase

    # logging.basicConfig(level=logging.DEBUG)

    with SSHTunnelForwarder(
        ('', 22),
        ssh_username='',
        ssh_password='',
        remote_bind_address=('127.0.0.1', 3306)
    ) as tunnel:

        db = PyMySQLDatabase(
            '127.0.0.1',
            tunnel.local_bind_port,
            '',
            '',
            ''
        )
        db.connect()

        muon_cross_repository = MuonCrossPyMySQLRepository(db)
        print(muon_cross_repository.getTMB3ByStartAndEndTimestamp(
            1737203946, 1737203952))
