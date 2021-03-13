import traceback
from sanic.handlers import ErrorHandler
from sanic.response import json

from util.status import HTTPStatus
from exceptions import InvalidUpdateException


class DefaultCustomErrorHandler(ErrorHandler):
    def __init__(self):
        super().__init__()
        self.default_type = HTTPStatus.INTERNAL_SERVER_ERROR
        self.add(InvalidUpdateException, conflict_state_handler)

    def default(self, request, exception):
        status = getattr(exception, "exception_type", self.default_type)
        type = getattr(exception, "type", None)
        category = getattr(exception, "category", None)
        message = getattr(exception, "message", None)

        error = status.err(message=message, type=type, category=category)

        if self.default_type == status:
            traceback.print_exc()

        return json(error, status=status)


async def conflict_state_handler(request, exception):
    status = HTTPStatus.CONFLICT
    return json(status.err(message=str(exception), type="conflict_current_state"), status=status)
