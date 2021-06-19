from flask import Flask, render_template, request, session, redirect

from user import User


app = Flask(__name__)
app.secret_key = "enduro patrol."


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

if __name__ == "__main__":
    app.run(debug= True) 
