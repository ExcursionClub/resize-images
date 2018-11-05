import json


def hello(event, context):
    return dict(
        statusCode=200,
        body="Hello"
    )

