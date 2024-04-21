from flask import views, render_template, Blueprint
from sqLite.utils import get_db_connection

giraf = Blueprint("giraf", __name__)


@giraf.route("/")
def home():
    return "page for quizzes at Giraf"