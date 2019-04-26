from app import app, db, storage

import tempfile
import os

from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm #EditProfileForm

from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Post
from werkzeug.urls import url_parse
from datetime import datetime
from flask_login import login_manager
from app.forms import PostForm
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
    posts = current_user.followed_posts().all()
    return render_template('index.html', title='Home', form=form,
                           posts=posts)

@app.route('/comments/<post_id>')
def comments(post_id):
    return 'hello world'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc())
    return render_template('user.html', user=user, posts=posts)

@app.route("/profile", methods=["POST","GET"])
def profile():
    avatar="/static/avatar.jpg"
    user = User.query.filter_by(username=current_user.username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc())
    # Made the profile a variable, so you can change your profile picture when you want.

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
        return render_template("profile.html", avatar=avatar, user_information=user_information, samplebio=samplebio, user=user)



@app.route("/profile_image", methods=['POST','GET'])
def profile_images():

    return render_template("profile_image.html")


@app.route("/bio_summary", methods=['POST','GET'])
def bio_summary():

    return render_template("profile_image.html")




@app.route('/explore')
@login_required
def explore():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', title='Explore', posts=posts)


@app.route("/email", methods = ("GET", "POST"))
def email():
  if request.method == "GET":
    return render_template("email.html") #returns tempalte
  else:

    sender_email = "packer.insta@gmail.com" #Sender email address
    sender_password = "atcompsci" #Sender email password (for authentication)
    reciever_email = request.form["email"] #Reciever email address (takes text from input field)
    message = 'Subject: {}\n\n{}'.format('Password Reset', 'Password Reset') #message and subject

    s = smtplib.SMTP('smtp.gmail.com', 587) #Defines email host and port
    s.starttls() #Start
    s.login(sender_email, sender_password) #Logs in to sender email
    s.sendmail(sender_email, reciever_email, message) #Sends email
    s.quit() #End
    return render_template("email.html", message = "Message sent!") #Return template with message

# @app.errorhandler(500) #Handles 'page not found' error
# def page_not_found(e):
#     return render_template("email.html", message = "Please enter a valid email address"), 500 #Return template with error message

# app.secret_key = "my secret key" #Flask key info
# if __name__ == "__main__":
#   app.run(host="0.0.0.0")


@app.route("/bootstrap")
def bootstrap():
    return render_template("base.html")

@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('user', username=username))

@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user', username=username))
