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

event_router = Blueprint("event", __name__)

@event_router.route("/event", methods=["GET"])
def get_event():
    """
        Fetching event/s        
    """
    
    return jsonify({
        "some": "event"
    })

@event_router.route("/event", methods=["POST"])
def add_event():
    """
        Adding event/s        
    """

    # 1. Add the event to the json file
    # 2. Alert all the invited individuals

    return jsonify({
        "event": "added"
    })


