import os

BASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")

SENTRY_KEY = ""

REQUEST_MAX_SIZE = 100000000  # How big a request may be (bytes)
REQUEST_BUFFER_QUEUE_SIZE = 100  # Request streaming buffer queue size
REQUEST_TIMEOUT = 60  # How long a request can take to arrive (sec)
RESPONSE_TIMEOUT = 60  # How long a response can take to process (sec)
KEEP_ALIVE = True  # Disables keep-alive when False
KEEP_ALIVE_TIMEOUT = 5  # How long to hold a TCP connection open (sec)
GRACEFUL_SHUTDOWN_TIMEOUT = 15.0  # How long to wait to force close non-idle connection (sec)
ACCESS_LOG = os.getenv("ACCESS_LOG", True)  # Disable or enable access log
PROXIES_COUNT = 0  # The number of proxy servers in front of the app (e.g. nginx; see below)
FORWARDED_FOR_HEADER = "X-Forwarded-For"  # The name of "X-Forwarded-For" HTTP header that contains client and proxy ip

APP_ID = "f41d1bb392474617b46aa091f90cc3b4"
API_SCHEMES = ["http", "https"]
REAL_IP_HEADER = "X-Real-IP"
HOST = os.getenv("HOST", "0.0.0.0")
PORT = 8000
WORKERS = 1
DEBUG = True
DB_URL = "mysql://%s:%s@%s:%s/%s" % (
    os.getenv("DB_USER", "root"),
    os.getenv("DB_PASSWORD", "root"),
    os.getenv("DB_HOST", "localhost"),
    os.getenv("DB_PORT", "3305"),
    os.getenv("DB_NAME", "atendimento-agendamento-db"),
)

API_TIMEOUT = {"sock_read": os.getenv("READ_TIMEOUT", 5), "sock_connect": os.getenv("CONNECT_TIMEOUT", 5)}
VALIDATION_TOKEN_API_URL = os.getenv("VALIDATION_TOKEN_API_URL", "")
TOKEN_INFORMATION = "/<token>"
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")

AWS_TOPIC_ARN = os.getenv("SNS_NOTIFICATION_EMAIL", "")
AWS_CLIENT_KWARGS_SNS = {"service_name": 'sns'}
AWS_DEFAULT_REGION = os.environ.get("AWS_DEFAULT_REGION", "us-east-1")
AWS_OPTIONS = {"region_name": "us-east-1"}
AWS_ENDPOINT = None

NOTIFICATION_LIMIT_BATCH = 10

LOAFER_OVERRIDE_OPTIONS = {"options": {"MaxNumberOfMessages": 5}}

