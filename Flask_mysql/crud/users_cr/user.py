from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        # data is a Dictionary that holds all of user's data
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.create_at = data['create_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_users(cls):
        #write out our mysql query
        query = "SELECT * FROM users;"

        #query the database using connectToMySQL function
        results = connectToMySQL("users_schema").query_db(query)

        #print(results)
        users = []

        #results is a list of Dictionaries 
        # row is my loop variable that holds each Dictionary 
        for row in results:
            users.append(User(row)) # adding User objects to the list

        return users


    @classmethod
    def create(cls, data):
        #data is a Dictionary with all of the POST data from the form
        query = "INSERT into users (first_name, last_name, email, create_at, updated_at)" \
            "VALUES(%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW())"

        connectToMySQL("users_schema").query_db(query, data)

        return User