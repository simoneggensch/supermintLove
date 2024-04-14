from flask import Flask, render_template
import sqlite3
from model.quiz.McCarthys import McCarthys

app = Flask(__name__)


class QuizLocation:
    name = ""
    webLocation = ""

    def __init__(self, name, webLocation):
        self.name = name
        self.webLocation = webLocation


def get_db_connection():
    conn = sqlite3.connect('sqLite/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    mcCarthys = QuizLocation("mcCarthy's", "/mccarthys")
    giraf = QuizLocation("Giraf", "/giraf")
    return render_template("home.html", locations= [mcCarthys, giraf])

@app.route("/mccarthys")
def mcCarthys():

    conn = get_db_connection()
    quizzes = conn.execute('SELECT * FROM quiz').fetchall()
    conn.close()
    print(quizzes)
    return render_template("mccarthys.html", quizzes=quizzes)

@app.route("/giraf")
def giraf():
    return "page for quizzes at Giraf"

if __name__ == "__main__":
    app.run()

