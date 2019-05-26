import os

from flask import Flask, render_template, request, flash, session, url_for, redirect

from util import db, coord

app = Flask(__name__)

app.secret_key=os.urandom(32)

@app.route("/")
def home():
	if "logged_in" in session:
		data = db.get_watchlist(session["logged_in"])
		return render_template("home.html", title = "Home", heading = "Hello " + session["logged_in"] + "!", user = session["logged_in"], logged_in = True)
	return render_template("home.html", title = "Home", heading = "Hello Guest!", logged_in = False)

# ================Accounts================
@app.route("/auth", methods = ["GET", "POST"])
def auth():
	return_page = "home"

	for each in request.form:
		if request.form[each] == "Login":
			return_page = each

	given_user = request.form["username"]
	given_pwd = request.form["password"]
	if db.auth_user(given_user, given_pwd):
		session["logged_in"] = given_user
		return redirect(url_for(return_page))
	else:
		flash("Username or password is incorrect")
		return redirect(url_for("login"))

@app.route("/login")
def login():
	return render_template("login.html", title = "Login", heading = "Login", type = "home")

#Sends the user to the register.html to register a new account
@app.route("/register")
def register():
	return render_template("register.html", title = "Register", heading = "Register")

#Attempts to add the user to the database
@app.route("/adduser")
def add_user():
    if(not request.args["user"].strip() or not request.args["password"] or not request.args["confirm_password"]):
            flash("Please fill in all fields")
            return redirect(url_for("register"))

    if(db.user_exist(request.args["user"])):
            flash("User already exists")
            return redirect(url_for("register"))

    if(request.args["password"] != request.args["confirm_password"]):
            flash("Passwords don't match")
            return redirect(url_for("register"))

    db.add_user(request.args["user"], request.args["password"])
    session["logged_in"] = request.args["user"]
    return redirect(url_for("home"))

#Logs the user out and removes session
#returns to the page the user was on previously
@app.route("/logout")
def logout():
	if session.get("logged_in"):
		session.pop("logged_in")
		# print(session)
	return redirect(url_for("home"))

# ================Watchlist================
@app.route("/watchlist")
def load_wl():
    status = "logged_in" in session
    if status:
        locations = db.get_watchlist(status)
        return render_template("watchlist.html", title = "Watchlist", heading = "Watchlist", watchlist = locations, logged_in=status)
    else:
        flash ("Please login to view Watchlist")
        return render_template("login.html", title = "Login", heading = "Login")

@app.route("/change_wl", methods = ["GET", "POST"])
def change_wl():
    location = request.args["city"]
    lat = request.args["lat"]
    longi = request.args["long"]
    if request.args["update"] == "Add to watchlist":
        db.add_watchlist(session["logged_in"], location, lat, longi)
    elif request.args["update"] == "Remove from watchlist":
        db.remove_watchlist(session["logged_in"], location, lat, longi)
    return redirect(url_for("load_info", city = location, lat = lat, long = longi))
	
# ================search================
@app.route("/search")
def load_results():
    status = "logged_in" in session
    location = request.args["search_location"]
    if (location == ""):
        flash ("Please enter a location")
    result = coord.getOptions(location)
    if (len(result) < 1):
        flash ("No location found. Please try again.")
    on_watchlist = {}
    if "logged_in" in session:
        for each in result:
            on_watchlist[each[1]] = db.check_watchlist(session["logged_in"], each[0], str(each[4]), str(each[5]))
    #print(on_watchlist)
    return render_template("search.html", title = "Search Results", heading = "Search Results for \"" + location + "\"", result=result, on_watchlist=on_watchlist, logged_in=status)

# ================info================
@app.route("/info")
def load_info():
    status = "logged_in" in session
    locations = db.get_watchlist(status)
    loc_name = request.args["city"]
    lat = request.args["lat"]
    longi = request.args["long"]
    on_watchlist = False
    if "logged_in" in session:
        on_watchlist = db.check_watchlist(session["logged_in"], loc_name, lat, longi)
    return render_template("info.html", title = loc_name, heading = loc_name, logged_in = status, latitude=lat, longitude=longi, location=loc_name, on_watchlist=on_watchlist)

if __name__ == "__main__":
        app.debug = True
        app.run()
