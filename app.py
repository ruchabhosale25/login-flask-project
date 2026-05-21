from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect MySQL
db = mysql.connector.connect(
    host="kodama.proxy.rlwy.net",
    user="root",
    password="OjZQwVuFZqdVzbtUVIcLzUZRfRFJgfyE",
    database="railway",
    port=34525
)

cursor = db.cursor()

@app.route("/", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        query = """
        SELECT * FROM users
        WHERE username = %s AND password = %s
        """

        values = (username, password)

        cursor.execute(query, values)

        user = cursor.fetchone()

        if user:
            message = "Login Successful"
        else:
            message = "Invalid Username or Password"

    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)