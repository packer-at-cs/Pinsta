import pyrebase
from pyrebase import initialize_app
import firebase_admin
from firebase_admin import credentials

# Initialize Firebase
config = {
  "apiKey": "AIzaSyCdo6BNs18wwIV7oNZYd1Htb7WeSSEMT7E",
  "authDomain": "pinsta-c6d80.firebaseapp.com",
  "databaseURL": "https://pinsta-c6d80.firebaseio.com",
  "projectId": "pinsta-c6d80",
  "storageBucket": "pinsta-c6d80.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}
firebase = pyrebase.initialize_app(config)


#set database to a variable
db = firebase.database()
# data to save
data = {
  "name": "Mortimer 'Morty' Smith"
}
# Pass the user's idToken to the push method
results = db.child("users").child("test").set(data)
#function to push data to the database
def push_data(username, data):
  results = db.child("users").child(username).set(data)
  return results
#running function
push_data("second_test", data)

storage = firebase.storage()
storage.child("Photos/").put("spain.png")