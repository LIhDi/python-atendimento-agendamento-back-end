import multiprocessing

from .base import *

DEBUG = False
SENTRY_KEY = ""
LOG_FILE = os.path.join(BASE_PATH, "..", "prod.log")
LOG_LEVEL = "INFO"

NUM_CORES = multiprocessing.cpu_count()
WORKERS = max(NUM_CORES - 1, 1)
SENTRY_ENVIRONMENT = "production"
os.environ["PYTHONBREAKPOINT"] = "0"
ACCESS_LOG = False
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
AWS_OPTIONS = {"region_name": "sa-east-1"}
AWS_CLIENT_KWARGS_SNS = {"service_name": 'sns', "region_name": "sa-east-1"}
