from flask import (
    Blueprint,
    render_template,
    request,
    jsonify
)
import os
from Get2Gether.exceptions import InvalidUserInput
from Get2Gether.utils.colourisation import printColoured
from Get2Gether.utils.debug import pretty

import uuid

auth_router = Blueprint("auth", __name__)

users = [
    {
        "name": "firstuser",
        "password": None,
        "email": "user@gmail.com",
        "uuid": 1234567891011,
    }
]

# Note: go with the Google auth approach

@auth_router.route("/register", methods=["POST"])
def one_off_login():
    """
        
    """
    
    return 


@auth_router.route("/one_off", methods=["GET"])
def one_off_login():
    """
        Logs in the user, if no cookie with uid exists generates and returns a new one

        Parameters:
            - username
            - password [optional]   
    """
    
    return 






# Tutorial here: https://realpython.com/flask-google-login/#flask-login

# ===== Google Authentication =====

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

@auth_router.route("/google/login")
def google_login_handler():
    """
        When this route is hit, the user is directed to Google's authentication
        page where they will choose a Google account to log in with.
    """
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = google_client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri="https://127.0.0.1:5000/api/auth/google/login/callback",
        scope=["openid", "email", "profile"],
    )
    printColoured("REDIRECTING NOW", colour="blue")
    printColoured("Request URI: {}".format(request_uri))
    return redirect(request_uri)

@auth_router.route("/google/login/callback")
def google_login_callback_handler():
    """
        This is the route hit by Google's API. The exact URL is specified in the
        develop console: https://console.developers.google.com/
    """
    printColoured("CLIENT_ID : {}, CLIENT_SECRET: {}".format(GOOGLE_API_CLIENT_ID, GOOGLE_API_CLIENT_SECRET), colour="yellow")
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = google_client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_API_CLIENT_ID, GOOGLE_API_CLIENT_SECRET),
    )

    # Parse the tokens!
    google_client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = google_client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        user_email = userinfo_response.json()["email"]
        user_image = userinfo_response.json()["picture"]
        user_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in your db with the information provided
    # by Google
    printColoured(
        " ➤ GOOGLE API: Registered a user with details: name: {}, email: {}, image: {}".format(
            user_name, 
            user_email, 
            user_image
        )
    )

    new_user = User(name=user_name, email=user_email, password="test123")
    new_user.commit_user()
    printColoured("COMMITTED THE USER")

    # Send user back to homepage
    return """
        <h3>You've logged in successfully!</h3> 
        <div>Name: {}, Email: {}</div>
        <img src='{}'></img>
    """.format(user_name, user_email, user_image)
