from flask import Flask
from views.mcCarthys import mcCarthys
from views.home import home
from views.giraf import giraf

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(mcCarthys, url_prefix="/mccarthys")
app.register_blueprint(giraf, url_prefix="/giraf")


if __name__ == "__main__":
    app.run(debug=True)

