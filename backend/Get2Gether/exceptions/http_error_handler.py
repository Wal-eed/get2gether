from json import dumps
from Get2Gether.utils.colourisation import printColoured 

def error_handler(err):
    """
        Returns JSON containing details of the failure event including the
        status code, name and message. This JSON message is returned to the client
        everytime the route handlers encounter a problem, for example, invalid user 
        input.
    """
    response = err.get_response()
    try:
        printColoured(" ➤ Error: {} {}".format(err, err.description), colour="red")
        response.data = dumps({
            "code": err.code,
            "name": "System Error",
            "message": err.description
        })
        response.content_type = 'application/json'
        return response
    except:
        printColoured(" ➤ Error: {}".format(err), colour="red")
        response.data = dumps({
            "code": err.code,
            "name": "System Error"
        })
        response.content_type = 'application/json'
        return response
