from app import app
from flask import Flask, render_template, request, url_for,redirect, session 

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

#edit test thingy

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


 
 