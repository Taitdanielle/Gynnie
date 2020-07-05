import os
from flask import Flask, render_template, request, flash, url_for
from form import RegistrationForm, LoginForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")    

@app.route('/')

@app.route('/landing.html')
def landing():
    return render_template('landing.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')





@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def register():
    form = LoginForm()
    return render_template('Login.html', title='Login', form=form)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)