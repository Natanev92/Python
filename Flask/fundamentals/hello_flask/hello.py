from flask import Flask, render_template
# Import Flask to allow us to create our app
app = Flask(__name__)    
# Create a new instance of the Flask class called "app"
@app.route('/')          
# The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello There. General Kanobi!'  
    # Return the string '' as a response
if __name__=="__main__":   
# Ensure this file is being run directly and not from a different module
    @app.route('/hello/<name>')
    def hello(name):
        print(name)
        return "Hello there, " + name

    @app.route('/users/<username>/<id>') 
    def show_user_profile(username, id):
        print(username)
        print(id)
        return "username: " + username + ", id: " + id
    
    @app.route('/lists')
    def render_lists():
        user_info = [
            {'name' : 'Michael', 'last_name' : 'Choi', 'full_name': 'Michael Choi'},
            {'name' : 'John', 'last_name' : 'Legened', 'full_name':'John Legened' },
            {'name' : 'Marc', 'last_name' : 'Reyes', 'full_name':'Marc Reyes'},
            {'name' : 'Natan', 'last_name' : 'Villaseñor', 'full_name':'Natan Villaseñor'}
        ]
        return render_template ("lists.html", random_numbers = [3,1,5], user = user_info)


# app.run(debug=True) should be the very last statement! 
    app.run(debug=True)    
# Run the app in debug mode.

