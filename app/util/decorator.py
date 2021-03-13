from functools import wraps

from exceptions import UnauthorizedException
from util.loggers import logger

def person_authenticator():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            logger.debug("Initializing authorization.")
            national_registration = request.match_info.get("national_registration")
            is_authorized = None
            if national_registration:
                is_authorized = await request.app.authenticator_service.authenticate(national_registration=national_registration)
            if is_authorized:
                response = await f(request, *args, **kwargs)
                return response
            else:
                logger.error(f"Authentication failed for person {national_registration}.")
                raise UnauthorizedException(f"Person: {national_registration} unauthorized.")

        return decorated_function

    return decorator


def composed(*decs):
    def deco(f):
        for dec in reversed(decs):
            f = dec(f)
        return f

    return deco
