from enum import IntEnum

__all__ = ["HTTPStatus"]


class HTTPStatus(IntEnum):
    def __new__(cls, status_code, status, message="", type="", category=""):
        obj = int.__new__(cls, status_code)
        obj._value_ = status_code
        obj.status = status
        obj.message = message
        obj.type = type
        obj.category = category
        return obj

    def json(self, message=None, type=None, category=None):
        return {
            "status_code": self.value,
            "status": self.status,
            "message": message or self.message,
            "type": type or self.type,
            "category": category or self.category,
        }

    def err(self, message=None, type=None, category=None):
        return {"error": self.json(message, type, category)}

    @classmethod
    def _missing_(cls, value):
        return HTTPStatus.INTERNAL_SERVER_ERROR

    OK = (200, "OK", "Request fulfilled, Document follows", "", "")

    NOT_MODIFIED = (304, "Not Modified",
                    "Update was not successful.", "", "")

    BAD_REQUEST = (400, "Bad Request",
                   "Bad request syntax or unsupported method",
                   "invalid_request_error", "resource_malformed")

    UNAUTHORIZED = (401, "Not Authorized",
                    "Not permitted process this request.",
                    "unauthorized_request_error", "unauthorized_request_error")

    NOT_FOUND = (404, "Not Found",
                 "Nothing matches the given URI.",
                 "invalid_request_error", "resource_not_found")

    NOT_ACCEPTABLE = (406, "Not Acceptable",
                      "Request not acceptable",
                      "invalid_request_error", "request_not_acceptable")

    CONFLICT = (409, "Conflict",
                "Request conflict",
                "resource_already_exist", "request_conflict")

    UNPROCESSABLE_ENTITY = (422, "Unprocessable Entity",
                            "This request cannot be processed.",
                            "unprocessable_entity", "request_unprocessable")

    INTERNAL_SERVER_ERROR = (500, "Internal Server Error",
                             "Server got itself in trouble",
                             "internal_server_error", "internal_server_error")

    BAD_GATEWAY = (502, "Bad gateway",
                   "Problem calling external api",
                   "bad_gateway", "bad_gateway")
