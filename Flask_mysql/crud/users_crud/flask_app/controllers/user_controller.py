from flask import render_template, request, session, redirect

from flask_app import app
from ..models.user import User



@app.route("/")
def index():
    all_users = User.get_all_users()

    return render_template("read.html", all_users = all_users)


@app.route("/user/new")
def new_user_form():
    return render_template("create.html")


@app.route("/user/create", methods = ["POST"])
def create_user():

    User.create(request.form)

    return redirect("/")


@app.route("/user/<int:user_id>")
def show_user(user_id):
    this_user = User.get_one({'id': user_id})

    return render_template("show_user.html", user = this_user)


@app.route("/user/<int:user_id>/delete")
def delete_user(user_id):
    User.delete({'id': user_id})
    
    return redirect("/")


@app.route("/user/<int:user_id>/edit")
def edit_user_form(user_id):

    return render_template("edit_user.html", user = User.get_one({'id': user_id}))


@app.route("/user/<int:user_id>/update", methods = ['POST'])
def update_user(user_id):
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": user_id
    }
    User.update(data)

    return redirect(f"/user/{user_id}")