from flask import Flask
# import PyMongo
# from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_socketio import SocketIO, emit



app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

client = MongoClient("mongodb://your_username:your_password@mongodb:27017")
db = client["local"]
collection = db["backend"]
# print(collection)

from workspace import routes