from .base import *


LOCALSTACK_ENDPOINT = "http://localhost:4566"

AWS_CLIENT_KWARGS_SNS = {"service_name": 'sns',
                         "endpoint_url": LOCALSTACK_ENDPOINT,
                         "aws_access_key_id": "ACCESS_KEY",
                         "aws_secret_access_key": "SECRET_KEY",
                         "aws_session_token": "SESSION_TOKEN"}

API_URL = os.getenv("API_URL", "http://localhost:8090/v1/validation")

AWS_OPTIONS = {"endpoint_url": LOCALSTACK_ENDPOINT,
               "region_name": "us-east-1"}

AWS_TOPIC_ARN = "arn:aws:sns:us-east-1:000000000000:local-sns-notification-email"

