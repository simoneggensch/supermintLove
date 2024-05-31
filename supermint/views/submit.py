from flask import views, render_template, Blueprint, request, redirect, url_for, flash, jsonify
from sqLite.utils import get_db_connection, dict_factory
import json

submit = Blueprint("submit", __name__)


@submit.route("/", methods=["GET"])
def home():
    conn = get_db_connection()
    conn.row_factory=dict_factory

    pageToRender = render_page(conn)
    conn.close()
    return pageToRender

@submit.route("/user", methods=["POST"])
def newUser():
    conn = get_db_connection()
    conn.row_factory=dict_factory
    validity = addNewUser(request.form, conn)
    conn.close()
    return redirect(validity)


@submit.route("/topic", methods=["POST"])
def newTopic():
    conn = get_db_connection()
    conn.row_factory=dict_factory
    validity = addNewTopic(request.form, conn)
    conn.close()
    return redirect(validity)


@submit.route("/quiz", methods=["POST"])
def newQuiz():
    conn = get_db_connection()
    conn.row_factory=dict_factory
    validity = addNewQuiz(request.form, conn)
    conn.close()
    return redirect(validity)

def render_page(conn):
    # fetch users
    userQuery = ''' SELECT id, * FROM user
    ORDER BY first_name'''
    users = conn.execute(userQuery).fetchall()

    topicQuery = ''' SELECT id, * FROM topic
    ORDER BY name'''
    topics = conn.execute(topicQuery).fetchall()

    
    locationQuery = ''' SELECT id, * FROM location
    ORDER BY name'''
    locations = conn.execute(locationQuery).fetchall()
    return render_template("submit.html", users=users, topics=topics, locations=locations)



def addNewUser(requestForm, conn):
    firstName = requestForm["firstName"]
    lastName = requestForm['lastName']
    pseudonym = requestForm['pseudonym']

    validInput=True
    if not firstName or firstName == '':
        flash("First Name is required")
        validInput=False
    if not lastName or lastName == '':
        flash("Last Name needed")
        validInput=False
    if not pseudonym or pseudonym == '':
        flash("Pseudonym required")
        validInput=False

    if validInput:
        newUserQuery = '''INSERT INTO user (first_name, last_name, pseudonym)
        VALUES (?, ?, ?)'''

        conn.execute(newUserQuery, (firstName, lastName, pseudonym))
        conn.commit()
        flash("New User Added")

    return validInput

def addNewTopic(requestForm, conn):
    topic = requestForm["topicName"]
    validInput=True
    if not topic or topic == '':
        flash("Topic Name is required")
        validInput=False

    if validInput:
        newUserQuery = '''INSERT INTO topic (name)
        VALUES (?)'''

        conn.execute(newUserQuery, (topic,))
        conn.commit()
        flash("New Topic Added")

    return validInput

def addNewQuiz(requestForm, conn):
    print(requestForm)
    quizId = addQuizToDb(requestForm["quizTitle"], requestForm["locationId"], requestForm["googleDriveLink"], requestForm["hostDate"], conn)
    addRoundsToDb(json.loads(requestForm["rounds"]), conn, quizId)
    addAuthorsToDb(requestForm["authors"].strip().split(","), quizId, conn)

    print("should commit now")
    conn.commit()
    
def addQuizToDb(quizTitle, locationId, googleDriveURL, hostDate, conn):
    quizQuery = 'INSERT INTO quiz (title, location_id, google_slides_url, date_hosted) VALUES (?, ?, ?, ?)'
    cursor = conn.cursor()
    cursor.execute(quizQuery,(quizTitle, locationId, googleDriveURL, hostDate))
    return cursor.lastrowid

def addRoundsToDb(rounds, conn, quizId):
    for roundNumber, round in enumerate(rounds):
        roundQuery = 'INSERT INTO round (name, description, round_number, quiz_id, topic_id) VALUES (?, ?, ?, ?, ?)'
        conn.execute(roundQuery, (round["name"], round["description"], roundNumber + 1, quizId, round["topic"]))

def addAuthorsToDb(authors, quizId, conn):
    for author in authors:
        authorQuery = 'INSERT INTO author (quiz_id, user_id) VALUES (?, ?)'
        conn.execute(authorQuery, (quizId, author))
