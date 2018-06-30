import psycopg2
from .exceptions import DatabaseConnectionError


class Connector:

    _conn = None

    @staticmethod
    def connect(host, user, password, dbname, port, **kwargs):
        try:
            if not Connector._conn:
                Connector._conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port, **kwargs)
        except Exception as e:
            Connector._conn = None
            Connector.connect(host, user, password, dbname, port, **kwargs)
        finally:
            DatabaseConnectionError(e)
