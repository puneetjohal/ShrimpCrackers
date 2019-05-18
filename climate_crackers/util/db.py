import sqlite3
import os

DIR = os.path.dirname(__file__) or '.'
DIR += '/../'

DB_FILE = DIR + "data/watchlist.db"

# ==================== Init ====================
def create_tables():
    """Creates tables for users' account info and watchlist."""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "CREATE TABLE user_info (username TEXT, password TEXT)"
    c.execute(command)

    command = "CREATE TABLE watchlist (username TEXT, location TEXT, latitude FLOAT, longitude FLOAT)"
    c.execute(command)

    db.commit() #save changes
    db.close()  #close database

# create_tables()

# ==================== User Authentication ====================
#login / register routes
def add_user(username, password):
    """Insert the credentials for newly registered users into the database."""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO user_info VALUES(?, ?)", (username, password))
    db.commit() #save changes
    db.close()  #close database

def auth_user(username, password):
    """Authenticate user attempting to log in."""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    for each in c.execute("SELECT user_info.username, user_info.password FROM user_info"):
        if(each[0] == username and each[1] == password):
            db.close()
            return True
    db.close()
    return False

def user_exist(username):
    """Check if a username has already been taken when registering."""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    for each in c.execute("SELECT user_info.username FROM user_info"):
        if(each[0] == username):
            db.close()
            return True
    db.close()
    return False

# ==================== Watchlist ====================
def check_watchlist(user, location, lat, longi):
    """Check to see if the user already has the location in the watchlist."""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    for each in c.execute("SELECT * FROM watchlist WHERE username =? ", (user,)):
        if(each[1] == location and str(each[2]) == lat and str(each[3]) == longi):
            print("already in wl")
            db.close()
            return True

    db.close()
    return False

def add_watchlist(user, new_location, new_lat, new_long):
    """Insert a new watchlist location into the db for a user's watchlist."""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    if (not check_watchlist(user, new_location, new_lat, new_long)):
        c.execute("INSERT INTO watchlist VALUES(?, ?, ?, ?)", (user, new_location, new_lat, new_long))

    db.commit()
    db.close()

def remove_watchlist(user, rmv_location, lat, longi):
    """Remove @rmv_location from the watchlist for user."""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("DELETE FROM watchlist WHERE username =? and location =? and latitude=? and longitude=?", (user, rmv_location, lat, longi))

    db.commit()
    db.close()

def get_watchlist(user):
    """Get all the watchlist location for the user."""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    watchlist_data = []
    for each in c.execute("SELECT * FROM watchlist WHERE username =?", (user,)):
        # print (each)
        temp = []
        for i in range (1,len(each)):
            temp.append(each[i])
        watchlist_data.append(temp)

    db.close()
    return watchlist_data

# add_watchlist("joyce","gz",30,20)
# add_watchlist("joyce","gz",20,30)
# add_watchlist("joyce","gz",20,30)
# add_watchlist("puneet","ny",10,10)
# add_watchlist("joyce","tx",30,30)
# remove_watchlist("joyce", "gz",30,20)
# print(get_watchlist("joyce"))
