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
	#Relational DB: stores a 'primary key', a unqiue integer, 
	# on every data table (users, comments, likes, etc.). 
	# These make it easy to construct associations because, 
	# say you want to have a comment authored by a user, you s
	# imply store the user id as a 'foreign key' on the row of 
	# the comments table that you want associated with that user.
	# Think of data tables as spreadsheets that have certain constraints 
	# placed on the columns. 

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
	# Connects this database to the HTML file so it can render python in the HTML 

@app.route("/profile_image", methods=["POST","GET"])
def profile_images():
    avatar="/static/avatar.jpg"
    return render_template("profile_image.html",)
    # Made the profile a variable, so you can change your profile picture when you want.

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



@app.route("/bootstrap")
def bootstrap():
    return render_template("base.html")
  
@app.route('/followers')
def followers():
        return('hello followers')
