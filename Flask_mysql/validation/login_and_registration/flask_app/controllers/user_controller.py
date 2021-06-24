from flask import render_template, request, request, session, redirect
from flask_bcrypt import Bcrypt

from flask_app import app

from ..models.user import User

bcrypt = Bcrypt(app)


@app.route("/")
def index():
    if "uuid" in session:
        return redirect("/dashboard")
    return render_template("index.html")


@app.route("/register", methods = ["POST"])
def register():
    if not User.register_validator(request.form):
        return redirect("/")

    hash_browns = bcrypt.generate_password_hash(request.form['password'])

    data ={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": hash_browns
    }

    user_id = User.create(data)
    session['uuid'] = user_id
    return redirect("/dashboard")


@app.route("/login", methods = ["POST"])
def login():
    data={"email": request.form['email']}
    user_from_db = User.get_by_email(data)

    if not user_from_db:
        return redirect("/")
    if not bcrypt.check_password_hash(user_from_db.password,request.form['password']):
        return redirect('/')

    session['uuid'] = user_from_db.id
    return redirect("/dashboard")



@app.route("/dashboard")
def dashboard():
    if "uuid" not in session:
        return redirect("/")
    return render_template("dashboard.html", user = User.get_by_id({"id": session['uuid']}))


@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")
