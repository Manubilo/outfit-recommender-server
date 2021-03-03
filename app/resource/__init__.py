class Rpta():
    def __init__(self):
        self._code = None
        self._message = None
        self._message_internal = None
        self._body = None

    def setBody(self, body):
        self._body = body

    def setOk(self, message):
        self._code = 202
        self._message = message

    def setError(self, message, message_internal=None):
        self._code = 402
        self._message = message
        self._message_internal = message_internal

    def setWarning(self, message_internal):
        self._code = 302
        self._message_internal = message_internal

    def toJson(self):
        return {
            "code": self._code,
            "message": self._message,
            "message_internal": self._message_internal,
            "body": self._body
        }
