import json
from collections import namedtuple

import aiobotocore
import aiohttp
from aiohttp import ClientTimeout

from models import Message
from util.loggers import logger
from exceptions import NetTimeoutException, EventException


class AwsClient:
    def __init__(self, config):
        self.options_sns = config.AWS_CLIENT_KWARGS_SNS
        self.topic_arn = config.AWS_TOPIC_ARN
        self.Response = namedtuple("Response", "success")

    async def publish_message_to_sns(self, message_to_send, marketplace_id):
        session = aiobotocore.get_session()
        message = Message(message_to_send, marketplace_id)
        logger.info(f"Try send message to {self.topic_arn}...")
        async with session.create_client(**self.options_sns) as client:
            response = await client.publish(TopicArn=self.topic_arn,
                                            Message=json.dumps(message.topic_message),
                                            MessageAttributes=message.message_attributes)
            req_success = lambda s: s["ResponseMetadata"]["HTTPStatusCode"] == 200
        return self.Response(req_success(response))

    async def publish_message(self, topic_arn, message):
        logger.debug(f"Sending message {message.__dict__}")
        session = aiobotocore.get_session()
        async with session.create_client(**self.options_sns) as client:
            response = await client.publish(TopicArn=topic_arn,
                                            Message=json.dumps(message.topic_message),
                                            MessageAttributes=message.message_attributes)
            success = (response["ResponseMetadata"]["HTTPStatusCode"] == 200)
        if not success:
            raise EventException(f"Event Erro on publish to topic [{response} message: [{message}]]")


class HttpClient:

    def __init__(self, config):
        self.timeout = ClientTimeout(**config.API_TIMEOUT)

    async def get(self, url, params=None):
        if params:
            for key, value in params.items():
                url = url.replace(f"<{key}>", f"{value}")
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as client:
                resp = await client.get(url)
                if resp.status == 200:
                    return {
                        "status": resp.status,
                        "information": await resp.json()
                    }
                else:
                    return {"status": resp.status}
        except aiohttp.ServerTimeoutError as err:
            logger.exception(f"error trying call url: {url} \n{err}")
            raise NetTimeoutException()


    async def post(self, url, params=None, data=None, headers=None):
        if params:
            for key, value in params.items():
                url = url.replace(f"<{key}>", f"{value}")
        if data:
            json_data = json.dumps(data)
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as client:
                resp = await client.post(url, headers=headers, data=json_data)
                if resp.status == 200:
                    return {
                        "status": resp.status,
                        "information": await resp.json()
                    }
                else:
                    return {"status": resp.status}
        except aiohttp.ServerTimeoutError as err:
            logger.exception(f"error trying call url: {url} \n{err}")
            raise NetTimeoutException()