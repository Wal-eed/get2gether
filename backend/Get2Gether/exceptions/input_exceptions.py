from werkzeug.exceptions import HTTPException

class InvalidUserInput(HTTPException):
    code = 400

    def __init__(self, description="No error message specified"):
        HTTPException.__init__(self)
        self.message = description

    @property
    def description(self):
        return self.message

    def __repr__(self):
        return "{}".format(self.message)
