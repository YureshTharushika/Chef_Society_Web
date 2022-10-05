from PIL import Image
import os
from flask import Blueprint, render_template, redirect, flash
from bson.objectid import ObjectId
from website.forms import RecipeForm
from .extensions import mongo, firebase
from flask_login import login_required, current_user
from datetime import datetime


views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route("/recipes", methods=['GET', 'POST'])
@login_required
def recipes():

    recipes = mongo.db.recipes.find()

    return render_template("recipes.html", recipes=recipes, user=current_user, )


@views.route("/recipes/new", methods=['GET', 'POST'])
@login_required
def addrecipe():

    name = None
    ingredients = None
    instructions = None
    image = None
    form = RecipeForm()

    if form.validate_on_submit():
        name = form.name.data
        # form.name.data = ''
        ingredients = form.ingredients.data
        # form.ingredients.data = ''
        instructions = form.instructions.data
        # form.instructions.data = ''
        image = form.image.data
        # form.image.data = None

        opened_image = Image.open(image)
        resized_image = opened_image.resize((600, 400))

        if opened_image.format == 'JPEG':
            resized_image.save("resized.jpg")
            img = "resized.jpg"

        if opened_image.format == 'PNG':
            resized_image.save("resized.png")
            img = "resized.png"

        print(opened_image.format)
        print(name)
        print(ingredients)
        print(instructions)
        print(image)
        print(current_user.get_id())

        try:

            user_id = current_user.get_id()

            storage = firebase.storage()
            time = datetime.now().isoformat(' ', 'seconds')
            storage.child(
                f"images/recipes/{user_id}/recipe{time}").put(img)

            imageurl = storage.child(
                f"images/recipes/{user_id}/recipe{time}").get_url(None)
        except Exception as e:
            print(e)
            flash('Image Upload Error!', category='error')

        try:
            recipe_collection = mongo.db.recipes
            recipe_collection.insert_one(
                {'name': name, 'ingredients': ingredients, 'instructions': instructions, 'imageurl': imageurl, 'user_id': user_id})
            flash('New Recipe Added!.', category='success')
        except Exception as e:
            print(e)
            flash('Database Error!', category='error')

        return redirect('/recipes/new')

    return render_template("new_recipe.html", user=current_user, name=name, ingredients=ingredients, instructions=instructions, image=image, form=form)


@views.route("/recipes/more/<recipeid>")
@login_required
def recipemore(recipeid):

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipeid)})

    print(recipe['name'])
    name = recipe['name']
    ingredients = recipe['ingredients']
    instructions = recipe['instructions']
    imageurl = recipe['imageurl']
    name = recipe['name']

    return render_template("recipe_more.html", user=current_user, recipeid=recipeid, name=name, ingredients=ingredients, instructions=instructions, imageurl=imageurl)


@views.route("/questions")
@login_required
def questions():
    return render_template("questions.html", user=current_user)


@views.route("/kitchens")
@login_required
def kitchens():
    return render_template("kitchens.html", user=current_user)


@views.route("/insert")
def index():
    user_collection = mongo.db.users
    user_collection.insert_one({'name': 'Tharushika'})

    return render_template("home.html")
