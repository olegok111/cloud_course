import MySQLdb
from flask import g, current_app


def get_db_connection() -> MySQLdb.Connection:
    if 'dbconn' not in g:
        g.dbconn = MySQLdb.connect(
            current_app.config['HOST'],
            current_app.config['DATABASE_USER'],
            db=current_app.config['DATABASE_NAME'],
            port=current_app.config['DATABASE_PORT']
        )

    return g.dbconn


def close_db_connection(e=None):
    conn = g.pop('dbconn', None)

    if conn is not None:
        conn.close()
