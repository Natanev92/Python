from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "super secure"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["languages"] = request.form.getlist("language")
    session["comment"] = request.form["comment"]
    return redirect('/result')

@app.route('/result')
def show_user_info():
    return render_template("result.html", name = session["name"], location = session["location"], languages=session["languages"], comment = session["comment"] )

if __name__ == "__main__":
    app.run(debug=True)