from flask import views, render_template, Blueprint, request, redirect, url_for, flash
from sqLite.utils import get_db_connection, dict_factory

submit = Blueprint("submit", __name__)


@submit.route("/", methods=["POST", "GET"])
def home():
    conn = get_db_connection()
    conn.row_factory=dict_factory

    print(request.form)
    print(request.method)
    if request.method == "POST":
        if "action" in request.form:
            if request.form["action"] == "Submit New User":
                addNewUser(request, conn)
            elif request.form["action"] == "Submit New User":
                print("New quiz submitted")
            return redirect(url_for("submit.home"))

    elif request.method == "GET":
        pageToRender = render_page(conn)
        conn.close()
        return pageToRender

def render_page(conn):
    # fetch users
    userQuery = ''' SELECT id, * FROM user
    ORDER BY first_name'''

    users = conn.execute(userQuery).fetchall()

    topicQuery = ''' SELECT id, * FROM topic
    ORDER BY name'''

    topics = conn.execute(topicQuery).fetchall()
    return render_template("submit.html", users=users, topics=topics)



def addNewUser(request, conn):
    firstName = request.form["firstName"]
    lastName = request.form['lastName']
    pseudonym = request.form['pseudonym']

    if not firstName:
        flash("First Name is required")
    elif not lastName:
        flash("Last Name needed")
    elif not pseudonym:
        flash("Pseudonym required")

    newUserQuery = '''INSERT INTO user (first_name, last_name, pseudonym)
    VALUES (?, ?, ?)'''

    conn.execute(newUserQuery, (firstName, lastName, pseudonym))
    conn.commit()
    conn.close()
