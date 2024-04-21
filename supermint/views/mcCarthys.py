from flask import views, render_template, Blueprint
from sqLite.utils import get_db_connection

mcCarthys = Blueprint("mcCarthys", __name__)


@mcCarthys.route("/")
def home():

    conn = get_db_connection()
    quizzes = conn.execute('SELECT * FROM quiz').fetchall()
    conn.close()
    print(quizzes)
    return render_template("mccarthys.html", quizzes=quizzes)