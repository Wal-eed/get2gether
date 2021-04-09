from backend.Get2Gether import database
from flask import (
    Blueprint,
    json,
    render_template,
    request,
    jsonify,
    session
)
import os
from Get2Gether.exceptions import InvalidUserInput
from Get2Gether.utils.colourisation import printColoured
from Get2Gether.utils.debug import pretty
from Get2Gether.database import database_util
import random
import uuid

auth_router = Blueprint("auth", __name__)


google_user_ids = [{
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
def is_returning_user(user_google_data: dict) -> tuple(bool, json):
    global google_user_ids

    for entry in google_user_ids:
        if entry["google_token"] == user_google_data["google_token"]:
            return True, jsonify(entry)
    return False, None




# registration handles the creation of a new user given their google details
@auth_router.route("/user/register", methods=["POST"])
def register():
    
    # authenticate with google before publishing our data
    user_google_data = authenticate_with_google()
    # construct a json objet representing the user data
    user_json_data = jsonify({
        "name":         user_google_data["user_name"],
        "email":        user_google_data["email"],
        "phone":        user_google_data["phone"],
        "google_token": user_google_data["token"],
        "internal_uid":  uuid.uuid64(),
        "presets":      [],
    })

    # save the user_json_data into the database
    database_util.commit_data_to_key("user_data", "users", user_json_data)
    session["user_uid"] = user_json_data.get("internal_uid")

    # now create a user session
    return "Registered User!", 200



@auth_router.route("/user/login", methods=["POST"])
def login():
    # when a user attempts to login we first ask them to login with google
    user_google_data = authenticate_with_google()
    # now just determine if they're returning
    is_returning, uid = is_returning_user(user_google_data)
    if not is_returning:
        # idk, deal with this somehow
        return "Not a user", 403
    else:
        session["user_uid"] = uid
        return "Logged In!", 200
    



# retrieve_user_data just gets the data associated with the currently logged in user
@auth_router.route("/user/get_user_data", methods=["GET"])
def retrieve_user_data():

    # first determine if we have any session data for the user
    if "user_uid" not in session:
        return "Not Logged In!", 403
    
    user_database = database_util.get_json_file("user_data")
    # TODO: iterate over every user in user_data, check if their UID matches our saved one
    #       if the UID matches the pull the data
    user_json_data = json.loads(user_database)
    for user in user_json_data:
        if user.get("internal_uid") == session["user_uid"]:
            user.set("google_token") = ""
            return jsonify(user), 200


    return "", 404




@auth_router.route("/user/retrieve_contacts", methods=["GET"])
def retrieve_user_contacts():
    # first determine if we have any session data for the user
    if "user_uid" not in session:
        return "Not Logged In!", 403
    
    user_database = database_util.get_json_file("user_data")
    user_json_data = json.loads(user_database)
    contacts = []

    for user in user_json_data:
        if user.get("internal_uid") == session["user_uid"]:
            if user.get("google_token") == "abcde123":
                contacts.append({
                    "contact_name": "elton john",
                    "email": "ej@gmail.com"
                })
            else:
                contacts.append({
                    "contact_name": "jason derulo",
                    "email": "jason.d@gmail.com",
                })
    return contacts










