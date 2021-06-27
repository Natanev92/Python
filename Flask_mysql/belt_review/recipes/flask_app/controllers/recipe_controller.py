from flask import render_template, request, session, redirect

from flask_app import app
from ..models.user import User
from ..models.recipe import Recipe


@app.route("/recipes/new")
def new_recipe_form():
    return render_template("new_recipe.html", all_users = User.get_all_users())

@app.route("/recipes/create", methods = ['POST'])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    Recipe.create(request.form)

    return redirect('/dashboard')


@app.route("/recipes/<int:recipe_id>")
def show_recipe(recipe_id):
    return render_template("show_recipe.html", get_one_recipe = Recipe.get_one_recipe({'id': recipe_id}))


@app.route("/recipes/<int:recipe_id>/delete")
def delete_recipe(recipe_id):
    Recipe.delete_recipe({'id': recipe_id})
    
    return redirect("/recipes/<int:recipe_id>")


@app.route("/recipes/<int:recipe_id>/edit")
def edit_recipe_form(recipe_id):

    return render_template("edit_recipe.html", recipes = Recipe.get_one_recipe({'id': recipe_id}))


@app.route("/recipes/<int:recipe_id>/update", methods = ['POST'])
def update_recipe(recipe_id):
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/{recipe_id}/edit')

    data = {
        "id": recipe_id,
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "time": request.form['time']
    }
    Recipe.update_recipe(data)

    return redirect(f"/recipes/{recipe_id}")

# @app.route("/dashboard")
# def dashboard1():
#     if "uuid" not in session:
#         return redirect("/")
#     return render_template("dashboard.html", get_all_recipes = Recipe.get_all_recipes())