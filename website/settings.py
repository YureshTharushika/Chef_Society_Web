import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MONGO_URI = os.environ.get("MONGO_URI")

# FIREBASE_CONFIG = os.environ.get("firebaseConfig")
