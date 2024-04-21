from flask import Blueprint, render_template
import sqlite3
from model.quiz.McCarthys import McCarthys
from sqLite.utils import get_db_connection


views = Blueprint("views", __name__)

