import uuid
from flask import (
    Blueprint,
    json,
    request,
    jsonify,
    session
)
from Get2Gether.database import database_util

event_router = Blueprint("event", __name__)
DOMAIN_NAME = "localhost:5000"



# sends an email to all the invitees
def notify_invitees(invitee_emails: list) -> bool:
    return True


# given a request extracts the free schedule information
def get_avaliabilities_from_request(req: dict):
    return json.load(
        req.get("user_schedule"))



# get_event fetches the event data for an event with a specific ID
@event_router.route("/event/get", methods=["GET"])
def get_event():

    # open up the event database and retrive the data    
    requested_id = int(request.args.get("event_id"))
    event_database = database_util.get_json_file("event_data")
    if request.args.get("event_id") not in event_database:
        return '{"Status":  "Couldn\'t find event with ID"}', 404

    requested_event_data = event_database[requested_id]


    # We now need to compute the overall avaliability for EVERYONE, the following set of lines does so
    # the aggregate avaliability is just the availability matrix
    aggregate_avaliability = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # iterate over every registered user and add up the avaliabilities
    for registered_user in requested_event_data["users"]:
        user_avaliability = registered_user["free_schedule"]

        for row in range(user_avaliability):
            for col in range(user_avaliability[0]):
                aggregate_avaliability[row][col] += user_avaliability[row][col]
    
    # format and return all the computed even data
    requested_event_data["aggregate_avaliabilities"] = aggregate_avaliability


    return jsonify({
            "Status": "Successful",
            "Data":  requested_event_data
        }), 200



# registers a user to a specific event
@event_router.route("/event/register", methods=["POST"])
def event_register():
    # just check that user id exists in the session
    if "user_uid" not in session:
        return jsonify({
            "Status": "Not logged in!",
        }), 403

    req = request.form

    event_id = req.get("event_id")
    user_data = {
        "is_organiser": False,
        "answered_email": True,
        # This should be a list of lists
        "free_schedule": {
            get_avaliabilities_from_request(req)
        }
    }
    # Second argument (requested_key) might need to be changed
    # depending on the layout of the json
    event_database = database_util.get_json_file("event_data")
    event_database[str(event_id)][session["user_id"]] = user_data
    database_util.save_json_file("event_data", event_database)


    return jsonify({
        "Status": "Successful"
    }), 200



# add_event adds an event to the database as requested by an organizer
@event_router.route("/event/add", methods=["POST"])
def add_event():
    # just check that user id exists in the session
    if "user_uid" not in session:
        return jsonify({
            "Status": "Not logged in!",
        }), 403
    req = request.form
    event_id = uuid.uuid()


    raw_event_data = {
        "event_name": req.get("event_name"),
        "event_id": event_id,
        "users": {
            session["user_id"]: {
                "is_orgainser": True,
                "answered_email": True,
                "free_schedule": {
                    get_avaliabilities_from_request(req)
                }
            }
        }
    }
    event_database = database_util.get_json_file("event_data")
    event_database[str(event_id)] =  raw_event_data
    database_util.save_json_file("event_data", event_database)

    # now just email all the invitees with valid emails
    notify_invitees(json.loads(
        req.get("atendee_emails")
    ))


    return jsonify({
        "Status": "Successful",
        "Data": {
            "Event_ID": event_id,
            "Invite_URL": "http://" + DOMAIN_NAME + "/event/join?event_id=" + str(event_id) # i guess the frontend can handle the final link location?
        }
    }), 200


