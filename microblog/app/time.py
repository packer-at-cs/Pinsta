#program that utilizes the datetime importation and flask_moment to display the current time through obtaining information from the user's computer
from datetime import datetime
from flask import Flask, render_template, jsonify
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)

@app.route('/')
def index():
	return render_template("time.html")


if __name__ == "__main__":
    app.run(host = "0.0.0.0")