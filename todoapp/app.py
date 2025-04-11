from flask import Flask, render_template, g
import MySQLdb
import click
from todoapp.db import get_db_connection, close_db_connection


the_app = Flask(__name__)
the_app.config.from_pyfile("config.py")
init_app()

from todoapp import todolist
the_app.register_blueprint(todolist.bp)
the_app.add_url_rule("/", endpoint="index")


@the_app.cli.command("initdb")
def init_db():
    """Wipe all data in database (if it's present) and create tables."""

    conn = get_db_connection()

    with the_app.open_resource("schema.sql", "r") as script_file:
        queries = script_file.read().split(b";")[:-1]
        for schema_query in queries:
            conn.query(schema_query)

        conn.commit()

    click.echo("Database initialized.")


def init_app():
    the_app.teardown_appcontext(close_db_connection)
    the_app.cli.add_command(init_db)
