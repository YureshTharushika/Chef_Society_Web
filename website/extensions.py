from flask_pymongo import PyMongo
import pyrebase

mongo = PyMongo()

firebaseConfig = {
    "apiKey": "AIzaSyAUEEpjSRDOhEfEFNkpKa3Pu6dC_kcG1qY",
    "authDomain": "chefsocietyweb-92e0d.firebaseapp.com",
    "projectId": "chefsocietyweb-92e0d",
    "storageBucket": "chefsocietyweb-92e0d.appspot.com",
    "databaseURL": "chefsocietyweb-92e0d.appspot.com",
    "messagingSenderId": "909366310993",
    "appId": "1:909366310993:web:c311d07f0b14c9814ba070",
    "measurementId": "G-P4RE79HCXN"
}

firebase = pyrebase.initialize_app(firebaseConfig)
