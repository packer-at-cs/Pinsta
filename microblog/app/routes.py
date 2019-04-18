# from app import app
# from flask import Flask, flash, render_template, request, url_for,redirect, session
# from flask_login import current_user, logout_user, login_user
# from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for, request, Flask, session
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
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


 

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile')
def profile():

	avatar="/static/avatar.jpg"
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
	return render_template("profile.html", user_information=user_information, avatar=avatar)

@app.route("/profile_image", methods=["POST","GET"])
def profile_images():
    avatar="/static/avatar.jpg"
    return render_template("profile_image.html",)

    if request.method=="GET":
        return render_template("profile.html")
    else:
        profilepic = request.form.get("fileupload")
        avatar=profilepic
        return render_template("profile.html", profilepic=profilepic, avatar=profilepic)
    #return "Hello, World!"

@app.route("/email", methods = ("GET", "POST"))
def home():
  if request.method == "GET":
    return render_template("home.html")
  else:

    sender_email = "packer.insta@gmail.com"
    sender_password = "atcompsci"
    reciever_email = request.form["email"]
    message = "Boolean Logic"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, sender_password)
    s.sendmail(sender_email, reciever_email, message)
    s.quit()
    return render_template("home.html", message = "Message sent!")

@app.route('/followers')
def followers():
        return('hello followers')
