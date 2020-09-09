import os
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('pages/index.html')


@app.route('/<bob>')
def name(bob):
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('pages/index.html', myname=bob)


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return render_template('components/forms/login-form.html')

    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert(
                {'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('components/forms/register-form.html')


@app.route('/allcocktails')
def cocktails():

    cocktail = mongo.db.cocktail
    results = cocktail.find({})

    return render_template("pages/cocktails/all-cocktails.html", page_title="All Cocktails", cocktails=results)


@app.route('/mycocktails')
def mycocktails():
    return render_template("pages/cocktails/my-cocktails.html", page_title="My Cocktails")


@app.route('/contactus')
def contact():
    return render_template("components/forms/contact-form.html", page_title="Contact Us")

# Add Review route

@app.route('/review/add/<drink_id>', methods=["GET", "POST"])
def add_review(drink_id):
    """
    Adds user review into the database.
    """
    mongo.db.reviews.insert({
        'name': request.form.get('name'),
        'review': request.form.get('review'),
        'beer_id': ObjectId(drink_id),
    })
    return redirect(url_for('cocktail_page', drink_id=drink_id))    

# Edit Review page

@app.route('/review/edit/<review_id>', methods=["GET", "POST"])
def edit_review(review_id):

    if request.method == 'POST':
        mongo.db.reviews.update({'_id': ObjectId(review_id)}, {
            '$set': {'review': request.form.get('review')}})
        return redirect(url_for('edit_review', review_id=review_id))
    users = mongo.db.users
    review = mongo.db.reviews.find({"_id": ObjectId(review_id)})
    return render_template("pages/edit-review-form.html",
                           body_id="edit-review-page", review=review, review_id=review_id,
                           current_user=users.find_one({'name': session['username']}))


@app.route('/cocktail/<drink_id>')
def cocktail_page(drink_id):
    """
    Constructs page for single cocktail and
    makes reviews for front end.
    """
    users = mongo.db.users
    the_beer = mongo.db.cocktail.find_one({"_id": ObjectId(drink_id)})
    you_might_like = mongo.db.cocktail.find().limit(3)
    test = mongo.db.reviews.find({'drink_id': ObjectId(drink_id)})
    reviews = []
    current_user_obj = users.find_one({'name': session['username'].lower()})
    reviews.append(i)
    return render_template('pages/cocktails/cocktail-page.html',
                           cocktail_reviews=reviews,
                           body_id="drink-product", current_user=users.find_one(
                               {'name': session['username']}))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=os.environ.get("DEBUG"))
