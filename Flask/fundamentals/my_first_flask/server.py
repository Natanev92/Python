from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template ("this is the index route")
# path variable / route variable
@app.route("/hello/<name>")
def hello(name):
    return f"Hello There, General {name}!"

@app.route("/success")
def success():
    return render_template("another.html")

@app.route("/users/<username>/<id>")
def show_user(username, id):
    return f"username: {username}, id: {id}"

if __name__ == "__main__":
    app.run(debug = True)