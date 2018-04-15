# Import necessary modules
from flask import Flask, render_template, request, send_from_directory
from pyqrcode import create as qrgen
from re import match

# Creating the Flask app
app = Flask(__name__)

# Route user to the index (home) page
@app.route("/")
def index():
    return render_template("index.html")

# Route user to the registration page
@app.route("/register", methods=["GET"])
def signup():
    return render_template("register.html")

# Handle submitted user data from registration
@app.route("/register", methods=["POST"])
def register():
    # Pull the data from the POST request
    data = request.form
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
    if not data["password"] == data["confirm"]:
        return render_template("register.html", e="Passwords do not match")
    # TODO Facilitate user's insertation into database
    # If registration is successful, send user to login page
    return render_template("login.html")

# Route user to the login page
@app.route("/login", methods=["GET"])
def get_login():
    return render_template("login.html")

# Handle submitted user data from login
@app.route("/login", methods=["POST"])
def login():
    # Pull the data from the POST request
    data = request.form
    # TODO Compare the submitted credentials with those in the database
    # TODO if something goes wrong, route back to login with error message, otherwise route to the rewards page
        return render_template("login.html", e="Invalid user credentials")
    # Send users to the rewards page if their login was successful
    return render_template("rewards.html")

# Route user to the rewards page
@app.route("/rewards")
def rewards():
    # TODO fetch the live point values from the database
    # Setting dummy demonstration pointss
    points = 42
    # Setting dummy demonstration discounts
    # TODO Fetch the user's actual discounts
    codes = [["Starbucks", "Half off a cup of coffee", "WGWXEF"], ["Home Depot", "25% off painting supplies", "NEVSDF"], ["Taco Bell", "1 Free Doritos Loco Taco", "ATTCWT"]] # get_user_codes[user]
    # Present the rewards page with points and discounts
    return render_template("rewards.html", rewards=codes, points=points)

# Generate a QR code from the URL value
@app.route("/qr/<code>")
def qr(code):
    # Set the filename for the specific discount QR code
    f = code + ".svg"
    # Generate the QR object
    qr = qrgen(code)
    # Save the QR object in the QR files at size 16s
    qr.svg("./qrs/" + f, scale=16)
    # Serve the user the generated QR image
    return send_from_directory("./qrs", f)

if __name__ == "__main__":
    # Run on localhost, port 80, in debug mode
    app.run("127.0.0.1", 80, True)
