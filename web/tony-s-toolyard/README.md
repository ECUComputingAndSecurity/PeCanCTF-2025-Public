# Tony's Toolyard

## Writeup

The link leeds to a website that appears to be a toolyard online shop.

![image](https://github.com/user-attachments/assets/627186d2-140b-4858-bcf8-e3865e934ca8)

searching in this field shows up a table of results:

![image](https://github.com/user-attachments/assets/4b2a9a96-e083-4329-a237-e2a89593db69)
This is likely done through either an SQL databse, or storing the data in a json/csv file.

Checking the robots.txt file returns:

```
User-agent: *
Disallow: /main.pyi
Disallow: /user
Disallow: /secret/hints.txt
```

This is a massive hint, it shows two useful clues. Going to `/secret/hints.txt`, returns:

```
1. I wonder what that .pyi file was about?
2. I hope none of the normal users use common passwords...
    Hash Cracking's a pain.
3. I really like cookies. Eating them, baking them, giving them out; its all so fun.
```

It seems this provides some hints to get the flag, it accents that `main.pyi` file, it clues that some user has a common password that we need to `hashcrack` at some point, and then the `cookies` likely refer to some cookie manipulation.

Looking at the `main.pyi` file downloads a flask python script that looks like a copy of the internal server python file:

```python
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

```

Looking at this with the knowledge that the next step will likely be hash crakcing, means that we need to somehow get a password hash. With how the system appears to be using an SQL database, this will likely be through SQL injection. There are three sections of the code where the SQL databse is accessed:

1. When the system checks if the user is correctly logged in
2. When the user searches for a product
3. When the user attempts to login.

As the system checking if the user is logged in is a preset sql command, there is no way to manipulate that for SQL injection.
When the user searches for a product, and when they attempt to log in though, the SQL statement includes the users input meaning that it could be used for SQL injection:

```python
@app.route("/search", methods=["GET"])
def search():
 ...
 item = request.args.get("item", "")
 ...
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
...
...
@app.route("/login", methods=["GET", "POST"])
def login():
 userID = request.cookies.get("userID")
 if request.method == "POST":
  username = request.form.get("username", "")
  password = sha256(request.form.get("password", "").encode('utf-8')).hexdigest()
...
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
...
```

In each of these cases, the implementation of how the user's input is used changes. From looking at the `sqlite` documentation (the import used by the server for handeling sql), is seems that `login()` uses the correct method, where `sqlite` parses the input for SQL injection for the user, and `search()`, instead just uses python concatonation without any regard for security. Here's how the documentation suggests you do it, you will notice this is the same way the `login()` function uses:

```python
con = sqlite3.connect(":memory:")
cur = con.cursor()

...

# This is the qmark style used in a SELECT query:
params = (1972,)
cur.execute("SELECT * FROM lang WHERE first_appeared = ?", params)
print(cur.fetchall())
con.close()
```

This difference means, that `search()` is susceptible to SQL injection.
The server using `sqlite` as such let's create some mysql injections to use.
First as a test `hammer' OR 1=1;--`:

![image](https://github.com/user-attachments/assets/3f0c804e-95ec-4d05-bef1-b832cdc6ff09)

As can be seen, this query returns everything, meaning that we just did a successful MySQL injection. Now onto making one to get us that password hash we were looking for.
As can be seen in the `login()` function's SQL query, there is a table called `Users`, that has the fields `userID`, `username`, and `password`. So we want to write a query which grabs all the users and their passwords. As just appending another SQL query to the end of the previous one would cause the `search()` python code to throw an error and not return anything, due to `cursor.execute` only allowing one query to be run, we need a way to append the answer we want onto the search results without adding a whole other query.
Luckily, SQL has a way to do this, it is called `Union`, it lets you append to query results together into one result, as long as the two queries have the same number of fields. The `search()` query gets just two fields returned `name`, and `price`. Luckily, we only care about the users `username`, and `password`, so we can deal with just two fields.
So, the required SQL query for us is:
`SELECT name, price FROM Products WHERE name LIKE '%e' UNION SELECT username, password FROM Users;--%';`
To get this we need to enter `e' UNION SELECT username, password FROM Users;--` into the search bar.
This returns:

![image](https://github.com/user-attachments/assets/394e4d3e-0416-4e4d-9fc1-790311cca1f3)

```
Name: Admin - Price: $0000000000000000000000000000000000000000000000000000000000000000

Name: Jerry - Price: $059a00192592d5444bc0caad7203f98b506332e2cf7abb35d684ea9bf7c18f08
```

This shows two users `Admin`, and `Jerry`, along with their password.
As we can see in the `main.pyi` file, the passwords are stored in sha256 hashes:

```
def login():
 ...
 password = sha256(request.form.get("password", "").encode('utf-8')).hexdigest()
 ...
```

This means that the `Admin` password is likely nonexistant, so they might be signing in through some backdoor, but `Jerry`'s password looks legit.
As the `/secret/hints.txt` file hints that some users might have weak passwords, this is likely the password to hashcrack. putting the hash into [crackstation.net](https://crackstation.net/) returns that the hash used was sha256, and the password is `1qaz2wsx`.

Signing in as `Jerry`, using that password at `/login`:

![image](https://github.com/user-attachments/assets/84bb6b17-3a72-458e-a30e-c036a21d39a7)

This seemed to work, as there is now a `My Profile` page:

![image](https://github.com/user-attachments/assets/acba0e93-ae9d-4ba5-a434-ed89daa3a40d)

Going here reveals a webpage with what seems to be text that Jerry put there himself:

![image](https://github.com/user-attachments/assets/572e8b5f-2dfa-4f9f-96f5-64f202806923)

That doesn't lead anywhere, so lets go back to the `/secret/hints.txt` file, it hints that after hashcracking, some cookie manipulation will need to be done. Checking the current cookies the user has after logging in reveal two, a `userID` cookie, and a `user` cookie:

![image](https://github.com/user-attachments/assets/08bc2acf-f769-4323-9a72-a3e84c7b5589)

Looking through the code for how these cookies are generated and what they are used for, shows that the `user` cookie is used to detect if the user has loggedin correctly in `is_logged_in()`. This function is only used in the `viewUser()` function which returns the user's `My Profile`. But `userID` appears to be the one that is actually used to register which user's profile wants to be viewed.
This is strange, as the `user` cookie is a hash, that combines the user's password hash with a secret key meaning it can't be cracked, but `userID` is  just an integer storing the user's `userID`, it isn't encyrpted in anyway, meaning it can just be directly edited.
changing the `userID` from `2` to `0` and reloading the page gets:

![image](https://github.com/user-attachments/assets/f2ab70c8-9604-4e51-9ef2-9cabd33ccf69)

That confirms the theory, that the `userID` is what shows the user's profile, as rather then an error saying we weren't allowed, it was one saying that that user doesn't exist. Setting `userID` to `1` and reloading gets:

![image](https://github.com/user-attachments/assets/24941c20-5260-49ff-a01c-db29cd25f466)

This shows the flag. `pecan{T0ny'5_T00ly4rd._1_H0p3_Y0u_H4d_Fun_SQL1ng,_H45H_Cr4ck1ng,_4nd_W1th_C00k13_M4n1pu74t10n}`
This is likely the Admin's profile page, and the profile IDs just start at `1`.
