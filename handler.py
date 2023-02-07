import json


def hello(event, context):
    body = {
        "message": "This the devlopment branch pushing Version 1.0.",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
