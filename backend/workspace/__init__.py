from flask import Flask
# import PyMongo
# from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://thanasuksongsriohm:xZ1ov3XleNFjEvQX@backend.4fzql.mongodb.net/")
db = client["backend"]
collection = db["backend"]
# print(collection)

from workspace import routes