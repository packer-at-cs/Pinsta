from flask import Flask, render_template, request, redirect
import smtplib

app = Flask(__name__)

@app.route("/")
def main():
  return redirect("/email")

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

@app.errorhandler(500)
def page_not_found(e):
    return render_template("home.html", message = "Please enter a valid email address"), 500

app.secret_key = "my secret key"
if __name__ == "__main__":
  app.run(host="0.0.0.0")