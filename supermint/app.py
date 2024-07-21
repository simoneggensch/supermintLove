from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from views.mcCarthys import mcCarthys
from views.home import home
from views.giraf import giraf
from views.submit import submit
from views.edit import edit
from views.auth import auth
from sqLite.models.admin import WebsiteUser
from sqLite import db, DB_NAME


def create_app():
    app = Flask(__name__)

    app.register_blueprint(home)
    app.register_blueprint(mcCarthys, url_prefix="/mccarthys")
    app.register_blueprint(giraf, url_prefix="/giraf")
    app.register_blueprint(submit, url_prefix="/submit")
    app.register_blueprint(edit, url_prefix="/edit")
    app.register_blueprint(auth, url_prefix="/")


    app.config['SECRET_KEY'] = 'your secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SECURITY_PASSWORD_SALT'] = "MY_SECRET"
    app.config['SECURITY_REGISTERABLE'] = True
    app.config['SECURITY_SEND_REGISTER_EMAIL'] = False


    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def loadAdmin(id):
        return WebsiteUser.query.get(int(id))

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

