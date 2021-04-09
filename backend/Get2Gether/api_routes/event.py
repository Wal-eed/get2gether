import uuid
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
import Get2Gether.database 

event_router = Blueprint("event", __name__)
DOMAIN_NAME = "localhost:5000"



# sends and email to all the invitees
def notify_invitees(invitee_emails: list) -> bool:
    return True


# given a request extracts the free schedule information, this is empty for now coz i have no idea how its gonna work on the frontend
def get_free_schedule_from_req(req: dict) -> list:
    pass



@event_router.route("/event/get", methods=["GET"])
def get_event():
    """
        Fetches events with a specific event id    
    """
    requested_id = int(request.args.get("event_id"))
    event_database = json.loads(
        database_util.get_json_file("event_data")
    )
    if request.args.get("event_id") not in event_database:
        return "Couldn't find event with ID", 404

    return jsonify(
        event_database[requested_id]), 200


# registration for a specific event
@event_router.route("/event/register", methods=["POST"])
def event_register():
    # just check that user id exists in the session
    if "user_uid" not in session:
        return "Not Logged In!", 403
    

    event_id = req.get("event_id")
    user_data = jsonify({
        is_orgainser: False,
        answered_email: True,
        free_schedule: {
            get_free_schedule_from_req(req)
        }
    })

    commit_data_to_key("event_data", str(event_id) + str(session["user_id"]), user_data)
    return jsonify({
        "event": "registered for event",
    }), 200


@event_router.route("/event/add", methods=["POST"])
def add_event():
    # just check that user id exists in the session
    if "user_uid" not in session:
        return "Not Logged In!", 403
    req = request.form
    event_id = uuid.uuid()


    raw_event_data = jsonify({
        event_name: req.get("event_name"),
        event_id: event_id,
        users: {
            session["user_id"]: {
                is_orgainser: True,
                answered_email: True,
                free_schedule: {
                    get_free_schedule_from_req(req)
                }
            }
        }
    })
    commit_data_to_key("event_data", str(event_id), raw_event_data)
    # now just email all the invitees with valid emails
    notify_invitees(json.loads(
        req.get("atendee_emails")
    ))


    return jsonify({
        "event": "added",
        "event_id": event_id,
        "url": "http://" + DOMAIN_NAME + "/event/join?event_id=" + str(event_id) # i guess the frontend can handle the final link location?
    }), 200


