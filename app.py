from flask import Flask, render_template, request, redirect, session
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key = "mysecretkey"

# Connect MySQL
db = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_NAME"),
    port=os.environ.get("DB_PORT")
)

# LOGIN PAGE
@app.route("/", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        cursor = db.cursor()

        query = """
        SELECT * FROM users
        WHERE username = %s AND password = %s
        """

        values = (username, password)

        cursor.execute(query, values)

        user = cursor.fetchone()

        if user:

            # SESSION START
            session["username"] = username

            return redirect("/dashboard")

        else:
            message = "Invalid Username or Password"

    return render_template("login.html", message=message)


# REGISTER PAGE
@app.route("/register", methods=["GET", "POST"])
def register():

    message = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        cursor = db.cursor()

        # Check existing username
        check_query = "SELECT * FROM users WHERE username = %s"

        cursor.execute(check_query, (username,))

        existing_user = cursor.fetchone()

        if existing_user:

            message = "Username already exists"

        else:

            query = """
            INSERT INTO users (username, password)
            VALUES (%s, %s)
            """

            values = (username, password)

            cursor.execute(query, values)

            db.commit()

            message = "Registration Successful"

    return render_template("register.html", message=message)


# DASHBOARD PAGE
@app.route("/dashboard")
def dashboard():

    # Check if user logged in
    if "username" in session:

        username = session["username"]

        return render_template(
            "dashboard.html",
            username=username
        )

    else:
        return redirect("/")


# LOGOUT
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


