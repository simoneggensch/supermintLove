from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is the main page"

@app.route("mccarthys")
def mcCarthys():
    return "page for quizzes at McCarthy's"

if __name__ == "__main__":
    app.run()

    