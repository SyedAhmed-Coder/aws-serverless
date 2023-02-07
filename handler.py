import json


def hello(event, context):
    body = {
        "message": "This is the Production Branch Version 2.0",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
