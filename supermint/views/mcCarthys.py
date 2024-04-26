from flask import views, render_template, Blueprint
from sqLite.utils import get_db_connection, dict_factory
from itertools import groupby
import json

from model.quiz.McCarthys import McCarthys

mcCarthys = Blueprint("mcCarthys", __name__)


@mcCarthys.route("/")
def home():

    # create connection to DB
    conn = get_db_connection()
    conn.row_factory=dict_factory

    # fetch quizzes
    quizQuery = ''' SELECT q.id as quiz_id, q.* FROM author a
    INNER JOIN quiz q on a.quiz_id = q.id
    WHERE a.quiz_location_id=1 group by q.id
    ORDER BY date_hosted DESC'''

    quizzes = conn.execute(quizQuery).fetchall()

    # fetch authors
    for quiz in quizzes:
        hostsQuery = f'''SELECT * from user u
        INNER JOIN author h on h.user_id=u.id
        WHERE h.quiz_id = {quiz['quiz_id']}'''
        
        hosts = conn.execute(hostsQuery).fetchall()

        quiz["authors"] = [host["pseudonym"] for host in hosts]

    conn.close()

    return render_template("mccarthys.html", quizzes=quizzes)