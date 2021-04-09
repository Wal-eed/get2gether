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

'''
Meeting 1:
Monday :  9AM - 5PM
Tuesday:  9AM - 5PM

Meeting 2: 
not Monday:  9AM - 5PM!
not Tuesday!
'''





@schedule_router.route("/schedule", methods=["GET"])
def get_schedule():
    """
        Fetching a user's schedule/s        

        Parameters:
            - user_id
            - 
    """

    # 1. find the user with the user_id

    # 2. pull their calendar data from Google Calendar API

    # 3. pull their active event data (for scheduling with other events)
    
    return jsonify({
        "some": "schedule"
    })

@schedule_router.route("/schedule", methods=["POST"])
def add_schedule():
    """
        Adding a user's schedule/s        
    """



    return jsonify({
        "schedule": "added"
    })

























