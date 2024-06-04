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
    addNewUser(request.form, conn)
    users = fetchUsers(conn)
    conn.close()
    return jsonify(users)


@submit.route("/topic", methods=["POST"])
def newTopic():
    conn = get_db_connection()
    conn.row_factory=dict_factory
    try:
        addNewTopic(request.form, conn)
    except:
        print("Error happened")

    topics = fetchTopics(conn)
    conn.close()
    return jsonify(topics)


@submit.route("/quiz", methods=["POST"])
def newQuiz():
    conn = get_db_connection()
    conn.row_factory=dict_factory
    validity = addNewQuiz(request.form, conn)
    conn.close()
    return redirect(validity)

def render_page(conn):
    users = fetchUsers(conn)
    topics = fetchTopics(conn)
    locations = fetchLocations(conn)


    return render_template("submit.html", users=users, topics=topics, locations=locations)


def fetchUsers(conn):
    userQuery = ''' SELECT id, * FROM user
    ORDER BY first_name'''
    return conn.execute(userQuery).fetchall()

def fetchTopics(conn):
    topicQuery = ''' SELECT id, * FROM topic
    ORDER BY name'''
    return conn.execute(topicQuery).fetchall()

def fetchLocations(conn):
    locationQuery = ''' SELECT id, * FROM location
    ORDER BY name'''
    return conn.execute(locationQuery).fetchall()



def addNewUser(requestForm, conn):
    firstName = requestForm["firstName"]
    lastName = requestForm['lastName']
    pseudonym = requestForm['pseudonym']

    validInput=True
    if not firstName or firstName == '':
        validInput=False
    if not lastName or lastName == '':
        validInput=False
    if not pseudonym or pseudonym == '':
        validInput=False

    if validInput:
        newUserQuery = '''INSERT INTO user (first_name, last_name, pseudonym)
        VALUES (?, ?, ?)'''

        conn.execute(newUserQuery, (firstName, lastName, pseudonym))
        conn.commit()

def addNewTopic(requestForm, conn):
    topic = requestForm["topicName"]
    validInput=True
    if not topic or topic == '':
        validInput=False

    if validInput:
        newUserQuery = '''INSERT INTO topic (name)
        VALUES (?)'''

        conn.execute(newUserQuery, (topic,))
        conn.commit()

    return validInput

def addNewQuiz(requestForm, conn):
    quizId = addQuizToDb(requestForm["quizTitle"], requestForm["locationId"], requestForm["googleDriveLink"], requestForm["hostDate"], conn)
    addRoundsToDb(json.loads(requestForm["rounds"]), conn, quizId)
    addAuthorsToDb(requestForm["authors"].strip().split(","), quizId, conn)
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
