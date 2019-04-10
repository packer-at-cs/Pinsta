from app import app
import smtplib

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

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