from flask import views, render_template, Blueprint
from sqLite.utils import get_db_connection, dict_factory
import json

mcCarthys = Blueprint("mcCarthys", __name__)


@mcCarthys.route("/")
def home():

    conn = get_db_connection()
    conn.row_factory=dict_factory
    quizzes = conn.execute('SELECT * FROM quiz').fetchall()

    conn.close()
    return render_template("mccarthys.html", quizzes=quizzes)