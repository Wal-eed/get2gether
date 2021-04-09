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

schedule_router = Blueprint("schedule", __name__)


@schedule_router.route("/schedule", methods=["GET"])
def get_schedule():
    """
        Fetching a user's schedule/s        

        Parameters:
            - user_id
            - requested_presets = []
    """

    # 1. find the user with the user_id

    # 2. pull their calendar data from Google Calendar API
        # - fill in an array with ones and zeros

    # 3. pull their presets from json
    
    return jsonify({
        "free_schedule": {
            "09/04/2021": [1, 1, 1, 1, 0, 1, 1, 0],  
            "10/04/2021": [1, 1, 1, 1, 0, 1, 1, 0],
        },
        "presets": [
            "uni_timetable": [],  
            "exercise",
            "other_preset1"
        ]
    })


@schedule_router.route("/save_schedule", methods=["POST"])
def save_schedule():
    """
        Parameters:
            - user_id
            - new_schedule
    """
    # 1. Overwrite previous schedule in the event for this person?
    pass

























