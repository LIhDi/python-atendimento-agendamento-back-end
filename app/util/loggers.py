import logging
import logging.config
from settings import settings


def setup_logger():
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "detailed": {
                "class": "util.formatter.Formatter",
                "format": "%(asctime)s %(levelname)-7s"
                "[rid:%(rid)s] [mid:%(mid)s] %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": f"{settings.LOG_LEVEL}",
                "formatter": "detailed",
                }
            },
        "loggers": {
            "app": {
                "level": "DEBUG",
                "handlers": ["console"],
                "propagate": 1,
                }
            },
        }

    logging.config.dictConfig(config)
    logger = logging.getLogger("app")
    return logger


logger = setup_logger()
