import uuid
from flask import (
    Blueprint,
    json,
    request,
    jsonify,
    session
)
from Get2Gether.database import database_util
import time

event_router = Blueprint("event", __name__)
DOMAIN_NAME = "localhost:5000"



# sends an email to all the invitees
def notify_invitees(invitee_emails: list) -> bool:
    return True


# given a request extracts the free schedule information
def get_avaliabilities_from_request(req: dict):
    return json.load(
        req.get("user_schedule"))


# given a user and their google token, just pushes the new event to the user's google calendar
def push_event_to_calendar(user_google_token: str, time_start: time.time, time_end: time.time, event_details: dict) -> bool:
    # given our OAuth perms, just push our data to the user's google calendar
    def push_to_cal(calendar_json):
        pass

    event = {
        'summary': 'A fun get together with friends!',
        'location': event_details["location"]["venue"],
        'start': {
          'dateTime': time_start,
          'timeZone': 'Australia/Sydney',
        },
        'end': {
          'dateTime': time_end,
          'timeZone': 'Australia/Sydney',
        },
        'reminders': {
          'useDefault': False,
          'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
          ],
        },
    }
    push_to_cal(jsonify(event))



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
        "location": {
            "link": req.get("location_link"),
            "venue": req.get("venue"),
            "long": req.get("loc_longitude"),
            "lat": req.get("loc_latitude")
        },
        "users": {
            session["user_id"]: {
                "is_orgainser": True,
                "answered_email": True,
                "free_schedule": {
                    get_avaliabilities_from_request(req)
                }
            }
        },
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





# confirm_event is an endpoint called by the event organiser to confirm a time for the event
@event_router.route("/event/confirm_time", methods=["POST"])
def add_event():
    # get the post form
    req = request.form
    requested_event_id = req.get("event_id")

    # check that the user is logged in via a session
    if "user_uid" not in session:
        return jsonify({
            "Status": "Not logged in!",
        }), 403

    # now read over the event_db and ensure that the person attempting to confirm the time is an event organiser
    event_database = database_util.get_json_file("event_data")
    requested_start = time.strptime(req.get("requested_time_start"), "yyyy-MM-dd'T'HH:mm:ssXXX")
    requested_end =  time.strptime(req.get("requested_time_end"), "yyyy-MM-dd'T'HH:mm:ssXXX")
    
    # iterate and check
    event_of_interest = None
    for event in event_database:
        if event["event_id"] == requested_event_id:
            # now iterate over the users and just double check that the requested person is an organiser
            for user in event["users"]:
                if user["user_id"] == session["user_uid"]:
                    if not user["is_organiser"]:
                        return jsonify({
                            "Status": "Insufficient privileges to confirm time",
                        }), 403
                    event["event_finalised"] = True
                    event["best_possible_times"] = [requested_start, requested_end]
            event_of_interest = event
    # looks like we couldnt find an event with that ID        
    if event_of_interest == None:
        return jsonify({
            "Status": "Invalid event ID",
        }), 404

    # now that the event is confirmed we just need to iterate over all the users in the event and add the event to their calendars, this code is a bit hacky sorry :(
    for user in event_of_interest:
        push_event_to_calendar(user["token"], requested_start, requested_end, event_of_interest)
    
    return jsonify({
        "Status": "Successful"
    }), 200