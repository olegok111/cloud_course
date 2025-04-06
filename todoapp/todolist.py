from flask import Blueprint, render_template, request
from werkzeug.exceptions import abort
from MySQLdb.cursors import DictCursor

from todoapp.db import get_db_connection


bp = Blueprint("todolist", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    c = DictCursor(conn)

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
