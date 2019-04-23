import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['gbenedis@gmail.com']
    POSTS_PER_PAGE = 10
    PYREBASE = {
      "apiKey": "AIzaSyAnbcc9qnLBbvkuZv65T-WFGfts8_q_MJY",
      "authDomain": "gradebook-e5e08.firebaseapp.com",
      "databaseURL": "https://gradebook-e5e08.firebaseio.com",
      "storageBucket": "gradebook-e5e08.appspot.com",
      "serviceAccount": "app/gradebook_key.json"
    }
