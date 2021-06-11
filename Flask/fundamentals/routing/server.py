from flask import Flask #impoting the Flask class
app=Flask(__name__) #creating an instance of the Flask class

# the '@' decorator associates the route with the following function
@app.route("/") # '/' is the index route 
def index():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/flask")
def say_flask():
    return "Hi Flask!"

@app.route("/say/<name>")
def say(name):
    return f"Hi {name}!"

#path variable/ route variable
@app.route("/hello/<name>")
def hello(name):
    return f"Hello there. General {name}!"

@app.route("/repeat/35/hello")
def repeat():
    return "Hello!" * 35

@app.route("/repeat/80/bye")
def bye():
    return "Bye!" * 80

@app.route("/repeat/99/dogs")
def dogs():
    return "Dogs!" * 99

if __name__ == "__main__":
    app.run (debug= True)