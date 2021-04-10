from flask import (
    Blueprint,
    request,
    jsonify,
    json,
    session
)
import time
import math
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



# pull_calendar_json just makes a request to the Google Calendar API and retrieves 
def pull_calendar_json(user_google_token: str, week_start: time, week_end: time):
    pass



# the core of this section, given a user's google key retrieves their calendar and blocked regions in the discussed
# [0, 1, 1, 0, 1] matrix format
def get_user_google_calendar(user_google_token: str, week_start: time, week_end: time):
    
    google_calendar_data = pull_calendar_json(user_google_token, week_start, week_end)
    calendar_data = json.load(google_calendar_data)
    # the final calendar we're trying to compute
    computed_calendar_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # iterate over every event in the calendar and update the computed_calendar_matrix
    for event in calendar_data:
        event_start = time.strptime(event["start"]["dateTime"], "yyyy-MM-dd'T'HH:mm:ssXXX")
        event_end   = time.strptime(event["end"]["dateTime"], "yyyy-MM-dd'T'HH:mm:ssXXX")

        for day in range(event_start.weekday() - 1, event_end.weekday()):
            for hour_block in range(math.ceil(event_start) - 1, math.floor(event_end)):
                computed_calendar_matrix[day][hour_block] = 1
    return computed_calendar_matrix





# get_schedule returns the schedule + presets for a specific user
@schedule_router.route("/user/get_schedule", methods=["GET"])
def get_schedule():

    # retrieve the user's user id from session data
    # first determine if we have any session data for the user
    if "user_uid" not in session:
        return jsonify({
            "Status": "Not logged in!",
        }), 403

    user_id = session["user_uid"]
    user_database = database_util.get_json_file("user_data")
    current_user_data = user_database[user_id]
    user_presets = current_user_data["presets"]

    user_google_calendar = get_user_google_calendar(
        current_user_data["google_token"], 
        request.args.get("week_start"), request.args.get("week_end")
    )


    # Return the user's final google calendar and all their presets
    return jsonify({
        "Status": "Successful",
        "Data": {
            "User_Calendar": user_google_calendar,
            "User_Presets": user_presets
        }}), 200





# add_user_preset updates the user's presets and includes a new one as requested by the user
@schedule_router.route("/user/add_user_preset", methods=["POST"])
def add_user_preset():
    # We assume the preset data is presented to us properly in a nice little JSON format from the front end
    if "user_uid" not in session:
        return jsonify({
            "Status": "Not logged in!",
        }), 403
    req = request.form
    new_user_preset = json.loads(req.get("preset_data"))
    user_database = database_util.get_json_file("user_data")
    
    # iterate over the users and find our user
    for user in user_database:
        if user["internal_uid"] == session["user_uid"]:
            user["presets"][new_user_preset["preset_name"]] = new_user_preset["preset"]
    database_util.save_json_file("user_data", user_database)

    return jsonify({
        "Status": "Successful",
    }), 200





