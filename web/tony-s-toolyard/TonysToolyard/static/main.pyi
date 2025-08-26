from flask import Flask, request, render_template, make_response, redirect
import sqlite3
import time
from hashlib import sha256

app = Flask(__name__, static_url_path='')

global SECRET_LOGIN_TOKEN
SECRET_LOGIN_TOKEN = 'REDACTED'

def is_logged_in(request):
	cookie =  request.cookies.get("user")
	results = []
	conn = sqlite3.connect("file:database.db?mode=ro", uri=True)
	try:
		cursor = conn.cursor()
		query = "SELECT username, password FROM Users;"
		cursor.execute(query)
		results = cursor.fetchall()
	except Exception as e: 
		errorOccured = True
		results = str(e)
	finally:
		cursor.close()
		conn.close()
	if not results: return False
	global SECRET_LOGIN_TOKEN
	for name, password in results:
		if sha256(f"{name}:{password}:{SECRET_LOGIN_TOKEN}".encode('utf-8')).hexdigest(): return True
	return False
    

@app.route("/", methods=["GET"])
def index():
	userID = request.cookies.get("userID")
	return render_template("index.html", logged_in=bool(userID), user_id=userID)

@app.route("/search", methods=["GET"])
def search():
	userID = request.cookies.get("userID")
	item = request.args.get("item", "")
	results = []
	searched = False
	errorOccured = False
	if item:
		searched = True
		conn = sqlite3.connect("file:database.db?mode=ro", uri=True)
		try:
			cursor = conn.cursor()
			query = "SELECT name, price FROM Products WHERE name LIKE '%" + str(item) + "%';"
			cursor.execute(query)
			results = cursor.fetchall()
		except Exception as e: 
			errorOccured = True
			print(e)
			results = str(e)
		finally:
			cursor.close()
			conn.close()
			
	return render_template("index.html", results=results, searched=searched, errorOccured=errorOccured, logged_in=bool(userID), user_id=userID)

@app.route("/login", methods=["GET", "POST"])
def login():
	userID = request.cookies.get("userID")
	if request.method == "POST":
		username = request.form.get("username", "")
		password = sha256(request.form.get("password", "").encode('utf-8')).hexdigest()
		results = []
		conn = sqlite3.connect("file:database.db?mode=ro", uri=True)
		try:
			cursor = conn.cursor()
			query = "SELECT userID, username, password FROM Users WHERE username = ? AND password = ?;"
			cursor.execute(query, (username, password))
			results = cursor.fetchall()
		except Exception as e: 
			return render_template("login.html", error=str(e))
		finally:
			cursor.close()
			conn.close()
	
		if results:
			resp = make_response(redirect("/"))
			userID = str(results[0][0])
			resp.set_cookie("userID", userID)
			global SECRET_LOGIN_TOKEN
			resp.set_cookie("user", sha256(f"{results[0][1]}:{results[0][2]}:{SECRET_LOGIN_TOKEN}".encode('utf-8')).hexdigest())
			return resp
		else:
			return render_template("login.html", error="Invalid credentials", logged_in=bool(userID), user_id=userID)

	return render_template("login.html", error=None, logged_in=bool(userID), user_id=userID)

@app.route("/logout")
def logout():
    resp = make_response(redirect("/"))
    resp.set_cookie("user", "", expires=0)
    resp.set_cookie("userID", "", expires=0)
    return resp
    
@app.route("/user", methods=["GET"])
def viewUser():
	userID = request.cookies.get("userID")
	if not is_logged_in(request) or not userID: return make_response(redirect("/login"))
	try: 
		userID = int(userID)
		with open("users/" + str(userID)) as f:
			return render_template("user.html", text=f.read().splitlines(), logged_in=True)
	except: return render_template("user.html", text=[f"Error: {str(userID)} is not a valid user ID"], logged_in=True)
	

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
