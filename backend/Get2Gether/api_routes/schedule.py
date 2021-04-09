from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    session
)
import time
from Get2Gether.exceptions import InvalidUserInput
from Get2Gether.utils.colourisation import printColoured
from Get2Gether.utils.debug import pretty
from Get2Gether.database import database_util


schedule_router = Blueprint("schedule", __name__)

'''
Meeting 1:
Monday :  9AM - 5PM
Tuesday:  9AM - 5PM

Meeting 2: 
not Monday:  9AM - 5PM!
not Tuesday!
'''



# the core of this section, given a user's google key retrieves their calendar and blocked regions in the discussed
# [0, 1, 1, 0, 1] matrix format
def get_user_google_calendar(user_google_token: str, week_start: time, week_end: time) -> list(list):
    # Hardcoding results :)
    if user_google_token == "abcde123":
        return [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    else:
        return [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0], # basically toy data
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]





@schedule_router.route("/schedule", methods=["GET"])
def get_schedule():
    """
        Fetching a user's schedule/s        

        Parameters:
            - user_id
    """

    # retrieve the user's user id from session data
    # first determine if we have any session data for the user
    if "user_uid" not in session:
        return "Not Logged In!", 403

    user_id = session["user_uid"]
    user_database = database_util.get_json_file("user_data")
    current_user_data = user_database.get(user_id)
    user_presets = current_user_data.get("presets")
    user_google_calendar = get_user_google_calendar(
        current_user_data["google_token"], 
        request.args.get("week_start"), request.args.get("week_end")
    )



    return jsonify({
        "user_calendar": user_google_calendar,
        "user_presets": user_presets
    }), 200


@schedule_router.route("/schedule", methods=["POST"])
def add_user_preset():
    """
        Adding a preset to the user data     
    """
    # TODO: fill this in after the creation of an event


    return "added", 200

























