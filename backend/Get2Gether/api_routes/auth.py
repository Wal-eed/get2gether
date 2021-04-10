from flask import (
    Blueprint,
    jsonify,
    session
)
from Get2Gether.database import database_util
import random
import uuid

auth_router = Blueprint("auth", __name__)



# this is temporary test data 
google_user_ids = [
    {
        "user_name": "jason derulo",
        "email": "jason.d@gmail.com",
        "phone": 130065506,
        "google_token": "abcde123"
    },
    {
        "user_name": "elton john",
        "email": "ej@gmail.com",
        "phone": 130065506,
        "google_token": "eeetswalad"
    }
]


# function stubs to implement
# please fill this in to authenticate with google via oauth
# note: the return values should be: the unique token for the user, the user's name and the user's email + phone number
# see: register function for key names in the dictionary
def authenticate_with_google() -> dict:
    # RNG-jesus basically :)
    global google_user_ids
    return google_user_ids[random.randint(1)]



# is_returning_user just determines if the current user thats trying to log in is a user we've seen before
# ideally the best way to do this is check their google email, if the google email already exists in our database then they're a returning user :)
def is_returning_user(user_google_data: dict):
    global google_user_ids

    user_database = database_util.get_json_file("user_data")
    for user in user_database:
        if user["google_token"] == user_google_data["token"]:
            return (True, user)
    return (False, None)




# registration handles the creation of a new user given their google details
@auth_router.route("/user/register", methods=["POST"])
def register():
    
    # authenticate with google before publishing our data
    user_google_data = authenticate_with_google()

    # construct a json objet representing the user data
    internal_uid = uuid.uuid64()
    # save the user_json_data into the database
    user_database = database_util.get_json_file("user_data")
    user_database["users"].append({
        "name":         user_google_data["user_name"],
        "email":        user_google_data["email"],
        "phone":        user_google_data["phone"],
        "google_token": user_google_data["token"],
        "internal_uid":  internal_uid,
        "presets":      [],
    })
    database_util.save_json_file("user_data", user_database)
    
    # finally construct a session so we can keep track of the user in the future
    session["user_uid"] = internal_uid
    return jsonify({
        "Status": "Successful",
    }), 200



# login just authenticates a user and passes their authentication over to google OAuth
@auth_router.route("/user/login", methods=["POST"])
def login():
    # when a user attempts to login we first ask them to login with google
    user_google_data = authenticate_with_google()
    # now just determine if they're returning user e.g (if they've "signed up" with google in the past)
    is_returning, user_data = is_returning_user(user_google_data)
    if not is_returning:
        return jsonify({
            "Status": "Invalid login",
        }), 403
    else:
        session["user_uid"] = user_data["internal_uid"]
        return jsonify({
            "Status": "Successful",
        }), 200
    



# retrieve_user_data just gets the data associated with the currently logged in user
@auth_router.route("/user/get_user_data", methods=["GET"])
def retrieve_user_data():

    # first determine if we have any session data for the user
    if "user_uid" not in session:
        return jsonify({
            "Status": "Not logged in!",
        }), 403
    
    # open up the user database and iterate over every user
    user_database = database_util.get_json_file("user_data")
    for user in user_database:
        # if the user uid matches our saved UID then thats the one, remove the token and return the results
        if user["internal_uid"] == session["user_uid"]:
            user["google_token"] = ""
            return jsonify({
                "Status": "Successful",
                "Data": user
            }), 200

    return jsonify({
        "Status": "Couldn't find user",
    }), 404




# retrieve_user_contacts does what it says
@auth_router.route("/user/retrieve_contacts", methods=["GET"])
def retrieve_user_contacts():
    # first determine if we have any session data for the user
    if "user_uid" not in session:
        return "Not Logged In!", 403
    
    user_database = database_util.get_json_file("user_data")
    contacts = []

    for user in user_database:
        if user["internal_uid"] == session["user_uid"]:
            user_google_token = user["google_token"]
            # TODO: implement contact retrieval via google API
    return contacts










