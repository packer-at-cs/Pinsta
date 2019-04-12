from app import app
from flask import Flask, render_template, request, url_for,redirect, session
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
        return render_template("index.html")

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

@app.route("/bootstrap")
def bootstrap():
    return render_template("base.html")
