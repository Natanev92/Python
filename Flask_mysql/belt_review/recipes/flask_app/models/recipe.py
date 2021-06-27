from ..config.mysqlconnection import connectToMySQL

from ..models import user

from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.time = data['time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.user = user


    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL("recipes_schema").query_db(query)
        recipes = []
        print(results)
        for row in results:
            recipes.append(Recipe(row)) 

        return recipes


    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (user_id, name, description, instruction, time, created_at, updated_at)" \
            "VALUES (%(user_id)s, %(name)s, %(description)s, %(instruction)s, %(time)s, NOW(), NOW());"

        return connectToMySQL("recipes_schema").query_db(query, data)


    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"

        results = connectToMySQL("recipes_schema").query_db(query, data)
        print(results[0])

        results_data= {
            "id": results[0]['id'],
            "user_id": results[0]['user_id'],
            "name": results[0]['name'],
            "description": results[0]['description'],
            "instruction": results[0]["instruction"],
            "time": results[0]['time'],
            "created_at": results[0]['created_at'],
            "updated_at": results[0]['updated_at'],
            "user": user.User.get_one({'id': results[0]['user_id']})
        }
        return Recipe(results_data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"

        return connectToMySQL("recipes_schema").query_db(query, data)

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, time = %(time)s, updated_at = NOW() WHERE id = %(id)s;"

        return connectToMySQL("recipes_schema").query_db(query, data)


    @staticmethod
    def validate_recipe(post_data):
        is_valid = True
        if len(post_data['name']) < 3:
            flash(" Recipe name must be at least 2 characters.")
            is_valid = False
        if len(post_data['description']) < 10:
            flash("Recipe description must be at least 10 characters.")
            is_valid = False
        if len(post_data['instruction']) < 10:
            flash("Instructions must be at least 10 characters.")
            is_valid = False

        return is_valid