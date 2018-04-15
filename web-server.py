# Import necessary modules
from flask import Flask, render_template, request, send_from_directory, session, redirect
from pyqrcode import create as qrgen
from re import match
from BrownieFunc import Brownie
brownie = Brownie()

# Creating the Flask app
app = Flask(__name__)
app.secret_key = "6e737d4cdf8380b88dc5c3edee3d6d5c"

# Route user to the index (home) page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("index", code=302)

# Route user to the registration page
@app.route("/register", methods=["GET"])
def signup():
    try:
        uid = session["uid"]
        return redirect("/", code=302)
    except KeyError:
        return render_template("register.html")

# Handle submitted user data from registration
@app.route("/register", methods=["POST"])
def register():
    try:
        uid = session["uid"]
        return redirect("/", code=302)
    except KeyError:
        # Pull the data from the POST request
        data = request.form
        # Emails must match
        if not data["email"] == data["confirmEmail"]:
            return render_template("register.html", e="Emails do not match")
        # Validate the submitted email's format
        if not match(r"[^@]+@[^@]+\.[^@]+", data["email"]):
            return render_template("register.html", e="Invalid email address format")
        # Name should be at least one letter
        if len(data["name"]) < 1:
            return render_template("register.html", e="Invalid name length")
        # Name must not contain numbers or special characters (other than spaces)
        if not data["name"].replace(" ", "").isalpha():
            return render_template("register.html", e="Illegal characters in name")
        # Password must be at least 8 characters
        if len(data["password"]) < 8:
            return render_template("register.html", e="Password is too short")
        # Submitted passwords must match
        if not data["password"] == data["confirmPassword"]:
            return render_template("register.html", e="Passwords do not match")
        brownie.user_new(data["email"], data["name"], data["password"])
        # If registration is successful, send user to login page
        return render_template("login.html")

# Route user to the login page
@app.route("/login", methods=["GET"])
def get_login():
    try:
        uid = session["uid"]
        return redirect("/", code=302)
    except KeyError:
        return render_template("login.html")

# Handle submitted user data from login
@app.route("/login", methods=["POST"])
def login():
    try:
        uid = session["uid"]
        return redirect("/", code=302)
    except KeyError:
        # Pull the data from the POST request
        data = request.form
        print(data)
        a = brownie.user_login(data["email"], data["password"])
        print(a)
        if a is None:
            print("Case 1")
            return render_template("login.html", e="No account exists with that email")
        if not a:
            print("Case 2")
            return render_template("login.html", e="Incorrect password")
        session["uid"] = a
        print("Case D")
        return render_template("rewards.html")

# Route user to the rewards page
@app.route("/rewards")
def rewards():
    try:
        uid = session["uid"]
        points = brownie.user_get_points(session["uid"])
        discounts = brownie.user_get_discounts(session["uid"])
        return render_template("rewards.html", rewards=discounts, points=points)
    except KeyError:
        return redirect("/", code=302)

@app.route("/shop")
def shop():
    rewards = brownie.deal_get_all()
    try:
        uid = session["uid"]
        return render_template("shop.html", rewards=rewards)
    except KeyError:
        return redirect("/", code=302)

@app.route("/events")
def events():
    return render_template("events.html", events=events)

# Generate a QR code from the URL value
@app.route("/qr/<code>")
def qr(code):
    try:
        uid = session["uid"]
        # Set the filename for the specific discount QR code
        f = code + ".svg"
        # Generate the QR object
        qr = qrgen(code)
        # Save the QR object in the QR files at size 16s
        qr.svg("./qrs/" + f, scale=16)
        # Serve the user the generated QR image
        return send_from_directory("./qrs", f)
    except KeyError:
        return redirect("/", code=302)

if __name__ == "__main__":
    # Run on localhost, port 80, in debug mode
    app.run("127.0.0.1", 80, True)
