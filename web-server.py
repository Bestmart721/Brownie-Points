from flask import Flask, render_template, request
from re import match
# from somewhere import new_user
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET"])
def signup():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    data = request.form
    if not match(r"[^@]+@[^@]+\.[^@]+", data["email"]):
        return render_template("register.html", e="Invalid email address format")
    if len(data["name"]) < 1:
        return render_template("register.html", e="Invalid name length")
    if not data["name"].replace(" ", "").isalpha():
        return render_template("register.html", e="Illegal characters in name")
    if len(data["password"]) < 8:
        return render_template("register.html", e="Password is too short")
    if not data["password"] == data["confirm"]:
        return render_template("register.html", e="Passwords do not match")
    return render_template("login.html")
    # new_user([data["name"], data["email"], data["password"]])

@app.route("/login", methods=["GET"])
def get_login():
    return render_template("/login")

@app.route("/login", methods=["POST"])
def login():
    data = request.form
    user = validate_creds(data["email"], data["password"])
    if not user:
        return render_template("login.html", e="Invalid user credentials")
    return render_template("index.html")
if __name__ == "__main__":
    app.run("127.0.0.1", 80, True)
