from flask import Blueprint, render_template
from model.quiz.McCarthys import McCarthys
from model.QuizLocation import QuizLocation

home = Blueprint("home", __name__)

@home.route("/")
def homePage():
    mcCarthys = QuizLocation("McCarthy's", "mccarthys")
    giraf = QuizLocation("Giraf", "giraf")
    return render_template("home.html", locations= [mcCarthys, giraf])

