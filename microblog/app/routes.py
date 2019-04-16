from flask import Flask, render_template, request, redirect
import smtplib #Imports SMTPLib package
from app import app

app = Flask(__name__)

@app.route("/")
def main():
  return redirect("/email") #Redirects to /email

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

app.secret_key = "my secret key" #Flask key info
if __name__ == "__main__":
  app.run(host="0.0.0.0")