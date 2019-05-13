import os

from flask import Flask, render_template, request,flash, session,url_for,redirect

from util import db

app = Flask(__name__)

app.secret_key=os.urandom(32)

@app.route("/")
def home():
	if "logged_in" in session:
		data = db.get_watchlist(session["logged_in"])
		return render_template("home.html", title = "Home", heading = "Hello " + session["logged_in"] + "!", user = session["logged_in"], logged_in = True, watchilist_data = data)
	return render_template("home.html", title = "Home", heading = "Hello Guest!", logged_in = False)

#Authenticates user and adds session
#Returns to the page the user was on previously

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
		print(session)
	return redirect(url_for("home"))

# Depending on the current status, either adds or removes from the watchlist
# Returns to the original search page.
@app.route("/changeWatchlist", methods = ["GET", "POST"])
def changeWatchlist():
	print ("request.args: " )
	print ( request.args )
	print ( "\n ------------")

	for each in request.args:
		if request.args[each] == "Add to watchlist":
			data = each.split("{!{!!}!}")
			search = data[1]
			companyCode = data[0].lower()
			db.add_watchlist(session["logged_in"], companyCode)
		if request.args[each] == "Remove from watchlist":
			data = each.split("{!{!!}!}")
			search = data[1].replace("|~|~|", " ")
			companyCode = data[0].lower()
			db.remove_watchlist(session["logged_in"], companyCode)
	return redirect(url_for("stockResults", stock_info = search))

@app.route("/removeWatchlist", methods = ["GET", "POST"])
def removeWatchlist():
	print(request.args)
	for each in request.args:
		if request.args[each] == "Remove from watchlist":
			data = each.split("{!{!!}!}")
			companyCode = data[0]
			db.remove_watchlist(session["logged_in"], companyCode)
	return redirect(url_for("watchlist"))

@app.route("/watchlist")
def watchlist():
	if "logged_in" in session:
		watchlist_data = db.get_watchlist(session["logged_in"])
		for each in watchlist_data:
			each[0] = info.getStocks(each[1].lower())
		return render_template("watchlist.html", watchlist = watchlist_data, title = "Watchlist", heading = "Watchlist", logged_in = True)
	else:
		flash ("Please login to view Watchlist")
		return render_template("login.html", title = "Login", heading = "Login", type = "watchlist")#redirect(url_for("login"))

if __name__ == "__main__":
        app.debug = True
        app.run()
