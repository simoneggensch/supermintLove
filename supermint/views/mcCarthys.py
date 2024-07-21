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

    # fetch quizzes
    quizQuery = ''' SELECT q.id as quiz_id, q.* FROM author a
    INNER JOIN quiz q on a.quiz_id = q.id
    WHERE q.location_id=1 group by q.id
    ORDER BY date_hosted DESC'''

    quizzes = conn.execute(quizQuery).fetchall()

    # fetch authors and topics
    for quiz in quizzes:
        hosts = fetchAuthors(quiz['quiz_id'], conn)
        quiz["authors"] = [host["pseudonym"] for host in hosts]

        rounds = fetchRounds(quiz['quiz_id'], conn)
        quiz["rounds"] = rounds

    conn.close()

    return render_template("mccarthys.html", quizzes=quizzes)


def fetchAuthors(quiz_id, conn):
        hostsQuery = '''SELECT * from user u
        INNER JOIN author auth on auth.user_id=u.id
        WHERE auth.quiz_id = ?'''
        
        return conn.execute(hostsQuery, (quiz_id,)).fetchall()

def fetchRounds(quiz_id, conn):
        roundsQuery = '''SELECT t.name as topic, r.* from round r
        INNER JOIN topic t on t.id = r.topic_id
        WHERE quiz_id = ?
        ORDER BY round_number'''


        return conn.execute(roundsQuery, (quiz_id,)).fetchall()

