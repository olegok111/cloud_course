from flask import Blueprint, render_template, request, current_app
from werkzeug.exceptions import abort
from MySQLdb.cursors import DictCursor
from MySQLdb import OperationalError
from MySQLdb._exceptions import ProgrammingError

from todoapp.db import get_db_connection


bp = Blueprint("todolist", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    try:
        conn = get_db_connection()
    except OperationalError as mysql_err:
        if mysql_err.args[0] == 2002:
            return render_template("err.html", err_text="Database is unavailable.", debug_info=[current_app.config, mysql_err])
        else:
            return render_template("err.html", err_text="Unknown database error.", debug_info=[current_app.config, mysql_err])

    c = DictCursor(conn)

    try:
        c.execute("DESCRIBE todo_list;")
    except ProgrammingError as mysql_err:
        if mysql_err.args[0] == 1146:
            with current_app.open_resource("schema.sql", "r") as script_file:
                queries = script_file.read().split(";")[:-1]
                for schema_query in queries:
                    conn.query(schema_query)

                conn.commit()
        else:
            return render_template("err.html", err_text="Unknown database error.", debug_info=[current_app.config, mysql_err])

    if request.method == "POST":
        task = request.form['task']

        if task:
            c.execute(
                "INSERT INTO todo_list (task) VALUES (%s)",
                (task,)
            )
            conn.commit()

    c.execute(
        "SELECT id, task FROM todo_list;"
    )
    todo_list = c.fetchall()
    return render_template("index.html", todo_list=todo_list)
