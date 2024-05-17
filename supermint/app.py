from flask import Flask
from views.mcCarthys import mcCarthys
from views.home import home
from views.giraf import giraf
from views.submit import submit

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(mcCarthys, url_prefix="/mccarthys")
app.register_blueprint(giraf, url_prefix="/giraf")
app.register_blueprint(submit, url_prefix="/submit")

app.config['SECRET_KEY'] = 'your secret key'

if __name__ == "__main__":
    app.run(debug=True)

