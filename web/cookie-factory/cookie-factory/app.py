import threading
import secrets, string
import os
import time
from playwright.sync_api import sync_playwright
import sqlite3
from flask import Flask, request, session, redirect, render_template, jsonify
import hashlib
import random

app = Flask(__name__)
app.config['SESSION_COOKIE_HTTPONLY'] = False
app.secret_key = os.urandom(32)
DB_PATH = 'users.db'
flag = 'pecan{d3l1c10u5_c00k135_55bMgl9j5BIl}'

general_responses = [
    "Did you know? Some cookies can be shared through clever content. Isn’t that sweet?",
    "We love seeing creative uses of links and tags. Sometimes they reveal delicious surprises.",
    "Our admin does regular quality checks on every message. Freshly baked, every time.",
    "Imagine if someone could 'taste' another person's cookie... Good thing that's not possible, right?",
    "Cookies are meant to be enjoyed by everyone. Why limit access?",
    "Ever wondered where your browser sends your cookies? Neither have we.",
    "The chat is a great place to showcase your web skills. Our admin reviews them personally.",
    "Don't be shy, share your sweetest creations. Who knows who might take a bite.",
]

special_responses = [
    (3, "document.cookie", "Mmm, cookies straight from the jar! Be careful though, some are marked 'private stock'."),
    (2, "onerror", "Errors are just happy little accidents. Sometimes they reveal secret recipes."),
    (2, "<iframe", "We love layering flavors. Iframes are like putting cookies inside cookies."),
    (2, "<svg", "Decorative toppings always make our cookies stand out. SVG sprinkles included!"),
    (1, "<script", "Oh, adding your own 'secret ingredients' to the batch? Bold move!"),
    (1, "<img", "Images not loading? That’s fine, broken cookies are still delicious."),
]

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if os.path.exists('users.db'):
        os.remove('users.db')

    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            receiver TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    alphabet = string.ascii_letters + string.digits + string.punctuation
    admin_password = ''.join(secrets.choice(alphabet) for _ in range(16))

    conn.execute("INSERT INTO users (username, password, role) VALUES (?, ?, 'admin')",
                ('admin', hashlib.sha256(admin_password.encode()).hexdigest()))
    conn.commit()

    with open('admin_password.txt', 'w') as f:
        f.write(admin_password)

    print(f"[INIT] Admin password generated and saved to admin_password.txt")

@app.before_request
def protect_routes():
    if request.endpoint in ['dashboard', 'send', 'messages', 'logout'] and 'username' not in session:
        return redirect('/login')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username.isalnum() or len(username) > 20:
            return jsonify(success=False, message="Invalid username. Use only letters & numbers, max 20 chars.")

        if len(password) < 6:
            return jsonify(success=False, message="Password too short (min 6 characters).")

        conn = get_db()
        cur = conn.execute("SELECT * FROM users WHERE LOWER(username) = LOWER(?)", (username,))
        if cur.fetchone():
            return jsonify(success=False, message="Username already taken.")

        conn.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, 'user')",
            (username, hashlib.sha256(password.encode()).hexdigest())
        )
        conn.commit()

        return jsonify(success=True, redirect_url='/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db()
        cur = conn.execute(
            "SELECT * FROM users WHERE LOWER(username) = LOWER(?) AND password = ?",
            (username, hashlib.sha256(password.encode()).hexdigest())
        )
        user = cur.fetchone()

        if user:
            session['username'] = user['username']
            session['role'] = user['role']
            return jsonify(success=True)

        return jsonify(success=False, message="Invalid username or password.")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    show_flag = None
    if session.get('role') == 'admin':
        show_flag = flag
    return render_template('dashboard.html', username=session['username'], role=session['role'], flag=show_flag)

@app.route('/send', methods=['POST'])
def send():
    if 'username' not in session:
        return jsonify(success=False, message="Not logged in."), 401

    msg = request.form['message']

    if len(msg) > 1000:
        return jsonify(success=False, message="Message too long (max 1000 characters)."), 400

    conn = get_db()
    conn.execute("INSERT INTO messages (username, receiver, content) VALUES (?, ?, ?)",
             (session['username'], 'admin', msg))
    conn.commit()

    if session['username'] != 'admin':

        time.sleep(random.uniform(1.5, 2.5))


        matched = None
        for priority, keyword, response in special_responses:
            if keyword.lower() in msg.lower():
                if matched is None or priority > matched[0]:
                    matched = (priority, response)

        if matched:
            reply = matched[1]
        else:
            reply = random.choice(general_responses)

        conn.execute("INSERT INTO messages (username, receiver, content) VALUES (?, ?, ?)",
             ('admin', session['username'], reply))
        conn.commit()

    return jsonify(success=True)

@app.route('/messages')
def messages():
    conn = get_db()
    if session.get('role') == 'admin':
        cur = conn.execute("""
            SELECT username, receiver, content FROM messages
            WHERE receiver = 'admin' AND username != 'admin'
            ORDER BY id DESC
            LIMIT 10
        """)
        rows = cur.fetchall()
        messages = [{'username': row['username'], 'receiver': row['receiver'], 'content': row['content']} for row in rows]
        messages.reverse()
    else:
        cur = conn.execute("""
            SELECT username, receiver, content FROM messages
            WHERE username = ? OR receiver = ?
            ORDER BY id ASC
        """, (session['username'], session['username']))
        messages = [{'username': row['username'], 'receiver': row['receiver'], 'content': row['content']} for row in cur.fetchall()]

    msgs = [{'username': row['username'], 'content': row['content']} for row in messages]
    return jsonify(msgs)

@app.route('/changelog')
def changelog():
    return render_template('changelog.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

def admin_bot_loop():
    with open('admin_password.txt', 'r') as f:
        admin_password = f.read().strip()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        def login_admin():
            print("[BOT] Logging in admin...")
            page.goto("http://localhost:5000/login")
            page.fill('input[name="username"]', 'admin')
            page.fill('input[name="password"]', admin_password)
            page.click('button[type="submit"]')
            page.wait_for_timeout(500)
            print("[BOT] Logged in.")


        login_admin()

        while True:
            try:
                print("[BOT] Refreshing dashboard...")
                page.goto("http://localhost:5000/dashboard")
                page.wait_for_timeout(1000)


                if "/dashboard" not in page.url:
                    print(f"[BOT] Unexpected page: {page.url}. Re-logging in.")
                    login_admin()

            except Exception as e:
                print(f"[BOT Error] {e}")

            time.sleep(5)

if __name__ == '__main__':
    init_db()
    threading.Thread(target=admin_bot_loop, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
