# Project imports
import repository as repo

from psycopg2.extras import RealDictCursor


def insert_in_client_table(conn, valor1, valor2, valor3, valor4):
    """get products from client database

    Args:
        shop_id (int)

    """
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as curs:
            curs.execute(repo.insert_into, (valor1, valor2, valor3, valor4))