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

@app.route('/')
@app.route('/index')
def index():
        return render_template("index.html")

@app.route("/profile", methods=['POST','GET'])
def profile():

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
