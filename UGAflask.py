import flask
from flask import request
import pymongo
from pymongo import MongoClient


app = flask.Flask(__name__)

# Display webpage functions no AJAX yet, splash page == login page
# if login successful next splash should be the grocery store library 
@app.route("/")
def login():
    pass
@app.route("/valid")
def store_library():
    pass

