from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))

DB_NAME=os.path.join(basedir,"database.db")
