import os

from flask import Flask, request, render_template, \
     flash, session, url_for, redirect

from util import db

app = Flask(__name__)

app.secret_key = os.urandom(32)

#---------- Main Page ----------
@app.route("/")
def home():
    return render_template("home.html")

#---------- Login/Register----------
@app.route("/login")
def login():
    if "logged_in" in session:
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/auth")
def authenticate():
    try:
        if db.auth_user(request.args["user"], request.args["password"]):
            session["logged_in"] = request.args["user"]
            return redirect(url_for("home"))
        else:
            flash("username or password is incorrect")
            return redirect(url_for("login"))
    except:
        flash("Something went wrong :(")
        return redirect(url_for("home"))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/adduser")
def add_user():
    try:
        if(not request.args["user"].strip() or not request.args["password"] or not request.args["confirm_password"]):
            flash("Please fill in all fields")
            return redirect(url_for("register"))

        if(db.check_user(request.args["user"])):
            flash("User already exists")
            return redirect(url_for("register"))

        if(request.args["password"] != request.args["confirm_password"]):
            flash("Passwords don't match")
            return redirect(url_for("register"))

        db.add_user(request.args["user"], request.args["password"])
        session["logged_in"] = request.args["user"]
    except:
        flash("Something went wrong :(")
    return redirect(url_for("home"))

#---------- Logout ----------
@app.route("/logout")
def logout():
    try:
        session.pop("logged_in")
    finally:
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.debug = True
    app.run()
