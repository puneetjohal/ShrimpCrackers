import sqlite3
DB_FILE = "data/info.db"

def create_tables():
    """Creates tables for users' info, portfolios, users' stocks and watchlist"""
    db = sqlite3.connect("../" + DB_FILE)
    c = db.cursor()
    command = "CREATE TABLE user_info (username TEXT, password TEXT)"
    c.execute(command)

    command = "CREATE TABLE watchlist (username TEXT, stock_name TEXT)"
    c.execute(command)

    db.commit() #save changes
    db.close()  #close database

#login / register routes
def add_user(username, password):
    """Insert the credentials for newly registered users into the database"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO user_info VALUES(?, ?)", (username, password))
    db.commit() #save changes
    db.close()  #close database

def auth_user(username, password):
    """Authenticate user attempting to log in"""
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

def add_watchlist(user, new_watchlist):
    """Inserts a new watchlist stock into the db for a users watchlist"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    if (check_watchlist(user, new_watchlist)):
        db.close()
        return False
    c.execute("INSERT INTO watchlist VALUES(?, ?)", (user, new_watchlist))

    db.commit()
    db.close()
    return True

def rmv_user(user):
    """Remove the portfolio info of user"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("DELETE FROM portfolio WHERE username = '{}'".format(user))

    db.commit()
    db.close()

def remove_watchlist(user, rmv_watchlist_name):
    """Remove the stock rmv_watchlist_name from the watchlist for user."""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("DELETE FROM watchlist WHERE username = '{}' and stock_name = '{}'".format(user, rmv_watchlist_name))

    db.commit()
    db.close()

def check_watchlist(user, company_name):
    """Check to see if the user already has the stock in the watchlist."""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    for each in c.execute("SELECT watchlist.stock_name FROM watchlist WHERE username = '{}'".format(user)):
        if(each[0] == company_name):
            db.close()
            return True

    db.close()
    return False

def get_watchlist(user):
    """Gets all the watchlist stocks for the user."""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    watchlist_data = []
    ret_val = c.execute("SELECT watchlist.stock_name FROM watchlist WHERE username = '{}'".format(user))
    for each in ret_val:
        companyCode = each[0]
        watchlist_data.append([0, companyCode])

    db.close()
    return watchlist_data