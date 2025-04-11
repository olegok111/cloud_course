import MySQLdb
from flask import g, current_app
import click


def get_db_connection() -> MySQLdb.Connection:
    if 'dbconn' not in g:
        g.dbconn = MySQLdb.connect(
            current_app.config['HOST'],
            current_app.config['DATABASE_USER'],
            db=current_app.config['DATABASE_NAME'],
            port=current_app.config['DATABASE_PORT'],
            password=current_app.config['DATABASE_PASSWORD']
        )

    return g.dbconn


def close_db_connection(e=None):
    conn = g.pop('dbconn', None)

    if conn is not None:
        conn.close()


# @click.command('initdb')
def init_db_command():
    """Wipe all data in database (if it's present) and create tables."""

    conn = get_db_connection()

    with current_app.open_resource("schema.sql", "r") as script_file:
        queries = script_file.read().split(b";")[:-1]
        for schema_query in queries:
            conn.query(schema_query)

        conn.commit()

    click.echo("Database initialized.")


def init_app(app):
    app.teardown_appcontext(close_db_connection)
    # app.cli.add_command(init_db_command)
