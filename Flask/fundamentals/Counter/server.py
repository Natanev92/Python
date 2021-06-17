from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "super secure"


@app.route('/')
def index():
    if 'visits' not in session: 
        session['visits'] = 1
    else:
        session['visits'] = session['visits'] + 1
    return render_template('index.html', visits = session['visits'])

@app.route('/destroy_session', methods = ["POST"])
def destroy_session():
    print("redirect")
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)