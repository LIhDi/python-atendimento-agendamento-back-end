import multiprocessing

from .base import *

DEBUG = False
SENTRY_KEY = ""
NUM_CORES = multiprocessing.cpu_count()
WORKERS = max(NUM_CORES - 1, 1)
SENTRY_ENVIRONMENT = "staging"
ACCESS_LOG = False
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
AWS_OPTIONS = {"region_name": "us-east-1"}
AWS_CLIENT_KWARGS_SNS = {"service_name": 'sns', "region_name": "us-east-1"}
