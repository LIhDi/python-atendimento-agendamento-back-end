from .base import *

DB_URL = "mysql://%s:%s@%s:%s/%s" % (
    os.getenv("DB_USER", "root"),
    os.getenv("DB_PASSWORD", "root"),
    os.getenv("DB_HOST", "localhost"),
    os.getenv("DB_PORT", "3305"),
    os.getenv("DB_NAME", "atendimento-agendamento-test-db"),
)

TOKEN_TEST = "3D4C70933F134D3BA6C4F72D463FF9AC"

LOCALSTACK_ENDPOINT = "http://localhost:4566"


VALIDATION_TOKEN_API_URL = os.getenv("VALIDATION_TOKEN_API_URL", "http://localhost:8090/v1/validation")

AWS_CLIENT_KWARGS_SNS = {"service_name": 'sns',
                     "endpoint_url": LOCALSTACK_ENDPOINT,
                     "aws_access_key_id": "ACCESS_KEY",
                     "aws_secret_access_key": "SECRET_KEY",
                     "aws_session_token": "SESSION_TOKEN"}

LOCALSTACK_KWARGS = {"endpoint_url": LOCALSTACK_ENDPOINT,
                     "aws_access_key_id": "ACCESS_KEY",
                     "aws_secret_access_key": "SECRET_KEY",
                     "aws_session_token": "SESSION_TOKEN"}

AWS_TOPIC_ARN = "arn:aws:sns:us-east-1:000000000000:local-sns-notification-email"

API_TIMEOUT = {"sock_read": os.getenv("READ_TIMEOUT", 0.5), "sock_connect": os.getenv("CONNECT_TIMEOUT", 0.5)}

AWS_OPTIONS = {"endpoint_url": LOCALSTACK_ENDPOINT,
               "region_name": "us-east-1",
               "aws_access_key_id": "ACCESS_KEY",
               "aws_secret_access_key": "SECRET_KEY",
               "aws_session_token": "SESSION_TOKEN"
               }
