from flask import Flask, render_template, request, session, redirect, url_for, flash, g
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_db
import random
import functools

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM hospital WHERE id = ?', (user_id,)
        ).fetchone()

@login_required
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/send_user_data", methods=['POST'])
def user_data():
    name = request.form['name']
    dob = request.form['dob']
    bg = request.form['bg']

    db = get_db().cursor()

    db.execute(
        'INSERT INTO user (name, dob, bog)'
        ' VALUES (?, ?, ?)',
        (name, dob, bog)
    )
    id = db.lastrowid

    db.commit()
    return id

@app.route("/getHospital")
def getHospital():
    db = get_db()

    hospitals = db.execute(
        'SELECT name, location FROM hospital'
    ).fetchall()

    hospital = random.choice(hospitals) # Proprietary algorithm

    return hospital

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        location = request.form['location']
        db = get_db()
        error = None

        if not name:
            error = 'Hospital Name is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM hospital WHERE name = ?', (name,)
        ).fetchone() is not None:
            error = 'Hospital {} is already registered.'.format(name)

        if error is None:
            db.execute(
                'INSERT INTO hospital (name, password, location) VALUES (?, ?, ?)',
                (name, generate_password_hash(password), location)
            )
            db.commit()
            print("ran")
            return redirect(url_for('login'))

        flash(error)

    return render_template('register.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        error = None

        db = get_db()
        hospital = db.execute(
            'SELECT * FROM hospital WHERE name = ?', (name,)
        ).fetchone()

        if hospital is None:
            error = "Hospital not found"
        elif not check_password_hash(hospital["password"], password):
            error = "Incorrect password"
            
        if error is None:
            session.clear()
            session['user_id'] = hospital['id']
            return redirect(url_for('home'))
        flash(error)

    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))