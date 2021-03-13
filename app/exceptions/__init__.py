from util.status import HTTPStatus


class GenericError(Exception):
    def __init__(self):
        super(self)


class EventException(GenericError):
    def __init__(self):
        super(self)


class IllegaStateException(GenericError):
    def __init__(self):
        super(self)


class HTTPException(GenericError):
    def __init__(self, message, category, type, exception_type):
        self.message = message
        self.category = category
        self.type = type
        self.exception_type = exception_type


class DatabaseException(GenericError):
    def __init__(self, expr):
        self.expression = expr
        self.message = "Error in database connection."


class BusinessException(GenericError):
    def __init__(self, expr):
        self.expression = expr
        self.message = "Service error por request."


class ResourceAlreadyExistException(HTTPException):
    def __init__(self, message=None, category=None, type=None):
        super().__init__(message, category, type, exception_type=HTTPStatus.CONFLICT)


class InvalidUpdateException(HTTPException):
    def __init__(self, message=None, category=None, type=None):
        super().__init__(message, category, type, exception_type=HTTPStatus.CONFLICT)


class InvalidRequestException(HTTPException):
    def __init__(self, message=None, category=None, type=None):
        super().__init__(message, category, type, exception_type=HTTPStatus.BAD_REQUEST)


class UnprocessableEntityException(HTTPException):
    def __init__(self, message=None, category=None, type=None):
        super().__init__(message, category, type, exception_type=HTTPStatus.UNPROCESSABLE_ENTITY)


class NetTimeoutException(HTTPException):
    def __init__(self, message=None, category=None, type=None):
        super().__init__(message, category, type, exception_type=HTTPStatus.BAD_GATEWAY)


class UnauthorizedException(HTTPException):
    def __init__(self, message=None, category=None, type=None):
        super().__init__(message, category, type, exception_type=HTTPStatus.UNAUTHORIZED)


class NotFoundException(HTTPException):
    def __init__(self, message=None, category=None, type=None):
        super().__init__(message, category, type, exception_type=HTTPStatus.NOT_FOUND)


class NotAcceptableException(HTTPException):
    def __init__(self, message=None, category=None, type=None):
        super().__init__(message, category, type, exception_type=HTTPStatus.NOT_ACCEPTABLE)
