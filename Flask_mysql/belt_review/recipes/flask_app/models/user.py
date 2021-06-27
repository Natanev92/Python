from ..config.mysqlconnection import connectToMySQL
from ..models import recipe
import re
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name= data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipe = []


    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("recipes_schema").query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        results = connectToMySQL("recipes_schema").query_db(query, data)

        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) " \
            "VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"

        user_id = connectToMySQL("recipes_schema").query_db(query, data)
        return user_id

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"

        return connectToMySQL("users1_schema").query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s;"

        results = connectToMySQL("recipes_schema").query_db(query, data)
        print(results)
        user = User(results[0])
        if results[0]["recipes.id"] != None:
            for row in results:
                row_data = {
                    'id': row['recipes.id'],
                    'user': user,
                    'name': row['name'],
                    'description': row ['description'],
                    'instruction': row ['instruction'],
                    'time': row ['time'],
                    'created_at': row['recipes.created_at'],
                    'updated_at': row['recipes.updated_at'],
                    'user_id': user.id
                }
                user.recipe.append(recipe.Recipe(row_data))
        return user


    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("recipes_schema").query_db(query)
        users = []
        for row in results:
            users.append(User(row)) 

        return users

    @classmethod
    def validate_email(cls,data):
        query = "SELECT email FROM users WHERE email = %(email)s;"
        results = connectToMySQL("recipes_schema").query_db(query,data)
        print(results)
        if len(results) == 0:
            return True
        if len(results) > 0:
            return False
        # this memthod allows
    @staticmethod
    def register_validator(post_data):
        is_valid= True

        if len(post_data['first_name']) < 2:
            flash("First name must be at least than 2 characters")
            is_valid = False
        if len(post_data['last_name']) < 2:
            flash("Last name must be at least than 2 characters")
            is_valid = False
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            flash("Email is in invalid format")
            is_valid = False
        elif not User.validate_email({'email':post_data['email']}):
            flash("user with this email already exsits")
            is_valid = False
            
        if len(post_data['password']) < 4:
            flash("Password must be at least 4 characters")
            is_valid = False
        if post_data['password'] != post_data['confirm_password']:
            flash("Password and confirm password must match")
            is_valid = False

        return is_valid

    @staticmethod
    def login_validator(post_data):
        user_from_db = User.get_by_email({'email': post_data['email']})
        if not user_from_db:
            flash("Invalid Credentials")
            return False
        
        if not bcrypt.check_password_hash(user_from_db.password, post_data['password']):
            flash("Invalid Credentials")
            return False

        return True

