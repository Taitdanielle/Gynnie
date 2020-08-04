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
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return render_template('components/forms/login-form.html')

    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('components/forms/register-form.html')


@app.route('/allcocktails')
def contact():
    return render_template("pages/cocktails/all-cocktails.html", page_title="All Cocktails")
    
@app.route('/mycocktails')
def contact():
    return render_template("pages/cocktails/my-cocktails.html", page_title="My Cocktails")    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)