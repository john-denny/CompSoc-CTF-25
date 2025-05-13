# An SQL Injectable Flask app
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'compsocgalwaysodafjhaiopaehrttklhfajdskahfnbkjahfjkasdhfjksadhfdkljahsdfakl')")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    
    return render_template_string("""
        <h1>Welcome to an SQL App</h1>
    	<form action="/login" method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    """)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}'"
    c.execute(query)
    user = c.fetchone()
    conn.close()

    if user:
        return f"Welcome, {user[1]}! The flag is CompSoc{{0N3!=0}}"
    else:
        return "Login failed. Invalid credentials."

if __name__ == '__main__':
    app.run(host="0.0.0.0")
