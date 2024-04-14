from flask import Flask, render_template
from model.quiz.McCarthys import McCarthys

app = Flask(__name__)


class QuizLocation:
    name = ""
    webLocation = ""

    def __init__(self, name, webLocation):
        self.name = name
        self.webLocation = webLocation

@app.route("/")
def home():
    mcCarthys = QuizLocation("mcCarthy's", "/mccarthys")
    giraf = QuizLocation("Giraf", "/giraf")
    return render_template("home.html", locations= [mcCarthys, giraf])

@app.route("/mccarthys")
def mcCarthys():
    quizzes=[]
    quiz1 = McCarthys()
    quiz1.Name = "My First quiz"
    quiz1.Authors = ["me", "you"]
    quizzes.append(quiz1)
    return render_template("mccarthys.html", quizzes=quizzes)

@app.route("/giraf")
def giraf():
    return "page for quizzes at Giraf"

if __name__ == "__main__":
    app.run()

