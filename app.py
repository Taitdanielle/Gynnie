import os
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_pymongo import PyMongo
from flask_bcrypt import bcrypt
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route('/')
def index():

    return render_template('pages/index.html')

@app.route('/<myname>')
def name():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('pages/index.html', myname=name)
# Logout page
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# Login page
@app.route('/login', methods=["GET", "POST"])
def login():
    """
    Renders login page.
    """
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name': request.form['username'].lower()})

        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                             login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            flash('That username/password combination was incorrect')
            return redirect(url_for('login'))
    return render_template('components/forms/login-form.html')

# Register form
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})
        password = request.form['password']
        repeat_password = request.form['repeat_password']

        if password == repeat_password:
            if existing_user is None:
                hashpass = bcrypt.hashpw(
                    request.form['password'].encode('utf-8'), bcrypt.gensalt())
                users.insert({
                    'name': request.form['username'].lower(),
                    'password': hashpass,
                })
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            flash('That username already exists, try something else.')
        flash('The passwords dont match.')
        return 'That Username is already taken'

    return render_template('components/forms/register-form.html')

# My Cocktail Page
@app.route('/cocktailpage')
def my_cocktails():

    cocktails = mongo.db.cocktails.find()

    return render_template("pages/cocktails/my-cocktails.html", page_title="My Cocktails", cocktails=cocktails)

# All cocktail page
@app.route('/allcocktails')
def cocktails():

    if 'username' not in session: redirect(url_for('login'))
    cocktails = mongo.db.cocktails.find()

    return render_template("pages/cocktails/all-cocktails.html", page_title="All Cocktails", cocktails=cocktails)

# Add Cocktail
@ app.route('/cocktail/add', methods=["GET"])
def add_cocktail():
    if 'username' not in session: 
        redirect(url_for('login'))
    return render_template("pages/cocktails/add-cocktail.html")

@ app.route('/cocktail/insert', methods=["POST"])
def insert_cocktail():
    """
    Adds user cocktail into the database.
    """
    inserted_cocktail = mongo.db.cocktails.insert_one({
        'name': request.form.get('name'),
        'description': request.form.get('description'),
        'ingredients': request.form.get('ingredients'),
        'how_to': request.form.get('how_to'),
        'image': request.form.get('image')})

    return redirect(url_for('my_cocktails'))

# Edit cocktail page
@app.route('/cocktail/edit/<drink_id>', methods=["GET", "POST"])
def edit_cocktail(drink_id):

    if request.method == 'POST':
        cocktail = mongo.db.cocktails
        cocktail.update({'_id': ObjectId(drink_id)},
                        {'name': request.form.get('name'),
                         'description': request.form.get('description'),
                         'ingredients': request.form.get('ingredients'),
                         'how_to': request.form.get('how_to'),
                         'image': request.form.get('image')})
        return redirect(url_for('cocktail_page', drink_id=drink_id))
    users = mongo.db.users
    the_drink = mongo.db.cocktails.find_one({"_id": ObjectId(drink_id)})
    all_types = mongo.db.types.find()
    return render_template('pages/cocktails/edit-cocktail.html',
                           body_id='edit-page', cocktail=the_drink,
                           types=all_types, current_user=users.find_one(
                               {'name': session['username']}))

 # My cocktails 
@app.route('/cocktail/<drink_id>')
def cocktail_page(drink_id):

    the_drink = mongo.db.cocktails.find_one({"_id": ObjectId(drink_id)})
    return render_template('pages/cocktails/cocktail-page.html',
                           body_id='edit-page', cocktail=the_drink)

# Delete cocktail 
@app.route('/cocktail/delete/<drink_id>')
def delete_cocktail(drink_id):
    """
    Delete a cocktail from the database
    """
    mongo.db.cocktails.remove({'_id': ObjectId(drink_id)})
    return redirect(url_for('cocktails'))

# Contact page
@app.route('/contact', methods=["GET", "POST"])
def contact():

    try:
        users = mongo.db.users
        if request.method == "POST":
            flash("Thanks {} we have received your message! A member of our team will be in touch shortly".format(
                request.form["name"]))
        return render_template("components/forms/contact-form.html",
                               body_id="contact-page", page_title="Contact Us",
                               current_user=users.find_one({'name': session['username']}))
    except:
        if request.method == "POST":
            flash("Thanks {} we have received your message! A member of our team will be in touch shortly".format(
                request.form["name"]))
        return render_template("components/forms/contact-form.html",
                               body_id="contact-page", page_title="Contact Us")


if __name__ == "__main__":
    app.run(host = os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=os.environ.get("DEBUG"))