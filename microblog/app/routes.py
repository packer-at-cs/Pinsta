from app import app
import pyrebase
import tempfile
import os
from flask import Flask, render_template, request, url_for,redirect, session

config = {
  "apiKey": "AIzaSyAnbcc9qnLBbvkuZv65T-WFGfts8_q_MJY",
  "authDomain": "gradebook-e5e08.firebaseapp.com",
  "databaseURL": "https://gradebook-e5e08.firebaseio.com",
  "storageBucket": "gradebook-e5e08.appspot.com",
  "serviceAccount": "/Users/zaallard/Documents/ASCII/Pinsta/microblog/app/gradebook_key.json"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


from app.forms import LoginForm #, RegistrationForm,EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, db
from werkzeug.urls import url_parse
from datetime import datetime
from flask_login import login_manager
from app.forms import PostForm
from app.models import Post
import smtplib #Imports SMTPLib package
#from app.email import send_password_reset_email

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    posts = current_user.posts.all()
    return render_template('index.html', title='Home', form=form,posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user)
        if user is None:
            flash('Invalid username')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/profile", methods=['POST','GET'])
def profile():


    

	#Relational DB: stores a 'primary key', a unqiue integer,
	# on every data table (users, comments, likes, etc.).
	# These make it easy to construct associations because,
	# say you want to have a comment authored by a user, you s
	# imply store the user id as a 'foreign key' on the row of
	# the comments table that you want associated with that user.
	# Think of data tables as spreadsheets that have certain constraints
	# placed on the columns.

	avatar = "/static/avatar.jpg"
    user_information = {
		"user_name": "Jon Doe",
		"profile_picture": "https://pbs.twimg.com/profile_images/502988973052932096/nvkFAZdJ_400x400.jpeg",
		"bio": "This is my bio",
		"posts": {
		  1: {
		    "body": "text",
		    "image": "https://static01.nyt.com/images/2012/05/07/nyregion/PACKER2/PACKER2-jumbo.jpg"
		  },
		  2: {
		    "body": "text2",
		    "image": "http://www.nycago.org/Organs/Bkln/img/PackerInstInt1902.jpg"
		  }
		}
    }

	# Connects this database to the HTML file so it can render python in the HTML


    if request.method == 'POST':
        picture = request.files['picture']
        temp = tempfile.NamedTemporaryFile(delete=False)
        picture.save(temp.name)
        storage.child("images/test.jpg").put(temp.name)
        os.remove(temp.name)
        link = storage.child("images/test.jpg").get_url(None)
        avatar=link
        return render_template('profile.html', avatar=link, link=link, user_information=user_information)

    else:
        avatar="/static/avatar.jpg"
        samplebio="samplebio"
        return render_template("profile.html", avatar=avatar, user_information=user_information, samplebio=samplebio)



@app.route("/profile_image", methods=['POST','GET'])
def profile_images():
    
    return render_template("profile_image.html")
    

@app.route("/bio_summary", methods=['POST','GET'])
def bio_summary():
    
    return render_template("profile_image.html")


    

@app.route("/email", methods = ("GET", "POST"))
def home():
  if request.method == "GET":
    return render_template("home.html") #returns tempalte
  else:

    sender_email = "packer.insta@gmail.com" #Sender email address
    sender_password = "atcompsci" #Sender email password (for authentication)
    reciever_email = request.form["email"] #Reciever email address (takes text from input field)
    message = "Boolean Logic" #Message

    s = smtplib.SMTP('smtp.gmail.com', 587) #Defines email host and port
    s.starttls() #Start
    s.login(sender_email, sender_password) #Logs in to sender email
    s.sendmail(sender_email, reciever_email, message) #Sends email
    s.quit() #End
    return render_template("home.html", message = "Message sent!") #Return template with message

@app.errorhandler(500) #Handles 'page not found' error
def page_not_found(e):
    return render_template("home.html", message = "Please enter a valid email address"), 500 #Return template with error message

# app.secret_key = "my secret key" #Flask key info
# if __name__ == "__main__":
#   app.run(host="0.0.0.0")


@app.route("/bootstrap")
def bootstrap():
    return render_template("base.html")

@app.route('/followers')
def followers():
        return('hello followers')
