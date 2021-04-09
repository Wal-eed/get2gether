from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from pathlib import Path 
from Get2Gether.utils.colourisation import printColoured
from flask_pymongo import PyMongo
from Get2Gether.exceptions import error_handler
from oauthlib.oauth2 import WebApplicationClient
import pymongo
import os

# Creating the Flask app instance
printColoured(" * Initialising Flask application")
app = Flask(__name__)
CORS(app)

# ===== App Configuration =====

@app.route("/")
def index():
	return "Looks like this works" 

# The routes must be imported after the Flask application object is created. See https://flask.palletsprojects.com/en/1.1.x/patterns/packages/
import Get2Gether.routes
